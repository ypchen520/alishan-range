# Supervised ML & Sentiment Analysis

## Supervised ML

* input features X and a set of labels Y
* goal is to minimize your error rates or cost as much as possible
* prediction function which takes in parameters data to map your features to output labels Y hat
* best mapping from features to labels
  * between the expected values Y and the predicted values Y hat is minimized
    * the cost function does by comparing how closely your output Y hat is to your label Y
* update your parameters and repeat the whole process until your cost is minimized

## Sentiment analysis

* tweet: "I'm happy because I'm learning NLP"
* Goal: predict whether a tweet has a positive or a negative sentiment
* logistic regression classifier
  * first process the raw tweets in your training sets and extract useful features
  * train your logistic regression classifier while minimizing the cost

## Vocabulary & Feature Extraction

* Vocabulary
  * be the list of unique words from your list of tweets
    * go through **all the words** from all your tweets and save every new word that appears in your search
* Features
  * check if every word from your vocabulary appears in the tweet.
    * sparse representation

### sparse representation

* This representation would have a number of features equal to **the size of your entire vocabulary**
* a lot of features equal to 0 for every tweet
* a logistic regression model would have to learn n plus 1 (bias) parameters

## Negative and Positive Frequencies

* Positive and negative counts
  * freqs: mapping from (word, class) to frequency

## Feature Extraction with Frequencies
