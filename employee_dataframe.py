import pandas as pd
df=pd.DataFrame({'emp id':[101,102,103,104,105,105],
                 'age':[25,30,None,45,120,None],
                 'deparment':['HR','IT','Finance',None,'IT','IT'],
                 'experience':[2,5,None,20,3,3],
                 'performance':[85,90,88,None,95,95]})
print("original data:\n",df)

df['age']=df['Age'].fillna(df['Age'].mean())
df['experience']=df['experience'].fillna(df['experience'].mean())
df['performance']=df['performance'].fillna(df['performance'].mean())
df['deparment']=df['deparment'].fillna('unknown')
print("\ndata after remove missing values: \n",df)

df.drop_duplicates(inplace=True)
print("\ndata after removing duplicates :\n",df)

Q1,Q3=df['age'].quantile(0.25),df['age'].quantile(0.75)
IQR=Q3-Q1
print("\noutliers in age:\n",df[(df['age']<Q1-1.5*IQR)|(df['age']>Q3+1.5*IQR)])