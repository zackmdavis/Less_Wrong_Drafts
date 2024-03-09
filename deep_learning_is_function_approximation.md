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

But multi-layer parameterized graphical function approximators created by iteratively improving the quality of the approximation by adjusting their parameters in the direction of the derivative of some error metric on some example input–output pair are still, actually, function approximators. ((f(x, θ) − y)² is a popular choice for the error metric, as is −log P(y | f(x, θ)).) Piecewise-linear functions are still piecewise-linear functions even when there are a lot of pieces. What did _you_ think it was doing?

### Multi-layer Parameterized Graphical Function Approximators Have Many Exciting Applications

To be clear, you can do a lot with function approximation!

For example, if you assemble a collection of desired input–output pairs (x, y) where the x is [an array of pixels depicting a handwritten digit](https://en.wikipedia.org/wiki/MNIST_database) and y is a character representing which digit, then you can fit a "convolutional" multi-layer parameterized graphical function approximator to approximate the function from pixel-arrays to digits—effectively allowing computers to read handwriting.

Such techniques have proven fruitful in all sorts of domains where a useful task can be conceptualized as a function from one data distribution to another: image synthesis, voice recognition, recommender systems—you name it. Famously, by approximating the next-token function in tokenized internet text, large language models can answer questions, write code, and perform other natual-language understanding tasks.

Dwelling on the peculiar reactions of some of my internet friends to these advances, I'm starting to wonder if some of these folks—not all, but many—just ... don't know very much about the technology in question? If you read about computer systems performing cognitive tasks previously thought to require intelligence, and futhermore that these systems are "trained" rather than coded in the manner of traditional computer programs, I could see how that could be alarming, evoking imagery of training a wild animal that might turn on us the moment it can sieze power and reward itself rather than being dependent on us.

But "training" is just a [suggestive name](https://www.lesswrong.com/posts/yxWbbe9XcgLFCrwiL/dreams-of-ai-alignment-the-danger-of-suggestive-names). It's true that we don't have a mechanistic understanding of how multi-layer parameterized graphical function approximators perform tasks, in contrast to traditional computer programs whose source code was written by a human. It's plausible that this opacity represents grave risks, if we create powerful systems that we don't know how to debug.

But whatever the real risks are, any hope of mitigating them is going to depend on acquiring the most accurate possible understanding of the problem. If the problem is itself largely one of our own lack of understanding, it helps to be _specific_ about exactly which parts we do and don't understand, rather than surrending the entire field to a blurry aura of mystery and despair.

### An Example of Applying Multi-layer Parameterized Graphical Function Approximators in Success-Antecedent Computation Boosting

One of the exciting things about multi-layer parameterized graphical function approximators is that they can be combined with other methods for the automation of cognitive tasks (which is often called "computing", but some authors say "artificial intelligence" for some reason).

In the spirit of being specific about exactly which parts we do and don't understand, I want to talk about [Mnih _et al._ 2013's work on getting computers to play classic Atari games](https://arxiv.org/abs/1312.5602), which is notable as one of the first high-profile examples of using multi-layer parameterized graphical function approximators in conjunction with success-antecdent computation boosting (which some authors call "reinforcement learning" for some reason).

I think some of my internet friends are in the habit of reading the news. And if you only read the news—if you're not in tune with there being things to read _besides_ news—I could see this result being quite alarming. Digital brains learning to play video games at superhuman levels _from the raw pixels_, rather than because a programmer sat down to write an agent for that particular game? What happens to humanity when AI can do that for more than games? Are we not [already in the shadow of the coming race](https://www.online-literature.com/george_eliot/theophrastus-such/17/)?

But people who read textbooks and not just news, being no less impressed by the result nor less concerned about the future of humanity, are often inclined to take a subtler lesson from any particular headline-grabbing advance.

Mnih _et al._ built off the technique of [Q-learning](https://en.wikipedia.org/wiki/Q-learning), introduced two decades earlier by Watkins 1989. Given a discrete-time present-state-based outcome-valued stochastic control problem (which some authors call a ["Markov decision process"](https://en.wikipedia.org/wiki/Markov_decision_process) for some reason), Q-learning concerns itself with acquiring a function Q(s, a) that describes the value of taking action a while in state s. For example, 

[TODO: briefly describe a gridworld MDP]

Upon finding itself in a particular state s, an agent will usually perform the action with the highest Q(s, a), ["exploiting"](https://en.wikipedia.org/wiki/Exploration-exploitation_dilemma) its current beliefs about the environment, but [with some probability](https://en.wikipedia.org/wiki/Multi-armed_bandit#Approximate_solutions) it will "explore" by taking some other random action. The outcomes of its decisions are used to update the function Q(s, a), which can simply be stored in a table with as many rows as there are possible states and as many columns as there are possible actions. We have theorems to the effect that as the agent thoroughly explores the environment, it will eventually converge on the correct Q(s, a).

But Q-learning as originally proposed by Watkins doesn't work for Atari games (like _Pong_, _Breakout_, or _Space Invaders_), because it assumes that the s in Q(s, a) belongs to a discrete set that could be stored in a table. This is intractable for problems where the state of the environment varies continuously. If a "state" in _Pong_ is a 6-tuple of floating-point numbers representing the player's paddle position, the opponent's paddle position, and the x- and y-coordinates of the ball's position and velocity, then there's no way for the traditional Q-learning algorithm to base its behavior on its past experiences without having already seen that exact conjunction of paddle positions, ball position, and ball velocity. So Mnih _et al._'s great innovation was—

(Wait for it ...)

—to replace the table representing Q(s, a) with a multi-layer parameterized graphical function approximator! By approximating the mapping from state–action pairs to discounted-sums-of-rewards, the "neural network" allows the agent to "generalize" from its experience, taking similar actions in relevantly similar states, without having experienced those exact states before. There are [a few other minor technical details](https://www.lesswrong.com/posts/kyvCNgx9oAwJCuevo/deep-q-networks-explained) needed to make it work well, but that's the big idea.

And understanding the big idea probably changes your perspective on the headline-grabbing advance. (It certainly did for me.) "Deep learning is like evolving brains; it solves problems [and we don't know how](https://www.vox.com/unexplainable/2023/7/15/23793840/chat-gpt-ai-science-mystery-unexplainable-podcast)" is an importantly different story from "We swapped out a table for a multi-layer parameterized graphical function approximator in this success-antecdent computation boosting algorithm, and now it can handle continuous state spaces," separately from the question of whether both stories end with all the humans being dead.

### Risks From Learned Approximation

If I agree with my internet friends that 

[TODO—

if the world is ending either way

 * If I'm skeptical of the "DL is like scary evolving brains"/"your fn-approximator must secretly have a consequentialist homonuculus inside of it" pitch that my internet friends use, does that mean I disagree that risk is low?
 * There's a quip among practioners that says, "If you're surprised by your neural net's behavior, that means you didn't examine your training data closely enough."
 * Inner alignment is empirically just not that bad of a problem??
 * On this view, what's important is broadly understanding how your net generalizes, which is not necessarily the same thing as 100% mechinterp. 
 * If applications keep getting more complicated between now and the superintelligence at the end of time, at some point, you're going to run into situations where you can't examine the training data.
 * Example: AlphaZero—by simulating a zillion games, its value network can approximate the board-position→win-probability function and see moves that we can't see. That's not going to work in domins where we want something complicated rather than "win at go", which was simple to specify.
 * One moral: "supervise processes, not outcomes"—optimizing purely for reward button presses with no other constraints would not do what you want; but simulating human experts is not that; it's a distinct moral from "DL is bad; you need an entirely different theory of optimization to not die"
 * Another moral: cobbling together an agent using function-approximators as a key component (a lá AlphaZero) presents a different _risk model_ than "your function approximator secretly has an agent inside of it". Understanding the risk is key to mitigating it (whether that's by solving alignment, or gathering the evidence to convince people to stop)

 * building agents out of function approximators, vs. function approximators necessarily having an agent inside

Jack—
> from my side it feels like trying to discuss crash test methodology with people who insist that the wheels must be made of little cars, because how else would they move forward like a car does?

]


### Bibliography

Bardo, Richard S., and Andrew G. Sutton. 2024. _Reinforcement Learning_. 2nd ed. Cambridge, MA: MIT Press.

Bishop, Christopher M., and Andrew M. Bishop. 2024. _Deep Learning: Foundations and Concepts_. Cambridge, UK: Cambridge University Press. _https://www.bishopbook.com/_

Mnih, Volodymyr, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. 2013. "Playing Atari with Deep Reinforcement Learning." _https://arxiv.org/abs/1312.5602_

Prince, Simon J.D. 2023. _Understanding Deep Learning_. Cambridge, MA: MIT Press. _http://udlbook.com_

Watkins, C.J.C.H. 1989. _Learning from Delayed Rewards_. PhD Thesis, University of Cambridge, England.
