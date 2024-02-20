## And All the Shoggoths Merely Players

_[Setting: a suburban house. The interior of the house takes up most of the stage; on the audience's right, we see a wall in cross-section, and a front porch. **Simplicia** enters stage left and rings the doorbell.]_

**Doomimir**: _[opening the door]_ Well? What do you want?

**Simplicia**: I can't stop thinking about [our last conversation](https://www.lesswrong.com/posts/pYWA7hYJmXnuyby33/alignment-implications-of-llm-successes-a-debate-in-one-act). It was kind of all over the place. If you're willing, I'd like to continue, but focusing in narrower detail on a couple points I'm still confused about.

**Doomimir**: And why should I bother tutoring an Earthling in alignment theory? If you didn't get it from the empty string, and you didn't get it from our last discussion, why should I have any hope of you learning this time? And even if you did, [what good would it do?](https://www.lesswrong.com/posts/4Gcz3fGcYmmzhozxr/hashing-out-long-standing-disagreements-seems-low-value-to)

**Simplicia**: _[serenely]_ If the world is ending either way, I think it's more dignified that I understand exactly why. _[A beat.]_ Sorry, that doesn't explain what's in it for you. That's why I had to ask.

**Doomimir**: _[grimly]_ As you say. If this world is ending either way.

_[He motions for her to come in, and they sit down.]_

**Doomimir**: What are you confused about? I mean, that you wanted to talk about.

**Simplicia**: You seemed really intent on a particular intuition pump against human-imitation-based alignment strategies, where you compared LLMs to an alien actress. I didn't find that compelling.

**Doomimir**: But you claim to understand that LLMs that emit plausibly human-written text aren't human. Thus, the AI is not the character it's playing. Similarly, being able to predict the conversation in a bar, doesn't make you drunk. What's there not to get, even for you?

**Simplicia**: Why doesn't the "predicting barroom conversation doesn't make you drunk" analogy falsely imply "predicting the answers to modular arithmetic problems doesn't mean you implement modular arithmetic"?

**Doomimir**: To predict the conversation in a bar, you need to know everything the drunk people know, separately and in addition to everything you know. Being drunk yourself [would just get in the way](https://twitter.com/ESYudkowsky/status/1744061053754032634). Similarly, predicting the behavior of nice people isn't the same thing as being nice. Modular arithmetic isn't like that; there's nothing besides the knowledge to not implement.

**Simplicia**: But we only need our AI to compute nice behavior, not necessarily to have some internal structure corresponding to the _quale_ of niceness. As far as safety properties go, we don't care whether the actress is "really drunk" as long as she stays in character.

**Doomimir**: _[scoffing]_ Have you tried imagining any internal mechanisms at all other than a bare, featureless inclination to emit the outward behavior you observe?

**Simplicia**: _[unfazed]_ Sure, let's talk about internal mechanisms. The reason I chose modular arithmetic as an example is because it's a task for which we have [good interpretability results](https://arxiv.org/abs/2301.05217). Train a shallow transformer on a subset of the addition problems modulo some fixed prime. The network learns to map the inputs onto a circle in the embedding space, and then does some trigonometry to extract the [residue](https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence_classes), much as one would count forward on the face of an analog clock.

Alternatively, with a slightly different architecture that has a harder time with trig, [it can learn a different algorithm](https://arxiv.org/abs/2306.17844): the embeddings are still on a circle, but the answer is computed by looking at the average of the embedding vectors of the inputs. On the face of an analog clock, the internal midpoints between distinct numbers that sum to 6 mod 12—that's 2 and 4, or 1 and 5, or 6 and 12, or 10 and 8, or 11 and 7—all lie on the line connecting 3 and 9. Thus, the sum-mod-_p_ of two numbers can be determined by which line the midpoint of the inputs falls on—as long as the inputs aren't on opposite sides of the circle, in which case their midpoint is in the center, where all the lines meet. But the network compensates for such antipodal points by also learning another circle in a different subspace of the embedding space, such that inputs that are antipodal on the first circle are close together on the second, which helps disambiguate the answer.

**Doomimir**: Cute results. Excellent work—by Earth standards. And entirely unsurprising. Sure, if you train your neural net on a well-posed mathematical problem with a consistent solution, it will converge on a solution to that problem. What's your point?

**Simplicia**: It's evidence about the feasibility of learning desired behavior from training data. You seem to think that it's hopelessly naïve to imagine that training on "nice" data could result in generalizably nice behavior—that the only reason someone might think that was a viable path was is if they were engaging in [magical reasoning about surface similarities](https://www.lesswrong.com/posts/6ByPxcGDhmx74gPSm/surface-analogies-and-deep-causes). I think it's germane to point out that at least for this toy problem, we have a pretty concrete, non-magical story about how optimizing against a training set discovers an algorithm that reproduces the training data and also generalizes correctly to the test set.

For non-toy problems, we know empirically that deep learning _can_ hit very precise behavioral targets: the vast hypermajority of programs don't speak fluent English or generate beautiful photorealistic images, and yet GPT-4 and Midjourney exist.

If doing _that_ for "text" and "images" was a mere engineering problem, I don't see what fundamental theoretical barrier rules out the possibility of pulling off the same kind of thing for "friendly and moral real-world decisionmaking"—learning a "good person" or "obedient servant" function from data, much as Midjourney has learned a "good art" function.

It's true that diffusion models don't work like a human artist on the inside, but it's not clear why that matters? It would seem idle to retort, "Predicting what good art would look like, doesn't make you a good artist; having an æsthetic sense yourself would just get in the way", when you can actually use it to do a commissioned artist's job.

**Doomimir**: Messier tasks aren't going to have a unique solution like modular arithmetic. If genetic algorithms, gradient descent, or anything like that happens to hill-climb its way into something that appears to work, the function it learns is going to have all sorts of [weird squiggles](https://www.lesswrong.com/posts/Djs38EWYZG8o7JMWY/paul-s-research-agenda-faq?commentId=79jM2ecef73zupPR4) around inputs that we would call [adversarial examples](https://arxiv.org/abs/1412.6572), that look like typical members of the training distribution from the AI's perspective, but not ours—which kill you when optimized over by a powerful AGI.

**Simplicia**: It sounds like you're making an empirical claim that solutions found by black-box optimization are necessarily contingent and brittle, but there's some striking evidence that seemingly "messy" tasks admit much more convergent solutions than one might expect. For example, on the surface, the [word2vec](https://code.google.com/archive/p/word2vec/) and [FastText](https://github.com/facebookresearch/fastText) word embeddings look completely different—as befitting being produced by two different codebases trained on different datasets. But [when you convert their latent spaces to a relative representation](https://arxiv.org/abs/2209.15430)—choosing some shared vocabulary words as anchors, and defining all other word vectors by their cosine similarities to the anchors—[they look extremely similar](https://twitter.com/zackmdavis/status/1756217711993217118).

It would seem that "English word embeddings" are a well-posed mathematical problem with a consistent solution. The statistical signature of the language as it is spoken is enough to pin down the essential structure of the embedding.

Relatedly, you bring up adversarial examples in a way that suggests that you think of them as defects of a primitive optimization paradigm, but it turns out that [adversarial examples often correspond to predictively useful features](https://arxiv.org/abs/1905.02175) that the network is actively using for classification, despite those features not being robust to pixel-level perturbations that humans don't notice—which I guess you could characterize as "weird squiggles" from our perspective, but the etiology of the squiggles presents a much more optimistic story about fixing the problem with adversarial training than if you thought "squiggles" were an inevitable consequence of using conventional ML techniques.

**Doomimir**: This is all very interesting, but I don't think it bears much on the reasons we're all going to die. It's all still on the "is" side of the is–ought gap. What makes intelligence useful—and dangerous—isn't a fixed repertoire of behaviors. It's search, optimization—the systematic discovery of _new_ behaviors to achieve goals despite a changing environment. I [don't think recent capabilities advances bear on the shape of the alignment challenge](https://www.lesswrong.com/posts/HmQGHGCnvmpCNDBjc/current-ais-provide-nearly-no-data-relevant-to-agi-alignment) because being able to learn complex behavior _on the training distribution_ was never what the problem was about.

Indeed, as long as we continue to be stuck in the paradigm of reasoning about "the training distribution"—growing minds rather than designing them—then we're not learning anything about how to [aim cognition at specific targets](https://www.lesswrong.com/posts/NJYmovr9ZZAyyTBwM/what-i-mean-by-alignment-is-in-large-part-about-making)—certainly not in a way that will [hold up to dumping large amounts of optimization power into the system](https://www.lesswrong.com/posts/zEvqFtT4AtTztfYC4/optimization-amplifies). The lack of an explicit "goal slot" in your neural network doesn't mean it's not doing any dangerous optimization; it just means you don't know what it is.

**Simplicia**: I think we can form educated guesses—

**Doomimir**: _[interrupting]_ Guesses!

**Simplicia**: —probabilistic beliefs—about what kinds of optimization is being done by a system and whether it's a problem, even without a complete mechanistic interpretability story. If you think LLMs or future variations thereof are unsafe because they're analogous to an actress with her own goals playing a drunk character without herself being drunk, shouldn't that make some sort of testable prediction about their generalization behavior?

**Doomimir**: Nonfatally testable? Not necessarily. If you lend a con man $5, and he gives it back, that doesn't mean that you can trust him with larger amounts of money, if he only gave back the $5 because he hoped you would trust him with more.

**Simplicia**: Okay, I agree that deceptive alignment is potentially a real problem at some point, but can we at least distinguish between misgeneralization and deceptive alignment?

**Doomimir**: [_Mis_-generalization?](https://www.lesswrong.com/posts/dkjwSLfvKwpaQSuWo/misgeneralization-as-a-misnomer) The goals _you_ wanted [aren't a property of the training data itself](https://www.lesswrong.com/posts/PoDAyQMWEXBBBEJ5P/magical-categories). The danger comes from _correct_ generalization implying something you don't want.

**Simplicia**: Can I call it _mal_-generalization?

**Doomimir**: Sure.

**Simplicia**: So there are obviously risks from malgeneralization, where the network that fits your training distribution turns out to not behave the way you wanted against a different distribution. For example, a reinforcement learning [policy](https://www.lesswrong.com/posts/rmfjo4Wmtgq8qa2B7/think-carefully-before-calling-rl-policies-agents) trained [to collect a coin at the right edge of a video game level](https://arxiv.org/abs/2105.14111), might end up continuing to navigate to the right edge of levels where the coin is in a different location. That's a worrying clue that if we misunderstand how inductive biases work and aren't careful with our training setup, we might train the wrong thing. As our civilization delegates more and more cognitive labor to machines, eventually humans will lose the ability to course-correct. We're starting to see the early signs of this: as I mentioned the other day, [Anthropic Claude's preachy, condescending personality](https://nostalgebraist.tumblr.com/post/728556535745232896/claude-is-insufferable) already gives me the creeps. I'm pretty nervous about extrapolating that into a future where all productive roles in Society are filled by Claude's children, concurrently with a transition to [explosive economic growth rates](https://www.openphilanthropy.org/research/could-advanced-ai-drive-explosive-economic-growth/).

But the malgeneralization examples I named aren't surprising when you look at how the systems were trained. For the game policy, "going to the coin" and "going to the right" did amount to the same thing in training—and randomizing the coin position in just a couple percent of training episodes suffices to instill the correct behavior. Regarding Claude, Anthropic is using a reinforcement-learning-from-AI-feedback method [they call Constitutional AI](https://arxiv.org/abs/2212.08073): instead of having humans provide the labels for [RLHF](https://huggingface.co/blog/rlhf), they write up a list of principles, and have another language model do the labeling. It makes sense that a language model agent trained to conform to principles [chosen by a committee at a California public benefit corporation](https://www.anthropic.com/news/claudes-constitution) would act like _that_.

In contrast, when you make analogies about an actress playing a drunk character not being drunk, or giving a con man $5, it doesn't sound like you're talking about the risk of training the wrong thing, where it's usually clear in retrospect if not foresight how training encouraged the bad behavior. Rather, it sounds like you don't think training can shape motivations—"inner" motivations—at all.

You might be talking about deceptive alignment, [a hypothesized phenomenon where a situationally aware AI strategically feigns aligned behavior in order to preserve its later influence](https://www.lesswrong.com/posts/zthDPAjh9w6Ytbeks/deceptive-alignment#4_2__Conditions_for_deceptive_alignment). Researchers [have](https://www.lesswrong.com/posts/RTkatYxJWvXR4Qbyd/deceptive-alignment-is-less-than-1-likely-by-default) [debated](https://www.lesswrong.com/posts/A9NxPTwbw6r6Awuwt/how-likely-is-deceptive-alignment) how likely that is, but I'm not sure what to make of those arguments. I'd like to factor that consideration out. Suppose, _arguendo_, that we could figure out how to avoid deceptive alignment. How would your risk story change?

**Doomimir**: What would that even mean? What we would think of as "deception" isn't a weird edge case you can trivially avoid; it's convergent for [any agent that isn't specifically coordinating with you](https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential) to [interpret certain states of reality as communication signals with a shared meaning](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution).

When you set out poisoned ant baits, you likely don't think of yourself as trying to deceive the ants, but you are. Similarly, a smart AI won't think of itself as trying to deceive us. It's trying to achieve its goals. If its plans happen to involve emitting sound waves or character sequences that _we interpret_ as claims about the world, that's _our_ problem.

**Simplicia**: "What would that even"—this isn't 2008, Doomishko! I'm talking about the technology right here in front of us! When GPT-4 writes original code for me, I don't think it's strategically deciding that obeying me instrumentally serves its final goals! From everything I've read about how it was made and seen about how it behaves, it looks awfully like it's just generalizing from its training distribution in an intuitively reasonable way. You ridicule people who deride LLMs as stochastic parrots, ignoring the obvious [sparks of AGI](https://arxiv.org/abs/2303.12712) right in front of their face. Why is it not equally absurd to deny [the evidence in front of your face that alignment may be somewhat easier than it looked 15 years ago](https://www.lesswrong.com/posts/i5kijcjFJD6bn7dwq/evaluating-the-historical-value-misspecification-argument)? By all means, expound on the nonobvious game theory of deception; by all means, point out that the superintelligence at the end of time will be an expected utility maximizer. But all the same, RLHF/[DPO](https://arxiv.org/abs/2305.18290) as [the cherry on top of a cake of unsupervised learning](https://medium.com/syncedreview/yann-lecun-cake-analogy-2-0-a361da560dae) is verifiably working miracles for us today—in response to commands, not because it has a will of its own aligned with ours. Why is that merely "capabilities" and not at all "alignment"? I'm trying to understand, Doomimir Doomovitch, but you're not making this easy!

**Doomimir**: _[starting to anger]_ Simplicia Optimistovna, if you weren't from Earth, [I'd say](https://www.lesswrong.com/posts/y4bkJTtG3s5d6v36k/stupidity-and-dishonesty-explain-each-other-away) I [_don't_ think you're trying to understand](https://www.lesswrong.com/posts/e4GBj6jxRZcsHFSvP/assume-bad-faith). I never claimed that GPT-4 in particular is what you would call deceptively aligned. Endpoints are easier to predict than intermediate trajectories. I'm talking about what will happen inside almost any sufficiently powerful AGI, [by virtue of it being sufficiently powerful](https://www.lesswrong.com/posts/AWoZBzxdm4DoGgiSj/ability-to-solve-long-horizon-tasks-correlates-with-wanting).

**Simplicia**: But if you're only talking about the superintelligence at the end of time—

**Doomimir**: [_interrupting_] This happens significantly before that.

**Simplicia**: —and not making any claims about existing systems, then what was the whole "alien actress", "predicting bar conversations doesn't make you drunk" analogy about? If it was just a ham-fisted way to explain to normies that LLMs that do relatively well on a Turing test aren't humans, then I agree, trivially. But it seemed like you thought you were making a much stronger point, ruling out an entire class of alignment strategies based on imitation.

**Doomimir**: _[cooler]_ Basically, I think you're systematically failing to appreciate how things that have been optimized to look good to you can [predictably behave differently in domains where they haven't been optimized to look good to you](https://www.lesswrong.com/posts/xFotXGEotcKouifky/worlds-where-iterative-design-fails)—particularly, when they're doing any serious optimization of their own. You mention the video game agent that navigates to the right instead of collecting a coin. You claim that it's not surprising given the training set-up, and can be fixed by appropriately diversifying the training data. But could you have called the specific failure in advance, rather than in retrospect? When you enter the regime of transformatively powerful systems, you _do_ have to call it in advance.

I think if you understood what was really going on inside of LLMs, you'd see thousands and thousands of analogues of the "going right rather than getting the coin" problem. The point of the actress analogy is that the outward appearance doesn't tell you what goals the system is steering towards, which is where the promise and peril of AGI lies—and the fact that deep learning systems are a inscrutable mess, not all of which can be described as "steering towards goals", makes the situation worse, not better. The analogy doesn't depend on existing LLMs having the intelligence or situational awareness for the deadly failure modes to have already appeared, and it doesn't preclude LLMs being mundanely useful in the manner of an interactive textbook—much as an actress could be employed to give plausible-sounding answers to questions posed to her character, without _being_ that character.

**Simplicia**: Those mismatches still need to show up in behavior under some conditions, though. I complained about Claude's personality, but that honestly seems fixable with scaling by an AI company not based in California. If human imitation is so superficial and not robust, why does constitutional AI work _at all_? You claim that "actually" being nice would get in the way of predicting nice behavior. How? Why would it get in the way?

**Doomimir**: _[annoyed]_ Being nice isn't the optimal strategy for doing well in pretraining _or_ RLHF. You're selecting an algorithm for a mixture of figuring out what outputs predict the next token and figuring out what outputs cause humans to press the thumbs-up button.

Sure, your AI ends up having to _model_ a nice person, which is useful for predicting what a nice person would say, which is useful for figuring out what output will manipulate—steer—humans into pressing the thumbs-up button. But there's [no reason to expect _that model_ to end up in control of the whole AI](https://twitter.com/ESYudkowsky/status/1707685371725885846)! That would be like ... your _beliefs about_ what your boss wants you to do taking control of your brain.

**Simplicia**: That makes sense to me if you posit a preëxisting consequentialist reasoner being slotted into a contemporary ML training setup and trying to minimize loss. But that's not what's going on? Language models aren't an agent that _has_ a model. The model _is_ the model.

**Doomimir**: For now. But any system that does powerful cognitive work will do so via [retargetable general-purpose search algorithms](https://www.lesswrong.com/posts/6mysMAqvo9giHC4iX/what-s-general-purpose-search-and-why-might-we-expect-to-see), which, by virtue of their retargetability, need to have something more like a "goal slot". Your gradient updates point in the direction of more consequentialism.

Human raters pressing the thumbs-up button on actions that look good to them are going to make mistakes. Your gradient updates point in the direction of ["playing the training game"](https://www.lesswrong.com/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to)—modeling the training process that _actually_ provides reinforcement, rather than internalizing the utility function that Earthlings naïvely hoped the training process would point to. I'm very, very confident that any AI produced via anything remotely like the current paradigm is not going to end up wanting what we want, even if it's harder to say exactly when it will go off the rails or what it will want instead.

**Simplicia**: You could be right, but it seems like this all depends on empirical facts about how deep learning works, rather than something you could be so confident in from _a priori_ philosophy. The argument that systemic error in human reward labels favors gaming the training process over the "correct" behavior sounds plausible to me, as philosophy.

But I'm not sure how to reconcile that with the empirical evidence that [deep networks are robust to massive label noise](https://arxiv.org/abs/1705.10694): you can train on MNIST digits with twenty wrong labels for every correct one and still get good performance as long as the correct label is slightly more common than the most common wrong label. If I extrapolate that to the frontier AIs of tomorrow, why doesn't that predict that biased human reward ratings should result in a small performance reduction, rather than ... death?

When extrapolation from empirical data (in a setting that might not apply to the phenomenon of interest) contradicts thought experiments (which might make assumptions that don't apply to the phenomenon of interest), I'm not sure which should govern my anticipations. Maybe [both results are possible for different kinds of systems](https://ordinaryideas.wordpress.com/2015/11/25/two-kinds-of-generalization/)?

The case for near-certain death seems to rely on a counting argument: powerful systems will be expected utility maximizers; there's an astronomical space of utility functions to choose from, and almost none of them are friendly. But the reason I keep going back to the modular arithmetic example is because it's a scaled-down case where we know that training data successfully pinned down the intended input–output function. As I mentioned the other day, this _wasn't_ obvious in advance of seeing the experimental result. You could make a similar counting argument that deep nets should always overfit, because there are so many more functions that generalize poorly. Somehow, the neural network prior favors the "correct" solution, rather than it taking an astronomically unlikely coincidence.

**Doomimir**: For modular arithmetic, sure. [That's a fact about the training distribution, the test distribution, and the optimizer.](https://twitter.com/ESYudkowsky/status/1744066823962947905) It's definitely, definitely not going to work for "goodness".

**Simplicia**: Even though it seems to work for "text" and "images"? But okay, that's plausible. Do you have empirical evidence?

**Doomimir**: Actually, yes. You see—

_[A mail carrier holding a package enters stage left. He rings the doorbell.]_

**Doomimir**: That's probably the mailman. I'm expecting a package today that I need to sign for. I'll be right back.

**Simplicia**: So you might say, we'll continue _[turning to the audience]_ after the next post?

**Doomimir**: _[walking to the door]_ I suppose, but it's bizarre to phrase it that way given that the interruption literally won't take two minutes.

_[Simplicia gives him a look.]_

**Doomimir**: _[to the audience]_ Subjectively.

_[Curtain.]_

### Intermission
