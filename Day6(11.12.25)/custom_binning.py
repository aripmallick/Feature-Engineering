import pandas as pd
df=pd.DataFrame(
    {
        'value':[5,12,18,25,32,45,55,63,75,89]
    }
)
print(df)

bin=[0,40,70,100]
label=['Low','Medium','High']
df['Custom_Bin']=pd.cut(df['value'],bins=bin,labels=label)
print(df)