import pandas as pd
df=pd.DataFrame(
    {
        'value':[5,12,17,24,35,46,59,63,72]
    }
)
print(df)

bin=[0,12,18,60,100]
label=['Child','Teen','Adult','Senior']
df['Custom_Bin']=pd.cut(df['value'],bins=bin,labels=label,right=False)
print(df)