## And All the Shoggoths Merely Players

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

_[Curtain.]_

### Scene 1

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

Indeed, as long as we continue to be stuck in the paradigm of reasoning about "the training distribution"—growing minds rather than designing them—then we're not learning anything about how to [aim cognition at specific targets](https://www.lesswrong.com/posts/NJYmovr9ZZAyyTBwM/what-i-mean-by-alignment-is-in-large-part-about-making)—certainly not in a way that will [hold up to dumping large amounts of optimization power into the system](https://www.lesswrong.com/posts/zEvqFtT4AtTztfYC4/optimization-amplifies).

_[he eyes the television]_ Does that suffice? Will you leave me to enjoy my short life?

**Simplicia**: Not yet. I understand the theory of utility optimization—

**Doomimir**: No you don't.

**Simplicia**: I have some nonzero but undoubtedly incomplete understanding of the theory of utility optimization?

_[Doomimir nods graciously.]_

**Simplicia**: The theory inspires me to imagine a simple story where AI is a magic box with a "goal slot" where the user inputs a utility function _U_. When you switch the box on, it computes a plan to maximize _U_. As you turn the dial up to make it use more magic, then at some point, everyone dies, because we're made out of atoms that can be arranged into a higher-_U_ configuration.

**Doomimir**: More or less.

**Simplicia**: I assume we agree that contemporary deep learning techniques are not a magic box with a goal slot. _I_ think we should be looking at contemporary techniques and their likely future extensions, and figuring out how to make them safe and useful, bearing in mind the danger implied by our theories which suggest that the superintelligence at the end of time will look more like the magic box. I think that _you_ think that I'm retarded for having any hope at all that likely future extensions of contemporary techniques could be made safe.

**Doomimir**: Again, more or less. The lack of an explicit "goal slot" in your neural network doesn't mean it's not doing any dangerous optimization; it just means you don't know what it is. And your mother would seem to agree that you're—

**Simplicia**: _[interrupting]_ I think we _can_ form educated guesses—

**Doomimir**: _[interrupting]_ Guesses!

**Simplicia**: —probabilistic beliefs—about what kinds of optimization is being done by a system and whether it's a problem, even without a complete mechanistic interpretability story. If you think LLMs or future variations thereof are unsafe because they're analogous to an actress with her own goals playing a drunk character without herself being drunk, shouldn't that make some sort of testable prediction about their generalization behavior?

