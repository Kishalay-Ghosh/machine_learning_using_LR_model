import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
sns.set(color_codes=True)
#for kappa statistic and roc_auc

from sklearn.datasets import make_circles
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
#Loading and Reviewing the Data
from sklearn.model_selection import train_test_split
feature_col_names = ['Your gender[ Male=1 , Female=0 ]','College student','Divorced','Separated','Eating disorders( Anorexia, Bulimia, Binge eating etc.)','Faced this situation currently','Facing these problems less than 1 month','Hallucination','Fatigue','Guilt without any reasons','Drug and alcohol misuse','Excessive mental stress for studies','Social disadvantage, poverty or debt','Being a long-term carer for someone','Being involved in a serious incident in which you feared for your life','Is your problem diagnosed ?','Are you still in treatment ?','More than 1 month and less than 6 months in treatment ','Is your problem fixed with helped by friends or relatives','Is your problem fixed by self realization or self motivation','Trust Issues','Health Crisis'
]


predicted_class_names = ['Outcome']
data_frame = pd.read_csv("test.csv")

data_frame.shape
data_frame.head(5)
data_frame.tail(5)
#Check for null values
print (data_frame.isnull().values.any())

num_obs = len(data_frame)
num_true = len(data_frame.loc[data_frame['Outcome'] == 1])
num_false = len(data_frame.loc[data_frame['Outcome'] == 0])
print("Number of True cases:  {0} ({1:2.2f}%)".format(num_true, ((1.00 * num_true)/(1.0 * num_obs)) * 100))
print("Number of False cases: {0} ({1:2.2f}%)".format(num_false, (( 1.0 * num_false)/(1.0 * num_obs)) * 100))


#Spliting the data
#from sklearn.cross_validation import train_test_split


# replace 'nAn' values with AVERAGE
data_frame=data_frame.fillna(data_frame.mean())


X = data_frame[feature_col_names].values     # predictor feature columns (8 X m)
y = data_frame[predicted_class_names].values # predicted class (1=true, 0=false) column (1 X m)
split_test_size = 0.20

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=42)
                            # test_size = 0.3 is 30%, 42 is the answer to everything


#We check to ensure we have the the desired 70% train, 30% test split of the data
trainval = (1.0 * len(X_train)) / (1.0 * len(data_frame.index))
testval = (1.0 * len(X_test)) / (1.0 * len(data_frame.index))
print("{0:0.2f}% in training set".format(trainval * 100))
print("{0:0.2f}% in test set".format(testval * 100))



#Verifying predicted value was split correctly
print("Original True  : {0} ({1:2.2f}%)".format(len(data_frame.loc[data_frame['Outcome'] == 1]), (len(data_frame.loc[data_frame['Outcome'] == 1])/len(data_frame.index)) * 100.0))
print("Original False : {0} ({1:2.2f}%)".format(len(data_frame.loc[data_frame['Outcome'] == 0]), (len(data_frame.loc[data_frame['Outcome'] == 0])/len(data_frame.index)) * 100.0))
print("")
print("Training True  : {0} ({1:2.2f}%)".format(len(y_train[y_train[:] == 1]), (len(y_train[y_train[:] == 1])/len(y_train) * 100.0)))
print("Training False : {0} ({1:2.2f}%)".format(len(y_train[y_train[:] == 0]), (len(y_train[y_train[:] == 0])/len(y_train) * 100.0)))
print("")
print("Test True      : {0} ({1:2.2f}%)".format(len(y_test[y_test[:] == 1]), (len(y_test[y_test[:] == 1])/len(y_test) * 100.0)))
print("Test False     : {0} ({1:2.2f}%)".format(len(y_test[y_test[:] == 0]), (len(y_test[y_test[:] == 0])/len(y_test) * 100.0)))



#Training Initial Algorithm - Logistic Regression

      
      
      
split_test_size = 0.20

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=42)      




print('**********************************Logistic Regression*****************************************')



lr_model = LogisticRegression(C=0.7, random_state=42)
lr_model.fit(X_train, y_train.ravel())
lr_predict_test = lr_model.predict(X_test)

# training metrics
print ("Accuracy : {0:.4f}".format(metrics.accuracy_score(y_test, lr_predict_test)))

print ("Confusion Matrix")

print (metrics.confusion_matrix(y_test, lr_predict_test, labels=[1, 0]))

print ("")

print ("Classification Report")

print (metrics.classification_report(y_test, lr_predict_test, labels=[1, 0]))
print("************************Kappa Statistic and ROC_AUC*********************")

kappa = cohen_kappa_score(y_test, lr_predict_test)
print('Cohens kappa: %f' % kappa)
# ROC AUC
auc = roc_auc_score(y_test, lr_predict_test)
print('ROC AUC: %f' % auc)

print ("")
print ("")
print ("")
print ("")
print ("")



