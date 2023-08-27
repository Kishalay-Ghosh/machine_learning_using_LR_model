# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:31:52 2022

@author: KISHALAY GHOSH
"""

# -- coding: utf-8 --
"""
Created on Sat Jan 14 21:07:46 2022

@author: KISHALAY GHOSH
"""

def avg(lst,length):
    sum=0
    #lst=int(lst)
    for i in range(length+1):
        sum+=lst[i]
    mean_value=sum/len(lst)
    return mean_value

def coefficient(x,xm,y,ym,length):
    l1=[]
    l2=[]
    sum1=0
    sum2=0
    for i in range(length+1):
        temp=(x[i]-xm)*(y[i]-ym)
        temp1=(x[i]-xm)**2
        l1.append(temp)
        l2.append(temp1)
    for i in range(length+1):
        sum1+=l1[i]
        sum2+=l2[i]
    return sum1/sum2

def calculate_A(l,ym,x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22):
    a=ym-((l[0]*x0)+(l[1]*x1)+(l[2]*x2)+(l[3]*x3)+(l[4]*x4)+(l[5]*x5)+(l[6]*x6)+(l[7]*x7)+(l[8]*x8)+(l[9]*x9)+(l[10]*x10)+(l[11]*x11)+(l[12]*x12)+(l[13]*x13)+(l[14]*x14)+(l[15]*x15)+(l[16]*x16)+(l[17]*x17)+(l[18]*x18)+(l[19]*x19)+(l[20]*x20)+(l[21]*x21)+(l[22]*x22))
    return a

def linear_to_logistic(a,b,start,end,x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22):
    l=[]
    for i in range(start,end+1):
        y=a+(b[0]*x0[i])+(b[1]*x1[i])+(b[2]*x2[i])+(b[3]*x3[i])+(b[4]*x4[i])+(b[5]*x5[i])+(b[6]*x6[i])+(b[7]*x7[i])+(b[8]*x8[i])+(b[9]*x9[i])+(b[10]*x10[i])+(b[11]*x11[i])+(b[12]*x12[i])+(b[13]*x13[i])+(b[14]*x14[i])+(b[15]*x15[i])+(b[16]*x16[i])+(b[17]*x17[i])+(b[18]*x18[i])+(b[19]*x19[i])+(b[20]*x20[i])+(b[21]*x21[i])+(b[22]*x22[i])
        yk=1/((1+(1/2.718)**y))
        if(yk>=0.7):
            l.append(1)
        else:
            l.append(0)
    return l

def calaulate_accuracy(y_logistic,y,start,end):
    count=0
    for i in range(start,end):
        if(y_logistic[i-start]==y[i]):
            count+=1
    accuracy=(count*100)/(end-start)
    return accuracy
def TP_TN_FP_FN_SENSITIVITY_SPECIFICITY_and_Accuracy_CALCULATE(yp,yl,start,end):
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(start,end):
        if(yl[i]==1 and yp[i-start]==1):
            tp+=1
        elif(yl[i]==0 and yp[i-start]==0):
            tn+=1
        elif(yl[i]==1 and yp[i-start]==0):
            fn+=1
        else:
            fp+=1
    sensitivity=tp/(tp+fn)
    specificity=tn/(tn+fp)
    accuracy=(tp+tn)/(tp+tn+fp+fn)
    
    p_correct=((tp+fp)/tp+tn+fp+fn)*((tp+fn)/tp+tn+fp+fn)
    p_incorrect=((tn+fp)/tp+tn+fp+fn)*((tn+fn)/tp+tn+fp+fn)
    
    p_e= p_correct+ p_incorrect
    
    kappa=(accuracy-p_e)/(1-p_e)
    
    precession=tp/(tp+fp)
    recall=tp/(tp+fn)
    t4=(recall+precession)
    if(t4==0):
        t4=0.0000000000001
    f1_score=((2*recall*precession)/t4)
    
    return sensitivity*100,specificity*100,accuracy*100,kappa,precession,recall,f1_score,tp,fn,fp,tn


    

        