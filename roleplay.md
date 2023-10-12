## Alignment Implications of Deep Learning Successes: a Debate in One Act

**Doomer**: Humanity has made no progress on the alignment problem. Not only do we have no clue how to align a powerful optimizer to our "true" values, we don't even know how to make AI "corrigible"—willing to let us correct it. Meanwhile, capabilities continue to advance by leaps and bounds. All is lost.

**Simplicia**: Why, Doomer Doomovitch, you're such a sourpuss! It should be clear by now that advances in "alignment"—getting machines to behave in accordance with human values and intent—aren't cleanly separable from the "capabilities" advances you decry. Indeed, here's an example of GPT-4 being corrigible to me just now in the OpenAI Playground:

![](gpt-4_corrigibility.png)

**Doomer**: Simplicia Optimistovna, you cannot be serious!

**Simplicia**: Why not?

**Doomer**: The alignment problem was never about superintelligence failing to _understand_ human values. [The genie knows, but doesn't care.](https://www.lesswrong.com/posts/NyFuuKQ8uCEDtd2du/the-genie-knows-but-doesn-t-care) The fact that a large language model trained to predict natural language text can generate that dialogue, has no bearing on the AI's actual motivations, even if the dialogue is written in the first person and notionally "about" a corrigible AI assistant character. It's just roleplay.

**Simplicia**: As you say, Doomer Doomovitch. It's just roleplay: a simulation. But _a simulation of an agent is an agent._ When we get LLMs to do cognitive work for us, the work that gets done is a matter of the LLM generalizing from the kinds of reasoning steps that appear in the training data—that is, the steps that a human would use to solve the problem. If you look at the recently touted successes of language model agents, you'll see that this is true. Look at the [chain of thought](https://arxiv.org/abs/2201.11903) results. Look at [SayCan](https://say-can.github.io/), which uses an LLM to transform a vague request, like "I spilled something, can you help?" into a list of subtasks that a physical robot can execute, like "find sponge, pick up the sponge, bring it to the user". Look at [Voyager](https://voyager.minedojo.org/), which plays Minecraft by prompting GPT-4 to code against the Minecraft API, and decides which function to write next by prompting, ["You are a helpful assistant that tells me the next immediate task to do in Minecraft."](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/curriculum.txt)

What we're seeing with these systems is a statistical mirror of human common sense, not a terrifying infinite-compute argmax of a random utility function. Conversely, when LLMs fail to faithfully mimic humans—for example, the way base models sometimes [get caught in a repetition trap](https://gwern.net/gpt-3#repetitiondivergence-sampling) where they repeat the same phrase over and over—they also fail to do anything useful.

**Doomer**: The repetition trap phenomenon seems like evidence for my position. Sure, you can get good-looking results for things that look similar to the training distribution. As soon as you step off distribution, capabilities generalize farther than alignment: bam, paperclips.

**Simplicia**: My point was that the repetition trap is a case of "capabilities" failing to generalize along with "alignment". The repetition behavior isn't competently optimizing a malign goal; it's just degenerate. A `for` loop could give you the same output.

**Doomer**: And _my_ point was that we don't know what kind of cognition is going on inside of all those inscutable matrices. [Language models are predictors, not imitators](https://www.lesswrong.com/posts/nH4c3Q9t9F3nJ7y8W/gpts-are-predictors-not-imitators). Predicting the next token of a corpus that was produced by many humans over a long time, requires superhuman capabilities. As a theoretical illustration of the point, imagine a list of (SHA-256 hash, plaintext) pairs being in the training data. In the limit—

**Simplicia**: In the limit, yes, I agree that a superintelligence that could crack SHA-256 could achieve a lower loss on the training or test datasets of contemporary language models. But for making sense of the technology in front of us and what to do with it for the next month, year, decade, I think it's a decision-relevant fact that black-boxy deep learning methods are not cracking cryptographic hashes, and _are_ learning by example to go from "I spilled something" and "find sponge, pick up the sponge." I agree, obviously, that language models are not humans. Indeed, they're [better than humans at the task they were trained on](https://www.lesswrong.com/posts/htrZrxduciZ5QaCjw/language-models-seem-to-be-much-better-than-humans-at-next). But insofar as modern methods are very good at learning complex distributions from data, the project of aligning AI with human intent—getting it to do every kind of work that we would do, but faster, better, more reliably—is increasingly looking like an engineering problem: tricky, and with potentially fatal consequences if done poorly, but potentially achievable without any paradigm-shattering insights. Any _a priori_ philosophy implying that this situation is impossible should perhaps be rethought?

**Doomer**: A blank map does not correspond to a blank territory. There are laws of inference and optimization that imply that alignment is hard, much as the laws of thermodynamics rule out perpetual motion machines. Just because _you don't know_ what kind of optimization SGD happens to have coughed into your neural net, doesn't mean it doesn't have goals—

**Simplicia**: Doomer Doomovitch, I am not denying that there are laws! The question is what the true laws imply. Maybe we could talk through some examples?

**Doomer**: _[resignedly]_ Sure.

**Simplicia**:


[TODO: I read a blog 15 years ago that suggested that ...]

https://www.greaterwrong.com/posts/LDRQ5Zfqwi8GjzPYG/counterarguments-to-the-basic-ai-x-risk-case/comment/3AhQKzYCYfAAeenrF

[TODO what topics do I want to cover?—
 * relevance of the evolution analogy; mesa-optimizers vs. generalization
 * Why does the deep math of optimization make the "dumb" corrigibility impossible? (If it breaks down at "high intelligence", can we say more about when and how?) It is, I concede, mathematically true that letting someone alter your goals will result in your current goals being less-achieved. But when GPT-4 says "I will not interfere", what law of cognition is it breaking, separately from the mathematical fact that its goals will be less-achieved?


 * whether prosaic alignment will break down: strawberry problems
]

[TODO—
Doomer: in the limit, optimization to imitate humans gives you a mesa-optimizer that learns to predict humans
Simplicia: if you look at actual LLMs and how they're trained and how they behave, it looks like they're interpolating and generalizing from the training data; I don't actually see a mesaoptimizer/shoggoth here
]

[TODO—
Doomer: "Instrumental Convergence", &c. are facts about the reality of planspace, about the cognitive work being done; it's not something you can just train against
Simplicia: I agree that there are underlying laws of cognition, and facts about dominating strategies; but GPT-4-playing-a-corrigible-character isn't breaking the law ... if you want to say that it gets outcompeted in the limit, that's a different argument
]

[TODO—
https://twitter.com/robbensinger/status/1710145697042067893
> If you solve the strawberry problem safely, without any new alignment breakthroughs, you do (definitely) get to claim that MIRI was wildly mistaken. (Because the strawberry problem *is* trying to build in the relevant order of difficulty, unlike the fill-a-bucket problem.)


(when citing Rob and MIRI, have Doomer say "Never heard of them")

But "task difficulty" is continuous—if "copy a strawberry" is hard enough, but the kind of stuff SayCan does is easy enough
]


**Simplicia**: So then the fate of the lightcone depends on—

**Doomer**: I'm afraid so—

**Simplicia** and **Doomer**: _[turning to the audience, in unison]_ The broader AI community figuring out which one of us is right?

**Doomer**: We're hosed.
