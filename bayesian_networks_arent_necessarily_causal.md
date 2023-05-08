## Bayesian Networks Aren't Necessarily Causal

As a casual formal epistemology fan, you've probably [heard that the philosophical notion of causality can be formalized in terms of Bayesian networks](https://www.lesswrong.com/posts/hzuSDMx7pd2uxFc5w/causal-diagrams-and-causal-models), which involve directed graphs where the arrows point from "cause" to "effect"—but also as a casual formal epistemology fan, [you also probably don't](https://www.lesswrong.com/posts/tp4rEtQqRshPavZsr/learn-bayes-nets) know the details all that well.

One day, while going through the family archives, you come across a meticulously maintained dataset describing a joint probability distribution over four variables: whether it rained that day, whether the sprinkler was on, whether the sidewalk was wet, and whether the sidewalk was slippery. The distribution is specified in this table (using the abbreviated labels "rain", "slippery", "sprinkler", and "wet"):

[TODO: joint distribution table]

(You wonder what happened that one day out of 140,000 when it rained, and the sprinkler was on, and the sidewalk was slippery but not wet. Did—did someone put a tarp up to keep the sidewalk dry, but also spill slippery oil, which didn't count as being relevantly "wet"? Also, 140,000 days is more than 383 years—were "sprinklers" even a thing in the year 1640 C.E.? You quickly put these questions out of your mind: it is not your place to question the correctness of the family archives.)

You're slightly uncomfortable with this unwieldy sixteen-row table. You think that there must be some other way to represent the same information, while making it clearer that it's not a coincidence that rain and wet sidewalks tend to co-occur.

You've read that Bayesian networks "factorize" an unwieldly joint probability distribution into a number of more compact _conditional_ probability distributions, related by a directed acyclic graph. (Even a casual formal epistemology fan knows _that_ much.) The graph represents knowledge that each variable is [conditionally independent](https://en.wikipedia.org/wiki/Conditional_independence) of its non-descendants given its parents, which enables "local" computations: given the values of just a variable's parents in the graph, we can compute a conditional distribution for that variable, without needing to consider what is known about other variables elsewhere in the graph ...

You've _read_ that, but you've never actually done it before! You decide that constructing a Bayesian network to represent this distribution will be a useful excercise.

To start, you re-label the variables for brevity. (On a whim, you assign indices in reverse-alphabetical order: $X_1$ = wet, $X_2$ = sprinkler, $X_3$ = slippery, $X_4$ = rain.)

[TODO: joint distribution table, with x₁=wet, x₂=sprinkler, x₃=slippery, x₄=rain]

Now, how do you go about building a Bayesian network? Consulting algorithm 3.2 in §3.4.1 of [the book by Daphne Koller and the other guy](https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/), it seems like you should be able to just—pick a variable, allocate a graph node to represent it, find the smallest subset of the previously-allocated variables such that the variable represented by the new node is conditionally independent of the other previously-allocated variables given that subset, and then draw directed edges from each of the nodes in the subset to the new node?—and keep doing that for each variable—and then compute conditional probability tables for each variable given its parents in the resulting graph?

That seems complicated when you say it abstractly, but you have faith that it will make more sense as you carry out the computations.

First, you allocate a graph node for $X_1$. It doesn't have any parents, so the associated conditional ("conditional") probability distribution, is really just the marginal distribution for $X_1$.

[TODO: crazy graph in progress, with just X₁, including CPD]

Then you allocate a node for $X_2$. $X_2$ is not independent of $X_1$. (Because $P(X_1 \land X_2)$ = 169/1400, which isn't the same as $P(X_1) \cdot P(X_2)$ = 8/25 · 1/7 = 8/175.) So you make $X_1$ a parent of $X_2$, and your conditional probability table for $X_2$ separately specifies the probabilities of $X_2$ being true or false, depending on whether $X_1$ is true or false.

[TODO: crazy graph in progress, with X₁ and X₂, including CPDs]

Next is $X_3$. Now that you have two possible parents, you need to check whether conditioning on either of $X_1$ and $X_2$ would render $X_3$ conditionally independent of the other. If not, then both $X_1$ and $X_2$ will be parents of $X_3$; if so, then the variable you conditioned on will be the sole parent. (You assume that the case where $X_3$ is just independent from both $X_1$ and $X_2$ does not pertain; if that were true, $X_3$ wouldn't be connected to the rest of the graph at all.)

It turns out that $X_3$ and $X_2$ are conditionally independent given $X_1$. That is, $P(X_3 \land X_2 \mid X_1) = P(X_3 \mid X_1) \cdot P(X_2 \mid X_1)$. (Because the left-hand side is $\frac{P(X_3 \land X_2 \land X_1)}{P(X_1)} = \frac{507}{1792}$, and the right-hand side is $\frac{3}{4} \cdot \frac{169}{448} = \frac{507}{1792}$.) So $X_1$ is a parent of $X_3$, and $X_2$ isn't; you draw an arrow from $X_1$ (and only $X_1$) to $X_3$, and compile the corresponding conditional probability table.

[TODO: crazy graph in progress, with X₁ and X₂ and X₃, including CPDs]

Finally, you have $X_4$. The chore of finding the parents is starting to feel more intuitive now. Out of the $2^3 = 8$ possible subsets of the preceding variables, you need to find the smallest subset, such that conditioning on that subset renders $X_4$ (conditionally) independent of the variables not in that subset. After some calculations that the authors of expository blog posts have sometimes been known to callously leave as an exercise to the reader, you determine that $X_1$ and $X_2$ are the parents of $X_4$.

And with one more conditional probability table, your Bayesian network is complete!

[TODO: completed crazy graph]

Eager to interpret the meaning of this structure regarding the philosophy of causality, you translate the $X_i$ variable labels back to English:

[TODO: completed crazy graph with English labels]

...

This can't be right. The arrow from "wet" to "slippery" seems fine. But all the others are clearly absurd. Wet sidewalks cause rain? Sprinklers cause rain? Wet sidewalks cause the sprinkler to be on?

You despair. You thought you had understood the algorithm. You can't find any errors in your calculations. What did you do wrong?

...

Actually, nothing! The procedure you used for factorizing a joint distribution into a Bayesian network is sensitive to what order the variables are visited in. Different orderings produce different networks, which all represent the same distribution: querying any of the resulting networks for marginal probabilities (like $P(\mathrm{rain})$) or conditional probabilities (like $P(\mathrm{slippery} \mid \mathrm{rain})$) will give the same answers.

If you had carried out your procedure in the order $X_4$, $X_2$, $X_1$, $X_3$ (using the $X_i$ labels), you would have gotten this network (with the English labels):

[TODO: completed true graph with English labels]

—for which giving the arrows a causal interpretation seems much more reasonable.

You now have additional questions. If both the "true" network (with the arrows running from commonsensical cause to effect) and your "crazy" network (with "wet" at the root, apparently causing everything) both represent the same probability distribution, what happened to the dream of understanding causality with Bayesian networks? In this example, you know from reasons _outside_ the math, that "wet" shouldn't cause "rain", but you couldn't count on that were you to apply these methods to problems further removed from intuition. The "true" network and the "crazy" network give the same answers to marginal and conditional probability queries—which amounts to them making the _same predictions_ about the world. So if [beliefs are supposed to correspond to predictions](https://www.lesswrong.com/posts/a7n8GdKiAZRX86T5A/making-beliefs-pay-rent-in-anticipated-experiences), in what sense could the "true" network be _better_? What does your conviction that rain causes wetness even _mean_, if someone who believed the opposite could make all the same predictions?

