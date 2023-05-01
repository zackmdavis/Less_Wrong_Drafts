import itertools

from collections import namedtuple
from fractions import Fraction

def our_joint_distribution():
    worlds = []
    for rain in [True, False]:
        for sprinkler in [True, False]:
            for wet in [True, False]:
                for slippery in [True, False]:
                    rain_p = Fraction(1, 4) if rain else Fraction(3, 4)
                    sprinkler_p = Fraction(1, 7) if sprinkler else Fraction(6, 7)

                    if rain and sprinkler:
                        wet_p = Fraction(98, 100) if wet else Fraction(2, 100)
                    elif rain and not sprinkler:
                        wet_p = Fraction(9, 10) if wet else Fraction(1, 10)
                    elif not rain and sprinkler:
                        wet_p = Fraction(8, 10) if wet else Fraction(2, 10)
                    elif not rain and not sprinkler:
                        wet_p = Fraction(1, 100) if wet else Fraction(99, 100)
                    else:
                        raise ValueError("exhaustive match")

                    if wet:
                        slippery_p = Fraction(3, 4) if slippery else Fraction(1, 4)
                    else:
                        slippery_p = Fraction(1, 100) if slippery else Fraction(99, 100)
                    worlds.append(
                        (
                            {'rain': rain, 'sprinkler': sprinkler, 'wet': wet, 'slippery': slippery},
                            rain_p * sprinkler_p * wet_p * slippery_p
                        )
                    )
    worlds = sorted(worlds, key=lambda e: (e[1], sorted(e[0].items())))
    return worlds

def merge(d1, *more):
    out = d1.copy()
    for di in more:
        out.update(di)
    return out

def is_subworld(superworld, candidate_subworld):
    return set(candidate_subworld.items()) <= set(superworld.items())

def query(distribution, events):
    total_probability = 0
    for world, probability in distribution:
        if all(world[k] == v for k, v in events.items()):
            total_probability += probability
    return total_probability

def conditional_query(distribution, events, conditions):
    # P(A|C) = P(A & C) / P(C)
    return (
        query(distribution, merge(events, conditions)) /
        query(distribution, conditions)
    )

def joint_distribution_build_step(old_joint, new_identifier, conditional_distribution):
    # joint distribution format is a list of (world-state-dict, probability)
    # tuples, summing to 1
    #
    # conditional distribution format is a list of (parent-states-dict,
    # list-of-probabilities-for-this-state) tuples, where each of the
    # list-of-probabilities-for-this-state sum to 1
    #
    # A → C induces P(A, B, C) = P(A, B)P(C | A)
    #
    # The `P(C | A)` factor will be used more than once (for multiple values of
    # B), but that's fine
    worlds = []
    identifiers = list(old_joint[0][0].keys()) + [new_identifier]
    n = len(identifiers)
    for old_world, p in old_joint:
        conditional_table_rows = [
            (w, ps) for w, ps in conditional_distribution
            if is_subworld(old_world, w)
        ]
        assert len(conditional_table_rows) == 1, "actually got {} rows: {}".format(len(conditional_table_rows), conditional_table_rows)

        conditional_table_row, = conditional_table_rows
        parent_subworld, new_value_distribution = conditional_table_row
        for new_value, l in zip([True, False], new_value_distribution):
            worlds.append(
                (merge(old_world, {new_identifier: new_value}), p * l)
            )
    return worlds

def conditionally_independent(distribution, u, v, givens):
    # P(U & V | G) = P(U | G) * P(V | G)
    # → P(U & V & G) / P(G) = P(U & G)/P(G) * P(V & G)/P(G)

    # I think it's only because the variables are binary that I'm allowed to
    # conflate independence of events and independence of variables?

    normalizer = query(distribution, givens)
    joint = query(distribution, merge(u, v, givens))
    left = query(distribution, merge(u, givens))
    right = query(distribution, merge(v, givens))

    return joint/normalizer == (left/normalizer) * (right/normalizer)

def powerset(s):
    if not s:
        return frozenset([frozenset()])
    else:
        e, *rest = s
        subproblem = powerset(rest)
        return subproblem | frozenset({t | frozenset({e}) for t in subproblem})


class Variable:
    def __init__(self, network, identifier):
        self.network = network
        self.identifier = identifier
        self.parents = []

    def add_parent(self, variable):
        self.parents.append(variable)

    def build_conditional_distribution(self):
        parent_identifiers = [p.identifier for p in self.parents]
        n = len(parent_identifiers)
        worlds = []
        for keys, values in zip(
                itertools.repeat(parent_identifiers, 2**n),
                itertools.product([True, False], repeat=n)
        ):
            world = dict(zip(keys, values))
            worlds.append(
                (
                    world,
                    [
                        conditional_query(
                            self.network.distribution,
                            {self.identifier: v},
                            world
                        )
                        for v in [True, False]
                    ]
                )
            )
        self.conditional_distribution = worlds
        return worlds

    def intervene(self, value):
        self.parents = []
        self.conditional_distribution = [({}, [1, 0] if value else [0, 1])]


