# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 23:05:41 2023

@author: KISHALAY GHOSH
"""

def avg(lst):
    sum=0
    #lst=int(lst)
    for i in lst:
        sum+=i
    mean_value=sum/len(lst)
    return mean_value

def coefficient(x,xm,y,ym):
    l1=[]
    l2=[]
    sum1=0
    sum2=0
    length=len(y)
    for i in range(length):
        temp=(x[i]-xm)*(y[i]-ym)
        temp1=(x[i]-xm)**2
        l1.append(temp)
        l2.append(temp1)
    for i in range(length):
        sum1+=l1[i]
        sum2+=l2[i]
    if(sum2==0):
        sum2=0.00000000001
    return sum1/sum2

def calculate_A(l,ym,x2,x5,x9,x11,x14,x23):
    a=ym-((l[0]*x2)+(l[1]*x5)+(l[2]*x9)+(l[3]*x11)+(l[4]*x14)+(l[5]*x23))
    return a

def linear_to_logistic(a,b,x2,x5,x9,x11,x14,x23):
    l=[]
    for i in range(len(x2)):
        y=a+((b[0]*x2[i])+(b[1]*x5[i])+(b[2]*x9[i])+(b[3]*x11[i])+(b[4]*x14[i])+(b[5]*x23[i]))
        yk=1/((1+(1/2.718)**y))
        if(yk>=0.5):
            l.append(1)
        else:
            l.append(0)
    return l

def calaulate_accuracy(y_logistic,y_test):
    count=0
    for i in range(len(y_test)):
        if(y_logistic[i]==y_test[i]):
            count+=1
    accuracy=(count*100)/len(y_test)
    return accuracy

def TP_TN_FP_FN_SENSITIVITY_SPECIFICITY_and_Accuracy_CALCULATE(yp,y_acctual):
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(len(y_acctual)):
        if(y_acctual[i]==1 and yp[i]==1):
            tp+=1
        elif(y_acctual[i]==0 and yp[i]==0):
            tn+=1
        elif(y_acctual[i]==1 and yp[i]==0):
            fp+=1
        else:
            fn+=1
    t1=(tp+fn)
    t2=(tn+fp)
    t3=(tp+tn+fp+fn)
    
    if(t1==0):
        t1=0.000000000001
    if(t2==0):
        t2=0.000000000001
    if(t3==0):
        t3=0.000000000001
            
    sensitivity=tp/t1
    specificity=tn/t2
    accuracy=(tp+tn)/t3    #p0=accuracy
    
    p_correct=((tp+fp)/t3)*((tp+fn)/t3)
    p_incorrect=((tn+fp)/t3)*((tn+fn)/t3)
    
    p_e= p_correct+ p_incorrect
    
    kappa=(accuracy-p_e)/(1-p_e)
    
    return sensitivity*100,specificity*100,accuracy*100,kappa