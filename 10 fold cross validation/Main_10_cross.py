# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 00:47:38 2023

@author: KISHALAY GHOSH
"""

import module_10_cross as mr
import pandas as pd
coef=[]   #store coefficient value
dt=pd.read_csv(r'C:\mental_health\health research.csv')

'''start 10 fold cross validation'''
length=dt['Thought of self harm or suicide'].tolist()
diff=len(length)//10
#print(diff)

start=0
end=diff

for i in range(10):
    
    '''train data set for cross validation'''
    
    yl= dt['Thought of self harm or suicide'].tolist()[:start]+dt['Thought of self harm or suicide'].tolist()[end:]
    ym=mr.avg(yl)
    
    x0=dt['Your gender[ Male=1 , Female=0 ]'].tolist()[:start]+dt['Your gender[ Male=1 , Female=0 ]'].tolist()[end:]
    x1=dt['College student'].tolist()[:start]+dt['College student'].tolist()[end:]
    x2=dt['Anxiety'].tolist()[:start]+dt['Anxiety'].tolist()[end:]
    x3=dt['Separated'].tolist()[:start]+dt['Separated'].tolist()[end:]
    x4=dt['Eating disorders( Anorexia, Bulimia, Binge eating etc.)'].tolist()[:start]+dt['Eating disorders( Anorexia, Bulimia, Binge eating etc.)'].tolist()[end:]
    x5=dt['Faced this situation currently'].tolist()[:start]+dt['Faced this situation currently'].tolist()[end:]
    x6=dt['Facing these problems less than 1 month'].tolist()[:start]+dt['Facing these problems less than 1 month'].tolist()[end:]
    x7=dt['Hallucination'].tolist()[:start]+dt['Hallucination'].tolist()[end:]
    x8=dt['Fatigue'].tolist()[:start]+dt['Fatigue'].tolist()[end:]
    x9=dt['Guilt without any reasons'].tolist()[:start]+dt['Guilt without any reasons'].tolist()[end:]
    x10=dt['Drug and alcohol misuse'].tolist()[:start]+dt['Drug and alcohol misuse'].tolist()[end:]
    x11=dt['Excessive mental stress for studies'].tolist()[:start]+dt['Excessive mental stress for studies'].tolist()[end:]
    x12=dt['Social disadvantage, poverty or debt'].tolist()[:start]+dt['Social disadvantage, poverty or debt'].tolist()[end:]
    x13=dt['Being a long-term carer for someone'].tolist()[:start]+dt['Being a long-term carer for someone'].tolist()[end:]
    x14=dt['Being involved in a serious incident in which you feared for your life'].tolist()[:start]+dt['Being involved in a serious incident in which you feared for your life'].tolist()[end:]
    x15=dt['Is your problem diagnosed ?'].tolist()[:start]+dt['Is your problem diagnosed ?'].tolist()[end:]
    x16=dt['Are you still in treatment ?'].tolist()[:start]+dt['Are you still in treatment ?'].tolist()[end:]
    x17=dt['More than 1 month and less than 6 months in treatment '].tolist()[:start]+dt['More than 1 month and less than 6 months in treatment '].tolist()[end:]
    x18=dt['Is your problem fixed with helped by friends or relatives'].tolist()[:start]+dt['Is your problem fixed with helped by friends or relatives'].tolist()[end:]
    x19=dt['Is your problem fixed by self realization or self motivation'].tolist()[:start]+dt['Is your problem fixed by self realization or self motivation'].tolist()[end:]
    x20=dt['Trust Issues'].tolist()[:start]+dt['Trust Issues'].tolist()[end:]
    x21=dt['Health Crisis'].tolist()[:start]+dt['Health Crisis'].tolist()[end:]
    
    x22=dt['Depression'].tolist()[:start]+dt['Depression'].tolist()[end:]
    
    
    '''test data set for cross validation'''
    yl_test=dt['Thought of self harm or suicide'].tolist()[start:end]
    x0_test=dt['Your gender[ Male=1 , Female=0 ]'].tolist()[start:end]
    x1_test=dt['College student'].tolist()[start:end]
    x2_test=dt['Anxiety'].tolist()[start:end]
    x3_test=dt['Separated'].tolist()[start:end]
    x4_test=dt['Eating disorders( Anorexia, Bulimia, Binge eating etc.)'].tolist()[start:end]
    x5_test=dt['Faced this situation currently'].tolist()[start:end]
    x6_test=dt['Facing these problems less than 1 month'].tolist()[start:end]
    x7_test=dt['Hallucination'].tolist()[start:end]
    x8_test=dt['Fatigue'].tolist()[start:end]
    x9_test=dt['Guilt without any reasons'].tolist()[start:end]
    x10_test=dt['Drug and alcohol misuse'].tolist()[start:end]
    x11_test=dt['Excessive mental stress for studies'].tolist()[start:end]
    x12_test=dt['Social disadvantage, poverty or debt'].tolist()[start:end]
    x13_test=dt['Being a long-term carer for someone'].tolist()[start:end]
    x14_test=dt['Being involved in a serious incident in which you feared for your life'].tolist()[start:end]
    x15_test=dt['Is your problem diagnosed ?'].tolist()[start:end]
    x16_test=dt['Are you still in treatment ?'].tolist()[start:end]
    x17_test=dt['More than 1 month and less than 6 months in treatment '].tolist()[start:end]
    x18_test=dt['Is your problem fixed with helped by friends or relatives'].tolist()[start:end]
    x19_test=dt['Is your problem fixed by self realization or self motivation'].tolist()[start:end]
    x20_test=dt['Trust Issues'].tolist()[start:end]
    x21_test=dt['Health Crisis'].tolist()[start:end]
   
    x22_test=dt['Depression'].tolist()[start:end]
    
    
    '''calculate b value and append it in coef list'''
    
    coef=[]
    coef.append(mr.coefficient(x0, mr.avg(x0), yl, ym))
    coef.append(mr.coefficient(x1, mr.avg(x1), yl, ym))
    coef.append(mr.coefficient(x2, mr.avg(x2), yl, ym))
    coef.append(mr.coefficient(x3, mr.avg(x3), yl, ym))
    coef.append(mr.coefficient(x4, mr.avg(x4), yl, ym))
    coef.append(mr.coefficient(x5, mr.avg(x5), yl, ym))
    coef.append(mr.coefficient(x6, mr.avg(x6), yl, ym))
    coef.append(mr.coefficient(x7, mr.avg(x7), yl, ym))
    coef.append(mr.coefficient(x8, mr.avg(x8), yl, ym))
    coef.append(mr.coefficient(x9, mr.avg(x9), yl, ym))
    coef.append(mr.coefficient(x10, mr.avg(x10), yl, ym))
    coef.append(mr.coefficient(x11, mr.avg(x11), yl, ym))
    coef.append(mr.coefficient(x12, mr.avg(x12), yl, ym))
    coef.append(mr.coefficient(x13, mr.avg(x13), yl, ym))
    coef.append(mr.coefficient(x14, mr.avg(x14), yl, ym))
    coef.append(mr.coefficient(x15, mr.avg(x15), yl, ym))
    coef.append(mr.coefficient(x16, mr.avg(x16), yl, ym))
    coef.append(mr.coefficient(x17, mr.avg(x17), yl, ym))
    coef.append(mr.coefficient(x18, mr.avg(x18), yl, ym))
    coef.append(mr.coefficient(x19, mr.avg(x19), yl, ym))
    coef.append(mr.coefficient(x20, mr.avg(x20), yl, ym))
    coef.append(mr.coefficient(x21, mr.avg(x21), yl, ym))
    coef.append(mr.coefficient(x22, mr.avg(x22), yl, ym))
   
    
    '''calculate a value'''
    
    a=mr.calculate_A(coef,ym,mr.avg(x0),mr.avg(x1),mr.avg(x2),mr.avg(x3),mr.avg(x4),mr.avg(x5),mr.avg(x6),mr.avg(x7),mr.avg(x8),mr.avg(x9),mr.avg(x10),mr.avg(x11),mr.avg(x12),mr.avg(x13),mr.avg(x14),mr.avg(x15),mr.avg(x16),mr.avg(x17),mr.avg(x18),mr.avg(x19),mr.avg(x20),mr.avg(x21),mr.avg(x22))
    
    '''linear to logistic convertion'''
    y_logistic=mr.linear_to_logistic(a,coef,x0_test,x1_test,x2_test,x3_test,x4_test,x5_test,x6_test,x7_test,x8_test,x9_test,x10_test,x11_test,x12_test,x13_test,x14_test,x15_test,x16_test,x17_test,x18_test,x19_test,x20_test,x21_test,x22_test)
    '''calculate accuracy'''
    accuracy=mr.calaulate_accuracy(y_logistic, yl_test)
    
    sensitivity,specificity,accuracy1,kappa,precession,recall,f1_score,tp,fn,fp,tn=mr.TP_TN_FP_FN_SENSITIVITY_SPECIFICITY_and_Accuracy_CALCULATE(y_logistic,yl_test)
    
    print(i+1," fold result---->")
    print("\nConfusion matrix---->\n")
    print(tp,"\t",fn,"\n")
    print(fp,"\t",tn,"\n")
    print("accuracy=", accuracy,"%")
    print("sensitivity=",sensitivity,"%   ","specificity=",specificity,"% ","accuracy by t=",accuracy1,"%  kappa=",kappa," precession=",precession," recall=",recall," f1_score=",f1_score, )
    print("\n\n")
    
    '''increment start and end variable'''
    start+=diff
    end+=diff
    
    
    