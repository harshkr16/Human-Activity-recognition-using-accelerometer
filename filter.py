def filter():
    import pandas as pd
    import re
#read csv file
    df1 = pd.read_csv(r"/home/harsh/Downloads/accel_data.csv")
#read x axis
    df2=df1
    df2['x']=df1.iloc[:,0:1]
    df2['y']=df1.iloc[:,1:2]
    df2['z']=df1.iloc[:,2:3]	
    df1=df2.iloc[:,3:6]
#convert to list type
    x=df1["x"].tolist()
    y=df1["y"].tolist()
    z=df1["z"].tolist()
    def func(x):
        w=50
        wh=int(w/2)
        l=len(x)
        i=0
        tx=[]
        mx=[]

        for i in range(l):
            if w%2==0:
                if i<=int(wh):
                    tx.append(sum(x[0:i])+sum(x[i:(wh+i)]))
                    mx.append(tx[i]/(wh+i))
            
                elif wh<i<=l-wh:          
                    tx.append(sum(x[i-wh:i])+sum(x[i:i+wh]))
                    mx.append(tx[i]/w)


                elif i>l-wh:
                    tx.append(sum(x[i-wh:i])+sum(x[i:l+1]))
                    mx.append(tx[i]/(wh+len(x[i:l+1])))        
    
        return mx

    lx=func(x)
    ly=func(y)
    lz=func(z)
    df=pd.DataFrame([lx,ly,lz],columns=['x','y','z'])
    return df





            
