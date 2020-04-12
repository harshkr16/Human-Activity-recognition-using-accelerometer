
import socket
import requests
import os
import signal
import time


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('', 9004))
buf=''
d=['1','2','3']
serversocket.listen(5)
f= open("accel_data.csv","w+")
count=0
c1,c2,c3,c4=[],[],[],[]
c11,c22,c33,c44=0,0,0,0
while serversocket.accept():
        connection, address = serversocket.accept()
        start=time.time()
        while(connection.recv(1024)):
            #start=time.time()
            count +=1
            buf=connection.recv(1024).decode()
            #model(buf)
            buf = list(buf.split(","))
            print(buf)
            if buf==['']:
                d=[0,0,0]
                    
            else:
                for i in range(3):
                    d[i]=float(buf[i])    
           
            #end=time.time()
            

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
            df3=np.asarray(d)
            df3=df3.reshape(1,-1)
            pred=classifier.predict(df3)
            print(pred[0])
            if pred=="sitting":
                c1.append(1)
            elif pred=="walking":
                c2.append(1)
            elif pred=="standing":
                c3.append(1)
            else: 
                c4.append(1)
         
        end=time.time()	
        temp = end-start
        print(temp)
        print(count)
        c11=len(c1)*0.176
        c22=len(c2)*0.176
        c33=len(c3)*0.176
        c44=len(c4)*0.176
        print("sitting for:%f seconds\n walking for:%f seconds \n standing for:%f seconds\n sleeping for:%f seconds"%(c11,c22,c33,c44))
        os.kill(os.getpid(),signal.SIGINT)
        serversocket.close() 
            
