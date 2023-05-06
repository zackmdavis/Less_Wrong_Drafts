## Bayesian Networks Aren't Necessarily Causal

As a casual formal epistemology fan, you've probably heard that the philosophical notion of causality can be formalized in terms of Bayesian networks—but also as a casual formal epistemology fan, you also probably don't know the details all that well.

One day, while going through the family archives, you come across a meticulously maintained dataset describing a joint probability distribution over four variables: whether it rained that day, whether the sprinkler was on, whether the sidewalk was wet, and whether the sidewalk was slippery. The distribution is specified in this table:

[TODO: joint distribution table]

(You wonder what happened that one day out of 140,000 when it rained, and the sprinkler was on, and the sidewalk was slippery but not wet. Did—did someone put a tarp up to keep the sidewalk dry, but also spill slippery oil, which didn't count as being relevantly "wet"? Also, 140,000 days is more than 383 years—were "sprinklers" even a thing in the year 1640 C.E.? You quickly put these questions out of your mind: it is not your place to question the correctness of the family archives.)

You're slightly uncomfortable with this unwieldy sixteen-row table. You think that there must be some other way to represent the same information, while making it clearer that it's not a coincidence that rain and wet sidewalks tend to co-occur.

You've read that Bayesian networks "factorize" an unwieldly joint probability distribution into a number of more compact _conditional_ probability distributions, related by a directed acyclic graph. (Even a casual formal epistemology fan knows _that_ much.) The graph represents knowledge that each variable is conditionally independent of its non-descendants given its parents, which enables "local" computations: given the values of just a variable's parents in the graph, we can compute a conditional distribution for that variable, without needing to consider what is known about other variables elsewhere in the graph ...

You've _read_ that, but you've never actually done it before! You decide that constructing a Bayesian network to represent this distribution will be a useful excercise.

To start, you re-label the variables for brevity:

[TODO: joint distribution table, with x₁=wet, x₂=sprinkler, x₃=slippery, x₄=rain]

Now, how do you go about building a Bayesian network? Consulting algorithm 3.2 in §3.4.1 of the book by Daphne Koller and the other guy, it seems like you should be able to just—pick a variable, allocate a graph node to represent it, find the smallest subset of the previously-allocated nodes such that the variable represented by the new node is conditionally independent of the other previously-allocated variables given that subset, and then draw directed edges from each of the nodes in that subset to the new node?—and keep doing that for each variable—and then compute conditional probability tables for each variable given its parents in the graph?

That seems complicated when you say it abstractly, but you have faith that it will make more sense as you carry out the computations.

First, you allocate a graph node for $x_1$. It doesn't have any parents, so the associated conditional ("conditional") probability distribution, is really just the marginal distribution for $x_1$.

[TODO: crazy graph in progress, with just x₁, including CPD]

Then you allocate a node for $x_2$.

$x_2$ is not independent of $x_1$, so you make $x_1$ a parent of $x_2$, and your conditional probability table for $x_2$ separately specifies the probabilities of $x_2$ being true or false, depedning on whether $x_1$ is true or false.

[TODO: crazy graph in progress, with x₁ and x₂, including CPDs]

Next is $x_3$. Now that you have more than one preceding node—more than one possible parent—you need to check whether conditioning on a _subset_ of $x_1$ and $x_2$ would render $x_3$ conditionally independent of the other.
