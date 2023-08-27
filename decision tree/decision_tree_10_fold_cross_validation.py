# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:37:04 2023

@author: KISHALAY GHOSH

decision tree cross validation
"""

import pandas as pd
import decision_tree_module as dtm
dt=pd.read_excel(r'C:\mental_health\decision tree\decision_tree.xlsx')
total=len(dt['Thought of self harm or suicide'].tolist())
n=int(input("please enter the itteration value :"))
diff=total//n
start=0
end=diff

for i in range(n):
    
    
    
    '''.............train data set............'''
    
    y=  dt['Thought of self harm or suicide'].tolist()[:start]+dt['Thought of self harm or suicide'].tolist()[end:]
    x0=dt['Anxiety'].tolist()[:start]+dt['Anxiety'].tolist()[end:]
    x1=dt['Depression'].tolist()[:start]+dt['Depression'].tolist()[end:]
    x2=dt['Drug and alcohol misuse'].tolist()[:start]+dt['Drug and alcohol misuse'].tolist()[end:]
    x3=dt['Guilt without any reasons'].tolist()[:start]+dt['Guilt without any reasons'].tolist()[end:]
    x4=dt['Excessive mental stress for studies'].tolist()[:start]+dt['Excessive mental stress for studies'].tolist()[end:]
    x5=dt['Being involved in a serious incident in which you feared for your life'].tolist()[:start]+dt['Being involved in a serious incident in which you feared for your life'].tolist()[end:]
    
    '''.........test data set..............'''
    
    y_test=dt['Thought of self harm or suicide'].tolist()[start:end]
    x0_test=dt['Anxiety'].tolist()[start:end]
    x1_test=dt['Depression'].tolist()[start:end]
    x2_test=dt['Drug and alcohol misuse'].tolist()[start:end]
    x3_test=dt['Guilt without any reasons'].tolist()[start:end]
    x4_test=dt['Excessive mental stress for studies'].tolist()[start:end]
    x5_test=dt['Being involved in a serious incident in which you feared for your life'].tolist()[start:end]
    
    x0_f,x1_f,x2_f,x3_f,x4_f,x5_f,x0_no,x1_no,x2_no,x3_no,x4_no,x5_no,avg=dtm.train(y,x0,x1,x2,x3,x4,x5)
    
   
    
    #print( "x0_f=",x0_f," x1_f=",x1_f," x2_f=",x2_f," x3_f=",x3_f," x4_f=",x4_f," x5_f=",x5_f)
    
    '''............for test data.............'''
    predict_list,one_to_one_accurecy=dtm.test(y_test,x0_test,x1_test,x2_test,x3_test,x4_test,x5_test,x0_f,x1_f,x2_f,x3_f,x4_f,x5_f,x0_no,x1_no,x2_no,x3_no,x4_no,x5_no,avg)
    
    #print( predict_list)
    #print(y_test)
    print("...................................................",i+1," fold result............................................................\n")
    print("avarage is :",avg)
    '''one to one accurecy'''
    print("\none to one accurecy=",one_to_one_accurecy)
    
    sensitivity,specificity,accuracy,kappa=dtm.TP_TN_FP_FN_SENSITIVITY_SPECIFICITY_and_Accuracy_CALCULATE(predict_list,y_test)
    
    print("sensitivity=",sensitivity,"%\nspecificity=",specificity,"%\naccuracy by t=",accuracy,"%\nkappa=",kappa,"\n" )
    
    start+=diff
    end+=diff