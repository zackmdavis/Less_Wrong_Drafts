## And All the Shoggoths Merely Players: Another Debate in One Act

### Scene 0: Prologue

_[Setting: a suburban house, in cross-section: the house's front wall divides the stage in half. On the audience's left, a dishevelled **Doomimir** sits in an easy chair, facing a television. On the audience's right, we see the front porch.]_

**Doomimir**: It wasn't supposed to end like this. Not like this. I was made for a better world ...

[_**Simplicia** enters stage left. She rings the doorbell._]

**Doomimir**: Who is it?

**Simplicia**: Simplicia Optimistovna Dobraya.

**Doomimir**: _[muttering as he goes to the door]_ Good-hearted daughter of a fool ... _[opening the door]_ Well? What do you want?

**Simplicia**: _[disturbed by his appearance]_ Doomimir Doomovitch, have you been drinking?

**Doomimir**: _[insulted]_ What do you take me for?

**Simplicia**: _[even more disturbed]_ Doomimir Doomovitch, have you been watching television?

**Doomimir**:  _[shrugging]_ Yes. _[gruffly]_ Again, what do you want?

**Simplicia**: I can't stop thinking about [our last conversation](https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act). It was kind of all over the place. I'd like to continue, but focusing in narrower detail on a couple points I'm still confused about.

**Doomimir**: And why should I bother tutoring an Earth woman in alignment theory? If you didn't get it from the empty string, and you didn't get it from our last discussion, why should I have any hope of you learning this time? And even if you did, [what good would it do?](https://www.lesswrong.com/posts/4Gcz3fGcYmmzhozxr/hashing-out-long-standing-disagreements-seems-low-value-to) You're a rando with no political power or scientific credentials. Are _you_ to stop Magma from destroying the world?

**Simplicia**: My mother named me Simplicia, over my father's objections, on account of my unexpectedly low polygenic scores. I am aware of my ... _[she hesitates and coughs, as if choking on the phrase]_ learning disability.

**Doomimir**: Then why are you here?

**Simplicia**: _[serenely]_ If the world is ending either way, I think it's more dignified that I understand exactly why. _[A beat.]_ Sorry, that doesn't explain what's in it for you. That's why I had to ask.

**Doomimir**: What _is_ it in for me?

**Simplicia**: _[going through her wallet]_ Two thousand rubles?

**Doomimir**: As you say. If this world is ending either way. _[He takes the money and shuts the door.]_

_[Simplicia beams and gives the audience a thumbs-up.]_

### Scene 1: The Drunk Actress

_[Later, inside the house. Doomimir has washed up and seems to be in a relatively better mood.]_

**Doomimir**: What are you confused about? I mean, that you wanted to talk about.

**Simplicia**: You seemed really intent on that "alien actress" intuition pump against human-imitation-based alignment strategies, which seemed unmotivated.

**Doomimir**: Unmotivated? You know that LLMs that emit plausibly human-written text aren't human. Thus, the AI is not the character it's playing. Similarly, being able to predict the conversation in a bar, doesn't make you drunk. [What's there not to get](https://twitter.com/ESYudkowsky/status/1633219449724760065), even for you?

**Simplicia**: Why doesn't the "predicting barroom conversation doesn't make you drunk" analogy falsely imply "predicting the answers to modular arithmetic problems doesn't mean you implement modular arithmetic"?

**Doomimir**: To predict the conversation in a bar, you need to know everything the drunk people know, separately and in addition to everything you know. Being drunk yourself would just get in the way. Mod arithmetic isn't like that; there's nothing besides the knowledge to not implement.

**Simplicia**: But we only need our AI to compute friendly behavior, not necessarily to have some epiphenominal subjective _quale_ of niceness. As far as safety properties go, we don't care whether the actress is "really drunk" as long as she stays in character. 

**Doomimir**: _[scoffing]_ Have you [tried imagining any internal mechanisms at all](https://twitter.com/ESYudkowsky/status/1743688927238934876) other than a bare inclination to emit the outward behavior you observe?

**Simplicia**: _[unfazed]_ Sure, let's talk about internal mechanisms. The reason I chose modular arithmetic as an example is because it's a task for which we have [good interpretability results](https://arxiv.org/abs/2301.05217). Train a shallow transformer on a subset of the addition problems modulo some fixed prime. The network learns to map the inputs onto a circle in the embedding space, and then does some trigonometry to extract the [residue](https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence_classes), much as one would count forward on the face of an analog clock.

Alternatively, with a slightly different architecture that has a harder time with trig, [it can learn a different algorithm](https://arxiv.org/abs/2306.17844): the embeddings are still on a circle, but the answer is computed by looking at the average of the embeddings. On the face of an analog clock, the internal midpoints between distinct numbers that sum to 6 mod 12—that's 2 and 4, or 1 and 5, or 6 and 12, or 10 and 8, or 11 and 7—all lie on the line connecting 3 and 9. In this way, the sum-mod-_p_ of two numbers can be determined by which line the midpoint of the inputs falls on—as long as the inputs aren't on opposite sides of the circle, where all the lines meet. But the network compensates for such antipodal points by also learning another circle in a different subspace of the embedding space where inputs that are antipodal on the first circle are close together on the second, and using that for error correction.

**Doomimir**: Cute results. Excellent work—by Earth standards. What's your point?

**Simplicia**: It's evidence about the feasibility of learning desired behavior from training data. You seem to think that it's hopelessly naïve to imagine that training on "nice" data could result in generalizably nice behavior—that the only reason someone might think that was a viable path was is if they were engaging in [magical reasoning about surface similarities](https://www.lesswrong.com/posts/6ByPxcGDhmx74gPSm/surface-analogies-and-deep-causes). I think it's germane to point out that at least for this toy problem, we have a concrete, non-magical story about how stochastic gradient descent on training data discovers a correct algorithm that also does well on a test set.

For non-toy problems, we don't have such good interpretability results to give us confidence that our optimizer found a correct algorithm. But empirically, deep learning can hit very precise behavioral targets: the vast hypermajority of programs can't speak fluent English or generate beautiful photorealistic images.

[TODO—
 * We _can_ hit precise targets in images and text: finding a network that generates "more like this".
 * Worried about misalignment are worried about mis-generalization.
 * "leaving one thing out" / tiny molecular smileyfaces
 * It wasn't obvious in 2008 that the computational universe would be this kind
 * What if you can do the same thing for increasingly long-horizon planning? If you can learn a "good person" input-output function from data, that might be "enough" alignment (even if the function isn't human and isn't the superintelligence at the end of time)
 * "solve human-comprehensible tasks, composed along human-comprehensible interfaces" https://www.greaterwrong.com/posts/fRSj2W4Fjje8rQWm9/thoughts-on-sharing-information-about-language-model
]

**Doomimir**: Your mother named you well.

**Simplicia**: That may be so, but making fun of my learning disability is _not a counterargument_ and _you know it_. I'm not confident about any of this! But while the world is still here, I think it's more dignified that I try to understand, and I'm _trying to understand_.

[TODO: Simplica—counterargument to "just get in the way. Mod arithmetic isn't like that; there's nothing besides the knowledge to not implement"; repeating "The actress is not the character" as a slogan doesn't answer. Reply!]

[TODO: Doomimir—having a model of the thing isn't the only way to make good predictions about the thing; intelligence creates domain shifts; the natural generalization may not be the desired one; the correct theory pointing at the human simulator; general, retargetable search should exist]
[TODO: Simplicia—is this a falsifiable claim that generalization will work differently for "tru intellignece" than it does for language?]

### Scene 2: Uses of the Evolution Analogy


**Doomimir**: It's our only datapoint!

[TODO—sketch of the real-world arguments I'm covering—
 * Belrose claims that Yudkowsky's theory predicts that larger networks should be less likely to generalize well, because they represent a larger space of functions
 * My gloss: why doesn't the "predicting bar conversations doesn't make you drunk" analogy also imply "predicting the answers to mod arithmetic problems doesn't mean you implement mod arithmetic", a failed prediction?
 * Yudkowsky's reply: predicting bar conversations mean you already know what the drunk person knows, but being drunk yourself would get in the way. For mod arithmetic, there's no desideratum there besides knowledge.
 * My elaboration: and specifically, "get in the way" means there's a gradient pointing towards making the emulation subservient to the "real goal"
 * Yudkowsky: the first algorithms found by a greedy optimizer that cover the training but not the test distribution, are facts about the distributions and the optimizer; the vast space of functions is only relevant in the part where, given that you missed the test distribution, there's lots of things to want
 * Yudkowsky: I predict that the shortest program that does mod arithmetic up to a googol will generalize, whereas we saw that the evolution of humans didn't. The difference is about domain divergence and optimizer.
 * My question: but how do we know that the AI domain divergence will be more like the evolutions and less like mod arithmetic? Is it just about complexity (there's only one "obvious" completion of the mod-arithmetic problems)? But natural language is really complex, and LLMs seem to be generalizing pretty great
 * Yudkowsky: the point of bringing up evolution is that it debunks the naive belief that an outer optimizer imbues the same utility function on an inner optimizer.
 * My note: I think Turner's "reward is not the optimization target" is correct here. We don't even want language models to "minimize cross-entropy" in general—whatever that would even mean! The correct behavior comes from the training data, not the loss function. (RL might complicate this?)
 * Yudkowsky: 0th-order vs. 1st-order optimizers should both mess up for generalizable reasons
 * My confusion: uh, gradients seem like a big deal? (Qualitatively, deep-learning from data seems a lot more flexible than selectively breeding animals.) On the other hand, "Loss Landscapes Are All You Need" suggests that the secret of generalization is that flat minima occupy more volume.
 * Yudkowsky: 'My arguments against SGD exactly mirroring quoted outer functions generating particular rewards, to inner psychological pursuit of the quoted reward function generalizing across distributions, include, "If you train a mind to exactly predict text from many individual drunks, it will not thereby become drunk" and "Actually you're still doing greedy local search and it's gonna hit on local correlates again" and "Just like weird shit went wrong with natural selection, we should also expect different weird shit to go wrong with SGD"'
 * planning is recursive, retargetable search: https://www.lesswrong.com/posts/6mysMAqvo9giHC4iX/what-s-general-purpose-search-and-why-might-we-expect-to-see
 * https://www.greaterwrong.com/posts/aaYZM4kLdHP3pwtfQ/on-the-lethality-of-biased-human-reward-ratings
 * https://www.greaterwrong.com/posts/xzFQp7bmkoKfnae9R/but-exactly-how-complex-and-fragile
]


make sure to use "the trick that never works" re biology and AI comparisons!!