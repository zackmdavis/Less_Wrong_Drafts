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

**Simplicia**: I can't stop thinking about [our last conversation](https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act). It was kind of all over the place. If you're up for it, I'd like to continue, but focusing in narrower detail on a couple points I'm still confused about.

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

**Simplicia**: You seemed really intent on a particular intuition pump against human-imitation-based alignment strategies, where you compared AI to an alien actress. I didn't find that compelling.

**Doomimir**: But you claim to understand that LLMs that emit plausibly human-written text aren't human. Thus, the AI is not the character it's playing. Similarly, being able to predict the conversation in a bar, doesn't make you drunk. [What's there not to get](https://twitter.com/ESYudkowsky/status/1633219449724760065), even for you?

**Simplicia**: Why doesn't the "predicting barroom conversation doesn't make you drunk" analogy falsely imply "predicting the answers to modular arithmetic problems doesn't mean you implement modular arithmetic"?

**Doomimir**: To predict the conversation in a bar, you need to know everything the drunk people know, separately and in addition to everything you know. Being drunk yourself [would just get in the way](https://twitter.com/ESYudkowsky/status/1744061053754032634). Similarly, predicting the behavior of nice people isn't the same thing as being nice. Modular arithmetic isn't like that; there's nothing besides the knowledge to not implement.

**Simplicia**: But we only need our AI to compute nice behavior, not necessarily to have some internal structure corresponding to the _quale_ of niceness. As far as safety properties go, we don't care whether the actress is "really drunk" as long as she stays in character.

**Doomimir**: _[scoffing]_ Have you [tried imagining any internal mechanisms at all](https://twitter.com/ESYudkowsky/status/1743688927238934876) other than a bare, featureless inclination to emit the outward behavior you observe?

**Simplicia**: _[unfazed]_ Sure, let's talk about internal mechanisms. The reason I chose modular arithmetic as an example is because it's a task for which we have [good interpretability results](https://arxiv.org/abs/2301.05217). Train a shallow transformer on a subset of the addition problems modulo some fixed prime. The network learns to map the inputs onto a circle in the embedding space, and then does some trigonometry to extract the [residue](https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence_classes), much as one would count forward on the face of an analog clock.

Alternatively, with a slightly different architecture that has a harder time with trig, [it can learn a different algorithm](https://arxiv.org/abs/2306.17844): the embeddings are still on a circle, but the answer is computed by looking at the average of the embedding vectors of the inputs. On the face of an analog clock, the internal midpoints between distinct numbers that sum to 6 mod 12—that's 2 and 4, or 1 and 5, or 6 and 12, or 10 and 8, or 11 and 7—all lie on the line connecting 3 and 9. In this way, the sum-mod-_p_ of two numbers can be determined by which line the midpoint of the inputs falls on—as long as the inputs aren't on opposite sides of the circle, in which case their midpoint is in the center, where all the lines meet. But the network compensates for such antipodal points by also learning another circle in a different subspace of the embedding space, such that inputs that are antipodal on the first circle are close together on the second, which helps disambiguate the result.

**Doomimir**: Cute results. Excellent work—by Earth standards. What's your point?

**Simplicia**: It's evidence about the feasibility of learning desired behavior from training data. You seem to think that it's hopelessly naïve to imagine that training on "nice" data could result in generalizably nice behavior—that the only reason someone might think that was a viable path was is if they were engaging in [magical reasoning about surface similarities](https://www.lesswrong.com/posts/6ByPxcGDhmx74gPSm/surface-analogies-and-deep-causes). I think it's germane to point out that at least for this toy problem, we have a pretty concrete, non-magical story about how gradient descent on a training set discovers an algorithm that reproduces the training data and also generalizes correctly to the test set.

For non-toy problems, we don't have such good interpretability results to give us confidence that our optimizer found a correct algorithm. But empirically, deep learning _can_ hit very precise behavioral targets: the vast hypermajority of programs don't speak fluent English or generate beautiful photorealistic images, and yet GPT-4 and Midjourney exist.

If doing _that_ for "text" and "images" was a mere engineering problem, I don't see what fundamental theoretical barrier rules out the possibility of pulling off the same kind of thing for "friendly and moral real-world decisionmaking"—learning a "good person" function from data, much as Midjourney has learned a "good art" function.

It's true that diffusion models don't work like a human artist on the inside, but it's not clear why that matters? It would seem idle to retort, "Predicting what good art would look like, doesn't make you a good artist; having an æsthetic sense yourself would just get in the way", when you can actually use it to do a commissioned artist's job.

**Doomimir**: _[shaking his head]_ Your mother named you well.

**Simplicia**: _[defiant]_ That may be so, but making fun of my learning disability is _not a counterargument_ and _you know it_. I'm not confident about any of this! But while the world is still here, I think it's more dignified that I try to understand, and I'm _trying to understand_. Maybe everything I just said is wrong, but if that's so self-evident, it should be correspondingly easy to explain _why_ it's wrong. Why can't we use a good-person-predicting machine to do the cognitive work a good person would have done, even though a good-person-predicting machine isn't implemented as a good person on the inside? Reply!

**Doomimir**: What makes intelligence useful—and dangerous—isn't a fixed repetoire of behaviors. It's search, optimization—the systematic discovery of _new_ behaviors to achieve goals despite a changing environment. I [don't think recent capabilities advances bear on the shape of the alignment challenge](https://www.lesswrong.com/posts/HmQGHGCnvmpCNDBjc/current-ais-provide-nearly-no-data-relevant-to-agi-alignment) because being able to learn complex behavior _on the training distribution_ was never what the problem was about.

Indeed, as long as we continue to be stuck in the paradigm of reasoning about "the training distribution"—growing minds rather than designing them—then we're not learning anything about how to [aim cognition](https://www.lesswrong.com/posts/NJYmovr9ZZAyyTBwM/what-i-mean-by-alignment-is-in-large-part-about-making) at specific optimization targets—certainly not in a way that will [hold up to dumping large amounts of optimization power into the system](https://www.lesswrong.com/posts/zEvqFtT4AtTztfYC4/optimization-amplifies).

_[he eyes the television]_ Does that suffice? Will you leave me to enjoy my short life?

**Simplicia**: Not yet. I understand the theory of utility optimization—

**Doomimir**: No you don't.

**Simplicia**: I have some nonzero but undoubtedly incomplete understanding of the theory of utility optimization?

_[Doomimir nods graciously.]_

**Simplicia**: The theory inspires me to imagine a simple story where AI is a magic box with a "goal slot" where the user inputs a utility function _U_. When you switch the box on, it computes a plan to maximize _U_. As you turn the dial up to make it use more magic, then at some point, everyone dies, because we're made out of atoms that can be arranged into a higher-_U_ configuration.

**Doomimir**: More or less.

**Simplicia**: We agree that contemporary AI techniques are not a magic box with a goal slot. _I_ think we should be looking at contemporary techniques and their likely future extensions, and figuring out how to make them safe and useful, bearing in mind the danger implied by our theories which suggest that the limiting case of arbitrarily powerful AI should look more like the magic box. I think that _you_ think that I'm retarded for having any hope at all that likely future extensions of contemporary techniques could be made safe.

**Doomimir**: Again, more or less. The lack of an explicit "goal slot" in your neural network doesn't mean it's not doing any dangerous optimization; it just means you don't know what it is. And your mother would seem to agree that you're—

**Simplicia**: _[interrupting]_ I think we _can_ form educated guesses—

**Doomimir**: _[interrupting]_ Guesses!

**Simplicia**: —probabilistic beliefs—about what kinds of optimization is being done by a system and whether it's a problem, even without a complete mechanistic interpretability story. If you think LLMs or future variations thereof are unsafe because they're analogous to an actress with her own goals playing a drunk character without herself being drunk, shouldn't that make some sort of testable prediction about their generalization behavior?

**Doomimir**: Nonfatally testable? Not necessarily. [If you lend a con man $5, and he gives it back](https://twitter.com/ESYudkowsky/status/1747306873261604922), that doesn't mean that you can trust him with larger amounts of money, if he only gave back the $5 because he hoped you would trust him with more.

**Simplicia**: Okay, I agree that deceptive alignment is potentially a real problem, but can we at least distinguish between misgeneralization and deceptive alignment?

**Doomimir**: [_Mis_-generalization?](https://www.lesswrong.com/posts/dkjwSLfvKwpaQSuWo/misgeneralization-as-a-misnomer) The goals _you_ wanted [aren't a property of the training data itself](https://www.lesswrong.com/posts/PoDAyQMWEXBBBEJ5P/magical-categories). The danger comes from _correct_ generalization implying something you don't want.

**Simplicia**: Can I call it _mal_-generalization?

**Doomimir**: Sure.

**Simplicia**: So there are obviously risks from malgeneralization, where the network that SGD sculpted to fit your training distribution, turns out to not behave the way you wanted against a different distribution. For example, [a reinforcement learning agent trained to collect a coin at the right edge of a video game level](https://arxiv.org/abs/2105.14111), might end up continuing to navigate to the right edge of levels where the coin is in a different location.


[TODO— points to cover before scene break—
 * generalization doesn't work in our favor
 * "getting in the way"
 * the text modeling task is going to result in retargetable consequentialism being learned
 * a fact about the training distribution, the test distribution, and the optimizer

https://www.lesswrong.com/posts/zthDPAjh9w6Ytbeks/deceptive-alignment#4_2__Conditions_for_deceptive_alignment
https://nintil.com/situational-awareness-agi/
https://optimists.ai/2023/02/21/deceptive-alignment-is-1-likely-by-default/
https://arbital.greaterwrong.com/p/dont_solve_whole_problem
https://nonint.com/2023/06/10/the-it-in-ai-models-is-the-dataset/
"cherry on the cake"

ArXiv paper on fit to noisy data still generalizes?

]

**Simplicia**: Actually, before you answer that—can I use your bathroom?

**Doomimir**: _[pointing]_ Down the hall.

**Simplicia**: _[to the audience]_ We'll be right back.

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
 * https://www.lesswrong.com/posts/HmQGHGCnvmpCNDBjc/current-ais-provide-nearly-no-data-relevant-to-agi-alignment
 * https://www.lesswrong.com/posts/ax695frGJEzGxFBK4/biology-inspired-agi-timelines-the-trick-that-never-works
]

parametrically retargetable agents seek power

not having a goal slot makes things worse, not better


https://www.lesswrong.com/posts/AyNHoTWWAJ5eb99ji/another-outer-alignment-failure-story
https://www.lesswrong.com/posts/BtffzD5yNB4CzSTJe/genetic-fitness-is-a-measure-of-selection-strength-not-the
https://www.greaterwrong.com/posts/LDRQ5Zfqwi8GjzPYG/counterarguments-to-the-basic-ai-x-risk-case/comment/3AhQKzYCYfAAeenrF
https://www.greaterwrong.com/posts/hvz9qjWyv8cLX9JJR/evolution-provides-no-evidence-for-the-sharp-left-turn

https://arxiv.org/abs/1805.08522 "Deep learning generalizes because the parameter-function map is biased towards simple functions"

https://www.greaterwrong.com/posts/PoDAyQMWEXBBBEJ5P/magical-categories

"You wouldn't upload a bird" seems less compelling in the LLM era

make sure to use "the trick that never works" re biology and AI comparisons!!

https://www.greaterwrong.com/posts/BtffzD5yNB4CzSTJe/genetic-fitness-is-a-measure-of-selection-strength-not-the/comment/kGtqbD7hCxuiFv3XL some drives are more abstract

> The reason we want a function B that can map world states to utilities is so that we can optimize on that number.
https://www.greaterwrong.com/posts/LDRQ5Zfqwi8GjzPYG/counterarguments-to-the-basic-ai-x-risk-case/comment/qBLeyiPzidctBmSB8

https://banburismus.substack.com/p/safety-as-a-scientific-pursuit

https://towardsdatascience.com/deep-neural-networks-are-biased-at-initialisation-towards-simple-functions-a63487edcb99

https://www.lesswrong.com/posts/qoHwKgLFfPcEuwaba/conditioning-predictive-models-making-inner-alignment-as#The_RLHF_conditioning_hypothesis

