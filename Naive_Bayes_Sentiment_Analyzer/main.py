import nltk
import random
import pickle

from nltk.corpus import movie_reviews

# SINCE WE WANT TO CLASSIFY INTO POSITIVE AND NEGATIVE REVIEWS, SUPERVISED LEARNING WITH NAÏVE BAYES

documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# now we need to define a feature extractor

# we get all words and their features

# encoding number of times that each outcome of an experiment occurs
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

# we use 2000, to limit the number of features the classifier needs to process, best practices according to NLTK reference
word_features = list(all_words)[:2000]


#feature extractor
def document_features(document):
    # checking if something belongs in a set is much faster than in a list

    # set of all words in the document
    document_words = set(document)
    features = {}
    for word in word_features:
        features[f"contains({word})"] = (word in document_words)
    return features


# now we train the Naive Bayes classifier
featureset = [(document_features(d), c) for d,c in documents]
train, test = featureset[100:], featureset[:100]
classifier = nltk.NaiveBayesClassifier.train(train)


# testing the classifier
print(nltk.classify.accuracy(classifier, test))


# classifying a sample review
# print(classifier.classify(document_features("it sucks")))



# shows the most important classifying features
#classifier.show_most_informative_features(5)

# now to save the train classifier in memory
save_class = open("sentiment_classifier.pickle", "wb")
pickle.dump(classifier, save_class)
save_class.close()


"""

#to load it and use it
#important to add pickle, nltk and all of the above as a requirement
classifier_f = open("sentiment_classifier.pickle")
sclass = pickle.load(classifier)


# line when done
sentiment_classifier.close()
"""