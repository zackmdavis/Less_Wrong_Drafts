# Comment on "Robustified ANNs Reveal Wormholes Between Human Category Precepts"

### Background: Adversarial Examples

 * Image recognition models are famously plagued by adversarial examples: add a little bit of noise to an image, and it completely changes the class, even though the image looks the same to humans
 * This is a problem, if it means that our image classifiers aren't really doing what they appear to be. They haven't really learned recognize cats; they've learned to recognize a weird squiggly set in imagespace that includes a lot of obvious non-cats and excludes a lot of obvious cats
 * On the other hand, can't simply be explained by overfitting, because they transfer between models ("Explaining and Harnessing") and you can train on adversarial examples to get performance on original dataset ("They Are Features")


### Robustified ANNs Reveal Wormholes Between Human Category Precepts?!

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

#### Adversarial spheres (https://arxiv.org/abs/1801.02774)

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
