# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:43:13 2023

@author: KISHALAY GHOSH

decission tree main
"""
import pandas as pd
import decision_tree_module as dtm
dt=pd.read_excel(r'C:\mental_health\decision tree\decision_tree.xlsx')
n=int(input("please enter the itteration value :"))
for i in range(n):
    p=int(input("please input the train data range in percentage :")) 
    l=(210*p)//100 #convert percentage into interger value
    
    
    '''.............train data set............'''
    
    y=  dt['Thought of self harm or suicide'].tolist()[:l]
    x0=dt['Anxiety'].tolist()[:l]
    x1=dt['Depression'].tolist()[:l]
    x2=dt['Drug and alcohol misuse'].tolist()[:l]
    x3=dt['Guilt without any reasons'].tolist()[:l]
    x4=dt['Excessive mental stress for studies'].tolist()[:l]
    x5=dt['Being involved in a serious incident in which you feared for your life'].tolist()[:l]
    
    '''.........test data set..............'''
    
    y_test=dt['Thought of self harm or suicide'].tolist()[l:]
    x0_test=dt['Anxiety'].tolist()[l:]
    x1_test=dt['Depression'].tolist()[l:]
    x2_test=dt['Drug and alcohol misuse'].tolist()[l:]
    x3_test=dt['Guilt without any reasons'].tolist()[l:]
    x4_test=dt['Excessive mental stress for studies'].tolist()[l:]
    x5_test=dt['Being involved in a serious incident in which you feared for your life'].tolist()[l:]
    
    x0_f,x1_f,x2_f,x3_f,x4_f,x5_f,x0_no,x1_no,x2_no,x3_no,x4_no,x5_no,avg=dtm.train(y,x0,x1,x2,x3,x4,x5)
    
    print("avarage is :",avg)
    
    print( "x0_f=",x0_f," x1_f=",x1_f," x2_f=",x2_f," x3_f=",x3_f," x4_f=",x4_f," x5_f=",x5_f)
    
    '''............for test data.............'''
    predict_list,one_to_one_accurecy=dtm.test(y_test,x0_test,x1_test,x2_test,x3_test,x4_test,x5_test,x0_f,x1_f,x2_f,x3_f,x4_f,x5_f,x0_no,x1_no,x2_no,x3_no,x4_no,x5_no,avg)
    
    print( predict_list)
    print(y_test)
    
    '''one to one accurecy'''
    print("\none to one accurecy=",one_to_one_accurecy)
    
    sensitivity,specificity,accuracy,kappa=dtm.TP_TN_FP_FN_SENSITIVITY_SPECIFICITY_and_Accuracy_CALCULATE(predict_list,y_test)
    print("sensitivity=",sensitivity,"%   ","specificity=",specificity,"% ","accuracy by t=",accuracy,"%  kappa=",kappa,"\n" )
   