import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import preprocessing
import math
import operator
training_file=open("your_csv_file.csv")
reader=csv.reader(training_file)
train_set=[]
train_set1=[]
answers=[]
for data in reader:
	train_set.append(data[0])
	answers.append(data[1])
	train_set1.append(data[0])
vectorizer = CountVectorizer(ngram_range=(0,3),stop_words='english') #for making tokens
tfidf = TfidfTransformer()
training_set_counter=vectorizer.fit_transform(train_set)
training_set_tfidf = tfidf.fit_transform(training_set_counter) #assigning weights to each token

# sorted_x = sorted(vectorizer.vocabulary_.items(), key=operator.itemgetter(0))

#--------- 
#converting question to class labels and mapping each of them with index value
train_set1.append("")
le = preprocessing.LabelEncoder()
le.fit(train_set1)
# le.transform(list(le.classes_))
#-----------

lr=MultinomialNB().fit(training_set_tfidf,le.transform(list(le.classes_))) #classifier

query=raw_input('enter your question\n')
user_input_query=[query]

user_input_query_counter=vectorizer.transform(user_input_query)
user_input_query_tfidf=tfidf.transform(user_input_query_counter)
predicted=lr.predict(user_input_query_tfidf)

for index_of in predicted:
	print "Predicted Question->",'%s' % (train_set[index_of])
	print "answers->",'%s' % (answers[index_of])
