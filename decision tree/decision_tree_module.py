# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:45:18 2023

@author: KISHALAY GHOSH

decision tree module
"""

def train(y,x0,x1,x2,x3,x4,x5):
    x0_0=0
    x0_1=0
    x1_0=0
    x1_1=0
    x2_0=0
    x2_1=0   
    x3_0=0
    x3_1=0
    x4_0=0
    x4_1=0
    x5_0=0
    x5_1=0
    
    nx0_0=0
    nx0_1=0
    nx1_0=0
    nx1_1=0
    nx2_0=0
    nx2_1=0
    nx3_0=0
    nx3_1=0
    nx4_0=0
    nx4_1=0
    nx5_0=0
    nx5_1=0
    ''' final value for return''' 
    x0_f=0
    x1_f=0
    x2_f=0
    x3_f=0
    x4_f=0
    x5_f=0
    
    
    
    for i in range(len(y)):
        '''.....for suidicedental tendency'''
        if(y[i]==1):
            if(x0[i]==1):
                 x0_1+=1
            else:
                x0_0+=1
            if(x1[i]==1):
                 x1_1+=1
            else:
                x1_0+=1
            if(x2[i]==1):
                 x2_1+=1
            else:
                x2_0+=1
            if(x3[i]==1):
                 x3_1+=1
            else:
                x3_0+=1
            if(x4[i]==1):
                 x4_1+=1
            else:
                x4_0+=1
            if(x5[i]==1):
                 x5_1+=1
            else:
                x5_0+=1
        #not suicidental tendency 
        
        else:
            if(x0[i]==1):
                 nx0_1+=1
            else:
                nx0_0+=1
            if(x1[i]==1):
                 nx1_1+=1
            else:
                nx1_0+=1
            if(x2[i]==1):
                 nx2_1+=1
            else:
                nx2_0+=1
            if(x3[i]==1):
                 nx3_1+=1
            else:
                nx3_0+=1
            if(x4[i]==1):
                 nx4_1+=1
            else:
                nx4_0+=1
            if(x5[i]==1):
                 nx5_1+=1
            else:
                nx5_0+=1
    
       
    if(x0_1>x0_0):
        x0_f=1
        x0_r=x0_1   #store the greater value
    else:
        x0_f=0
        x0_r=x0_0
    if(x1_1>x1_0):
        x1_f=1
        x1_r=x1_1
    else:
        x1_f=0
        x1_r=x1_0
    if(x2_1>x2_0):
        x2_f=1
        x2_r=x2_1
    else:
        x2_f=0
        x2_r=x2_0
    if(x3_1>x3_0):
        x3_f=1
        x3_r=x3_1
    else:
        x3_f=0
        x3_r=x3_0
    if(x4_1>x4_0):
        x4_f=1
        x4_r=x4_1
    else:
        x4_f=0
        x4_r=x4_0
             
    if(x5_1>x5_0):
        x5_f=1
        x5_r=x5_1
    else:
        x5_f=0
        x5_r=x5_0
    '''calculate a weight for each atribute for calculate threshold value and '''
    x0_no=(x0_r*100)/(x0_0+x0_1)
    x1_no=(x1_r*100)/(x1_0+x1_1)
    x2_no=(x2_r*100)/(x2_0+x2_1)
    x3_no=(x3_r*100)/(x3_0+x3_1)
    x4_no=(x4_r*100)/(x4_0+x4_1)
    x5_no=(x5_r*100)/(x5_0+x5_1)
    total_list=[]
    
   
    
    for i in range(len(y)):
        total=0
        if(y[i]==1):
            if(x0[i]==x0_f):
                total=total+x0_no
            else:
                total=total+100-x0_no
            if(x1[i]==x1_f):
                total=total+x1_no
            else:
                 total=total+100-x1_no
            if(x2[i]==x2_f):
                total=total+x2_no
            else:
                total=total+100-x2_no
            if(x3[i]==x3_f):
                total=total+x3_no
            else:
                total=total+100-x3_no
            if(x4[i]==x4_f):
                total=total+x4_no
            else:
                total=total+100-x4_no
            if(x5[i]==x5_f):
                total=total+x5_no
            else:
                 total=total+100-x5_no
        total_list.append(total)
        
       
       
    
    #avg=sum(total_list)/len(total_list)
    #avg=max(total_list)
    #avg=(max(total_list)+min(total_list))/2
    total_list.sort(reverse=True)
    avg=(total_list[0]+total_list[1])/2
            
    
    return x0_f,x1_f,x2_f,x3_f,x4_f,x5_f,x0_no,x1_no,x2_no,x3_no,x4_no,x5_no,avg
'''...............for test the data..............'''
def test(y,x0,x1,x2,x3,x4,x5,x0_f,x1_f,x2_f,x3_f,x4_f,x5_f,x0_no,x1_no,x2_no,x3_no,x4_no,x5_no,avg):
    
    predict_list=[]
    count=0
    for i in range(len(x0)):
        total=0
        if(x0[i]==x0_f):
                total=total+x0_no
        if(x1[i]==x1_f):
                total=total+x1_no
        if(x2[i]==x2_f):
                total=total+x2_no
        if(x3[i]==x3_f):
                total=total+x3_no
        if(x4[i]==x4_f):
                total=total+x4_no
        if(x5[i]==x5_f):
                total=total+x5_no
        if(total>=avg):
            predict_list.append(1)
        else:
             predict_list.append(0)
       
    for i in range(len(x0)):
        if(y[i]==predict_list[i]):
            count+=1
    one_to_one_accurecy=(count*100)/len(y)
    return predict_list,one_to_one_accurecy

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
            fn+=1
        else:
            fp+=1
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
    t=(1-p_e)
    if(t==0):
        t=0.0000000001
    kappa=(accuracy-p_e)/t
    
    return sensitivity*100,specificity*100,accuracy*100,kappa