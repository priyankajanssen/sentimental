

#import regex
import re

#start process_tweet
def processTweet(tweet):
    tweet=tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip('\'"')
    return tweet
#Read the tweets one by one and process it
fp = open('full_training_dataset5.csv', 'rt')
line = fp.readline()
text_file = open("Output.csv", "w+")
while line:
    processedTweet = processTweet(line)
    text_file.write(processedTweet)
    print(processedTweet)
    line = fp.readline()


#end loop
fp.close()
text_file.close()


