from textblob import TextBlob
import matplotlib.pyplot as plt
import base64
import io



def web_analytics(reviews):
    n = len(reviews)
    labels = 'Positive', 'Negative', 'Neutral'
    positives, negatives, neutrals = 0,0,0
    # we classify all the reviews with the loop
    for idx,review in enumerate(reviews):
        val = TextBlob(review.text).sentiment.polarity
        if  val > 0: positives += 1
        elif val == 0: neutrals += 1
        else: negatives += 1
    # get the percentage of each class
    per_neg, per_neutral, per_positives = negatives/n, neutrals/n, positives/n
    # generate the plot
    fig, ax = plt.subplots()
    ax.pie([per_neg, per_positives, per_neutral], labels = labels, autopct = '%1.1f%%', shadow = True, startangle = 90)
    ax.set_title("Site reviews")
    # encoding of the plot in base64
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


def seats_available(projections):
    # dictionary of tuples
    # we generate a stacked bar plot of seats taken vs seats available
    fig, ax = plt.subplots()
    # free, taken
    taken = []
    for key in projections.keys():
        aux = projections[key]
        taken.append(aux[1])
        projections[key] = aux[0]
    ax.barh(projections.keys(), projections.items())
    ax.barh(projections.keys(), taken)
    ax.set_title("Available and taken per projection")
    ax.get_yaxis().set_visible(False)
    # ax.set_xticklabels(movies.keys(),rotation=90)
    pic_IObytes = io.BytesIO()
    fig.savefig(pic_IObytes, format='png')
    pic_IObytes.seek(0)
    pic_hash = base64.b64encode(pic_IObytes.read())
    return pic_hash

