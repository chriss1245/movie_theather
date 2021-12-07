from textblob import TextBlob
import matplotlib.pyplot as plt
import base64
import io


# importar clase reviews





def web_analytics(reviews):
    n = len(reviews)
    labels = 'Positive', 'Negative', 'Neutral'
    positives, negatives, neutrals = 0,0,0
    for idx,review in enumerate(reviews):
        val = TextBlob(review.text).sentiment.polarity
        if  val > 0: positives += 1
        elif val == 0: neutrals += 1
        else: negatives += 1
    per_neg, per_neutral, per_positives = negatives/n, neutrals/n, positives/n

    fig, ax = plt.subplots()
    ax.pie([per_neg, per_positives, per_neutral], labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax.set_title("Site reviews")
    pic_IObytes = io.BytesIO()
    fig.savefig(pic_IObytes, format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())
    return pic_hash




def movie_analytics(movies):
    # generates a barplot and converts it to base 64

    fig, ax = plt.subplots()

    ax.barh(*zip(*movies.items()))
    for bar, movie in zip(ax.patches, movies.keys()):
        ax.text(0.1, bar.get_y()+bar.get_height()/2, movie, color = 'white', ha = 'left', va = 'center') 
    ax.set_title("Average movie reviews")
    ax.get_yaxis().set_visible(False)
    #ax.set_xticklabels(movies.keys(),rotation=90)
    pic_IObytes = io.BytesIO()
    fig.savefig(pic_IObytes, format='png')
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


