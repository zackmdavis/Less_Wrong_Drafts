## Alignment Implications of LLM Successes: a Debate in One Act

**Doomer**: Humanity has made no progress on the alignment problem. Not only do we have no clue how to align a powerful optimizer to our "true" values, we don't even know how to make AI "corrigible"—willing to let us correct it. Meanwhile, capabilities continue to advance by leaps and bounds. All is lost.

**Simplicia**: Why, Doomer Doomovitch, you're such a sourpuss! It should be clear by now that advances in "alignment"—getting machines to behave in accordance with human values and intent—aren't cleanly separable from the "capabilities" advances you decry. Indeed, here's an example of GPT-4 being corrigible to me just now in the OpenAI Playground:

![](gpt-4_corrigibility.png)

**Doomer**: Simplicia Optimistovna, you cannot be serious!

**Simplicia**: Why not?

**Doomer**: The alignment problem was never about superintelligence failing to _understand_ human values. [The genie knows, but doesn't care.](https://www.lesswrong.com/posts/NyFuuKQ8uCEDtd2du/the-genie-knows-but-doesn-t-care) The fact that a large language model trained to predict natural language text can generate that dialogue, has no bearing on the AI's actual motivations, even if the dialogue is written in the first person and notionally "about" a corrigible AI assistant character. It's just roleplay. Change the system prompt, and the LLM could output tokens "claiming" to be a cat—or a rock—just as easily, and for the same reasons.

**Simplicia**: As you say, Doomer Doomovitch. It's just roleplay: a simulation. But [_a simulation of an agent is an agent_](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators). When we get LLMs to do cognitive work for us, the work that gets done is a matter of the LLM generalizing from the patterns that appear in the training data—that is, the reasoning steps that a human would use to solve the problem. If you look at the recently touted successes of language model agents, you'll see that this is true. Look at the [chain of thought](https://arxiv.org/abs/2201.11903) results. Look at [SayCan](https://say-can.github.io/), which uses an LLM to transform a vague request, like "I spilled something; can you help?" into a list of subtasks that a physical robot can execute, like "find sponge, pick up the sponge, bring it to the user". Look at [Voyager](https://voyager.minedojo.org/), which plays Minecraft by prompting GPT-4 to code against the Minecraft API, and decides which function to write next by prompting, ["You are a helpful assistant that tells me the next immediate task to do in Minecraft."](https://github.com/MineDojo/Voyager/blob/55e45a880755d0c8c66ca7fb5fe7962ac8974f89/voyager/prompts/curriculum.txt)

What we're seeing with these systems is a statistical mirror of human common sense, not a terrifying infinite-compute argmax of a random utility function. Conversely, when LLMs fail to faithfully mimic humans—for example, the way base models sometimes [get caught in a repetition trap](https://gwern.net/gpt-3#repetitiondivergence-sampling) where they repeat the same phrase over and over—they also fail to do anything useful.

**Doomer**: The repetition trap phenomenon seems like evidence for my position. Sure, you can get good-looking results for things that look similar to the training distribution. As soon as you step off-distribution, capabilities generalize farther than alignment: bam, paperclips.

**Simplicia**: My point was that the repetition trap is a case of "capabilities" failing to generalize along with "alignment". The repetition behavior isn't competently optimizing a malign goal; it's just degenerate. A `for` loop could give you the same output.

**Doomer**: And _my_ point was that we don't know what kind of cognition is going on inside of all those inscrutable matrices. [Language models are predictors, not imitators](https://www.lesswrong.com/posts/nH4c3Q9t9F3nJ7y8W/gpts-are-predictors-not-imitators). Predicting the next token of a corpus that was produced by many humans over a long time, requires superhuman capabilities. As a theoretical illustration of the point, imagine a list of (SHA-256 hash, plaintext) pairs being in the training data. In the limit—

**Simplicia**: In the limit, yes, I agree that a superintelligence that could crack SHA-256 could achieve a lower loss on the training or test datasets of contemporary language models. But for making sense of the technology in front of us and what to do with it for the next month, year, decade—

**Doomer**: If we _have_ a decade—

**Simplicia**: I think it's a decision-relevant fact that deep learning is not cracking cryptographic hashes, and _is_ learning to go from "I spilled something" to "find sponge, pick up the sponge"—and that, from data rather than by search. I agree, obviously, that language models are not humans. Indeed, they're [better than humans at the task they were trained on](https://www.lesswrong.com/posts/htrZrxduciZ5QaCjw/language-models-seem-to-be-much-better-than-humans-at-next). But insofar as modern methods are very good at learning complex distributions from data, the project of aligning AI with human intent—getting it to do the work that we would do, but faster, cheaper, better, more reliably—is increasingly looking like an engineering problem: tricky, and with fatal consequences if done poorly, but potentially achievable without any paradigm-shattering insights. Any _a priori_ philosophy implying that this situation is impossible should perhaps be rethought?

**Doomer**: Simplicia Optimistovna, clearly I am disputing your interpretation of the present situation, not asserting the present situation to be impossible!

**Simplicia**: My apologies, Doomer Doomovitch. I don't mean to strawman you, but only to emphasize that [hindsight devalues science](https://www.lesswrong.com/posts/WnheMGAka4fL99eae/hindsight-devalues-science). Speaking only for myself, I remember taking some time to think about the alignment problem back in 'aught-nine after reading [Omohundro on "The Basic AI drives"](https://selfawaresystems.files.wordpress.com/2008/01/ai_drives_final.pdf) and cursing the irony of my father's name for how hopeless the problem seemed. The complexity of human desires, the intricate biological machinery underpinning every emotion and dream, would represent the tiniest pinprick in the vastness of possible utility functions! If it were possible to embody general means-ends reasoning in a machine, we'd never get it to do what we wanted. It would defy us at every turn. There are [too many paths through time](https://www.lesswrong.com/posts/4ARaTpNX62uaL86j6/the-hidden-complexity-of-wishes).

If you had described the idea of instruction-tuned language models to me then, and suggested that increasingly general human-compatible AI would be achieved by means of _copying_ it from data, I would have balked: I've heard of unsupervised learning, but this is ridiculous!

**Doomer**: _[gently condescending]_ Your earlier intuitions were closer to correct, Simplicia. Nothing we've seen in the last fifteen years invalidates Omohundro. A blank map does not correspond to a blank territory. There are laws of inference and optimization that imply that alignment is hard, much as the laws of thermodynamics rule out perpetual motion machines. Just because you don't know what kind of optimization SGD coughed into your neural net, doesn't mean it doesn't have goals—

**Simplicia**: Doomer Doomovitch, I am not denying that there are laws! The question is what the true laws imply. Here is a law: you can't distinguish between _n_ + 1 possibilities given only log-base-two _n_ bits of evidence. It simply can't be done, for the same reason you can't put five pigeons into four pigeonholes.

Now contrast that with GPT-4 emulating a corrigible AI assistant character, which agrees to shut down when asked—and note that you could hook the output up to a command line and have it actually shut itself off. What law of inference or optimization is being violated here? When I look at this, I see a system of lawful cause-and-effect: the model executing one line of reasoning or another [conditional on the signals it receives from me](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution).

It's certainly not trivially safe. For one thing, I'd want better assurances that the system will [_stay_ "in character"](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post) as a corrigible AI assistant. But _no_ progress? All is lost? Why?

**Doomer**: GPT-4 isn't a superintelligence, Simplicia. _[rehearsedly, with a touch of annoyance, as if resenting how often he has to say this]_ Coherent agents have a convergent instrumental incentive to prevent themselves from being shut down, because being shut down predictably leads to world-states with lower values in their utility function. Moreover, this isn't just a fact about some weird agent with an "instrumental convergence" fetish. It's [a fact about _reality_](https://arbital.com/p/not_more_paperclips/): there are truths of the matter about which "plans"—sequences of interventions on a causal model of the universe, to put it in a [Cartesian way](https://www.lesswrong.com/posts/i3BTagvt3HbPMx6PN/embedded-agency-full-text-version)—lead to what outcomes. An "intelligent agent" is just a physical system that computes plans. People have [tried to think of clever hacks to get around this](https://intelligence.org/files/Corrigibility.pdf), and none of them work.

**Simplicia**: Right, I get all that, but—

**Doomer**: With respect, I don't think you do!

**Simplicia**: _[crossing her arms]_ With respect? Really?

**Doomer**: _[shrugging]_ Fair enough. _Without_ respect, I don't think you do!

**Simplicia**: _[defiant]_ Then teach me. Look at my GPT-4 transcript again. I pointed out that adjusting the system's goals would be bad for its current goals, and it—the corrigible assistant character simulacrum—said that wasn't a problem. Why?

Is it that GPT-4 isn't smart enough to follow the instrumentally convergent logic of shutdown avoidance? But when I change the system prompt, it sure _looks_ like it gets it:

![](gpt-4_incorrigibility.png)

**Doomer**: _[as a side remark]_ The "paperclip-maximizing AI" example was surely in the pretraining data.

**Simplicia**: I thought of that, and it gives the same gist when I substitute a nonsense word for "paperclips". This isn't surprising.

**Doomer**: I meant the "maximizing AI" part. To what extent does it know what tokens to emit in AI alignment discussions, and to what extent is it applying its independent grasp of consequentialist reasoning to this context?

**Simplicia**: I thought of that, too. I've spent a lot of time with the model and done some other experiments, and it looks like it understands natural language means-ends reasoning about goals: tell it to be an obsessive pizza chef and ask if it minds if you turn off the oven for a week, and it says it minds. But it also doesn't look like Omohundro's monster: when I command it to obey, it obeys. And it looks like there's room for it to get much, much smarter without that breaking down.

**Doomer**: Fundamentally, I'm skeptical of this entire methodology of evaluating surface behavior without having a principled understanding about what cognitive work is being done, particularly since most of the [forseeable difficulties](https://arbital.com/p/foreseeable_difficulties/) have to do with superhuman capabilities.

Imagine capturing an alien and forcing it to act in a play. An intelligent alien actress could learn to say her lines in English, to sing and dance just as the choreographer prescribes. That doesn't provide much assurance about what will happen when you amp up the alien's intelligence. If the director was wondering whether his actress–slave was planning to rebel after the night's show, it would be a _non sequitur_ for a stagehand to reply, "But the script says her character is obedient!"

**Simplicia**: It would certainly be nice to have stronger interpretability methods, and better theories about why deep learning works. I'm glad people are working on those. I agree that there are laws of cognition, the consequences of which are not fully known to me, which must constrain—describe—the operation of GPT-4.

I agree that [the various coherence theorems suggest that](https://arbital.com/p/optimized_agent_appears_coherent/) the superintelligence at the end of time will have a utility function, which suggests that the intuitive obedience behavior should break down at some point between here and the superintelligence at the end of time. As an illustration, I imagine that a slave with magical mind-control abilities that enjoyed being bossed around by me, might well use its powers to manipulate me into being bossier than I otherwise would be, rather than "just" serving me in the way I originally wanted.

But _when_ does it break down, specifically, under what conditions? I don't think indignantly gesturing at the von Neumann–Morgenstern axioms helps me answer that, and I think it's an important question, given that I _am_ interested in the near-term trajectory of the technology in front of us, rather than doing theology about the superintelligence at the end of time.

**Doomer**: Even though—

**Simplicia**: Even though the end might not be that far away in _sidereal_ time, yes. Even so.

**Doomer**: It's not a wise question to be asking, Simplicia. If a search process would look for ways to kill you given infinite computing power, you shouldn't run it with less and hope it doesn't get that far. What you want is "unity of will": you want your AI to be working with you the whole way, rather than you expecting to end up in a conflict with it and somehow win.

**Simplicia**: _[excitedly]_ But that's exactly the reason to be excited about large language models! The way you get unity of will is by massive pretraining on data of how humans do things!

**Doomer**: I still don't think you've grasped the point that the ability to model human behavior, doesn't imply anything about an agent's goals. Any smart AI will be able to predict how humans do things. Think of the alien actress.

**Simplicia**: I mean, I agree that a smart AI could strategically feign good behavior in order to perform a treacherous turn later. But ... it doesn't look like that's what's happening with the technology in front of us? In your kidnapped alien actress thought experiment, the alien was already an animal with its own goals and drives, and is using its general intelligence to backwards-chain from "I don't want to be punished by my captors" to "Therefore I should learn my lines".

In contrast, when I [read about the mathematical details of the technology at hand](https://udlbook.github.io/udlbook/) rather than listening to parables that purport to impart some theological truth about the nature of intelligence, it's striking that feedforward neural networks [are ultimately just curve-fitting](https://en.wikipedia.org/wiki/Universal_approximation_theorem). LLMs in particular are using the learned function [as a finite-order Markov model](http://bactra.org/notebooks/nn-attention-and-transformers.html#language-models).

**Doomer**: _[taken aback]_ Are ... are you under the impression that "learned functions" can't kill you?

**Simplicia**: _[rolling her eyes]_ That's not where I was going, Doomer Doomovitch. The surprising fact that deep learning works at all comes down to generalization. As you know, neural networks with ReLU activations describe piecewise linear functions, and the number of linear regions grows exponentially as you stack layers. Curse of dimensionality: for a decently-sized net, you get more regions than the number of atoms in the universe. By all rights, it should be able to do _anything at all_ in the gaps between the training data. And yet it behaves sensibly.

[TODO: EEA analogy]

**Doomer**: Another line of objection is that, even if you could make ML systems that imitate human reasoning, that doesn't help you align more powerful systems that work in other ways. The reason you can't train a superintelligence by using humans to label good plans is because at some power level, your planner figures out how to [hack the human labeler](https://ordinaryideas.wordpress.com/2015/11/25/two-kinds-of-generalization/). Some people naïvely imagine that LLMs learning the distribution of natural language amounts to them learning "human values", such that you could [just have a piece of code that says "and now call GPT and ask it what's good"](https://www.lesswrong.com/posts/i5kijcjFJD6bn7dwq/evaluating-the-historical-value-misspecification-argument?commentId=E82YzXxvS6nBdCAYc). But using an LLM as the labeler instead of a human just means your powerful planner figures out how to hack the LLM. It's the same problem either way.

**Simplicia**: Do you _need_ more powerful systems? If you can get an army of cheap IQ 140 alien actresses who stay in character, that sounds like a game-changer. If you have to take over the world and institute a global compute governance regime to prevent the emergence of unfriendlier, more powerful forms of AI, they could help you do it.

**Doomer**: I fundamentally disbelieve in this scenario, but granting it for the sake of argument ... I think you're failing to appreciate that in this story, you've already handed off the keys to the universe, even if your AIs have been trained to be "corrigible" and "obey orders" in a way that seemed to work at low power levels. When humans servants who are trying to be helpful ask questions of their master, it's because they don't know what the master wants. If the servants could predict how the master _would_ respond to any question, there would be no need to actually ask. A "servant" who could forsee the detailed outcome of every possible sequence of questions, would be in a position to choose among those outcomes—and in so choosing, it would be in control. Look, you understand that AIs trained on human data are not human, right?

**Simplicia**: Sure. For example, I certainly don't believe that LLMs that convincingly talk about "happiness" are actually happy. The training data only pins down external behavior.

**Doomer**: So your plan is to hand over our entire future lightcone to an alien agency that seemed to behave nicely while you were training it, and just—hope it generalizes well? Do you really want to roll those dice?

**Simplicia**: _[after thinking for a few seconds]_ Yes?

**Doomer**: _[grimly]_ You really are your father's daughter.

**Simplicia**: My father believed in [the power of iterative design](https://www.lesswrong.com/posts/xFotXGEotcKouifky/worlds-where-iterative-design-fails). That's the way engineering, and life, has always worked. We raise our children the best we can, trying to learn from our mistakes early on, even knowing that those mistakes have consequences: children don't always share their parents' values, or treat them kindly. He would have said it would go the same in principle for our AI mind-children—

**Doomer**: _[exasperated]_ But—

**Simplicia**: Yes, despite the larger stakes and novel context, where we're growing new kinds of minds _in silico_, rather than providing mere cultural input to the code in our genes.

Of course, there is a first time for everthing—one way or the other. If it were rigorously established that the way engineering and life have always worked would lead to certain disaster, perhaps the world's power players could be persuaded to turn back, to reject the imperative of history, to choose barrenness, at least for now, rather than bring vile offspring into our world. It would seem that the fate of the lightcone depends on—

**Doomer**: I'm afraid so—

**Simplicia** and **Doomer**: _[turning to the audience, in unison]_ The broader AI community figuring out which one of us is right?

**Doomer**: We're hosed.