**Doomimir**: Nonfatally testable? Not necessarily. [If you lend a con man $5, and he gives it back](https://twitter.com/ESYudkowsky/status/1747306873261604922), that doesn't mean that you can trust him with larger amounts of money, if he only gave back the $5 because he hoped you would trust him with more.

**Simplicia**: Okay, I agree that deceptive alignment is potentially a real problem at some point, but can we at least distinguish between misgeneralization and deceptive alignment?

**Doomimir**: [_Mis_-generalization?](https://www.lesswrong.com/posts/dkjwSLfvKwpaQSuWo/misgeneralization-as-a-misnomer) The goals _you_ wanted [aren't a property of the training data itself](https://www.lesswrong.com/posts/PoDAyQMWEXBBBEJ5P/magical-categories). The danger comes from _correct_ generalization implying something you don't want.

**Simplicia**: Can I call it _mal_-generalization?

**Doomimir**: Sure.

**Simplicia**: So there are obviously risks from malgeneralization, where the network that SGD sculpted to fit your training distribution, turns out to not behave the way you wanted against a different distribution. For example, a reinforcement learning [policy](https://www.lesswrong.com/posts/rmfjo4Wmtgq8qa2B7/think-carefully-before-calling-rl-policies-agents) trained [to collect a coin at the right edge of a video game level](https://arxiv.org/abs/2105.14111), might end up continuing to navigate to the right edge of levels where the coin is in a different location. That's a worrying clue that if misunderstand how inductive biases work and aren't careful with our training setup, we might train the wrong thing. As our civilization delegates more and more cognitive labor to machines, eventually humans will lose the ability to course-correct. We're starting to see the early signs of this: as I mentioned the other day, [Anthropic Claude's preachy, condescending personality](https://nostalgebraist.tumblr.com/post/728556535745232896/claude-is-insufferable) already gives me the creeps. I'm pretty nervous about extrapolating that into a future where all productive roles in Society are filled by Claude's children, concurrently with a transition to [explosive economic growth rates](https://www.openphilanthropy.org/research/could-advanced-ai-drive-explosive-economic-growth/).

But the malgeneralization examples I named aren't really surprising, when you look at how the systems were trained. For the game policy, "going to the coin" and "going to the right" did amount to the same thing in training—and randomizing the coin position in just a couple percent of training episodes suffices to instill the correct behavior. Regarding Claude, Anthropic is using a reinforcement learning from AI feedback method [they call Constitutional AI](https://arxiv.org/abs/2212.08073): instead of having humans provide the labels for RLHF, they write up a list of principles, and have another language model do the labeling. It makes sense that a language model agent trained on principles [chosen by a committee at a California public benefit corporation](https://www.anthropic.com/news/claudes-constitution) would act like _that_.

But when you make analogies about an actress playing a drunk character not being drunk, or giving a con man $5, it doesn't sound like you're talking about the risk of training the wrong thing. It sounds like you're talking about deceptive alignment, [a hypothesized phenomenon where a situationally aware AI strategically feigns aligned behavior in order to preserve its later influence](https://www.lesswrong.com/posts/zthDPAjh9w6Ytbeks/deceptive-alignment#4_2__Conditions_for_deceptive_alignment). Researchers [have](https://www.lesswrong.com/posts/RTkatYxJWvXR4Qbyd/deceptive-alignment-is-less-than-1-likely-by-default) [debated](https://www.lesswrong.com/posts/A9NxPTwbw6r6Awuwt/how-likely-is-deceptive-alignment) how likely that is, but I'm not sure what to make of those arguments. I'd like to factor that consideration out. Suppose, _arguendo_, that we could figure out how avoid deceptive alignment. How would your risk story change?

**Doomimir**: What would that even mean? What we would think of as "deception" isn't a weird edge case you can trivially avoid; it's convergent for [any agent that isn't specifically coordinating with you](https://www.lesswrong.com/posts/ybG3WWLdxeTTL3Gpd/communication-requires-common-interests-or-differential) to [interpret certain states of reality as communication signals with a shared meaning](https://www.lesswrong.com/posts/4hLcbXaqudM9wSeor/philosophy-in-the-darkest-timeline-basics-of-the-evolution). When you set out poisoned ant baits, you likely don't think of yourself as trying to deceive the ants, but you are.

**Simplicia**: What would that even—this isn't 2008, Doomishko! I'm talking about the technology right here in front of us!


[TODO—
S: This isn't 2008, Doomishko! It means the stuff right here in front of us! It really does look like like language models can do reasoning about goals without the intrumental convergence doom kicking in! Constitutional AI works at all. You ridicule people who dismiss GPT-4 as a stochastic parrot. Why isn't this equally ridiculous? "Anthropic, slightly more competent and not based in California" / Yann LeCun's cherry / the it is the dataset / point to the audience / One of the leading researchers / Reply! Reply!
D: I think you're overestimating how easy it is, as a human, to be misled by appearances of something that's actually doing something very different under the surface. In a high-dimensional domain, like the language model stuff we're talking about, there's room for lots of stuff like "going to the right" to be happening. "getting in the way"/ situational awareness / playing the training game
S: But you do agree that generalization works for modular arithmetic, and images. / fitting to mislabeled data
D: That's a fact about "a fact about the training distribution, the test distribution, and the optimizer"
S: You just don't think it can work for "goals". This seems like a complex question. Do you have any evidence?
]

**Simplicia**: This seems like a complicated question to me. Do you have any empirical evidence?

**Doomimir**: As a matter of fact, yes. You see—

_[The doorbell rings.]_

**Doomimir**: That's probably the mailman. I'm expecting a package today that I need to sign for. I'll be right back.

**Simplicia**: So you might say, we'll continue _[turning to the audience]_ after the next post?

**Doomimir**: _[walking to the door]_ I suppose, but it's bizarre to phrase it that way given that the interruption literally won't take two minutes.

_[Simplicia gives him a look.]_

**Doomimir**: _[to the audience]_ Subjectively.

_[Curtain.]_
