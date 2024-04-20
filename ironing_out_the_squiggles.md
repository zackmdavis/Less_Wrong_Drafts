# Ironing Out the Squiggles

### Adversarial Examples: A Problem

The apparent successes of the deep learning revolution conceal a dark underbelly. It may seem that we now know how to get computers to (say) [check whether a photo is of a bird](https://xkcd.com/1425/), but this façade of seemingly good performance is belied by the existence of _adversarial examples_—specially prepared data that looks ordinary to humans, but is seen radically differently by machine learning models.

This discovery was made possible by the fact that the differentiable nature of neural networks, which make them possible to be trained at all, are also responsible for their downfall at the hands of an adversary. Deep learning models are fit using stochastic gradient descent to [approximate the function between](https://www.lesswrong.com/posts/DhjcdzTyqHte2v6bu/deep-learning-is-function-approximation) expected inputs and outputs. Given an input, an expected output, and a loss function (which measures "how bad" it is for the actual output to differ from the expected output), we can calculate the [gradient](https://en.wikipedia.org/wiki/Gradient) of the loss on the input—the derivative with respect to every parameter in our neural network—which tells us which direction to adjust the parameters in order to make the loss go down, to make the approximation better.[^image-classification]

[^image-classification]: This post and much of the literature about adversarial examples focuses on image classification, in which case the input would be the pixels of an image, the output would be a class label describing the content of the image, and the loss function would be the negative logarithm of the probability that the model assigned to the correct label. But the story for other tasks and modalities is going to be much the same.

But gradients are a double-edged sword: the same properties that make it easy to calculate how to adjust a _model_ to make it better at classifying an image, also make it easy to calculate how to adjust an _image_ to make to make the model classify it incorrectly. If we take the gradient of the loss with respect to the pixels of the image (rather than the parameters of the model), that tells us which direction to adjust the pixels to make the loss go down—_or up_. (The direction of steepest increase is just the opposite of the direction of steepest decrease.) A tiny step in that direction in imagespace perturbs the pixels of an image just so—making this one the tiniest bit darker, that one the tiniest bit lighter—in a way that humans don't even notice, but which completely breaks an image classifier sensitive to that direction in [the conjunction of many pixel-dimensions)(https://www.lesswrong.com/posts/cu7YY7WdgJBs3DpmJ/the-univariate-fallacy-1), making it report utmost confidence in nonsense classifications.

Some might ask: why does it matter if our image classifier fails on examples that have been mathematically constructed to fool it? If it works for the images one would naturally encounter, isn't that good enough?

One might mundanely reply that gracefully handling untrusted inputs is a decideratum for many real-world applications, but a more forward-thinking reply might instead emphasize what adversarial examples imply about our lack of understanding of the systems we're building, separately from whether we pragmatically expect to face an adversary. It's a problem if we think we've trained our machines to recognize birds, but they've actually learned to recognize a squiggly alien set in imagespace that includes a lot of obvious non-birds and excludes a lot of obvious birds. To plan good outcomes, we need to understand what's going on, and "The loss happens to increase in this direction" is at best only the start of a real explanation.

One obvious first guess as to what's going on is that the models are overfitting. Gradient descent isn't exactly a sophisticated algorithm. There's an intuition that the _first_ solution that you happen to find by climbing down the loss landscape is likely to have idiosyncratic quirks on any inputs it wasn't trained for. (And that an AI designer from a more competent civilization would use a principled understanding of vision to come up with something much better than what we get by shoveling compute into SGD.) Similarly, a hastily cobbled-together conventional computer program that passed a test suite is going to have bugs in areas not covered by the tests.

But that explanation in tension with other evidence, like the observation that adversarial examples often generalize between models. (An adversarial example optimized against one model is often misclassified by others, too, and even assigned the same class.) It seems less likely that different hastily cobbled-together programs would have the _same_ bug.

In ["Adversarial Examples Are Not Bugs, They Are Features"](https://arxiv.org/abs/1905.02175), Andrew Ilyas _et al._ propose an alternative explanation, that adversarial examples arise from predictively useful features that happen to not be robust to pixel-level perturbations. As far as the in-distribution predictive accuracy of the model is concerned, a high-frequency pattern that humans don't notice is fair game for distinguishing between image classes; there's no rule that the features that happen to be salient to humans need to take priority. Ilyas _et al._ provide some striking evidence for this thesis in the form of a model trained exclusively on adversarial examples yielding good performance on the original, unmodified test set (!!).[^adversarial-to-natural-transfer] On this view, adversarial examples arise from gradient descent being "too smart", not "too dumb". The program is fine; if the test suite didn't imply the behavior we wanted, that's our problem.

[^adversarial-to-natural-transfer]: That is, for example, training on a dataset of birds-perturbed-to-be-classified-as-bicycles and bicycles-pertrubed-to-be-classified-as-birds results in good performance on natural images of bicycles and birds.

On the other hand, there's also some evidence that gradient descent being "dumb" may also play a role in adversarial examples, in conjunction with the [counterintuitive properties of high-dimensional spaces](https://en.wikipedia.org/wiki/Curse_of_dimensionality). In ["Adversarial Spheres"](https://arxiv.org/abs/1801.02774), Justin Gilmer _et al._ investigated a simple synthetic dataset of two classes representing points on the surface of two concentric _n_-dimensional spheres of radiuses 1 and (an arbitrarily chosen) 1.3. For a simple network that yields an ellipsoidal decision boundary, training on a million datapoints produced a network with very high accuracy (no errors in 10 million samples), but for which most of the axes of the ellipsoidal decision boundary were wrong, lying inside the inner sphere or outside the outer sphere—implying the existence of on-distribution adversarial examples (points on one sphere classified by the network as belonging to the other). In high-dimensional space, pinning down the exact countours of the decision boundary is much harder for SGD to accomplish than merely being right virtually all of the time—even though a human wouldn't take a million datapoints to notice the hypothesis, "Hey, these all have a norm of exactly either 1 or 1.3."

### Adversarial Training: A Solution?

Our story so far: we used gradient-based optimization to find a neural network that seemed to get low loss on an image classification task—that is, until an adversary used gradient-based optimization to find images on which our neural network gets _high_ loss instead. Is that the end of the story? Is [deep learning hitting a wall](https://nautil.us/deep-learning-is-hitting-a-wall-238440/)?

Mathematically, instead of just trying to find network parameters $\theta$ that

$\min_\theta - \log(y \mid x)$

min_θ −log(y|x)
max_δ −log(y|x) δ


["Robustified ANNs Reveal Wormholes Between Human Category Percepts"](https://arxiv.org/abs/2308.06887) by Guy Gaziv, Michael J. Lee, and James J. DiCarlo.[^wormhole-paper-title]

[^wormhole-paper-title]: A version of this paper has [also appeared](https://openreview.net/forum?id=5GmTI4LNqX) under the less interesting title, "Strong and Precise Modulation of Human Percepts via Robustified ANNs". Do some reviewers have a prejudice against creative paper titles? While researching this post, I was disturbed to find that the newest version of the Gilmer _et al._ "Adversarial Spheres" paper had been re-titled "The Relationship Between High-Dimensional Geometry and Adversarial Examples".

 * The prevailing assumption had been that, unlike NNs, human perception is stable within a low-pixel-budget perturbation around most natural images—adding a small amount of noise isn't going to change how you see things
 * How are "small" perturbations operationalized? For 224×224×3 images, the maximal distance is 388. (You can think of an image as a list of 3 * 224^2 values, the square root of which is 388.) Typical difference between imagenet images is 130.
 * The obvious countermeasure: include adversarial examples as training data while optimizing the model.
 * It's not that this makes them immune to low-pixel budget attacks. (Although the paper claims less so.) It's that the attacks that are found also affect humans—the attacks don't look like random noise!!—imagespace has "wormholes"
 * (quip about boring alternate title)
 * The attacks don't affect the humans quite as much as the models, but the gap closed a lot, quantitatively
 * experiment restricted to nine ImageNet classes: dog, cat, frog, turtle, bird, primate, fish, crab, insect
 * targeted and untargeted attacks: one is trying to make subjects not report the real category; the other tries to transform to a target category
 * images shown to humans for 0.2 seconds (0.1 to 0.8 s in followup experiments)
 * Department of Questionable Typography: the paper uses both ε and ϵ with different meanings! The lunate epsilon ϵ is the is the budget for image pertrurbations in the experiment, whereas ε was the budget for training the robustified models
 * attack method: Projected Gradient Descent
 * Technical details. We have a classification model from images to logits: f: ℝ^(H×W×3) → ℝ^C that takes images x and outputs a class y. The loss L is cross-entropy. Then we're optimizing the perturbation δ to argmax L(f(x+δ), y) subject to ||δ|| < ϵ
 * SGD steps are followed by a projection step to the pixel budget.
 * Difference between disruption and target: "minimize class y" vs. "maximize class y" (or multiple such classes)

### Implications for Alignment?

 * The standard doom argument is fragility of value
 * Standard doom counterargument is that ML is good at learning complex distributions
 * Counter-counterargument centers on ML being flaky and non-robust, as illustrated by adversarial examples
 * But if adversarial training actually works, that should make us more optimistic?

--------

### My summaries of supplemental papers

#### "Explaining and harnessing adversarial examples" (https://arxiv.org/abs/1412.6572)

 * Models with different architecture trained on different training data subsets fell to the same adversarial example, which suggests a more serious blindspot rather than just an edge-case of no importance
 * "Linear behavior in high-dimensional spaces is sufficient to cause adversarial examples"
 * Generating adversarial examples quickly (sounds bad?!) makes adversarial training feasible (sounds good?)
 * "these algorithms have built a Potemkin village that works well on naturally occuring data, but is exposed as a fake when one visits points in space that do not have high probability in the data distribution"
 * The L_∞ norm of a perturbation doesn't grow with the dimensionality of the problem, but the change in activation from the perturbation does, so high-dimensionality lets you pertrub however you want
 * If finding examples quickly with gradients is an innovation of this paper, how were the original adversarial examples found? "L-BFGS", apparently? I might need to read the other paper.
 * Overfitting can't explain why adversarial examples often generalize between models! (Compare and contrast Yudkowsky's "first solution found" ... actually, this may be compatible with Yudkowsky's view? Goodfellow et al. say that it happens with differnet models because they're trained on a similar task. Difference between "SGD will find something crazy and idiosyncratic" vs. "SGD will find something convergent, but the convergent thing isn't what you want"
 * Space is not full of pockets of adversarial examples
 * "The existence of adversarial examples suggests that being able to explain the training data or even being able to correctly label the test data does not imply that our models truly understand the tasks we have asked them to perform"
 * "these models only behave reasonably on a very thin manifold encompassing the training data"


Adversarial attacks in images, graphs, and text: https://arxiv.org/abs/1909.08072
Towards Deep Learning Models Resistant to Adversarial Attacks: https://arxiv.org/abs/1706.06083
https://openai.com/research/attacking-machine-learning-with-adversarial-examples

#### "Intriguing Properties of Neural Networks" (https://arxiv.org/abs/1312.6199)

 * I'm mostly only looking at this one because I need to understand how the original adversarial examples were produced, why they're expensive
 * "dense like the rational numbers" hypothesis argued against in the Goodfellow et al. paper was proposed here

#### "Adversarial Spheres" (https://arxiv.org/abs/1801.02774)

 * concentric spheres are a nice synthetic dataset
 * projected GD lets you find adversarial examples on the sphere itself (therefore, on the data manifold)
 * My comment: the fact that you can find errors on the data manifold without observing natural errors is a symptom that NNs aren't algorithmically clean—a traditional computer program that just computed the norm wouldn't exhibit these. (This supports the Yudkowskian view on NNs.)
 * This is specifically a high-dimensional phenomenon: for n=100, the attack method doesn't turn up anything
 * They explore a network with a different activation, such that the decision boundary is an ellipsoid with analytically computable axes; there's a typical-set like phenomenon where most of the axes are wrong, but classification error is tiny
 * "for any model with reasonable accuracy, most errors are 'adversarial' relative to some example data point, in the sense that for a typical incorrectly classified point there is a small perturbation that will cause it to be correctly classified"! (this may be limited to the artificial sphere dataset??)

#### "Towards Deep Learning Models Resistant to Adversarial Examples" (https://arxiv.org/abs/1706.06083)

 * Adversarial robustness can be defined by min_θ max_δ L(θ, x + δ, y) (finding parameters that minimize the loss function, given an adversary choosing δ to maximize loss
 * Just training against FGSM examples isn't good enough; it overfits to them
 * Weak models fail to learn anything under pressure from the adversary
 * For MNIST, PGD couldn't find adv. ex. even for large values of ε—which makes sense in light of the wormholes result!! (There are low-norm perturbations that make a dog look like a fish, but none that make a 5 look like a 1 or zero; the MNIST digit data manifold is more constrained)
    * Caveat: the authors think this is an overestimate of the robustness
 * The FGSM linearizes the loss around the example; PGD is more sophisticated

#### "Adversarial Examples Are Not Bugs, They Are Features" (https://arxiv.org/abs/1905.02175)

 * training on a special dataset of adversarially-pertrubed examples yields good performance on the original, unmodified dataset

# implications for alignment notes—

https://www.lesswrong.com/posts/Djs38EWYZG8o7JMWY/paul-s-research-agenda-faq?commentId=79jM2ecef73zupPR4
> Eliezer expects weird squiggles from gradient descent - it's not that gradient descent can never produce par-human cognition, even natural selection will do that if you dump in enough computing power. But you will get the kind of weird squiggles in the learned function that adversarial examples expose in current nets - special inputs that weren't in the training distribution, but look like typical members of the training distribution from the perspective of the training distribution itself, will break what we think is the intended labeling from outside the system.
> [...]
> You cannot iron out the squiggles just by using more computing power in bounded in-universe amounts.

> assumed to be gradient descent, genetic algorithms, or something else that can be assumed neutral-of-itself rather than being an-AGI-of-itself whose previous alignment has to be assumed.

https://www.lesswrong.com/posts/Djs38EWYZG8o7JMWY/paul-s-research-agenda-faq?commentId=nbg277ZmT7GeN5zi5
> For adversarial examples in particular, I think that the most reasonable guess right now is that it takes more model capacity (and hence data) to classify all perturbations of natural images correctly rather than merely classifying most correctly—i.e., the smallest neural net that classifies them all right is bigger than the smallest neural net that gets most of them right—but that if you had enough capacity+data then adversarial training would probably be robust to adversarial perturbations. Do you want to make the opposite prediction?

https://www.lesswrong.com/posts/LDRQ5Zfqwi8GjzPYG/counterarguments-to-the-basic-ai-x-risk-case

https://www.lesswrong.com/posts/xzFQp7bmkoKfnae9R/but-exactly-how-complex-and-fragile

https://meteuphoric.com/2019/11/03/but-exactly-how-complex-and-fragile/#comment-66048
