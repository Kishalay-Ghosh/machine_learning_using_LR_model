import pandas
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import make_scorer
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
# Read data
feature_col_names = ['Your gender[ Male=1 , Female=0 ]','College student','Divorced','Separated','Eating disorders( Anorexia, Bulimia, Binge eating etc.)','Faced this situation currently','Facing these problems less than 1 month','Hallucination','Fatigue','Guilt without any reasons','Drug and alcohol misuse','Excessive mental stress for studies','Social disadvantage, poverty or debt','Being a long-term carer for someone','Being involved in a serious incident in which you feared for your life','Is your problem diagnosed ?','Are you still in treatment ?','More than 1 month and less than 6 months in treatment ','Is your problem fixed with helped by friends or relatives','Is your problem fixed by self realization or self motivation','Trust Issues','Health Crisis'
]


predicted_class_names = ['Outcome']
dataframe = pd.read_csv("test.csv")

# replace '0' values with 'nan'
#dataframe[[1,2,3,4,5] = dataframe[[1,2,3,4,5]].replace(0, nan)



# replace 'nAn' values with AVERAGE
dataframe=dataframe.fillna(dataframe.mean())


X = dataframe[feature_col_names].values     # predictor feature columns (8 X m)
Y = dataframe[predicted_class_names].values # predicted class (1=true, 0=false) column (1 X m)

scoring = 'accuracy'
#X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
seed = 7
print("")
print("")
print("")
print("")





##############################################################################################################

print("****Cross valid  logistic regression**** ")

kfold = model_selection.KFold(n_splits=10, random_state=seed)
modelLR = LogisticRegression()
modelLR.fit(X, Y.ravel())



from sklearn.model_selection import cross_val_score
Tscores= cross_val_score(modelLR, X, Y.ravel(), cv=10, scoring='accuracy')
totacu = round((Tscores.mean()*100),3) #average accuracy
Rscores= cross_val_score(modelLR, X, Y.ravel(), cv=10, scoring='recall_weighted')
sensitivityVal=round((Rscores.mean()*100),3)
Pscores= cross_val_score(modelLR, X, Y.ravel(), cv=10, scoring='precision_weighted')
precision=round((Pscores.mean()*100),3)
f1score=round(2*((sensitivityVal*precision)/(sensitivityVal+precision)),3)
print("*******************LR Model Cross Validation***************************")
print("Accuracy=")
print(totacu)

resultsLR = model_selection.cross_val_score(modelLR, X, Y.ravel(), cv=kfold, scoring=scoring)
print("Standard deviation=")
print(resultsLR.std())


print("Sensitivity=")
print(sensitivityVal)
print("Precision=")
print(precision)
print("F1 Score=")
print(f1score)
aucscores= cross_val_score(modelLR, X,Y.ravel(), cv=10,scoring='roc_auc')
auc_roc_sc=round((aucscores.mean()*100),3)
print("ROC_AUC:")
print(auc_roc_sc)
kappa_scorer = make_scorer(cohen_kappa_score)
kappascores= cross_val_score(modelLR, X, Y.ravel(), cv=10,scoring=kappa_scorer)

kappa_roc_sc=round((kappascores.mean()*100),3)
print("Kappa Score:")
print(kappa_roc_sc)
#print(kappascores)

from sklearn.model_selection import cross_val_predict
y_pred = cross_val_predict(modelLR, X, Y.ravel(), cv=10)
conf_mat = confusion_matrix(Y, y_pred)
print("Confusion Matrix")
print(conf_mat)

print("")
print("")
print("")
print("")
print("")
print("")
print("*************************************************************")
