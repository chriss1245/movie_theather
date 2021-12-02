from textblob import TextBlob
from model import Review
import matplotlib.pyplot as plt
import base64
import io




def web_analytics(reviews):
    # input is a list of instances of class Review
    n = len(reviews)
    labels = 'Positive', 'Negative', 'Neutral'
    positives, negatives, neutrals = 0,0,0
    for idx,review in enumerate(reviews):
        val = TextBlob(review.text).sentiment.polarity
        if  val > 0: positives += 1
        elif val == 0: neutrals += 1
        else: negatives += 1
    per_neg, per_neutral, per_positives = negatives/n, neutrals/n, positives/n
    plt.pie([per_neg, per_positives, per_neutral], labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.title("Site reviews")
    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes, format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())
    return pic_hash




def movie_analytics(movies):
    # generates a barplot and converts it to base 64
    plt.bar(*zip(*movies.items()))
    plt.title("Average movie reviews")
    pic_IObytes = io.BytesIO()
    plt.savefig(pic_IObytes, format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())
    return pic_hash

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


