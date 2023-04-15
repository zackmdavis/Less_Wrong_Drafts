from collections import namedtuple
from fractions import Fraction

def joint_distribution():
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
    return worlds

def query(distribution, conditions):
    total_probability = 0
    for world, probability in distribution:
        if all(world[k] == v for k, v in conditions.items()):
            total_probability += probability
    return total_probability


def merge(d1, *more):
    out = d1.copy()
    for di in more:
        out.update(di)
    return out

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


def build_graph(distribution, variables):
    # Algorithm 3.2 in Daphne Koller and the other guy §3.4.1, p. 80
    edges = []
    for i in range(len(variables)):
        predecessors = frozenset(variables[:i])
        parents = predecessors
        for prospective_parents in powerset(predecessors):
            if conditionally_independent(
                    distribution,
                    # XXX: conflating the variables with the "True" event
                    {variables[i]: True},
                    {s: True for s in predecessors - prospective_parents},
                    {s: True for s in prospective_parents}
            ):
                if len(prospective_parents) < len(parents):
                    parents = prospective_parents
        for parent in parents:
            edges.append("{} → {}".format(parent, variables[i]))
    return edges


if __name__ == "__main__":
    worlds = joint_distribution()
    worlds = sorted(worlds, key=lambda w: w[1])
    print(sum(world[1] for world in worlds))
    for world in worlds:
        print(world, float(world[1]))

    print(conditionally_independent(worlds, {"rain": True}, {"slippery": True}, givens={"wet": True})) # true, blocked by conditioning on "wet"
    print(conditionally_independent(worlds, {"rain": True}, {"sprinkler": True}, givens={})) # true, blocked by "wet" collider
    print(conditionally_independent(worlds, {"rain": True}, {"sprinkler": True}, givens={"wet": True})) # false, conditioning on "wet" collider unblocks

    true_graph = build_graph(worlds, ["rain", "sprinkler", "wet", "slippery"])
    print(true_graph)
    print(len(true_graph)) # 3

    crazy_graph = build_graph(worlds, ["wet", "sprinkler", "slippery", "rain"])
    print(crazy_graph)
    print(len(crazy_graph)) # 4

    # XXX: I have a bug; seeing "sprinkler → slippery" edges that shouldn't be there in both test cases
