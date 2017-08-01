# Introduction
Simple chatbot for answering questions, can be used with any csv file, containing questions in row[0] and their respective answers in row[1].
# Classifier used
Naive Bayes classifier for multinomialNB
# What's happening?
I am treating each question as individual class mapped with their indexes which are identified with tf-idf matrix used with n-grams(with n=3) (for more accuracy with continuous words) , ones naive bayes classifier classifies index value, that index value is used to retrieve question with it's answer.
 
 
 
