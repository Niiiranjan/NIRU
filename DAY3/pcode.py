import pandas as pd
data={"calories ":[420,380,390],"duration":[50,40,45]}
#load dataq into a DataFrame object:
df=pd.DataFrame(data)
print(df)

dataset={"Student": ["Des","Niru","Sam","Dittu","chukku","sapp","kari","Rohi","Anj","Kp"],"Marks":[95,99,75,80,90,70,95,88,92,78]}
result=pd.DataFrame(dataset)
print(result)

print(result.iloc[[0,1]])
