from math import log, sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_events = [1 if is_prime(i) else 0 for i in range(1, 100)]
alternating_events = [0, 1] * 50


def brier_score(events, predictions):
    # https://en.wikipedia.org/wiki/Brier_score#Definition
    total = 0
    for event, prediction in zip(events, predictions):
        total += (event - prediction)**2
    return total


def logarithmic_score(events, predictions):
    total = 0
    for event, prediction in zip(events, predictions):
        total += log(prediction) if event else log(1 - prediction)
    return total


# Now let's do the REL/RES/UNC decomposition, following "Kullback–Leibler
# Divergence as a Forecast Skill Score with Classic
# Reliability–Resolution–Uncertainty Decomposition"

def logarithmic_REL(events, predictions):
    # "the expected divergence of the observed probability distribution from the
    # forecast probability distribution, both stratified (conditioned) on all
    # issued forecast probabilities"
    total = 0
    for event, prediction in zip(events, predictions):
        total += event * (log(event) - log(prediction)) # ?
    return total

def logarithmic_RES(events, predictions):
    # "the expected divergence of the conditional frequencies from the marginal
    # frequency of occurrence"
    #
    # "In information theory, this quantity is known as the mutual information
    # I between the forecasts and the observation"
    total = 0
    for event, prediction in zip(events, predictions):
        total += ... # ?
    return total

def logartihmic_UNC(events, preductions):
    total = 0
    for event, prediction in zip(events, predictions):
        total += event * log(event)
    return total

# In the case of certain observations, I think REL is just going to be the
# score and RES and UNC are going to be zero?—that's what the paper says ("for
# a single forecast–observation pair, uncertainty and resolution are 0 and the
# total score is equal to the reliability, which acts as a scoring rule"), and
# that's confirmed by my coded understanding so far (where outcome certainty in
# REL reduces it to the log score, and UNC will be 0 for the known
# probability-one event).
#
# But then the paper says "Over a larger number of
# forecasts uncertainty approaches climatic uncertainty and reliability should
# go to zero if the forecast is well calibrated". What??

prime_predictions = prime_events
prime_number_theorem_predictions = [0, 1] + [1/log(n) for n in range(3,100)]
fifty_fifty_predictions = [0.5] * 100
quarter_predictions = [0.25] * 100

exclusions = [
    ('alternating', 'predict-primes', 'logarithmic_score'), # 0-probability predictions, uninteresting
]

for eventstream_name, eventstream in [('primes', prime_events), ('alternating', alternating_events)]:
    print("Event: {}".format(eventstream_name))
    for predictor_name, predictor in [('predict-primes', prime_predictions), ('predict-PNT', prime_number_theorem_predictions), ('predict-50–50', fifty_fifty_predictions), ('predict-¼', quarter_predictions)]:
        for score in [brier_score, logarithmic_score]:
            if (eventstream_name, predictor_name, score.__name__) in exclusions:
                continue
            print("{} {}: {}".format(predictor_name, score.__name__, score(eventstream, predictor)))
