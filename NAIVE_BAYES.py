import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Social_Network_Ads.csv')

x=dataset.iloc[:300,2].values
y=dataset.iloc[:300,3].values
z=dataset.iloc[:300,4].values

f=dataset.iloc[300:,4].values

q=dataset.iloc[:300,[2,3]].values
q1=dataset.iloc[300:,[2,3]].values

from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x5=sc_x.fit_transform(q)
x6=sc_x.fit_transform(q1)


def distance(x1,y1,x2,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**(0.5)

distance(x5[0][0],x5[0][1],x6[0][0],x6[0][1])

co=0   #COUNTS THE NUMBER OF PPL WHO CAN NOT BUY A CAR
c=0    #COUNTS THE NUMBER OF PPL WHO CAN BUY A CAR
for i in range(0,300):
    if z[i]==0:
        co+=1
    elif z[i]==1:
        c+=1

ar=[]

def naiveb(x,z,a):  #X IS THE ALREADY GIVEN COORDINATES. Z IS THE ALREADY GIVEN POINTS AND a IS THE TESTING VALUES
    for j in range(0,100):
        count=0   #COUNTS THE NUMBER OF SIMILAR POINTS LIEING IN A PARTICULAR REGION
        cz=0      #COUNTS THE NUMBER OF PPL WHO WALK AND LIE IN THAT PARTICULAR REGION
        for i in range(0,300):
            if (distance(x[i][0],x[i][1],a[j][0],a[j][1])<=1):
                if z[i]==0:
                    cz+=1
                count+=1
        print(count)
        print(cz)
        prob=((cz/co)*(co/300))/(count/300) #300 is the total number of observation 
        print(prob)
        if prob<=0.5:
            ar.append(1)
            print("the person's probably gonna buys the car")
        else:
            ar.append(0)
            print("the person's probably not gonna buys the car")
print(ar)
naiveb(x5,z,x6)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ar,f)
            
    
    
    
    
