## "Deep Learning" Is Function Approximation

### [TODO: introduction title]

As a programmer and epistemology enthusiast, I've been studying some statistical modeling techniques lately! It's been boodles of fun, and might even prove useful in a future dayjob if I decide to pivot my career away from the backend web development roles I've taken in the past.

Separately, a lot of my friends seem to belong to some sort of ... internet fanfiction cult? I'm still not entirely sure what it's about, but it seems harmless. Takes all sorts, I guess. Coincidentally, many of these people seem to be very excited about the same statistical modeling techniques that I've been learning about!

It's strange, though—when I explain what I've been studying, a lot of these folks start to _talk funny_—almost as if they've been taught to revere statistical modeling as a grave matter of eschatological importance, without having spent any time using statistical models? I don't get it.

The other week I was talking to one of these people about some things I learned from [the new Simon Prince book](https://udlbook.github.io/udlbook/) about multi-layer parametrized graphical function approximators (which some authors call "deep neural networks" for some reason).

[TODO— the big surprise of deep learning
Historically, 
> vgiven a lot of (x, y) data, we’re shockingly good at using lots of compute to find θ to fit a function f[x, θ] that generalizes to unseen y
literally curve-fitting
ReLU activations, it's piecewise linear
]

"What are the preconditions for this intuition about neural networks as function approximators?" asked my associate. (I paraphrase slightly.) "I would assume this is true under specific conditions, but I don't think we should expect such niceness to hold under capability increases. Why should we expect this to carry forward?"

I don't know where this person was getting their information, but this made zero sense to me. I mean, okay, [when you increase the number of parameters](https://gwern.net/scaling-hypothesis) in your multi-layer parametrized graphical function approximator, it gets better at representing more complicated functions, which I guess you could describe as "capability increases".

But multi-layer parametrized graphical function approximators with more parameters are still, actually, function approximators.

[TODO: transition sentence]

What did _you_ think it was doing?

### [TODO: title for § about applications]

To be clear, you can do a lot with function approximation!

[TODO:
 * straightforward or well-known examples of the "function approximation" frame paying rent
     * image classification (e.g. ImageNet or MNIST digits)
     * recommender systems
     * famously, approximating next-token prediction enables machines that can speak 

 * Maybe some people read about AI systems doing impressive things (true) and that they're "trained" rather than programmed (true), but then assume it's mysterious animal training a Mind (where who knows what could happen), rather than approximating a mapping between probability distributions, that fills a particular functional role in a system
   * You heard about DeepMind doing Atari
   * That was based on Q-learning, which involves a function Q(s, a) "the quality of taking action a in state s". For a simple MDP, you just store these values in a table and update them.
   * That won't work for Atari, because the table format doesn't work for a video game
   * DQN just replaces the table with a multi-layer parametrized graphical function approximators. There are a few other bells and whistles that make it work well.
   * The net enables generalization: you can do similar things in similar states, whereas the table required you to have already visited that state before to have a good estimate
   * The story of "DL is like evolving brains; it solves problems and we don't know how it works, scary" is a different story from "oh, they replaced the table with an NN in this specific algorithm, and now it can handle continuous state spaces"
]

### Risks From Learned Approximation

[TODO—
 * Simon Prince doesn't think of himself as building agents!
 * If I'm skeptical of the "DL is like scary evolving brains"/"your fn-approximator must secretly have a consequentialist homonuculus inside of it" pitch that my internet friends use, does that mean I disagree that risk is low?
 * There's a quip among practioners that says, "If you're surprised by your neural net's behavior, that means you didn't examine your training data closely enough."
 * Inner alignment is empirically just not that bad of a problem??
 * On this view, what's important is broadly understanding how your net generalizes, which is not necessarily the same thing as 100% mechinterp. 
 * If applications keep getting more complicated between now and the superintelligence at the end of time, at some point, you're going to run into situations where you can't examine the training data.
 * Example: AlphaZero—by simulating a zillion games, its value network can approximate the board-position→win-probability function and see moves that we can't see. That's not going to work in domins where we want something complicated rather than "win at go", which was simple to specify.
 * One moral: "supervise processes, not outcomes"—optimizing purely for reward button presses with no other constraints would not do what you want; but simulating human experts is not that; it's a distinct moral from "DL is bad; you need an entirely different theory of optimization to not die"
 * Another moral: cobbling together an agent using function-approximators as a key component (a lá AlphaZero) presents a different _risk model_ than "your function approximator secretly has an agent inside of it". Understanding the risk is key to mitigating it (whether that's by solving alignment, or gathering the evidence to convince people to stop)
]