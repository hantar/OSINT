import django
django.setup()
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from demo.models import Datacrawl
from OSINT.settings import *

db = [Datacrawl.objects.all()]

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def prepareData(tweets):
    tweets = [REPLACE_NO_SPACE.sub("", line.lower()) for line in tweets]
    tweets = [REPLACE_WITH_SPACE.sub(" ", line) for line in tweets]

    return tweets

def classifyData(X):
    target = [1 if i < 64 else 0 for i in range(41)]
    X_train, X_val, y_train, y_val = train_test_split(X, target, train_size = 0.75)

    for c in [0.01, 0.05, 0.25, 0.5, 1]:
        lr = LogisticRegression(C=c)
        lr.fit(X_train,y_train)
        print ("Accuracy for C=%s: %s" % (c, accuracy_score(y_val, lr.predict(X_val))))

    return target

def buildFinalModel(X, target, X_test):
    final_model = LogisticRegression(C=0.05)
    final_model.fit(X, target)
    print("Final Accuracy: %s" % accuracy_score(target, final_model.predict(X_test)))
    return final_model

def sanityCheck(cv, final_model):
    feature_to_coef = {
    word: coef for word, coef in zip(
        cv.get_feature_names(), final_model.coef_[0]
        )
    }
    for best_positive in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1], 
        reverse=True)[:5]:
        print (best_positive)

    for best_negative in sorted(
        feature_to_coef.items(), 
        key=lambda x: x[1])[:5]:
        print (best_negative)

#######################################################################

#create initial lists
tweetTrain = []
for line in db[0]:
	tweetTrain.append(str(line))

tweetTest = []
for line in db[0]:
	tweetTest.append(str(line))

#clean list formatting
tweetTrain_Clean = prepareData(tweetTrain)
tweetTest_Clean = prepareData(tweetTest)

print(tweetTrain_Clean)
print(tweetTest_Clean)

#data vectorization
cv = CountVectorizer(binary=True)
cv.fit(tweetTrain_Clean)
X = cv.transform(tweetTrain_Clean)
print(X.shape)
X_test = cv.transform(tweetTest_Clean)

#create targets
target = classifyData(X)

#build final model
final_model = buildFinalModel(X, target, X_test)

#run sanity check
sanityCheck(cv, final_model)