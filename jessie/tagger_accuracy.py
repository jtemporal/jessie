# -*- coding: utf-8 -*-
'''
Created on 16 de nov de 2016

@author: mateus
'''
import sys
from sklearn import metrics

def main():
    # loading tweets
    filename = sys.argv[1]
    tweets = []
    file = open(filename, "r")
    for line in file:
        tweets.append(line.replace('\n', ' ').replace('\r', ' ').lower())

    # loading manual annotated nouns
    filename = sys.argv[2]
    true_nouns = []
    file = open(filename, "r")
    for line in file:
        true_nouns.append(line.replace('\n', ' ').replace('\r', ' ').lower())


    # loading tagged nouns
    filename = sys.argv[3]
    pred_nouns = []
    file = open(filename, "r")
    for line in file:
        pred_nouns.append(line.replace('\n', ' ').replace('\r', ' ').lower())


    if len(tweets) != len(true_nouns) or len(tweets) != len(pred_nouns):
        print("Arquivos com tamanhos diferentes")
        sys.exit()




    y_true = []
    y_pred = []

    for i in range(len(tweets)):
        tweet = tweets[i]
        tweet_true_nouns = true_nouns[i].split(";")
        tweet_pred_nouns = pred_nouns[i].split(";")

        tweet_true_nouns = [x.strip(' ') for x in tweet_true_nouns]
        tweet_pred_nouns = [x.strip(' ') for x in tweet_pred_nouns]

        print(tweet)
        #print("")
        #print(tweet_true_nouns)
        #print("")
        #print(tweet_pred_nouns)
        #print("")
        tweet_words = tweet.split()
        for word in tweet_words:
            if word in tweet_true_nouns:
                c_true = "N"
            else:
                c_true = "O"

            if word in tweet_pred_nouns:
                c_pred = "N"
            else:
                c_pred = "O"

            y_pred.append(c_pred)
            y_true.append(c_true)

            if c_pred != c_true:
                print ("word: %s manual: %s pred: %s" % (word,c_true,c_pred))


        print("")
        print("")

    #for tweet in tweets:
    #    tweet_words = tweet.split()
        #for word in tweet_words:
        #    print(word)
    #    print("")
    print(y_pred[:10])
    print(y_true[:10])


    print(len(y_pred))
    print(len(y_true))


    print("Classification Report:")
    print(metrics.classification_report(y_true, y_pred))

    print("Confusion Matrix:")
    print(metrics.confusion_matrix(y_true, y_pred))


    #print metrics.accuracy_score(cm,ct)

    #print cm.array([[0, 1], [1, 1]])


if __name__ == '__main__':
    main()
