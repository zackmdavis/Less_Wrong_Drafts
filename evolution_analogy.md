_[Scene: a suburban house, a minute after the conclusion of ["And All the Shoggoths Merely Players"](https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players). **Doomimir** returns with his package, which he places by the door, and turns his attention to **Simplicia**, who has been waiting for him.]_

**Simplicia**: Right. To recap for _[coughs]_ no one in particular, when we left off _[pointedly, to the audience]_ one minute ago, Doomimir Doomovitch, you were expressing confidence that approaches to aligning artificial general intelligence within the current paradigm were almost certain to fail. You don't think that the apparent tractability of getting contemporary generative AI techniques to do what humans want bears on that question. But you did say you have empirical evidence for your view, which I'm excited to hear about!

**Doomimir**: Indeed, Simplicia Optimistovna. My empirical evidence is the example of the evolution of human intelligence. You see, humans were optimized for one thing only: inclusive genetic fitness—

[**Simplicia** turns to the audience and makes a face.]

**Doomimir**: _[annoyed]_ What?

**Simplicia**: When you said you had empirical evidence, I thought you meant empirical evidence _about AI_, not the same analogy to an unrelated field that I've been hearing for the last fifteen years. I was hoping for, you know, ArXiv papers about SGD's inductive biases, or online regret bounds, or singular learning theory ... something, anything at all, from this century, that engages with what we've learned from the experience of actually building artificial minds.

**Doomimir**: That's one of the many things you Earthlings refuse to understand. You didn't build that.

**Simplicia**: What?

**Doomimir**: The capabilities advances that your civilization's AI guys have been turning out these days haven't come from a deeper understanding of cognition, but by improvements to generic optimization methods, fueled with ever-increasing investments in compute. Deep learning not only [isn't a science](https://www.lesswrong.com/posts/JcLhYQQADzTsAEaXd/ai-as-a-science-and-three-obstacles-to-alignment-strategies), it isn't even an engineering discipline in the traditional sense: the opacity of the artifacts it produces has no analogue among bridge or engine designs. In effect, all the object-level engineering work is being done by gradient descent.

The autogenocidal maniac Richard Sutton calls this [the bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), and attributes the field's slowless to embrace it to ego and recalcitrance on the part of practioners. But in accordance with [the dictum to feel fully the emotion that fits the facts](https://www.yudkowsky.net/rational/virtues), I think bitterness is appropriate. It makes sense to be bitter about the shortsighted adoption of a fundamentally unalignable paradigm on the basis of its immediate performance, when a saner world would notice the glaring [foreseeable difficulties](https://arbital.com/p/foreseeable_difficulties/) and coordinate on Something Else Which Is Not That.

**Simplicia**: I don't think that's quite the correct reading of the bitter lesson. Sutton is advocating general methods that scale with compute in preference to hand-coding human domain knowledge, but that doesn't mean that we're ignorant of what those general methods are doing. One of the examples Sutton gives is computer chess, where [minimax search](https://en.wikipedia.org/wiki/Negamax) with optimizations like [α–β pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) prevailed over trying to explicitly encode what human grandmasters know about the game. But that seems fine. Writing a program that thinks about tactics the way humans do rather than [letting tactical play emerge from searching the game tree](http://zackmdavis.net/blog/2019/05/minimax-search-and-the-structure-of-cognition/) would be a lot more work for less than no benefit.

A broadly similar moral could apply to using deep learning to [approximate complicated functions between data distributions](https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation): we specify the training distribution, and the details of fitting it are delegated to a network architecture with the appropriate invariances: convolutional nets for processing image data, transformers for variable-length sequences. There's a whole literature—

**Doomimir**: The literature doesn't help if your civilization's authors aren't asking the questions we need answered in order to not die. What, specifically, am I supposed to learn from your world's literature? Give me an example.

**Simplicia**: I'm not sure what kind of example you're looking for. Just from common sense, it seems like the problem of aligning AI is going to involve intimate familiarity with the nitty-gritty empirical details of how AI works, for the same reason that building a rocket that doesn't blow up involves intimate familiarity with the nitty-gritty empirical details of rocketry. Why would you expect to eyeball the problem from your armchair and declare the whole thing intractable on the basis of an analogy to biological evolution, which is just not the same thing as ML training?

Picking something arbitrarily ... well, I was reading about residual networks recently. Deeper neural networks were found to be harder to train because [the gradient varied too quickly with respect to the input](https://arxiv.org/abs/1702.08591). Being the result of a many-fold function composition, the loss landscape in very deep networks becomes a mottled fractal of tiny mountains, rather than a smooth valley to descend. This is mitigated by introducing "residual" connections that skip some layers, creating shorter paths through the network which have less volatile gradients.

I don't understand how you can say this isn't science or engineering. It's a comprehensible explanation for why one design of information-processing system works better than alternatives, grounded in observation and mathematical reasoning. There are dozens of things like that. What did you expect the science of artificial minds to look like, exactly?

**Doomimir**: _[incredulous]_ _That's_ your example? Resnets?

**Simplicia**: ... sure?

**Doomimir**: By [conservation of expected evidence](https://www.lesswrong.com/posts/jiBFC7DcCrZjGmZnJ/conservation-of-expected-evidence), I take your failure to cite anything relevant as further confirmation of my views. I've never denied that you can write many dissertations about such tricks to make generic optimizers more efficient. The problem is that that knowledge brings us closer to being able to brute-force general intelligence, without teaching us _about intelligence_. What program are all those gradient updates building inside your network? How does it work?

**Simplicia**: _[uncomfortably]_ [People are working on that.](https://arxiv.org/abs/2404.14082)

**Doomimir**: Too little, too late. The reason I often bring up human evolution is because that's our only example of an outer optimization loop producing an inner general intelligence, which sure looks like the path your civilization is going down. Yes, there are differences between gradient descent and natural selection, but I don't think the differences are relevant to the morals I draw.

As I was saying, the concept of fitness isn't represented anywhere in our motivations. That is, the "outer" optimization criterion that evolution selected for while creating us, bears no visible resemblance to the "inner" optimization criteria that we use when selecting our plans.

As optimizers get more powerful, anything that's not explicitly valued in the utility function won't survive [edge instantiation](https://arbital.com/p/edge_instantiation/). The connection between parental love and inclusive fitness has grown much weaker in the industrial environment than it was in the EEA, as more options have opened up for humans to prioritize their loved ones' well-being in ways that don't track the number of copies of their alleles. In a transhumanist utopia with mind uploading, it could break entirely as we migrated our minds away from the biological substrate: if some other data storage format suited us better, why would we bother keeping around the specific molecule of DNA, which no one had heard of before the 19th or 20th century?

Of course, we're not going to get a transhumanist utopia with mind uploading, because history will repeat itself: the outer loss function that mad scientists use to grow the first AGI will bear no resemblance to the inner goals of the resulting superintelligence.

**Simplicia**: You seem to have a basically ideological conviction that outer optimization—a category inclusive of natural selection and gradient descent—can't be used to shape the behaviors of the inner optimizers it produces. But this just seems flatly contradicted by experience. We train deep learning systems for incredibly specific tasks all the time, and it works fantastically well.

Intuitively, I want to say that gradient descent works much better than evolution: I don't imagine succeeding at selectively breeding an animal that speaks perfect English the way LLMs do. Relatedly, we train LLMs from a blank slate, in contrast to how selective breeding only works with traits already present in the wild type; it's too slow to assemble adaptations from scratch. But even selective breeding basically works: we successfully domesticate loyal dogs and meaty livestock.
