# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:33:43 2023

@author: KISHALAY GHOSH
"""

# -- coding: utf-8 --
"""
Created on Sat Jan 14 20:47:06 2023

@author: KISHALAY GHOSH
"""
import m as mr
import pandas as pd
coef=[]   #store coefficient value
dt=pd.read_csv(r'C:\mental_health\health research.csv')
#print(dt)

for i in range(3):
    percent=int(input("please enter the train data set range in percentage :"))
    
    train_data_range=((210*percent)//100)
    
    yl=  dt['Thought of self harm or suicide'].tolist()
    ym=mr.avg(dt['Thought of self harm or suicide'].tolist(),train_data_range)
    
    x0=dt['Your gender[ Male=1 , Female=0 ]'].tolist()
    x1=dt['College student'].tolist()
    x2=dt['Anxiety'].tolist()
    x3=dt['Separated'].tolist()
    x4=dt['Eating disorders( Anorexia, Bulimia, Binge eating etc.)'].tolist()
    x5=dt['Faced this situation currently'].tolist()
    x6=dt['Facing these problems less than 1 month'].tolist()
    x7=dt['Hallucination'].tolist()
    x8=dt['Fatigue'].tolist()
    x9=dt['Guilt without any reasons'].tolist()
    x10=dt['Drug and alcohol misuse'].tolist()
    x11=dt['Excessive mental stress for studies'].tolist()
    x12=dt['Social disadvantage, poverty or debt'].tolist()
    x13=dt['Being a long-term carer for someone'].tolist()
    x14=dt['Being involved in a serious incident in which you feared for your life'].tolist()
    x15=dt['Is your problem diagnosed ?'].tolist()
    x16=dt['Are you still in treatment ?'].tolist()
    x17=dt['More than 1 month and less than 6 months in treatment '].tolist()
    x18=dt['Is your problem fixed with helped by friends or relatives'].tolist()
    x19=dt['Is your problem fixed by self realization or self motivation'].tolist()
    x20=dt['Trust Issues'].tolist()
    x21=dt['Health Crisis'].tolist()
    
    x22=dt['Depression'].tolist()
    
    
    coef.append(mr.coefficient(x0, mr.avg(x0,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x1, mr.avg(x1,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x2, mr.avg(x2,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x3, mr.avg(x3,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x4, mr.avg(x4,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x5, mr.avg(x5,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x6, mr.avg(x6,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x7, mr.avg(x7,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x8, mr.avg(x8,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x9, mr.avg(x9,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x10, mr.avg(x10,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x11, mr.avg(x11,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x12, mr.avg(x12,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x13, mr.avg(x13,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x14, mr.avg(x14,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x15, mr.avg(x15,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x16, mr.avg(x16,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x17, mr.avg(x17,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x18, mr.avg(x18,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x19, mr.avg(x19,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x20, mr.avg(x20,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x21, mr.avg(x21,train_data_range), yl, ym, train_data_range ))
    coef.append(mr.coefficient(x22, mr.avg(x22,train_data_range), yl, ym, train_data_range ))
    
    #print(len(coef))
    '''calculate value of a'''
    tdr=train_data_range
    a=mr.calculate_A(coef,ym,mr.avg(x0,tdr),mr.avg(x1,tdr),mr.avg(x2,tdr),mr.avg(x3,tdr),mr.avg(x4,tdr),mr.avg(x5,tdr),mr.avg(x6,tdr),mr.avg(x7,tdr),mr.avg(x8,tdr),mr.avg(x9,tdr),mr.avg(x10,tdr),mr.avg(x11,tdr),mr.avg(x12,tdr),mr.avg(x13,tdr),mr.avg(x14,tdr),mr.avg(x15,tdr),mr.avg(x16,tdr),mr.avg(x17,tdr),mr.avg(x18,tdr),mr.avg(x19,tdr),mr.avg(x20,tdr),mr.avg(x21,tdr),mr.avg(x22,tdr))
    #print(a)
    
    
    '''linear to logistic convertion'''
    y_logistic=mr.linear_to_logistic(a,coef,tdr+1,211,x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22)
    #print(y_logistic)
    
    '''calculate accuracy'''
    
    accuracy=mr.calaulate_accuracy(y_logistic,yl,tdr+1,211)
    print("Accuracy is (train data={}% test data={}% )--->{}%".format(percent,100-percent,accuracy ))
    #for i in range(tdr+1,211):
        #print(y_logistic[i-(tdr+1)],"    ",yl[i])
    '''tp tn fp and fn calculate'''
    '''calculate sensitivity and specificity'''
    
    sensitivity,specificity,accuracy1,kappa,precession,recall,f1_score,tp,fn,fp,tn=mr.TP_TN_FP_FN_SENSITIVITY_SPECIFICITY_and_Accuracy_CALCULATE(y_logistic,yl,tdr+1,211)
    print("\nConfusion matrix---->\n")
    print(tp,"\t",fn,"\n")
    print(fp,"\t",tn,"\n")
    print("sensitivity=",sensitivity,"%   ","specificity=",specificity,"% ","accuracy by t=",accuracy1,"%  kappa=",kappa," precession=",precession," recall=",recall," f1_score=",f1_score, )
    print("---------------------------------------------------------------------------------------------------------------------------------")
    