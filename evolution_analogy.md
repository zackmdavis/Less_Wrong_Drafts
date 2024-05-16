_[Scene: a suburban house, a minute after the conclusion of ["And All the Shoggoths Merely Players"](https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players). **Doomimir** returns with his package, which he places by the door, and turns his attention to **Simplicia**, who has been waiting for him.]_

**Simplicia**: Right. To recap for _[coughs]_ no one in particular, when we left off _[pointedly, to the audience]_ one minute ago, Doomimir Doomovitch, you were expressing confidence that approaches to aligning artificial general intelligence within the current paradigm were almost certain to fail. You don't think that the apparent tractability of getting contemporary generative AI to do what humans want bears on that question. But you did say you have empirical evidence for your view, which I'm excited to hear about!

**Doomimir**: Indeed, Simplicia Optimistovna. My empirical evidence is the example of the evolution of human intelligence. You see, humans were optimized for one thing only: inclusive genetic fitness—

[**Simplicia** turns to the audience and makes a face.]

**Doomimir**: _[annoyed]_ What?

**Simplicia**: When you said you had empirical evidence, I thought you meant empirical evidence _about AI_, not the same analogy to an unrelated field that I've been hearing for the last fifteen years. You know: ArXiv papers about SGD's inductive biases, or adversarial training, or singular learning theory, or mechanistic interpretability ... something, anything at all, from this century, that engages with what we've learned from the experience of actually building artificial minds.

**Doomimir**: That's one of the many things you Earthlings refuse to understand. You didn't build that.

**Simplicia**: What?

**Doomimir**: Deep learning isn't a science _or_ an engineering discipline. The capabilities advances that your civilization's AI guys have been turning out these days haven't come from a deeper understanding of cognition, but by fueling generic optimization methods with ever-larger blobs of compute; the actual engineering work is being done by gradient descent. The autogenocidal maniac Richard Sutton calls it [the bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).

**Simplicia**: I don't think that's quite the correct reading of the bitter lesson. Sutton is advocating general methods that scale with compute, rather than hard-coding human domain knowledge, but that doesn't mean that we're ignorant of what those general methods are doing. One of the examples Sutton gives is computer chess, where minimax search with optimizations like alpha–beta pruning prevailed over trying to explicitly encode what human grandmasters know. But that seems fine: we specified how to search the game tree; delegating the details to the machine is the point. A broadly similar moral could apply to using deep learning to [approximate complicated functions between data distributions](https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation): we specify the training distribution, and delegate the details of fitting it to a network architecture with the appropriate invariances. I don't understand how you can say this isn't science or engineering. There's a whole literature—

**Doomimir**: The literature doesn't help if your civilization's authors aren't even asking the questions we need to answer. If you're so sure the deep learning literature has something to say about alignment, name three examples.

**Simplicia**: My mother named me Simplicia, over my father's objections, on account of my unexpectedly low polygenic scores. I'm not an expert qualified to solve the problem myself. But just from common sense, it seems like the problem of aligning AI is going to involve detailed familiarity with how AI works. Why would you expect to eyeball it from your armchair and declare the whole thing intractable on the basis of an analogy to biological evolution, which is just not the same thing as ML training?

**Doomimir**: So that's a no, then.

[TODO EDIT/REWRITE—maybe give the shattered gradients explanation to Simplicia, and then have Doomimir contest its relevance? I enjoy the Informed Disability conceit, and I don't want to strawman the MIRI side by portraying Doomimir as ignorant, but it's more consistent if Simplicia is the one who introduces textbook/ArXiv points. Plus, the more Simplicia knows, the funnier the Informed Disability conceit is.]

**Simplicia**: I don't know what you expect me to say as a non-specialist. _[weakly]_ I was reading about resnets the other day—

**Doomimir**: _[smugly]_ That's actually a great example, Simplicia. The researchers of your world noticed that deeper networks were harder to train because [the gradient varied too quickly with respect to the input](https://arxiv.org/abs/1702.08591)—the loss landscape a mottled fractal of tiny mountains, rather than a smooth valley to descend. This is mitigated by introducing residual connections that skip some layers of the network, creating shorter paths through the network, which reduces the volatility of the gradients.

I don't deny that you can write many dissertations about such tricks to make generic optimizers more efficient. The problem is that that knowledge doesn't teach us _about intelligence_. Making your gradient-based optimizer more efficient doesn't help, if you don't know what program your optimizer is building—growing.

I often bring up human evolution because that's our _only example_ of an outer optimization loop producing an inner general intelligence. There are differences between gradient descent and natural selection, but I don't think the differences are relevant to the morals I draw.

As I was saying, the concept of fitness isn't represented anywhere in our motivations. That is, the "outer" optimization criterion that evolution selected for while creating us, bears no visible resemblance to the "inner" optimization criteria that we use when selecting our plans.

As optimizers get more powerful, anything that's not explicitly valued in the utility function won't survive [edge instantiation](https://arbital.com/p/edge_instantiation/). The connection between parental love and inclusive fitness has grown much weaker in the industrial environment than it was in the EEA, as more options have opened up for humans to prioritize their loved ones' well-being in ways that don't track the number of copies of their alleles. In a transhumanist utopia with mind uploading, it could break entirely, if we migrated our minds away from the biological substrate: if some other data storage format suited us better, why would we bother keeping around the specific molecule of DNA, which no one had heard of before the 19th or 20th century?

Of course, we're not going to get a transhumanist utopia with mind uploading, because history will repeat itself: the outer loss function that mad scientists use to grow AI will bear no resemblance to the inner goals of the resulting superintelligence.
