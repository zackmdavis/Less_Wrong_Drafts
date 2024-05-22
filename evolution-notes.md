**Doomimir**: It's our only datapoint!—

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

https://twitter.com/ESYudkowsky/status/1744066823962947905
> The space of possible programs that appear to do mod arithmetic correctly on domains up to a googol is also vast, and there are some which do it correctly up to a googol but then break above that.  But if you select the shortest program that does mod arithmetic correctly up to a googol, I bet you will find one that does it correctly for all numbers.  That's a fact about the training distribution, the test distribution, and the optimizer "go through all programs in order until you find the shortest one which solves that problem", which yields that result there.
>
> Conversely, for the case of the optimizer "do greedy local search on mutations and recombinations", and the domains "optimize inclusive genetic fitness in the ancestral environment" and "optimize inclusive genetic fitness using science powers in a market economy", we know of historical fact that the first algorithm found by the optimizer of natural selection, which generalizes mere epistemics (not preference) well enough to break the ancestral distribution and catapult the organism into the modern distribution, is not a pure desire to make more DNA copies which simply adapts that preference to the new distribution.


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
 * the "tries to predict the inner goals of a GPT-like model" criticism seems right?—Yudkowsky speculated a thing that wants to predict humans ends up liking maximally easy-to-predict things that meet the definition of "human"

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

-----

Notes on "Dealing with Sparse Rewards in Reinforcement Learning" Joshua Hare master's thesis—

 * citation chase: "Investigating Human Priors for Playing Video Games": when you ablate the obvious context cues (fire dangerous, ladders climbable), humans get much worse at video games, but RL agents perform the same
 * you can try to deal with sparse rewards with curiosity—try to explore novel states

-----

Notes on "Loss Landscapes Are All You Need"—

 * generalization of overparametrized DL is surprising
 * a widely believed hypothesis: SGD does implicit regularization
 * in this paper, our authors show that zeroth-order (gradient-free) optimizers generalize well!
 * caveat: this is a low-data regime (necessary for the zeroth-order approach to work at all); maybe it's different when you have/need more data
 * this supports the volume hypothesis—that good regions in the loss landscape are bigger
 * gradients are important because a first-order optimizer can find a local minimum in polynomial time independent of the dimsensionality, but zeroth-order needs to make exponentially in the dimensionality number of queries (cites to Noll, 2014 and Nesterov 2004)
 * the "guess and check" optimizer owes any good performance solely to the geomety of the loss landscape, not SGD
 * for a dataset where a simple decision boundary is preferred over a complicated by more robust one, the simple boundary has much more volume (as guess and check shows)

-----

Notes on "Understanding Deep Learning Requires Rethinking Generalization"—

 * deep networks easily fit random (!) labels
 * this rules out traditional explanations for generalization performance

------

Notes on "Understanding Generalization through Visualizations"—

 * you can use a "poisoned" loss function to find minima of the loss on the training set that are deliberately bad on other on-distribution data—they're everywhere
 * wiggling the parameters wiggles the decision boundary—flat minima have larger margins

-----

Notes on Belrose vs. Hubinger on counting arguments—

Hubinger says—
 * If you naively count the ways a model could behave on unseen inputs, that's implicitly an inverse simplicy prior?! Compare a program that does n bits for the core logic, vs. a program that takes 2n bits and then m additional bits specifying how it works on various unseen inputs. There are "more" ways those m bits could go ...
 * The real counting argument
 * n bit world model, m bit search procedure, x bit objective function
 * deceptive and non-deceptive both need the n + m world model and search
 * larger networks are more simplicity-prior-like than speed-prior-like


-----

