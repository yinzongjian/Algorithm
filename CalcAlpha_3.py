#! /usr/bin/env python
#coding utf-8aA
import pandas as pd
import numpy as np
Test_data=pd.read_excel("D:\TestData.xlsx",header=0,columns=1,index_col=0)
N=10
tmp=1
AlphaList=[0,0,0,0,0]
keys=list(Test_data.columns)
predict_2018=[0,0,0,0,0]
predict_2019=[0,0,0,0,0]
for i in range(0,N):
    predict=0
    key=0
    predict_2018[key]=0.1*i*Test_data.iloc[0,key]
    predict_2019[key]=0.1*i*Test_data.iloc[1,key]
    
    for j in range(0,N-i):
        key=1
        predict_2018[key]=predict_2018[key-1]+0.1*j*Test_data.iloc[0,key]
        predict_2019[key]=predict_2019[key-1]+0.1*j*Test_data.iloc[1,key]
        
        for z in range(0,N-i-j):
            key=2
            predict_2018[key]=predict_2018[key-1]+0.1*z*Test_data.iloc[0,key]
            predict_2019[key]=predict_2019[key-1]+0.1*z*Test_data.iloc[1,key]
            
            for k in range(0,N-i-j-z):
                key=3
                predict_2018[key]=predict_2018[key-1]+0.1*k*Test_data.iloc[0,key]
                predict_2019[key]=predict_2019[key-1]+0.1*k*Test_data.iloc[1,key]
                
                predict_final_2018=predict_2018[key]+0.1*(N-i-j-z-k)*Test_data.iloc[0,key+1]
                predict_final_2019=predict_2019[key]+0.1*(N-i-j-z-k)*Test_data.iloc[1,key+1]
                if (abs(predict_final_2018)+abs(predict_final_2019))<tmp:
                    tmp=(abs(predict_final_2018)+abs(predict_final_2019))
                    AlphaList[0]=i
                    AlphaList[1]=j
                    AlphaList[2]=z
                    AlphaList[3]=k
                    AlphaList[4]=N-i-j-z-k
print("系统权重：{:.1f}，机器学习权重：{:.1f}，16个非短周期模型权重：{:.1f}，24个全模型权重：{:.1f}，程序权重：{:.1f}".format(0.1*AlphaList[0],0.1*AlphaList[1],0.1*AlphaList[2],0.1*AlphaList[3],0.1*AlphaList[4]))
