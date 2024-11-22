
#  PART 2: SELECTING AND MANIPULATING DATA


#VIDEO: Deleting Rows and COlumns
# %%
##############
#Deleting columns
#Delete Manual2 column
import pandas as pd
df = pd.read_csv('./manual_vs_auto2.csv')
# %%

df1 = df.drop("Manual2", axis=1) #Creating a new dataframe df1. 
# Axis=1 means referring to column. 
print(df.columns)
print(df1.columns)
# %%

#To drop multiple columns
df2=df.drop(["Manual2", "Auto_th_2", "Auto_th_3"], axis=1)
print(df2.columns)
# %%

#Inserting new columns, 

import pandas as pd
df = pd.read_csv('./manual_vs_auto2.csv')
#as easy as just typing...
df['Date'] = "2019-05-06" 

# %%

print(df.head())  #New column addded
#But if you look at the data type....
print(df.dtypes)  #Date is not in date format, it is as object, otherwise string
# %%

#To properly format it as date so you can plot it later....
df['Date'] = pd.to_datetime("2019-05-06")

print(df.head())
print(df.dtypes)
# %%

#You can write the data back to a new csv.
df.to_csv('maual_vs_auto_updated.csv') #Open csv file to see
# %%

##################
#Deleting rows
import pandas as pd
df = pd.read_csv('./manual_vs_auto2.csv')
# %%

#Delete a specific row
df1 = df.drop(df.index[1])
#Delete first 10 rows
print(df1.head())
df = df.iloc[10:,]
print(df.head())
# %%

#Drop all rows if the row value is equal to some string or number
df1 = df[df["Unnamed: 0"] != "Set1"]
print(df1.head())


# %%
data = {
    "name": ["Ayowole", "Tunji", "Ahmed", "Racheal", "Dave", "santan"],
    "Age": [14,54,33,45,22,11],
    'Department': ['csc', 'ba', 'mee', 'che', 'mc', 'eee']
}

df = pd.DataFrame(data)
# %%
print(df)
# %%
import pandas as pd

data = [
    ["Ayowole", 14, 'csc'],
    ["Tunji", 54, 'ba'],
    ["Ahmed", 33, 'mee'],
    ["Racheal", 45, 'che'],
    ["Dave", 22, 'mc'],
    ["santan", 11, 'eee']
]

df = pd.DataFrame(data, columns=['name', 'age', 'department'])
print(df)

# %%
df['grades'] = ['A', "B", 'D', "B", "C", "A"]
print(df)
# %%
df['isAdult'] = df['age'] > 18
# %%
print(df)
# %%
df.loc[len(df)] = ["James", 28, "phy", "B", True]

print(len(df))
print(df)
# %%
# Only show adults
# adults = df[df["is_adult"]]


# Students in specific departments
specific_dept = df[df["department"].isin(["csc", "mee"])]
# %%
# Sort by age
df.sort_values(by="age", ascending=False, inplace=True)
print(df)
# %%
# Convert names to uppercase
df["name"] = df["name"].apply(lambda x: x.upper())
df["age"] = df["age"].apply(lambda x: x - 10 if x > 30 else x)
# %%
print(df)
# %%
# Group by department and calculate average age
grouped = df.groupby("name")["age"].mean()
print(grouped)

# %%
# Create a pivot table
pivot = df.pivot_table(index="grades", values="age", aggfunc="mean")

# %%
print(pivot)
# %%
df["description"] = f"{df["name"]} {df["department"]}"
print(df)
# %%
df.drop(columns=["description"], inplace=True)
# %%
print(df)

# %%
df["description"] = df["name"] + " " + df["department"]
print(df)
# %%