Notes on https://www.lesswrong.com/posts/5XbBm6gkuSdMJy9DT/conditions-for-mathematical-equivalence-of-stochastic —
 * actually, this is a lot of technical details that I'm too dumb to get a lot of insight out of :'(

-----

Notes on comments from 1a3orn on "AI as a Science"—
https://www.lesswrong.com/posts/JcLhYQQADzTsAEaXd/ai-as-a-science-and-three-obstacles-to-alignment-strategies?commentId=by4Ga9FZqPph7mtvJ 

 * DL likes shallow circuits; evolution can favor a mutation with lots of serial ops if the metabolic cost is low
 * a mutation alters protein folding; it doesn't matter how long the causal chain unfolding from that is


Rob's comment— knowing how a CPU executes individual instructions doesn't help you understand the program it's executing

-----

https://www.lesswrong.com/posts/wCtegGaWxttfKZsfx/we-don-t-understand-what-happened-with-culture-enough


[TODO—cruxes to hit—

 * Rapid capability gain/"secret sauce of general intelligence"—Simplicia kind of buys Pope's culture-as-overhang argument; Doomimir thinks humans have a key threshold of general intelligence
 * (Yudkowsky recently made another point point that there could be other, future one-time gains analogous to but besides the invention of language)
]

It's funny how we the MIRI position seems to simultaneously think evolution is "too weak" but also "too strong"?


**Simplicia**: Sure we do. It predicts the next token in its training distribution.

**Doomimir**: That's like saying humans just optimize inclusive genetic fitness.

**Simplicia**: Humans execute adaptations that optimize inclusive genetic fitness _in the environment of evolutionary adaptedness_.

-------

notes from "Introductory Lectures on Convex Optimization"—
 * an iterative local black box scheme for solving optimization problems—have a candidate point, call an "oracle" that gives you information for how to update your point
 * the oracle could be zero-order (just telling you the function value), first-order (gradient), second-order (Hessian)
 * analytical complexity is the number of calls to the oracle needed
 * arithmetic complexity counts the number of math operations used, including the operation of the oracle itself
 * for Lipschitz constant L and accuracy ε, the analytical complexity of zero-order grid sampling is (floor(L/(2ε) + 2)^ n, which is exponential in the dimensionality n

"complexity of gradient descent (a first-order method) to find an ε-suboptimal solution is O(L/ε), where L is the Lipschitz constant (Nesterov, 2004). This complexity is independent of the dimensionality of the problem. [...] On the other hand, for zeroth-order methods, the complexity of finding an ε-suboptimal solution for a convex and Lipschitz continuous function is O((L/ε)^n)"

The paper Sam sent me is— "Optimal rates for zero-order convex optimization: the power of two function evaluations"; it claims that the dependence on the dimensionality is \sqrt{d}

----
In that sense, first-order gradient methods seem like a better optimizer than zeroth-order evolution, which is also supported by theoretical results: gradient information lets you converge to a local minimum in polynomial time independently of the dimensionality of the problem, but zeroth order algorithms depend on the dimensionality.

[TODO: but even if you think SGD is like evolution, selective breeding also looks like it works? "Select for X, get X" works great on factory farms. If we bred dogs to be smarter than humans and also to love us, it seems likely that they would keep loving us, maybe not in exactly the way that we prefer to be loved, but we don't murder our dogs. Counterargument: Sequences-era examples of selecting for individual egg production or selective breeding. Counter-counter: it seems like this more like a "sparse reward" concern, which is different from condemning DL methods]

**Doomimir**: 
Livestock and LLMs aren'

[TODO—
 * SGD and evolution are still hill-climby algorithms; that's different from being able to intelligently change multiple things at once
 * dogs and livestock aren't generally intelligent, which is what broke alignment in humans

]

 * general intelligence is has special alignment-breaking properties; doing what you want on-distribution is trivial and unimpressive; the problem is that self-improvement changes the distribution, and the outcomes are very brittle

 * information theory: if you need 100 bits
     * counterargument: perfect English is also a lot of bits, yet LLMs exist

 * sparse rewards, training data, and the EEA

Ethan Perez's work about LLMs being better at writing reward functions https://arxiv.org/abs/2310.12921

https://ificl.github.io/images-that-sound/

--- (get a Tweet reference link to "starting from scratch with gradient descent would be stupid")

https://x.com/ESYudkowsky/status/1775548168530448895

> There is a lot to learn from the observation of how everything played out with natural selection, and throwing it all away and starting from scratch with gradient descent would be stupid.  No, it doesn't transfer directly.  It does transfer indirectly.

> From my perspective, the point of raising the example of natural selection is that it debunks the naive belief that if in general an outer optimizer trains on reward function, it gets an inner optimizer that pursues that reward function OOD.  Saying "But SGD is first-order and natural selection is zeroth-order!" doesn't refute the refutation of "For all n, nth-order outer optimizers, training on a reward, get inner optimizers pursuing that reward" which is the state of mind that naive arguers seem to want to appeal to.
>
> You could, perhaps, make a case for just 1st-order optimizers and not 0th-order or 2nd-order optimization algorithms producing inner minds that exactly pursue the quoted reward function that outer optimizers use to generate rewards.  I think this is also dumb after you've shaken loose of the naive mirroring expectation and studied in detail what went on with 0th-order natural selection, since a lot of those phenomena sure look to me like they ought to generalize.  Even though, yes, SGD is not exactly NS and therefore some straw argument that they were "exactly the same" is thereby refuted by pointing out any differences whatsoever.
>
> My arguments against SGD exactly mirroring quoted outer functions generating particular rewards, to inner psychological pursuit of the quoted reward function generalizing across distributions, include, "If you train a mind to exactly predict text from many individual drunks, it will not thereby become drunk" and "Actually you're still doing greedy local search and it's gonna hit on local correlates again" and "Just like weird shit went wrong with natural selection, we should also expect different weird shit to go wrong with SGD".
>
> Your own misrepresentation of the argument from large possibility spaces in mind design, in particular, is one where the flaw in your misrepresentation of what the theory implies, manifests the same way for 0th-order and 1st-order optimizers (NS and SGD); which is why you tried to use the analogy about genomes in the first place; and the refutation (showing what the theory actually predicts) is analogous for both cases.
>
> If you respond to all this by claiming that argument by analogy to natural selection has been "debunked", and therefore there's no need to talk about SGD maybe having any problems, I'm not sure what to do beyond saying to people, "She's misrepresenting both the original argument and its debunking" and letting them judge.
>
> Using the example of an individual human learning across their lifetime would be weird and pointless since a human brain is not a blank slate starting from scratch, it's a particular architecture extensively tested to work a particular way in the natural environment.  Everything a human brain does in the modern world needs to be understood as the malfunction of a complicated hunter-gatherer, not the correct function of a simple pleasure maximizer.
>
> If humans were blank slates pursuing pleasure, we'd use more heroin especially at the end of their lifespans.  We don't purely relentlessly pursue strategies that maximize the sum of physical pleasure over time, because that's not what a malfunctioning hunter-gatherer does.  Our cares are bound to objects in the external world, just, not bound to "make copies of your DNA" specifically.  That's true because natural selection optimized our ancestors to pursue particular things in the outer world, and tried and tested different brain systems until it found ones that happened to shake out that way.  It is meaningless to imagine a human brain as an artifact that popped into existence as a blank slate within a single lifetime.  We just aren't; we've got a bunch of complicated specific architecture whose testing and debugging happened before then.

https://x.com/ESYudkowsky/status/1666986593838837760
> +1 to what Xu asks here; "obey a constraint" is a programmer goal, not a system design.  "Have a committee flag constraint violations they know about, resulting in a lower reward to a system trained by SGD/DRL to maximize reward" is a system design.

https://x.com/ESYudkowsky/status/1660564623547047936
> No, ASI via SGD is like having to enter a Wish via 100,000 training examples, and then SGD fits some weird incredibly complicated function to that along local optima which are not global optima, so when the AI gets smarter It runs off and does some utterly other thing.  You're screwed irrespective of which Wish you try to make or who enters it, in a way that wouldn't make good fiction because the relation between Wish and outcome is not solvable by the reader and doesn't tell interesting ironic moral lessons about whichever Wish got made.  This is also true if you generate an objective function via SGD and optimize it via a planning mechanism.

https://x.com/ESYudkowsky/status/1775274359906791803
> Sounds like a level confusion to me?  The outer optimizer isn't trying to train in long-term goals.  That doesn't mean the thing it trains can't possibly have any long-term goals.  Natural selection didn't train anything into humans that wasn't, like, grandparent-grandchild level.  Some of us ended up caring about galaxies anyways.  Slapping a label on something that says "We, way out here, want it to be a function approximator" or "We're optimizing this to approximate a function" doesn't mean that there's nothing inside the black box but the target function plus some random noise.

instruction-tuning generalizing across languages

https://www.lesswrong.com/posts/YSFJosoHYFyXjoYWa/why-neural-networks-generalise-and-why-they-are-kind-of

