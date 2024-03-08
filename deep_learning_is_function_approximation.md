## "Deep Learning" Is Function Approximation

### A Surprising Development in the Study of Multi-layer Parametrized Graphical Function Approximators

As a programmer and epistemology enthusiast, I've been studying some statistical modeling techniques lately! It's been boodles of fun, and might even prove useful in a future dayjob if I decide to pivot my career away from the backend web development roles I've taken in the past.

Separately, a lot of my friends seem to belong to some sort of ... internet fanfiction cult? I'm still not entirely sure what it's about, but it seems harmless. Takes all sorts, I guess. Coincidentally, many of these people seem to be very excited about the same statistical modeling techniques that I've been learning about!

It's strange, though—when I explain what I've been studying, a lot of these folks start to _talk funny_—almost as if they've been taught to revere statistical modeling as a grave matter of eschatological importance, without having spent any time using statistical models? I don't get it.

The other week I was talking to one of these people about some things I learned from [the new Simon Prince book](https://udlbook.github.io/udlbook/) about multi-layer parametrized graphical function approximators (which some authors call "deep neural networks" for some reason), which map inputs to outputs via a sequence of affine transformations composed with nonlinear "activation" functions. It's a curve-fitting technique: by setting the multiplicative factors and additive terms appropriately, multi-layer parametrized graphical function approximators can [represent a vast space of functions](https://en.wikipedia.org/wiki/Universal_approximation_theorem). For a popular choice of "activation" function [which takes the maximum of the input and zero](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)), the curve is specifically a piecewise-linear function.

Basically, the big empirical surprise of [the previous decade](https://bmk.sh/2019/12/31/The-Decade-of-Deep-Learning/) is that given a lot of desired input–output pairs (x, y)  and the proper engineering know-how, you can use large amounts of computing power to find parameters θ to fit a multi-layer parametrized graphical function approximator f(x, θ) that "generalizes" well—meaning that if you compute ŷ = f(x, θ) for some x that wasn't in any of your original example input–output pairs (which some authors call "training" data for some reason), it turns out that ŷ is usually pretty similar to the y you would have used in an example (x, y) pair.

It wasn't obvious beforehand that this would work! You'd expect that if your multi-layer parametrized graphical function approximator has more parameters than you have example input–output pairs, it would [overfit](https://en.wikipedia.org/wiki/Overfitting), finding a complicated function that reproduced the example input–output pairs but outputted crazy nonsense elsewhere—the more expressive function-approximator proving useless for [the lack of evidence to pin down the correct approximation](https://www.lesswrong.com/posts/mB95aqTSJLNR9YyjH/message-length).

And that is what we see for multi-layer parametrized graphical function approximators with only slightly more parameters than example input–output pairs, but for _sufficiently large_ multi-layer parametrized graphical function approximators, [the trend reverses](https://www.lesswrong.com/posts/FRv7ryoqtvSuqBxuT/understanding-deep-double-descent) and "generalization" improves—the more expressive function-approximator proving useful after all, as it admits algorithmically simpler functions that fit the example pairs.

My associate seemed puzzled by this explanation, and asked, "What are the preconditions for this intuition about neural networks as function approximators?" (I paraphrase slightly.) "I would assume this is true under specific conditions," they continued, "but I don't think we should expect such niceness to hold under capability increases. Why should we expect this to carry forward?"

I don't know where this person was getting their information, but this made zero sense to me. I mean, okay, [when you increase the number of parameters](https://gwern.net/scaling-hypothesis) in your multi-layer parametrized graphical function approximator, it gets better at representing more complicated functions, which I guess you could describe as "capability increases"?

But multi-layer parametrized graphical function approximators with more parameters are still, actually, function approximators. Piecewise-linear functions are still piecewise-linear functions even when there are a lot of pieces. What some authors call "training" for some reason is just improving the quality of the approximation by adjusting the parameters in the direction of the derivative of some error metric on some example input–output pair. ((f(x, θ) − y)² is a popular choice.) What did _you_ think it was doing?

### Multi-layer Parametrized Graphical Function Approximators Have Many Exciting Applications

To be clear, you can do a lot with function approximation!

For example, if you assemble a collection of desired input–output pairs (x, y) where the x is [an array of pixels depicting a handwritten digit](https://en.wikipedia.org/wiki/MNIST_database) and y is a character representing which digit, then you can fit a "convolutional" multi-layer parametrized graphical function approximator to approximate the function from pixel-arrays to digits—effectively allowing computers to read handwriting.

Such techniques have proven fruitful in all sorts of domains where a useful task can be conceptualized as a function from one data distribution to another: image synthesis, voice recognition, recommender systems—you name it. Famously, approximating the next-token function in tokenized internet text, large language models can answer questions, write code, and perform other natual-language understanding tasks once thought to require strong artificial general intelligence.

Dwelling on the peculiar reactions of some of my internet friends to these advances, I'm starting to wonder if many of these folks just ... don't know very much about the technology in question? If you read about computer systems performing cognitive tasks previously thought to require intelligence, and futhermore that these systems are "trained" rather than coded in the manner of traditional computer programs, I could see how that could be alarming, evoking imagery of training a wild animal that might turn on us the moment it can sieze power and reward itself rather than being dependent on us.

But "training" is just a [suggestive name](https://www.lesswrong.com/posts/yxWbbe9XcgLFCrwiL/dreams-of-ai-alignment-the-danger-of-suggestive-names). It's true that we don't have a mechanistic understanding of how multi-layer parametrized graphical function approximators perform tasks, in contrast to traditional computer programs whose source code was written by a human. It's plausible that this opacity represents grave risks, if we create powerful systems that we don't know how to debug.


But whatever the real risks are,



It's a _problem_ if safety advocates haven't read the standard textbooks 







[TODO:
 * Maybe some people read about AI systems doing impressive things (true) and that they're "trained" rather than programmed (true), but then assume it's mysterious animal training a Mind (where who knows what could happen), rather than approximating a mapping between probability distributions, that fills a particular functional role in a system
 * Simon Prince does not think of himself as building agents
 * It's a _problem_ if safety advocates don't even know what the standard textbooks say!! (Both for the activism to be grounded in reality, and just for being convincing)
   * You heard about DeepMind doing Atari
   * That was based on Q-learning, which involves a function Q(s, a) "the quality of taking action a in state s". For a simple MDP, you just store these values in a table and update them.
   * That won't work for Atari, because the table format doesn't work for a video game
   * DQN just replaces the table with a multi-layer parametrized graphical function approximators. There are a few other bells and whistles that make it work well.
   * The net enables generalization: you can do similar things in similar states, whereas the table required you to have already visited that state before to have a good estimate
   * The story of "DL is like evolving brains; it solves problems and we don't know how it works, scary" is a different story from "oh, they replaced the table with an NN in this specific algorithm, and now it can handle continuous state spaces"
]

### Risks From Learned Approximation

[TODO—
 * If I'm skeptical of the "DL is like scary evolving brains"/"your fn-approximator must secretly have a consequentialist homonuculus inside of it" pitch that my internet friends use, does that mean I disagree that risk is low?
 * There's a quip among practioners that says, "If you're surprised by your neural net's behavior, that means you didn't examine your training data closely enough."
 * Inner alignment is empirically just not that bad of a problem??
 * On this view, what's important is broadly understanding how your net generalizes, which is not necessarily the same thing as 100% mechinterp. 
 * If applications keep getting more complicated between now and the superintelligence at the end of time, at some point, you're going to run into situations where you can't examine the training data.
 * Example: AlphaZero—by simulating a zillion games, its value network can approximate the board-position→win-probability function and see moves that we can't see. That's not going to work in domins where we want something complicated rather than "win at go", which was simple to specify.
 * One moral: "supervise processes, not outcomes"—optimizing purely for reward button presses with no other constraints would not do what you want; but simulating human experts is not that; it's a distinct moral from "DL is bad; you need an entirely different theory of optimization to not die"
 * Another moral: cobbling together an agent using function-approximators as a key component (a lá AlphaZero) presents a different _risk model_ than "your function approximator secretly has an agent inside of it". Understanding the risk is key to mitigating it (whether that's by solving alignment, or gathering the evidence to convince people to stop)
]


### Bibliography

Bardo, Richard S., and Andrew G. Sutton. 2024. _Reinforcement Learning_. 2nd ed. Cambridge, MA: MIT Press.

Bishop, Christopher M., and Andrew M. Bishop. 2024. _Deep Learning: Foundations and Concepts_. Cambridge, UK: Cambridge University Press. _https://www.bishopbook.com/_

Prince, Simon J.D. 2023. _Understanding Deep Learning_. Cambridge, MA: MIT Press. _http://udlbook.com_
