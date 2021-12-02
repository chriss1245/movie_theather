from textblob import TextBlob
import matplotlib.pyplot as plt
from random import randint

# importar clase reviews





def analytics_web(reviews):
    n = len(reviews)
    labels = 'Positive', 'Negative', 'Neutral'
    positives, negatives, neutrals = 0,0,0
    for idx,review in enumerate(reviews):
        val = TextBlob(review).sentiment.polarity
        if  val > 0: positives += 1
        elif val == 0: neutrals += 1
        else: negatives += 1
    per_neg, per_neutral, per_positives = negatives/n, neutrals/n, positives/n
    plt.pie([per_neg, per_positives, per_neutral], labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.title("Reviews")

    # needs to be converted into base64


"""
def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item.rating < pivot.rating:
            low.append(item.rating)
        elif item.rating == pivot.rating:
            same.append(item.rating)
        elif item > pivot:
            high.append(item.rating)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

"""


