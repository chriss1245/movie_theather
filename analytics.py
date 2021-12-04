from textblob import TextBlob
import matplotlib.pyplot as plt
import base64
import io


def web_analytics(reviews):

    n = len(reviews)
    labels = 'Positive', 'Negative', 'Neutral'
    positives, negatives, neutrals = 0, 0, 0
    for idx, review in enumerate(reviews):
        val = TextBlob(review.text).sentiment.polarity
        if val > 0:
            positives += 1
        elif val == 0:
            neutrals += 1
        else:
            negatives += 1
    per_neg, per_neutral, per_positives = negatives/n, neutrals/n, positives/n
    plt.pie([per_neg, per_positives, per_neutral], labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Site reviews")
    pic_iobytes = io.BytesIO()
    plt.savefig(pic_iobytes, format='png', transparent=True)
    pic_iobytes.seek(0)
    pic_hash = base64.b64encode(pic_iobytes.read())
    return pic_hash


def movie_analytics(movies):
    # generates a barplot and converts it to base 64
    plt.bar(*zip(*movies.items()))
    plt.title("Average movie reviews")
    pic_iobytes = io.BytesIO()
    plt.savefig(pic_iobytes, format='png', transparent=True)
    pic_iobytes.seek(0)
    pic_hash = base64.b64encode(pic_iobytes.read())
    return pic_hash
