## "Deep Learning" Is Function Approximation

### A Surprising Development in the Study of Multi-layer Parameterized Graphical Function Approximators

As a programmer and epistemology enthusiast, I've been studying some statistical modeling techniques lately! It's been boodles of fun, and might even prove useful in a future dayjob if I decide to pivot my career away from the backend web development roles I've taken in the past.

Separately, a lot of my friends seem to belong to some sort of ... internet fanfiction cult? I'm still not entirely sure what it's about, but it seems harmless. Takes all sorts, I guess. Coincidentally, many of these people seem to be very excited about the same statistical modeling techniques that I've been learning about!

It's strange, though—when I explain what I've been studying, a lot of these folks start to _talk funny_—almost as if they've been taught to revere statistical modeling as a grave matter of eschatological importance, without having spent any time using statistical models? I don't get it.

The other week I was talking to one of these people about some things I learned from [the new Simon Prince book](https://udlbook.github.io/udlbook/) about multi-layer parameterized graphical function approximators, which map inputs to outputs via a sequence of affine transformations composed with nonlinear "activation" functions.

(Some authors call these "deep neural networks" for some reason, but [I like my name better](https://www.lesswrong.com/posts/WBdvyyHLdxZSAMmoz/taboo-your-words).)

It's a curve-fitting technique: by setting the multiplicative factors and additive terms appropriately, multi-layer parameterized graphical function approximators can [approximate any function](https://en.wikipedia.org/wiki/Universal_approximation_theorem). For a popular choice of "activation" rule [which takes the maximum of the input and zero](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)), the curve is specifically a piecewise-linear function.

Basically, the big empirical surprise of [the previous decade](https://bmk.sh/2019/12/31/The-Decade-of-Deep-Learning/) is that given a lot of desired input–output pairs (x, y) and the proper engineering know-how, you can use large amounts of computing power to find parameters θ to fit a multi-layer parameterized graphical function approximator f(x, θ) that "generalizes" well—meaning that if you compute ŷ = f(x, θ) for some x that wasn't in any of your original example input–output pairs (which some authors call "training" data for some reason), it turns out that ŷ is usually pretty similar to the y you would have used in an example (x, y) pair.

It wasn't obvious beforehand that this would work! You'd expect that if your multi-layer parameterized graphical function approximator has more parameters than you have example input–output pairs, it would [overfit](https://en.wikipedia.org/wiki/Overfitting), finding a complicated function that reproduced the example input–output pairs but outputted crazy nonsense for other choices of x—the more expressive function-approximator proving useless for [the lack of evidence to pin down the correct approximation](https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length).

And that is what we see for multi-layer parameterized graphical function approximators with only slightly more parameters than example input–output pairs, but for _sufficiently large_ multi-layer parameterized graphical function approximators, [the trend reverses](https://www.lesswrong.com/posts/FRv7ryoqtvSuqBxuT/understanding-deep-double-descent) and "generalization" improves—the more expressive function-approximator proving useful after all, as it admits algorithmically simpler functions that fit the example pairs.

My associate seemed puzzled by this explanation, and asked, "What are the preconditions for this intuition about neural networks as function approximators?" (I paraphrase slightly.) "I would assume this is true under specific conditions," they continued, "but I don't think we should expect such niceness to hold under capability increases. Why should we expect this to carry forward?"

I don't know where this person was getting their information, but this made zero sense to me. I mean, okay, [when you increase the number of parameters](https://gwern.net/scaling-hypothesis) in your multi-layer parameterized graphical function approximator, it gets better at representing more complicated functions, which I guess you could describe as "capability increases"?

But multi-layer parameterized graphical function approximators created by iteratively improving the quality of the approximation by adjusting their parameters in the direction of the derivative of some error metric on some example input–output pair are still, actually, function approximators. (The [mean squared error](https://en.wikipedia.org/wiki/Mean_squared_error) (f(x, θ) − y)² is a popular choice for the error metric, as is the negative log likelihood −log P(y | f(x, θ)). Some authors call these "loss functions" for some reason.) Piecewise-linear functions are still piecewise-linear functions even when there are a lot of pieces. What did _you_ think it was doing?

### Multi-layer Parameterized Graphical Function Approximators Have Many Exciting Applications

To be clear, you can do a lot with function approximation!

For example, if you assemble a collection of desired input–output pairs (x, y) where the x is [an array of pixels depicting a handwritten digit](https://en.wikipedia.org/wiki/MNIST_database) and y is a character representing which digit, then you can fit a "convolutional" multi-layer parameterized graphical function approximator to approximate the function from pixel-arrays to digits—effectively allowing computers to read handwriting.

Such techniques have proven fruitful in all sorts of domains where a useful task can be conceptualized as a function from one data distribution to another: image synthesis, voice recognition, recommender systems—you name it. Famously, by approximating the next-token function in tokenized internet text, large language models can answer questions, write code, and perform other natual-language understanding tasks.

Dwelling on the peculiar reactions of some of my friends to these advances, I'm starting to wonder if some of these folks—not all, but many—just ... don't know very much about the technology in question? If you read about computer systems performing cognitive tasks previously thought to require intelligence, and futhermore that these systems are "trained" rather than coded in the manner of traditional computer programs, I could see how that could be alarming, evoking imagery of training a wild animal that might turn on us the moment it can sieze power and reward itself rather than being dependent on us.

But "training" is just a [suggestive name](https://www.lesswrong.com/posts/yxWbbe9XcgLFCrwiL/dreams-of-ai-alignment-the-danger-of-suggestive-names). It's true that we don't have a mechanistic understanding of how multi-layer parameterized graphical function approximators perform tasks, in contrast to traditional computer programs whose source code was written by a human. It's plausible that this opacity represents grave risks, if we create powerful systems that we don't know how to debug.

But whatever the real risks are, any hope of mitigating them is going to depend on acquiring the most accurate possible understanding of the problem. If the problem is itself largely one of our own lack of understanding, it helps to be _specific_ about exactly which parts we do and don't understand, rather than surrending the entire field to a blurry aura of mystery and despair.

### An Example of Applying Multi-layer Parameterized Graphical Function Approximators in Success-Antecedent Computation Boosting

One of the exciting things about multi-layer parameterized graphical function approximators is that they can be combined with other methods for the automation of cognitive tasks (which is usually called "computing", but some authors say "artificial intelligence" for some reason).

In the spirit of being specific about exactly which parts we do and don't understand, I want to talk about [Mnih _et al._ 2013's work on getting computers to play classic Atari games](https://arxiv.org/abs/1312.5602) (like [_Pong_](https://en.wikipedia.org/wiki/Pong), [_Breakout_](https://en.wikipedia.org/wiki/Breakout_(video_game)), or [_Space Invaders_](https://en.wikipedia.org/wiki/Space_Invaders)), which is notable as one of the first high-profile examples of using multi-layer parameterized graphical function approximators in conjunction with success-antecdent computation boosting (which some authors call "reinforcement learning" for some reason).

I think some of my internet friends are in the habit of reading the news. And if you only read the news—if you're not in tune with there being things to read _besides_ news—I could see this result being quite alarming. Digital brains learning to play video games at superhuman levels _from the raw pixels_, rather than because a programmer sat down to write an automation policy for that particular game? Are we not [already in the shadow of the coming race](https://www.online-literature.com/george_eliot/theophrastus-such/17/)?

But people who read textbooks and not just news, being no less impressed by the result, are often inclined to take a subtler lesson from any particular headline-grabbing advance.

Mnih _et al._'s Atari result built off the technique of [Q-learning](https://en.wikipedia.org/wiki/Q-learning) introduced two decades prior. Given a discrete-time present-state-based outcome-valued stochastic control problem (which some authors call a ["Markov decision process"](https://en.wikipedia.org/wiki/Markov_decision_process) for some reason), Q-learning concerns itself with defining a function Q(s, a) that describes the value of taking action a while in state s, for some discrete sets of states and actions. For example, to describe the problem faced by an policy for a grid-based video game, the states might be the squares of the grid, and the available actions might be moving left, right, up, or down. The Q-value for being on a particular square and taking the move-right action might be the expected change in the game's score from doing that.

Upon finding itself in a particular state s, a Q-learning [policy](https://www.lesswrong.com/posts/rmfjo4Wmtgq8qa2B7/think-carefully-before-calling-rl-policies-agents) will usually perform the action with the highest Q(s, a), ["exploiting"](https://en.wikipedia.org/wiki/Exploration-exploitation_dilemma) its current beliefs about the environment, but [with some probability](https://en.wikipedia.org/wiki/Multi-armed_bandit#Approximate_solutions) it will "explore" by taking some other random action. The actual outcomes of its decisions are compared to the predicted outcomes to update the function Q(s, a), which can simply be represented as a table with as many rows as there are possible states and as many columns as there are possible actions. We have theorems to the effect that as the policy thoroughly explores the environment, it will eventually converge on the correct Q(s, a).

But Q-learning as originally conceived doesn't work for the Atari games studied by Mnih _et al._, because it assumes a discrete set of possible states that could be represented as the rows in a table. This is intractable for problems where the state of the environment varies continuously. If a "state" in _Pong_ is a 6-tuple of floating-point numbers representing the player's paddle position, the opponent's paddle position, and the x- and y-coordinates of the ball's position and velocity, then there's no way for the traditional Q-learning algorithm to base its behavior on its past experiences without having already seen that exact conjunction of paddle positions, ball position, and ball velocity, which almost never happens. So Mnih _et al._'s great innovation was—

(Wait for it ...)

—to replace the table representing Q(s, a) with a multi-layer parameterized graphical function approximator! By approximating the mapping from state–action pairs to discounted-sums-of-"rewards", the "neural network" allows the policy to "generalize" from its experience, taking similar actions in relevantly similar states, without having visited those exact states before. There are [a few other minor technical details](https://www.lesswrong.com/posts/kyvCNgx9oAwJCuevo/deep-q-networks-explained) needed to make it work well, but that's the big idea.

And understanding the big idea probably changes your perspective on the headline-grabbing advance. (It certainly did for me.) "Deep learning is like evolving brains; it solves problems [and we don't know how](https://www.lesswrong.com/posts/CpjTJtW2RNKvzAehG/most-people-don-t-realize-we-have-no-idea-how-our-ais-work)" is an importantly different story from "We swapped out a table for a multi-layer parameterized graphical function approximator in this specific success-antecdent computation boosting algorithm, and now it can handle continuous state spaces."

### Risks From Learned Approximation

I asked some of my internet friends why they seemed be regarding statistical modeling techniques as a grave matter of eschatological importance, and they said (not verbatim) it was because statistical modeling techniques are probably going to kill every human being on Earth within the next two to fifteen years.

Big if true! I asked where I could read more about this thesis, and was directed to [a list of reputedly fatal problems, or "lethalities"](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities).

Unfortunately, I don't think I'm qualified to evaluate the list as a whole; I would seem to lack some necessary context. (The author keeps using the term "AGI" without defining it, and [adjusted gross income](https://www.irs.gov/e-file-providers/definition-of-adjusted-gross-income) doesn't make sense in context.)

But the parts of the list that discuss the kinds of statistical modeling techniques I've been studying lately seem to _talk funny_. I don't think someone who's been reading the same textbooks as I have (like [Prince 2023](http://udlbook.com) or [Bishop and Bishop 2024](https://www.bishopbook.com/)) would write like this:

> Okay, but as we all know, modern machine learning is like a genie where you just give it a wish, right? Expressed as some mysterious thing called a 'loss function', but which is basically just equivalent to an English wish phrasing, right? And then if you pour in enough computing power you get your wish, right? So why not train a giant stack of transformer layers on a dataset of agents doing nice things and not bad things, throw in the word 'corrigibility' somewhere, crank up that computing power, and get out an aligned AGI?
>
> [...]
>
> Even if you train really hard on an exact loss function, that doesn't thereby create an explicit internal representation of the loss function inside an AI that then continues to pursue that exact loss function in distribution-shifted environments. Humans don't explicitly pursue inclusive genetic fitness; **outer optimization even on a very exact, very simple loss function doesn't produce inner optimization in that direction.** [...] This is sufficient on its own [...] to trash entire categories of naive alignment proposals which assume that if you optimize a bunch on a loss function calculated using some simple concept, you get perfect inner alignment on that concept.

To be clear, I agree that if you fit a multi-layer parameterized graphical function approximator by iteratively adjusting its parameters in the direction of the derivative of some loss function on example input–output pairs, that doesn't create an explicit internal representation of the loss function inside the function approximator.

It's just—why would you want that? And really, what would that even mean? If I use the mean squared error loss function to approximate a set of data points in the plane with a line (which some authors call fitting a "linear regression model" for some reason), obviously the line itself does not somehow contain a representation of general squared-error-minimization. The line is just a line. The loss function defines how my choice of line responds to the data I'm trying to approximate with the line. (The mean squared error has some [elegant mathematical properties](https://www.benkuhn.net/squared/), but is more sensitive to outliers than the [mean absolute error](https://en.wikipedia.org/wiki/Mean_absolute_error).) It's the same thing for piecewise-linear functions defined by multi-layer parameterized graphical function approximators: [the model is the dataset](https://nonint.com/2023/06/10/the-it-in-ai-models-is-the-dataset/). It's just not meaningful to talk about what a loss function implies, independently of the training data. (Mean squared error _of what?_ Negative log likelihood _of what?_ Finish the sentence!)

The "basically just equivalent to an English wish phrasing" rhetoric appears to be making fun of someone, but I can't tell who the target of the derision is supposed to be, because [I'm not aware of anyone](https://www.lesswrong.com/posts/jq5WAQEboeufkxzsg/imaginary-positions) who has an opinion about loss functions that could even be caricatured that way. A couple sentences later, the author mocks the idea of "train[ing] a giant stack of transformer layers on a dataset of agents doing nice things and not bad things", as if proponents of this cognitive task automation design are the same people who purportedly think that loss functions are English wish phrasings. But automating cognitive tasks by approximating a dataset of agents doing the tasks ... seems to mostly work? If there's some sort of theoretical barrier implying all such designs are doomed, 180 million ChatGPT users haven't seemed to notice.

There would appear to be some sort of disconnect here. The "List of Lethalities" author seems preoccupied with the possibility of general computer agents—machines that have unboundedly want things in the real world as humans do, and are more competent than us at getting them. I absolutely agree that this presents a serious risk of human extinction. (We've incidentally driven other species extinct; there's no apparent reason why our creations wouldn't do the same to us, unless we design them not to want to.)

[TODO—
 * But his discussion of contemporary statistical modeling techniques (which he sees a dread harbinger) seems predicated on a particular threat model, where "outer" training results in an "inner" intelligence with arbitrary goals; something that doesn't just interpolate behaviors, but actively models and plans.
 * I guess that's possible? I can't rule it out! Maybe it would happen at some scale? https://www.lesswrong.com/posts/6mysMAqvo9giHC4iX/what-s-general-purpose-search-and-why-might-we-expect-to-see
 * But taking contemporary ML "at face value", that's not my default guess: I'd imagine someone deliberately building an agent using function-approximators as a key component, rather than your function-approximator secretly having an agent inside.
 * That's a different threat model! If you're trying to engineer an aligned agent, or considering coordination/regulatory solutions to prohibit people from building unaligned agents, it matters what your threat model is!
 * Worked example: AlphaZero. Policy and value function-approximators work together with tree search in a comprehensible way. It's not just one opaque neural net.
 * Be specific about how AlphaZero can learn better-than-human Go, while the networks are still approximatey and not agenty
  * One moral: "supervise processes, not outcomes"—optimizing purely for reward button presses with no other constraints would not do what you want; but simulating human experts is not that; it's a distinct moral from "DL is bad; you need an entirely different theory of optimization to not die"

https://thezvi.wordpress.com/2023/05/31/to-predict-what-happens-ask-what-happens/
https://www.lesswrong.com/posts/KJRBb43nDxk6mwLcR/ai-doom-from-an-llm-plateau-ist-perspective

Jack—
> from my side it feels like trying to discuss crash test methodology with people who insist that the wheels must be made of little cars, because how else would they move forward like a car does?

]


### Bibliography

Bardo, Richard S., and Andrew G. Sutton. 2024. _Reinforcement Learning_. 2nd ed. Cambridge, MA: MIT Press.

Bishop, Christopher M., and Andrew M. Bishop. 2024. _Deep Learning: Foundations and Concepts_. Cambridge, UK: Cambridge University Press. _https://www.bishopbook.com/_

Mnih, Volodymyr, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. 2013. "Playing Atari with Deep Reinforcement Learning." _https://arxiv.org/abs/1312.5602_

Prince, Simon J.D. 2023. _Understanding Deep Learning_. Cambridge, MA: MIT Press. _http://udlbook.com_
