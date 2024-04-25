
### Scene 2: Uses of the Evolution Analogy

**Doomimir**: It's our only datapoint!

[TODO—sketch of the real-world arguments I'm covering—
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
https://www.lesswrong.com/posts/a392MCzsGXAZP5KaS/deceptive-ai-deceptively-aligned-ai

https://www.lesswrong.com/posts/AWoZBzxdm4DoGgiSj/ability-to-solve-long-horizon-tasks-correlates-with-wanting


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

lottery ticket/prunability work points to SGD being "messy" like evolution

https://www.lesswrong.com/posts/qoHwKgLFfPcEuwaba/conditioning-predictive-models-making-inner-alignment-as#The_RLHF_conditioning_hypothesis

https://twitter.com/jd_pressman/status/1711465924031897910
> Basically he thinks that there is some program(s) in the model which generate the human values imitation, and that even if these programs continue *running* OOD they don't actually mean what they appear to mean outside the training distribution.

https://www.lesswrong.com/posts/fRSj2W4Fjje8rQWm9/thoughts-on-sharing-information-about-language-model
> LM agents based on chain of thought and decomposition seem like the most plausible approach to bootstrapping subhuman systems into trusted superhuman systems.

[TODO—
S: This isn't 2008, Doomishko! It means the stuff right here in front of us! It really does look like like language models can do reasoning about goals without the intrumental convergence doom kicking in! Constitutional AI works at all. You ridicule people who dismiss GPT-4 as a stochastic parrot. Why isn't this equally ridiculous? "Anthropic, slightly more competent and not based in California" / Yann LeCun's cherry / the it is the dataset / point to the audience / One of the leading researchers / Reply! Reply!
D: I think you're overestimating how easy it is, as a human, to be misled by appearances of something that's actually doing something very different under the surface. In a high-dimensional domain, like the language model stuff we're talking about, there's room for lots of stuff like "going to the right" to be happening. "getting in the way"/ situational awareness / playing the training game
S: But you do agree that generalization works for modular arithmetic, and images. / fitting to mislabeled data
D: That's a fact about "a fact about the training distribution, the test distribution, and the optimizer"
S: You just don't think it can work for "goals". This seems like a complex question. Do you have any evidence?
]

https://ordinaryideas.wordpress.com/2015/11/25/two-kinds-of-generalization/

**Simplicia**: 

**Doomimir**: _[despairing]_ You keep using that word. How do I show you that [...]

[TODO:
"being drunk yourself would get in the way"
That's 
]

**Simplicia**: This still seems like a subtle and complicated question to me. Do you have any empirical evidence?

**Doomimir**: As a matter of fact, yes. You see—

----------

Of course gradient descent isn't going to hit on a perfect consequentialist that calculates the optimal plan for manipulating humans into hitting the thumbs-up button. But in order to do powerful cognitive work, it is going to hit on flexible


It's hard to say in advance what local correlates of reward those optimizers will end up getting pointed at, but it would be an astronomically unlikely coincidence for it to end up being nice.

**Simplicia**: I can't say for sure that you're wrong, but it seems like it depends on empirical facts about how deep learning works, rather than something you could be confident in _a priori_. 

[TODO:
work in something about the paper about fitting to random labels—"Understanding Deep Learning Requires Rethinking Generalization", "Robust to Massive Label Noise"
D needs to be clearer about the gradient pointing towards "not allowed to interfere"
S should quip about the usage of "model"
DL as function approximation
]

--------

Notes on "Evolution Provides No Evidence for the Sharp Left Turn" (https://www.greaterwrong.com/posts/hvz9qjWyv8cLX9JJR/evolution-provides-no-evidence-for-the-sharp-left-turn)—

 * For non-human animal species, the only way to transmit information from one generation to the next is through genes; the billions of learning steps in an individual animal brain get thrown away
 * For humans, we transmit learned data through culture; the next generation doesn't have to invent everything from scratch
 * Within-lifetime learning is much faster than evolution
 * We don't train AIs by having an outer loop over inner learners, and then delete the inner learners after every stop of the outer loop
 * This was a one-time overhang
 * Takeoff could still be fast because of AIs contributing to research (recursive self-improvement)
 * AI could just learn faster than us
 * (separate post to also read: "Evolution is a bad analogy for AGI: inner alignment")
 * capabilities jumps due to recursive AI research won't break alignment; if you learn a lot about how to do RLHF; that's not necessarily going to break retrieval mechanisms or better optimizers, rather than RLHF suddenly being useless
    * I'm not sure I buy this; if, e.g., the key assumption for RLHF is that the model isn't much smarter than the evaluators

------

Notes on "Evolution is a bad analogy for AGI: inner alignment" (https://www.greaterwrong.com/posts/FyChg3kYG54tEN3u6/evolution-is-a-bad-analogy-for-agi-inner-alignment)—

 * Evolution didn't optimize over "values"; it optimized over learning process + reward circuits
 * claim: "learning process + reward function + training environment → the AI’s learned values" is a better analogy than "evolution → values"
    * my comment: it doesn't seem like these analogies should be in zero-sum competition with each other; if we're sufficiently specific about each
 * Evolution specifies genes and genes specify cognition; the extra step is much more indirect compared to how SGD directly optimizes the brain
 * genome is few parameters (highly compressed)
 * We have more evidence/data about humans
    * This consideration seems weak to me?
 * evolution couldn't have succeeded at aligning humans to fitness (where would the ancestral humans get that concept? In contrast to things that were already in their environment)
 * There are many sources of evidence about how inner goals relate to outer optimization criteria; evolution need not have more weight than "human within-lifetime learning"
    * The within-lifetime-learning analogy is much more optimistic; someone who was nice to dogs a lot while growing up probably doesn't want a dog-free future
    * (The obvious counterargument is, maybe they selfishly want a robot dog to fulfill their needs, which is different from what would be good for the dogs themselves)
    
------

Notes on "My Objections to 'We're All Gonna Die'"—
(just what leapt out at me)

 * He cites the "Relative representations enable zero-shot latent space communication" paper!!
 * the "tries to predict the inner goals of a GPT-like model" seems right?

------

Notes on Byrnes "Against Evolution as an Analogy" (https://www.greaterwrong.com/posts/pz7Mxyr7Ac43tWMaC/against-evolution-as-an-analogy-for-how-humans-will-create)—

 * deep RL and evolution are both "two-layer" algorithms
 * three ingredients for the evolution analogy: "outer + inner", "outer as lead designer", and "inner as AGI"
 * Byrnes doesn't think all three will hold
 * "outer as lead designer" doesn't apply if the outer loop is hyperparameter search &c.
    * but "outer as lead designer" mostly does hold for modern DL, right? We mostly don't know how LLMs know about language
 * "inner as AGI" doesn't hold if the outer algorithm is an essential part of the AGI's operation
 * better analogy: genome ⟺ Git repo with PyTorch, within-lifetime learning ⟺ training, human behavior ⟺ policy behavior
 * Byrnes expects AGI to have some black-boxy components (like learned world-model content), but doesn't expect learning-algorithm _and_ learned content _and_ reward function to all be tangled together in the same black box
 * Human engineers have sometimes been inspired by nature, which is not the same thing as running genetic algorithms
 * convnets, PPO, temporal difference learning, &c. were all invented by humans, not automated search
 * in a comment, Byrnes says he's impressed by the world-modeling in GPT-3's weights, but doesn't expect the trained model to learn in the AGI-hard sense, which would require somehow translating info from activations to weights
 * automated design is great for things that are computationally cheap but very complicated (so image classification is a great fit), whereas learning algorithms themselves are conceptually simple but eat up lots of compute at scale
 * (I'm skipping section 2)
 * the same NN architecture trained to do different tasks, will be executing "the same" low level operations (with different bit values), but the low-level steps of e.g. FFT vs. quicksort will be very different
 * ... which is relevant becuase of efficiency; maybe a superintelligent compiler could compile the differnet neural nets into programs with different performance characteristics, but the nets having the same perf characteristics in reality is
 * If you search over a space of algorithms with SGD &c., you might get what you're looking for, but not in a compute-efficient way
