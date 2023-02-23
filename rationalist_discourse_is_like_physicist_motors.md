## "Rationalist Discourse" Is Like "Physicist Motors"

Imagine being a student of physics, and coming across a blog post proposing a list of guidelines for "physicist motors"—motor designs informed by the knowledge of physicists, unlike ordinary motors.

Even if most of the things on the list seemed like sensible guidelines to keep in mind when designing a motor, the framing would seem very odd. The laws of physics describe how energy can be converted into work. To the extent that _any_ motor accomplishes anything, it happens within the laws of physics. There are theoretical ideals describing how motors need to work in principle, like [the Carnot engine](https://en.wikipedia.org/wiki/Carnot_heat_engine), but you can't actually build an ideal Carnot engine; real-world electric motors or diesel motors or jet engines all have their own idiosyncratic lore depending on the application and the materials at hand; an engineer who worked on one, might not the be best person to work on another. You might appeal to principles of physics to explain why some particular motor is inefficient or poorly-designed, but you would not speak of _physicist motors_ as if that were a distinct category of thing—and if someone _did_, you might quietly begin to doubt how much they really knew about physics.

As a student of rationality, I feel the same way about guidelines for "rationalist discourse." The laws of probability and decision theory describe how information can be converted into optimization power. To the extent that _any_ discourse accomplishes anything, [it happens within the laws of rationality](https://www.lesswrong.com/posts/eY45uCCX7DdwJ4Jha/no-one-can-exempt-you-from-rationality-s-laws).

Rob Bensinger proposes ["Elements of Rationalist Discourse"](https://www.lesswrong.com/posts/svuBpoSduzhYjFPrA/elements-of-rationalist-discourse) as a companion to Duncan Sabien's earlier ["Basics of Rationalist Discourse"](https://www.lesswrong.com/posts/XPv4sYrKnPzeJASuk/basics-of-rationalist-discourse-1). _Most_ of the things on both lists are, indeed, sensible guidelines that one might do well to keep in mind when arguing with people, but as Bensinger notes, "Probably this new version also won't match '_the_ basics' as other people perceive them."

But there's a reason for that: a list of guidelines has the wrong type signature for being "_the_ basics". The _actual_ basics are the principles of rationality one would appeal to _explain which guidelines are a good idea_: principles like how [evidence is the systematic correlation between possible states of your observations and possible states of reality](https://www.lesswrong.com/posts/6s3xABaXKPdFwA3FS/what-is-evidence), how [you need evidence to locate the correct hypothesis in the space of possibilities](https://www.lesswrong.com/posts/nj8JKFoLSMEmD3RGp/how-much-evidence-does-it-take), how [the quality of your conclusion can only be improved by arguments that have the power to _change_ that conclusion](https://www.lesswrong.com/posts/34XxbRFe54FycoCDw/the-bottom-line).

Contemplating these basics, it should be clear that there's just not going to be anything like a unique style of "rationalist discourse", any more than there is a unique "physicist motor." There are theoretical ideals describing how discourse needs to work in principle, like [Bayesian reasoners with common priors exchanging probability estimates](https://en.wikipedia.org/wiki/Aumann's_agreement_theorem), but you can't actually build an ideal Bayesian reasoner. Rather, different discourse algorithms (the collective analogue of ["cognitive algorithm"](https://www.lesswrong.com/posts/HcCpvYLoSFP4iAqSz/rationality-appreciating-cognitive-algorithms)) leverage the laws of rationality to convert information into optimization in somewhat different ways, depending on the application and the population of interlocutors at hand, much as electric motors and jet engines both leverage the laws of physics to convert energy into work without being identical to each other, and with each requiring their own engineering sub-specialty to design.

Or to use [another standard metaphor](https://www.lesswrong.com/posts/teaxCFgtmCQ3E9fy8/the-martial-art-of-rationality), there's also just not going to be a unique martial art. Boxing and karate and ju-jitsu all have their own idiosyncratic lore adapted to different combat circumstances, and a master of one would easily defeat a novice of the other. One might appeal to the laws of physics and the properties of the human body to explain why some particular martial arts school was not teaching their students to fight effectively. But if some particular karate master were to brand their own lessons as the "basics" or "elements" of "martialist fighting", you might quietly begin to doubt how much actual fighting they had done: either all fighting is "martialist" fighting, or "martialist" fighting isn't actually necessary for beating someone up.

One historically important form of discourse algorithm is _debate_, and its close variant the _adversarial court system_. It works by separating interlocutors into two groups: one that searches for arguments in favor of a belief, and another that seaches for arguments against the belief. Then anyone listening to the debate can consider all the arguments to help them decide whether or not to adopt the belief. (In the _court_ variant of debate, a designated "judge" or "jury" announces a "verdict" for or against the belief, which is added to the court's [shared map](https://www.lesswrong.com/posts/9QxnfMYccz9QRgZ5z/the-costly-coordination-mechanism-of-common-knowledge), where it can be referred to in subsequent debates, or "cases.")

The enduring success and legacy of the debate algorithm can be attributed to how it circumvents a critical design flaw in individual human reasoning, the tendency to "rationalize"—to preferentially search for new arguments for an already-determined conclusion.

(At least, "design flaw" is one way of looking at it—a more complete discussion would consider how individual human reasoning capabilities _co-evolved_ with the debate algorithm—and, as I'll briefly discuss later, this "bug" for the purposes of reasoning is actually a "feature" for the purposes of deception.)

As a consequence of rationalization, once a conclusion has been reached, even prematurely, further invocations of the biased argument-search process are likely to further entrench the conclusion, even when strong counterarguments exist (in regions of argument-space neglected by the biased search). The debate algorithm solves this sticky-conclusion bug by distributing a search for arguments and counterarguments among multiple humans, [ironing out falsehoods](https://www.lesswrong.com/posts/iThwqe3yPog56ytyq/aiming-for-convergence-is-like-discouraging-betting) by pitting two biased search processes against each other. (For readers more familiar with artificial than human intelligence, [generative adversarial networks](https://en.wikipedia.org/wiki/Generative_adversarial_network) work on a similar principle.)

For all its successes, the debate algorithm also suffers from many glaring flaws. For one example, the benefits of improved conclusions mostly accrue to third parties who haven't already entrenched on a conclusion; debate participants themselves are rarely seen changing their minds. For another, just the choice of what position to debate has a distortionary effect even on the audience; if [it takes more bits to _locate_ a hypothesis for consideration than to convincingly confirm or refute it](https://www.lesswrong.com/posts/MwQRucYo6BZZwjKE7/einstein-s-arrogance), then most of the relevant cognition has already happened by the time people are arguing for or against it. Debate is also inefficient: for example, if the "defense" in the court variant happens to find evidence or arguments that would benefit the "prosecution", the defense has no incentive to report it to the court, and there's no guarantee that the prosecution will independently find it themselves.

Really, the whole idea is so galaxy-brained that it's amazing it works at all. There's only one reality, so correct information-processing should result in everyone agreeing on the best, most-informed belief-state. [This is formalized in Aumann's famous agreement theorem](https://en.wikipedia.org/wiki/Aumann's_agreement_theorem), but even without studying the proofs, the result is _obvious_. A generalization to a more realistic setting without instantaneous communication gives the result that disagreements should be unpredictable: after Bob the Bayesian tells Carol the Coherent Reasoner his belief, Bob's expectation of the difference between his belief and Carol's new belief should be zero. (That is, Carol might still disagree, but Bob shouldn't be able to predict whether it's in the same direction as before, or whether Carol now holds a _more_ extreme position on what adherents to the debate algorithm would call "Bob's side.")

That being the normative math, why does the human world's enduringly dominant discourse algorithm take for granted the ubiquity of, not just disagreements, but _predictable_ disagreements? Isn't that crazy?

Yes. It is crazy. One might hope to do better by developing some sort of training or discipline that would allow discussions between practitioners of such "rational arts" to depart from the harnessed insanity of the debate algorithm with its stubbornly stable "sides", and instead mirror the side-less Bayesian ideal, the free flow of all available evidence channeling interlocutors to an unknown destination.

Back in late 'aughts, an attempt to articulate what such a discipline might look like was published on a blog called _Overcoming Bias_. (You probably haven't heard of it.) It's been well over a decade since then. How is that going?

Eliezer Yudkowsky [laments](https://www.lesswrong.com/posts/7im8at9PmhbT4JHsW/ngo-and-yudkowsky-on-alignment-difficulty):

> In the end, a lot of what people got out of all that writing I did, was not the deep object-level principles I was trying to point to—they did not really get [Bayesianism as thermodynamics](https://www.lesswrong.com/posts/QkX2bAkwG2EpGvNug/the-second-law-of-thermodynamics-and-engines-of-cognition), say, they did not become able to see [Bayesian structures](https://www.lesswrong.com/posts/QrhAeKBkm2WsdRYao/searching-for-bayes-structure) any time somebody sees a thing and changes their belief. What they got instead was something much more meta and general, a vague spirit of how to reason and argue, because that was what they'd spent a lot of time being exposed to over and over and over again in lots of blog posts.

"A vague spirit of how to reason and argue" seems like an apt description of what "Basics of Rationalist Discourse" and "Elements of Rationalist Discourse" are attempting to codify—but with no explicit instruction on which guidelines arise from deep object-level principles of normative reasoning, and which from mere taste, politeness, or adaptation to local circumstances, it's unclear whether students of 2020s-era "rationalism" are poised to significantly outperform the traditional debate algorithm—and it seems alarmingly possible to do _worse_, if the collaborative aspects of modern "rationalist" discourse allow participants to introduce errors that a designated adversary under the debate algorithm would have been incentivized to correct, and most "rationalist" practioners don't have a deep theoretical understanding of _why debate works_ as well as it does.

Looking at Bensinger's "Elements", there's a clear-enough connection between the first eight points (plus three sub-points) and the laws of normative reasoning. Truth-Seeking, Non-Deception, and Reality-Minding, trivial. Non-Violence, because violence doesn't distinguish between truth and falsehood. Localizability, in that I can affirm the [validity](https://www.lesswrong.com/posts/WQFioaudEH8R7fyhm/local-validity-as-a-key-to-sanity-and-civilization) of an argument that A would imply B, while simultaneously denying A. Alternative-Minding, because decisionmaking under uncertainty requires living in many possible worlds. And so on. (Lawful justifications for the elements of Reducibility and Purpose-Minding left as an exercise to the reader.)

But then we get this:

> 9. **Goodwill.** Reward others' good epistemic conduct (_e.g._, updating) more than most people naturally do. Err on the side of carrots over sticks, forgiveness over punishment, and civility over incivility, unless someone has explicitly set aside a weirder or more rough-and-tumble space.

I can believe that these are good ideas for having a pleasant conversation. But separately from whether "Err on the side of forgiveness over punishment" is a good idea, it's hard to see how it belongs on the _same_ list as things like "Try not to 'win' arguments using [...] tools that work similarly well whether you're right or wrong" and "[A]sk yourself what Bayesian evidence you have that you're not in those alternative worlds".

The difference is this. If your discourse algorithm lets people "win" arguments with tools that work equally well whether they're right or wrong, then your discourse _gets the wrong answer_ (unless, by coincidence, the people who are best at winning are also the best at being right). If the interlocutors in your discourse don't ask themselves what Bayesian evidence they have that they're not in alternative worlds, then your discourse _gets the wrong answer_ (if you happen to live in an alternative world).

If your discourse algorithm errs on the side of sticks over carrots (perhaps, emphasizing _punishing_ others' _bad_ epistemic conduct more than most people naturally do) ... then what? How, specifically, are more rough-and-tumble spaces less rational, such that an list of "Elements of Rationalist Discourse" has the authority to designate them as non-default?

I'm not saying that goodwill is _bad_, particularly. I totally believe that goodwill is a necessary part of many specific discourse algorithms that produce maps that reflect the territory. It just seems like a bizarre thing to put in a list of guidelines for "rationalist discourse".

It's as if a guideline for designing "physicist motors" had a point saying, "Use more pistons than most engineers naturally do." It's not that pistons are bad, particularly. Lots of engine designs use pistons! It's just, the pistons are there specifically to convert force from expanding gas into rotational motion.

[TODO: finish that graf]

The example given for "[r]eward[ing] others' good epistemic conduct" is "updating".

[TODO: my occasional problem where I agree too much with whoever I'm currently talking to; rewarding me for visibly "updating" would actually be wrong, an example of the guideline pointing in the wrong direction]

A footnote on the "Goodwill" element elaborates:

> Note that this doesn't require assuming everyone you talk to is honest or has good intentions.
>
> It does have some overlap with the rule of thumb "as a very strong but defeasible default, carry on object-level discourse as if you were role-playing being on the same side as the people who disagree with you".

[TODO: critique the "Goodwill" guideline from "Elements"
a lot of disagreements are explained by conflicts—people disorting  so obfuscating conflicts by "roleplaying being on the same side" makes things _worse_; it's better to explicit about not being on the same side, so then you can look for Pareto improvements to make the conflict less destructive
]

Links—
https://slatestarcodex.com/2014/03/24/should-you-reverse-any-advice-you-hear/
argumentative theory of reasoning
we change our minds less often than we think
Don't Double-Crux With Suicide Rock
We can't forsee to disagree
when you can't eliminate the word

 * If you don't trust people to understand the law, maybe you can lie-to-children them with a list of guidelines, as with how Sabien's list says its 80/20. I'm more optimistic in people's capabilities; rather than proposing my own list of guidelines, I think it's an informative excercise to look at other people's guidelines, and explain how they arise from the Law.

https://www.lesswrong.com/posts/bkSkRwo9SRYxJMiSY/beautiful-probability
https://www.lesswrong.com/posts/CPP2uLcaywEokFKQG/toolbox-thinking-and-law-thinking

if deficits of are deemed a legitimate cause to [shut down conversations](https://www.lesswrong.com/posts/wqmmv6NraYv4Xoeyj/conversation-halters).

https://twitter.com/ESYudkowsky/status/1355712437006204932
> A "Physics-ist" is trying to engage in a more special human activity, hopefully productively, where they *think* about light in order to use it better.
