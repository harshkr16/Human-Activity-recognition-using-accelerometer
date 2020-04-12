class model():
    import numpy as np
    import pandas as pd
    import warnings
    import requests
    import re
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
	
    df_walk=pd.read_csv(r"/home/harsh/Desktop/walkw.csv")
    df_sit=pd.read_csv(r"/home/harsh/Desktop/sitw.csv")
    df_stand=pd.read_csv(r"/home/harsh/Desktop/standw.csv")
    df_sleep=pd.read_csv(r"/home/harsh/Desktop/sleepw.csv")
    df=pd.concat([df_walk,df_sit,df_stand,df_sleep])
    X=df.iloc[:,0:3]
    Y=df.iloc[:,3:4]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42,shuffle=True)
    warnings.filterwarnings("ignore")
    classifier = KNeighborsClassifier(n_neighbors=4)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    
#read csv file
    #df1 = pd.read_csv(r"/home/harsh/Downloads/accel_data.csv",header=None)
    #df2=df1
    #df2['x']=df1.iloc[:,0:1] 
    #df2['y']=df1.iloc[:,1:2]
    #df2['z']=df1.iloc[:,2:3]	
    #df1=df2.iloc[:,3:6]
    #x=df1["x"].tolist()
    #y=df1["y"].tolist()
    #z=df1["z"].tolist()
   

    #def func(x):
     #   w=50
      #  wh=int(w/2)
       # l=len(x)
        #i=0
   #     tx=[]
    #    mx=[]
#
 #       for i in range(l):
  #          if w%2==0:
   #             if i<=int(wh):
     #               tx.append(sum(x[0:i])+sum(x[i:(wh+i)]))
    #                mx.append(tx[i]/(wh+i))
      #      
       #         elif wh<i<=l-wh:          
        #            tx.append(sum(x[i-wh:i])+sum(x[i:i+wh]))
         #           mx.append(tx[i]/w)


          #      elif i>l-wh: 
           #         tx.append(sum(x[i-wh:i])+sum(x[i:l+1]))
            #        mx.append(tx[i]/(wh+len(x[i:l+1])))        
    
        #return mx

    #lx=func(x)
    #ly=func(y)
    #lz=func(z)
    #df1=pd.DataFrame(lx,columns=['x'])
    #df2=pd.DataFrame(ly,columns=['y'])
    #df3=pd.DataFrame(lz,columns=['z'])
    #df1=df1.join([df2,df3])     
    #df3=df1.to_numpy()
    df3=numpy.fromstring(buf, dtype=int, sep=' ')
    pred=classifier.predict(df3)
    print(pred)
    #df4=pd.DataFrame(pred)
    count1=0
    count2=0
    count3=0
    count4=0
   # for i in range(0,len(df4)):
            #if df4[0][i]=='sitting':
    #if pred=='sitting':
        #count1 +=1
   # elif pred=='walking':
    #    count2 +=1
    #elif pred=='standing':
     #   count3 +=1
    #else:
     #   count4 +=1
    #if count1 > count2 and count1 > count3 and count1>count4:
        #print("!!!SITTING!!!")
        #requests.post("https://maker.ifttt.com/trigger/ADetection/with/key/cyg_84yTHZnW7d34s6LAcW")
    #elif count2 > count1 and count2 > count3 and count2>count4:
     #   print("!!!WALKING!!!")
      #  requests.post("https://maker.ifttt.com/trigger/ADetection2/with/key/cyg_84yTHZnW7d34s6LAcW")
    #elif count3>count1 and count3>count2 and count3>count4:
     #   print("!!!STANDING!!!")
      #  requests.post("https://maker.ifttt.com/trigger/ADetection1/with/key/cyg_84yTHZnW7d34s6LAcW")
    #else:
     #   print("!!!SLEEPING!!!")
      #  requests.post("https://maker.ifttt.com/trigger/ADetection3/with/key/cyg_84yTHZnW7d34s6LAcW")
    c1=count1*0.055*2
    c2=count2*0.055*2
    c3=count3*0.055*2
    c4=count4*0.055*2
   # print("\nsitting for:%f seconds\n walking for:%f seconds \n standing for:%f seconds\n sleeping for:%f seconds"%(c1,c2,c3,c4))
    






            



