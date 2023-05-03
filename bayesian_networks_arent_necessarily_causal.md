## Bayesian Networks Aren't Necessarily Causal

As a casual formal epistemology fan, you've probably heard that the philosophical notion of causality can be formalized in terms of Bayesian networks—but also as a casual formal epistemology fan, you also probably don't know the details all that well.

One day, while going through the family archives, you come across a meticulously maintained dataset describing a joint probability distribution over four variables: whether it rained that day, whether the sprinkler was on, whether the sidewalk was wet, and whether the sidewalk was slippery. The distribution is specified in this table:

[TODO: joint distribution table]

(You wonder what happened that one day out of 140,000 when it rained, and the sprinkler was on, and the sidewalk was slippery but not wet. Did—did someone put a tarp up to keep the sidewalk dry, but also spill slippery oil, which didn't count as being relevantly "wet"? Also, 140,000 days is more than 383 years—were "sprinklers" even a thing in year 1640 C.E.? You quickly put these questions out of your mind: it is not your place to question the correctness of the family archives.)

You decide that this dataset will be useful for learning more about how to think about causality using Bayesian networks! You've read that Bayesian networks "factorize" an unwieldly joint probability distribution into a number of more compact _conditional_ probability distributions, related by a directed acyclic graph. (Even a casual formal epistemology fan knows _that_ much.) The graph represents knowledge that each variable is independent of its non-descendants given its parents.
