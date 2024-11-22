# %%
import pandas as pd
# %%
data = pd.read_csv("./manual_vs_auto2.csv")
df = pd.DataFrame(data)
df['Manual'].fillna(100, inplace=True)
print(df.head(25))

# %%
import  seaborn as sns
# %%
# sns.displot(df['Manual'])
sns.kdeplot(df['Manual'], shade= True)

# %%
# sns.jointplot(x='Manual', y = "Auto_th_2", data= df, kind="kde")
# sns.pairplot(df, x_vars=)

print(df["Manual"].isnull().sum())      # Count NaN in the Manual column
print(df["Auto_th_2"].isnull().sum())  

# %%
from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(df["Manual"], df["Auto_th_2"])
print(f"Slope = {slope}")

print(df)
# %%
sns.swarmplot(x='Image_set', y='Manual', data=df, hue='cell_count_index')
# %%
