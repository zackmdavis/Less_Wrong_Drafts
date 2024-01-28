
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

https://www.lesswrong.com/posts/qoHwKgLFfPcEuwaba/conditioning-predictive-models-making-inner-alignment-as#The_RLHF_conditioning_hypothesis

https://twitter.com/jd_pressman/status/1711465924031897910
> Basically he thinks that there is some program(s) in the model which generate the human values imitation, and that even if these programs continue *running* OOD they don't actually mean what they appear to mean outside the training distribution.
