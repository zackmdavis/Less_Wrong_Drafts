_[Scene: a suburban house, a minute after the conclusion of ["And All the Shoggoths Merely Players"](https://www.lesswrong.com/posts/8yCXeafJo67tYe5L4/and-all-the-shoggoths-merely-players). **Doomimir** returns with his package, which he places by the door, and turns his attention to **Simplicia**, who has been waiting for him.]_

**Simplicia**: Right. To recap for _[coughs]_ no one in particular, when we left off _[pointedly, to the audience]_ one minute ago, Doomimir Doomovitch, you were expressing confidence that approaches to aligning artificial general intelligence within the current paradigm were almost certain to fail. You don't think that the apparent tractability of getting contemporary generative AI techniques to do what humans want bears on that question. But you did say you have empirical evidence for your view, which I'm excited to hear about!

**Doomimir**: Indeed, Simplicia Optimistovna. My empirical evidence is the example of the evolution of human intelligence. You see, humans were optimized for one thing only: inclusive genetic fitness—

[**Simplicia** turns to the audience and makes a face.]

**Doomimir**: _[annoyed]_ What?

**Simplicia**: When you said you had empirical evidence, I thought you meant empirical evidence _about AI_, not the same analogy to an unrelated field that I've been hearing for the last fifteen years. I was hoping for, you know, ArXiv papers about SGD's inductive biases, or online regret bounds, or singular learning theory ... something, anything at all, from this century, that engages with what we've learned from the experience of actually building artificial minds.

**Doomimir**: That's one of the many things you Earthlings refuse to understand. You didn't build that.

**Simplicia**: What?

**Doomimir**: The capabilities advances that your civilization's AI guys have been turning out these days haven't come from a deeper understanding of cognition, but by improvements to generic optimization methods, fueled with ever-increasing investments in compute. Deep learning not only [isn't a science](https://www.lesswrong.com/posts/JcLhYQQADzTsAEaXd/ai-as-a-science-and-three-obstacles-to-alignment-strategies), it isn't even an engineering discipline in the traditional sense: the opacity of the artifacts it produces has no analogue among bridge or engine designs. In effect, all the object-level engineering work is being done by gradient descent.

The autogenocidal maniac Richard Sutton calls this [the bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), and attributes the field's slowless to embrace it to ego and recalcitrance on the part of practioners. But in accordance with the dictum to [feel fully the emotion that fits the facts](https://www.yudkowsky.net/rational/virtues), I think bitterness is appropriate. It makes sense to be bitter about the shortsighted adoption of a fundamentally unalignable paradigm on the basis of its immediate performance, when a saner world would notice the glaring [foreseeable difficulties](https://arbital.com/p/foreseeable_difficulties/) and coordinate on doing Something Else Which Is Not That.

**Simplicia**: I don't think that's quite the correct reading of the bitter lesson. Sutton is advocating general methods that scale with compute in preference to hand-coding human domain knowledge, but that doesn't mean that we're ignorant of what those general methods are doing. One of the examples Sutton gives is computer chess, where [minimax search](https://en.wikipedia.org/wiki/Negamax) with optimizations like [α–β pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) prevailed over trying to explicitly encode what human grandmasters know about the game. But that seems fine. Writing a program that thinks about tactics the way humans do rather than [letting tactical play emerge from searching the game tree](http://zackmdavis.net/blog/2019/05/minimax-search-and-the-structure-of-cognition/) would be a lot more work for less than no benefit.

A broadly similar moral could apply to using deep learning to [approximate complicated functions between data distributions](https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation): we specify the training distribution, and the details of fitting it are delegated to a network architecture with the appropriate invariances: convolutional nets for processing image data, transformers for variable-length sequences. There's a whole literature—

**Doomimir**: The literature doesn't help if your civilization's authors aren't asking the questions we need answered in order to not die. What, specifically, am I supposed to learn from your world's literature? Give me an example.

**Simplicia**: I'm not sure what kind of example you're looking for. Just from common sense, it seems like the problem of aligning AI is going to involve intimate familiarity with the nitty-gritty empirical details of how AI works. Why would you expect to eyeball the problem from your armchair and declare the whole thing intractable on the basis of an analogy to biological evolution, which is just not the same thing as ML training?

Picking something arbitrarily ... well, I was reading about residual networks recently. Deeper neural networks were found to be harder to train because [the gradient varied too quickly with respect to the input](https://arxiv.org/abs/1702.08591). Being the result of a many-fold function composition, the loss landscape in very deep networks becomes a mottled fractal of tiny mountains, rather than a smooth valley to descend. This is mitigated by introducing "residual" connections that skip some layers, creating shorter paths through the network which have less volatile gradients.

I don't understand how you can say that this isn't science or engineering. It's a comprehensible explanation for why one design of information-processing system works better than alternatives, grounded in observation and mathematical reasoning. There are dozens of things like that. What did you expect the science of artificial minds to look like, exactly?

**Doomimir**: _[incredulous]_ _That's_ your example? Resnets?

**Simplicia**: ... sure?

**Doomimir**: By [conservation of expected evidence](https://www.lesswrong.com/posts/jiBFC7DcCrZjGmZnJ/conservation-of-expected-evidence), I take your failure to cite anything relevant as further confirmation of my views. I've never denied that you can write many dissertations about such tricks to make generic optimizers more efficient. The problem is that that knowledge brings us closer to being able to brute-force general intelligence, without teaching us _about intelligence_. What program are all those gradient updates building inside your network? How does it work?

**Simplicia**: _[uncomfortably]_ [People are working on that.](https://arxiv.org/abs/2404.14082)

**Doomimir**: Too little, too late. The reason I often bring up human evolution is because that's our only example of an outer optimization loop producing an inner general intelligence, which sure looks like the path your civilization is going down. Yes, there are differences between gradient descent and natural selection, but I don't think the differences are relevant to the morals I draw.

As I was saying, the concept of fitness isn't represented anywhere in our motivations. That is, the "outer" optimization criterion that evolution selected for while creating us, bears no visible resemblance to the "inner" optimization criteria that we use when selecting our plans.

As optimizers get more powerful, anything that's not explicitly valued in the utility function won't survive [edge instantiation](https://arbital.com/p/edge_instantiation/). The connection between parental love and inclusive fitness has grown much weaker in the industrial environment than it was in the EEA, as more options have opened up for humans to prioritize their loved ones' well-being in ways that don't track allele frequencies. In a transhumanist utopia with mind uploading, it would break entirely as we migrated our minds away from the biological substrate: if some other data storage format suited us better, why would we bother keeping around the specific molecule of DNA, which no one had heard of before the 19th or 20th century?

Of course, we're not going to get a transhumanist utopia with mind uploading, because history will repeat itself: the outer loss function that mad scientists use to grow the first AGI will bear no resemblance to the inner goals of the resulting superintelligence.

**Simplicia**: You seem to have a basically ideological conviction that outer optimization can't be used to shape the behaviors of the inner optimizers it produces, such that you [don't think that "We train for X and get X" is an allowable step in an alignment proposal](https://www.lesswrong.com/posts/Djs38EWYZG8o7JMWY/paul-s-research-agenda-faq?commentId=79jM2ecef73zupPR4). But this just seems flatly contradicted by experience. We train deep learning systems for incredibly specific tasks all the time, and it works fantastically well.

Intuitively, I want to say that it works much better than evolution: I don't imagine succeeding at selectively breeding an animal that speaks perfect English the way LLMs do. Relatedly, we can and do train LLMs from a blank slate, in contrast to how selective breeding only works with traits already present in the wild type; it's too slow to assemble adaptations from scratch.

But even selective breeding basically works. We successfully domesticate loyal dogs and meaty livestock. If we started breeding dogs for intelligence as well as being loyal and friendly to us, I'd expect them to still be approximately loyal and friendly as they started to surpass our intelligence, and to grant us equity in their hyperdog star empire. Not that that's necessarily a good idea—[I'd rather pass the world on to another generation of humans](https://www.lesswrong.com/posts/vwnSPgwtmLjvTK2Wa/amputation-of-destiny) [than a new dominant species](https://www.lesswrong.com/posts/gb6zWstjmkYHLrbrg/can-t-unbirth-a-child), even a friendly one. But your position doesn't seem to be, "Creating a new dominant species is a huge responsibility; we should take care to get the details right." Rather, you don't seem to think we can exert meaningful control over the outcome at all. Why?

Before the intermission, I asked how your pessimism about aligning AGI using training data was consistent with deep learning basically working. My pet example was the result where mechanistic interpretability researchers were able to confirm that training on modular arithmetic problems resulted in the network in fact learning a modular addition algorithm. You said something about that being a fact of the training distribution, the test distribution, and the optimizer, which wouldn't work for friendly AI. Can you explain that?

**Doomimir**: _[sighing]_ [If I must.](https://twitter.com/ESYudkowsky/status/1744066823962947905) There's a vast space of possible programs that do correct arithmetic mod _p_ for inputs up to a googol. If you select the shortest such program, my guess is that it would work for inputs over a googol as well. That's a sense in which I'll affirm that training data can "shape behavior", as you put it.

But that's a specific claim about what happens with the training distribution "mod arithmetic with inputs less than a googol", the test distribution "mod arithmetic with inputs over a googol", and the optimizer "go through all programs in order until you find one that fits the training distribution." It's not a generic claim that the inner optimizers found by outer optimizers will want what some humans who assembled the training set [optimistically imagined they would want](https://www.lesswrong.com/posts/RcZeZt8cPk48xxiQ8/anthropomorphic-optimism).

In the case of human evolution—again, our only example of outer optimization producing general intelligence—we know as a historical fact that the first program found by the optimizer "greedy local search of mutations and recombinations" for the training task "optimize inclusive genetic fitness in the environment of evolutionary adaptedness" did not generalize to optimizing inclusive genetic fitness in the test distribution of the modern world. Likewise, your claim that selective breeding "basically works" is problematized by all the times when it doesn't work—like when [selecting for small subpopulation sizes in insects results in of cannabalism of larvæ rather than restricted breeding](https://www.lesswrong.com/posts/QsMJQSFj7WfoTMNgW/the-tragedy-of-group-selectionism), or when [selecting chickens that lay the most eggs in a coop gets you more aggressive chickens who make their neighbors less productive](https://www.lesswrong.com/posts/KE8wPzGiX5QPotyS8/conjuring-an-evolution-to-serve-you).

**Simplicia**: _[nodding]_ Uh-huh. With you so far.

**Doomimir**: I don't believe you. If you were really with me so far, you'd have noticed that I just [disproved the naïve mirroring expectation](https://twitter.com/ESYudkowsky/status/1744100219367931906) that outer optimizers training on a reward result in inner optimizers pursuing that reward.

**Simplicia**: Yeah, that sounds like a really dumb idea. If you ever meet someone who believes that, I hope you manage to talk them out of it.

**Doomimir**: _[frustrated]_ If you're _not_ implicitly assuming the naïve mirroring expectation—whether you realize it or not—then I don't understand why you think "We train for X and get X" is an allowable step in an alignment proposal.

**Simplicia**: It depends on the value of X—and the value of "train". As you say, there are facts of the matter as to which outer optimizers and training distributions produce which inner optimizers, and how those inner optimizers generalize to different test environments. As you say, the facts aren't swayed by wishful thinking: someone who reasoned, "I pressed the reward button when my AI did good things, therefore it will learn to be good," will be disappointed if it turns out that the system generalizes to value reward-button pushes themselves—what you would call an outer alignment failure—or any number of possible training correlates of reward—what you would call an inner alignment failure.

**Doomimir**: _[patronizingly]_ With you so far. And why doesn't this instantly sink "We train for X and get X" as an allowable step in an alignment proposal?

**Simplicia**: Because I think it's possible to [make predictions about how inner optimizers will behave and to choose training setups accordingly](https://www.lesswrong.com/posts/FDJnZt8Ks2djouQTZ/how-do-we-become-confident-in-the-safety-of-a-machine). I don't have a complete theory of exactly how this works, but I think [the complete theory is going to be more nuanced than](https://www.lesswrong.com/posts/gHefoxiznGfsbiAu9/inner-and-outer-alignment-decompose-one-hard-problem-into), "Either training converts the outer loss function into an inner utility function, in which case it kills you, or there's no way to tell what it will do, in which case it also kills you," and that we can glimpse the outlines of the more nuanced theory by more carefully examining the details of the examples we've discussed.

In the case of evolution, you can view fitness as being [_defined_ as "that which got selected for"](https://www.lesswrong.com/posts/BtffzD5yNB4CzSTJe/genetic-fitness-is-a-measure-of-selection-strength-not-the). On this view, selective breeding isn't different from natural selection: it's just that the breeder gets to choose the environment of evolutionary adaptedness. The sense in which a farmer breeds cows for milk production is distinct from the sense in which evolution selects organisms for fitness. If we apply the same standards to Nature as we do to the famer, of looking at the mechanisms that lead to an organism being selected, rather than taking "being selected" itself as a utility function that "should" be optimized arbitrarily hard, then humans _weren't_ optimized for inclusive genetic fitness: they were optimized to mate, hunt, gather, acquire allies, avoid disease, _&c._ Construed that way, the relationship between the outer training task and the inner policy's motivations looks a lot more like "We train for X and get X" than you're giving it credit for.

That said, it is true that the solutions found by evolution can be surprising to a breeder who hasn't thought carefully about what selection pressures they're applying. As in your examples, the simplest change to an insect that draws on existing variation to respond to selection pressure for smaller subpopulations might be to promote cannabalism; the simplest change to a chicken to lay more eggs than neighboring chickens might be to become a bully.

**Doomimir**: Is this a troll where you concede all of my points and then put on a performance of pretending to somehow disagree? That's what I've been trying to teach you: the solutions found by outer optimization _can be surprising_—

**Simplicia**: —to a designer that hasn't thought carefully about what optimization pressures they're applying. Responsible use of outer optimization—

_[**Doomimir** guffaws]_

**Simplicia**: —just doesn't seem like an intractable engineering problem, and the case for deep learning looks a lot more favorable than for evolution. The seemingly tenuous connection between the concept of inclusive fitness and humanity's ["thousand shards of desire"](https://www.lesswrong.com/posts/cSXZpvqpa9vbGGLtG/thou-art-godshatter) can be seen as a manifestation of sparse rewards: if the outer optimizer only measures allele frequencies and is otherwise silent on the matter of which alleles are good, then the simplest solution—with respect to natural selection's implied simplicity prior—is going to depend on a lot of random-looking contingencies of the EEA, which would be surprising if you expected to get a pure DNA-copy maximizer.

In contrast, when we build AI systems, we can make the outer optimizer supply as much supervision as we like, and dense supervision tightly constrains the solutions that are found. It's believed that reason neural nets generalize at all is because [the parameter–function map is biased towards simple functions](https://arxiv.org/abs/1805.08522). There's even some striking evidence that, to a first approximation, training is equivalent to [doing a Bayesian update on the observation that a net with randomly initialized weights happens to fit the training data](https://arxiv.org/abs/2006.15191). We're not limited to searching for a program that happens to succeed at some simple goal and accepting whatever weird drives happened to be the easiest way to accomplish that; we're searching for a program that approximates the billions of expected input–output pairs we trained it on.

In the case of large language models, it seems like a reasonable guess that the simplest function that predicts the next token of webtext, really is just a next token predictor. Not a next-token predicting consequentialist which will wirehead with easily-predicted tokens, but a predictor of the webtext training distribution. The distribution-specificity that you consider an inner alignment failure in the case of human evolution is a feature, not a bug. We trained for X and got X.

**Doomimir**: And then immediately subjected it to _reinforcement learning_.

**Simplicia**: As it happens, I _also_ don't think RLHF is as damning as you do. Early theoretical discussions of AI alignment would sometimes talk about what would go wrong if you tried to align AI with a "reward button." Those discussions were philosophically valuable. Indeed, if you had a hypercomputer and your AI design method was to run a brute-force search for the simplest program that resulted in the most reward-button pushes, that would predictably not end well. While a weak agent selected on that basis might behave how you wanted, a stronger agent would find creative ways to trick or brainwash you into pushing the button, or just sieze the button itself. If we had a hypercomputer in real life and were literally brute-forcing AI that way, I would be terrified.

But again, this isn't a philosophy problem anymore. Fifteen years later, our state-of-the-art methods do have a brute-force aspect to them, but the details are different, and the details matter. RLHF _isn't_ an unconstrained hypercomputer search for whatever makes humans hit the thumbs-up button. It's reinforcing the state–action trajectories that got reward in the past. Most of the bits of search are coming from pretraining. It ... seems to be working pretty well?

**Doomimir**: _Of course_ it seems to be working pretty well! It's been optimized for seeming-good-to-you!

Simplicia, I was willing to give this a shot, but I do despair of leading you over this _pons asinorum_. You're so close to getting it: you can describe

[TODO: you can describe what's going wrong in simple cases, but then the get misled by complexities that cater to your conceptual blind spots. Humans in the EEA would have looked like they were optimizing fitness. Finanical advisors.]

**Simplicia**: [TODO: ugh, more analogies]

**Doomimir**: [TODO: what am I supposed to do?]

**Simplicia**: [TODO: would they have? It seems like it should have been possible to predict how humans would generalize. Discuss "Ironing Out the Squiggles"; that superficially good classification performance can be deceiving, but it's possible to robustify/check]

**Doomimir**: [TODO: Shakespeare's folio's metaphor https://x.com/ESYudkowsky/status/1793754829631934959 ]

**Simplicia**: [TODO: this seems like it depends on how fragile value is; altruism might not be hard to hit]

[TODO: wrap-up; until next time]
