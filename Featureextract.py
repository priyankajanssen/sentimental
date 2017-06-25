import preprocesstweets
import Filtering
import csv
import nltk classify

#Read the tweets one by one and process it
inpTweets = open('full_training_dataset5.csv', 'r')
reader=csv.reader(inpTweets,delimiter=',')
stopWords = Filtering.getStopWordList('stopwords.txt')
featureList = []

# Get tweet words
tweets = []
for row in reader:
    print(row)
    sentiment = row[0]
    tweet = row[1]
    processedTweet = preprocesstweets.processTweet(tweet)
    featureVector = Filtering.getFeatureVector(processedTweet)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment))

#end loop

# Remove featureList duplicates
featureList = list(set(featureList))

# Extract feature vector for all tweets in one shote
training_set = nltk.classify.util.apply_features('feature_list.txt', tweets)

NBClassifier = nltk.NaiveBayesClassifier.train(training_set)

# Test the classifier
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = preprocesstweets.processTweet(testTweet)
print(NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet))))