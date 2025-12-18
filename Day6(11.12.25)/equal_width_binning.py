import pandas as pd
df=pd.DataFrame(
    {
        'value':[5,12,18,25,32,45,55,63,75,89]
    }
)
print(df)

df['Equal_width_Bin']=pd.cut(df['value'],bins=4)
print(df)