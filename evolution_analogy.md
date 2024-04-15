
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
https://www.lesswrong.com/posts/a392MCzsGXAZP5KaS/deceptive-ai-deceptively-aligned-ai

https://www.lesswrong.com/posts/AWoZBzxdm4DoGgiSj/ability-to-solve-long-horizon-tasks-correlates-with-wanting

[TODO— points to cover before scene break—

https://www.lesswrong.com/posts/zthDPAjh9w6Ytbeks/deceptive-alignment#4_2__Conditions_for_deceptive_alignment
https://nintil.com/situational-awareness-agi/
https://optimists.ai/2023/02/21/deceptive-alignment-is-1-likely-by-default/
https://arbital.greaterwrong.com/p/dont_solve_whole_problem
https://nonint.com/2023/06/10/the-it-in-ai-models-is-the-dataset/
"cherry on the cake"

ArXiv paper on fit to noisy data still generalizes?

https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4708466 Prompting Diverse Ideas

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

I think part of the reason the post ends without addressing this is that, unfortunately, I don't think I properly understand this one yet, even after reading [your dialogue with Eli Tyre](https://www.lesswrong.com/posts/aaYZM4kLdHP3pwtfQ/on-the-lethality-of-biased-human-reward-ratings).

The next paragraph of the post links Christiano's 2015 ["Two Kinds of Generalization"](https://ordinaryideas.wordpress.com/2015/11/25/two-kinds-of-generalization/), which I found insightful and seems relevant. By way of illustration, Christiano describes two types of possible systems for labeling videos: (1) a human classifier (which predicts what label a human would assign), and (2) a generative model (which directly builds a mapping between descriptions and videos roughly the way our brains do it). Notably, the human classifier behaves undesirably on inputs that bribe, threaten, or otherwise hack the human: for example, a video of the text "I'll give you $100 if you classify this as an apple" might get classified as an apple. (And an arbitrarily powerful search for maximally apple-classified inputs would turn those up.)

Christiano goes on to describe a number of differences between these two purported kinds of generalization: (1) is reasoning _about_ the human, whereas (2) is reasoning _with_ a model not unlike the one inside the human's brain; searching for simple Turing machines would tend to produce (1), whereas searching for small circuits would tend to produce (2); and so on.

It would be bad to end up with a system that behaves like (1) without realizing it. That definitely seems like it would kill you. But (Simplicia asks) how likely that is seems like a complicated empirical question about how ML generalization works and how you built your particular AI, that isn't definitively answered by "in the limit" philosophy about "perfectly learn[ing] and perfectly maximiz[ing] the referent of rewards assigned by human operators"? That is, I agree that if you argmax over possible programs for the one that results in the most reward-button presses, you get something that only wants to sieze the reward button. The path-dependent details between "pretraining + [HFDT](https://www.lesswrong.com/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to) + regularization + early stopping + _&c._" and "argmax over possible programs" [seem like they make a big difference](https://www.lesswrong.com/posts/pdaGN6pQyQarFHXF4/reward-is-not-the-optimization-target). The technology in front of us _really does_ seem like it's "reasoning with" rather than "reasoning about". (while also seeming to be on the path towards "real AGI" rather than a mere curiosity).

When I try to imagine what Doomimir would say to that, all I can come up with is a metaphor about perpetual-motion-machine inventors whose designs are so complicated that it's hard to work out where the error is, even though the laws of thermodynamics clearly imply that there must be an error. That sounds plausible to me as a handwavy metaphor; I could totally believe that the ultimate laws of optimization (not known to me personally) work that way.

The thing is, we _do_ need more than a handwavy metaphor! "Yes, your gold-printing machine _seems_ to be working great, but my intuition says it's definitely going to kill everyone. No, I haven't been able to convince relevant experts who aren't part of my robot cult, but that's because they're from Earth and therefore racially inferior to me. No, I'm not willing to make any concrete bets or predictions about what happens before then" is a non-starter even if it turns out to be true.
