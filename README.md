# Introduction:
Simple chatbot for answering questions, can be used with any csv file, containing questions in first column and their respective answers in second column.
## Classifier used:
Naive Bayes classifier for multinomialNB
## What's happening?
I am treating each question as individual class mapped with their indexes which are identified with tf-idf matrix used with n-grams(with n=3) (for more accuracy with continuous words) , ones naive bayes classifier classifies index value, that index value is used to retrieve question with it's answer.
## Library used:
scikit-learn 
## demo-screenshots
![00000192](https://user-images.githubusercontent.com/15835800/28823140-c3e3101e-76d9-11e7-9d16-dc035ab0c614.jpg)
![00000276](https://user-images.githubusercontent.com/15835800/28823179-f134c8dc-76d9-11e7-83b2-4d9bbd1d64b6.jpg)


