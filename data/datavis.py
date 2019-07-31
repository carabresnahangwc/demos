'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Search term used for this tweet
#We want to filter this out!
tweetSearch = "automation"

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)

# Part 1
#Create a Sentiment List
polarityList = []

#[OPTIONAL] Subjectivity
subjectivityList = []

#Get Sentiment Data
for tweet in tweetData:
	tweetblob = TextBlob(tweet["text"])
	polarityList.append(tweetblob.polarity)

	#[OPTIONAL] Subjectivity
	subjectivityList.append(tweetblob.subjectivity)

print(polarityList)
print(subjectivityList)

#Part 2
#Create the Graph
plt.hist(polarityList, bins=[-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Histogram of Tweet Polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

#[OPTIONAL] Subjectivity
plt.plot(polarityList, subjectivityList, 'ro')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.title('Tweet Polarity vs Subjectivity')
plt.axis([-1.1, 1.1, -0.1, 1.1])
plt.grid(True)
plt.show()


#Part 3
'''
Use textblob.words to get just the words

'''

combinedTweets = ""
for tweet in tweetData:
	combinedTweets += tweet['text']

#Create a Combined Tweet Blob
tweetblob = TextBlob(combinedTweets)

#Filter Words
wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could", tweetSearch]
filteredDictionary = dict()

for word in tweetblob.words:
	#skip tiny words
	if len(word) < 2:
		continue
	#skip words with random characters or numbers
	if not word.isalpha():
		continue
	#skip words in our filter
	if word.lower() in wordsToFilter:
		continue
	#don't want lower case words smaller than 5 letters
	if len(word) < 5 and word.upper() != word:
		continue;

	#Try lower case only, try with upper case!
	filteredDictionary[word.lower()] = tweetblob.word_counts[word.lower()]

#Create the word cloud
wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