class BayesianNetwork:
    def __init__(self, distribution, variable_ordering):
        self.distribution = distribution
        self.variable_ordering = variable_ordering
        identifiers = distribution[0][0].keys()
        self.variables = {}
        for identifier in identifiers:
            self.variables[identifier] = Variable(self, identifier)

    def render_edges(self):
        edges = []
        for variable in self.variables.values():
            for parent in variable.parents:
                edges.append("{} → {}".format(parent.identifier, variable.identifier))
        return edges

    def recompile_distribution(self):
        worlds = [({}, 1)]
        for identifier in self.variable_ordering:
            worlds = joint_distribution_build_step(
                worlds,
                identifier,
                self.variables[identifier].conditional_distribution
            )
        worlds = sorted(worlds, key=lambda e: (e[1], sorted(e[0].items())))
        self.distribution = worlds
        return worlds


def build_graph(distribution, variable_ordering):
    # Algorithm 3.2 in Daphne Koller and the other guy §3.4.1, p. 80
    network = BayesianNetwork(distribution, variable_ordering)
    for i in range(len(variable_ordering)):
        predecessors = frozenset(variable_ordering[:i])
        parents = predecessors
        for prospective_parents in powerset(predecessors):
            if conditionally_independent(
                    distribution,
                    # XXX: conflating the variables with the "True" event
                    {variable_ordering[i]: True},
                    {s: True for s in predecessors - prospective_parents},
                    {s: True for s in prospective_parents}
            ):
                if len(prospective_parents) < len(parents):
                    parents = prospective_parents
        for parent in parents:
            network.variables[variable_ordering[i]].add_parent(
                network.variables[parent]
            )
    for _, v in network.variables.items():
        v.build_conditional_distribution()
    return network


if __name__ == "__main__":
    worlds = our_joint_distribution()
    print(sum(world[1] for world in worlds))
    for world in worlds:
        print(world, float(world[1]))

    print(conditionally_independent(worlds, {"rain": True}, {"slippery": True}, givens={"wet": True})) # true, blocked by conditioning on "wet"
    print(conditionally_independent(worlds, {"rain": True}, {"sprinkler": True}, givens={})) # true, blocked by "wet" collider
    print(conditionally_independent(worlds, {"rain": True}, {"sprinkler": True}, givens={"wet": True})) # false, conditioning on "wet" collider unblocks

    true_graph = build_graph(worlds.copy(), ["rain", "sprinkler", "wet", "slippery"])
    print(true_graph.render_edges())

    crazy_graph = build_graph(worlds.copy(), ["wet", "sprinkler", "slippery", "rain"])
    print(crazy_graph.render_edges())

    # 'wet' is a collider in the true graph; two parents
    true_wet_cpd = true_graph.variables['wet'].conditional_distribution
    print(true_wet_cpd, len(true_wet_cpd))

    # 'wet' is the root in the crazy graph; this should be unconditional
    crazy_wet_cpd = crazy_graph.variables['wet'].conditional_distribution
    print(crazy_wet_cpd, len(crazy_wet_cpd))

    print(query(worlds, {"wet": True}))

    recompiled_true = true_graph.recompile_distribution()
    recompiled_crazy = crazy_graph.recompile_distribution()

    print("recompiled from faithful graph = original ", recompiled_true == worlds)
    print("recompiled from crazy graph = original ", recompiled_crazy == worlds)

    # in the true graph, intervening on wet doesn't change the probability
    # of rain
    print("original P(rain)", query(worlds, {'rain': True}))
    true_graph.variables['wet'].intervene(True)
    true_graph.recompile_distribution()
    print("P(rain | do(wet))", query(true_graph.distribution, {'rain': True}))

    # in the crazy graph, intervening on 'wet' does change the probability of 'rain'
    print("original (but 'crazy') P(rain)", query(worlds, {'rain': True}))
    crazy_graph.variables['wet'].intervene(True)
    crazy_graph.recompile_distribution()
    print("'crazy' P(rain | do(wet))", query(crazy_graph.distribution, {'rain': True}))  # 319/448—it changed!

    print("\n\n")

    # in the crazy graph, intervening on 'sprinkler' also changes the
    # probability of 'rain', but doesn't change the probability of 'wet'
    crazy_graph = build_graph(worlds.copy(), ["wet", "sprinkler", "slippery", "rain"])
    print("original (but 'crazy') P(rain)", query(worlds, {'rain': True}))
    print("original (but 'crazy') P(wet)", query(worlds, {'wet': True}))

    crazy_graph.variables['sprinkler'].intervene(True)
    crazy_graph.recompile_distribution()

    print("'crazy' P(rain | do(sprinkler))", query(crazy_graph.distribution, {'rain': True}))
    print("'crazy' P(wet | do(sprinkler))", query(crazy_graph.distribution, {'wet': True}))
