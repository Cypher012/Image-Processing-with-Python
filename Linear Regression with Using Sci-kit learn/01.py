# %%
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import os

# %%
df = pd.read_csv("./cells.csv")
print(df)
# %%

plt.ylabel('cells')
plt.xlabel("time")
sns.scatterplot(df, x='time', y="cells", color='red', markers="+")
# %%

x_df = df.drop('cells', axis="columns")
y_df = df.cells
print(y_df)
# %%
reg = LinearRegression()
reg.fit(x_df, y_df)


print(reg.score(x_df, y_df))


print(f'Predicted cells..., {reg.predict([[2.3]])}') # type:ignore
# %%
c = reg.intercept_
m = reg.coef_
calc = m * (2.3) + c
print(f'From manual calculation, cell = {calc}')
# %%
cells_predict = np.linspace(0.1, 4, 40).tolist()
cells_predict = list(map(lambda x: round(x,1), cells_predict))
print(cells_predict)
# %%
data = {
    "time": cells_predict
}

df = pd.DataFrame(data)
print(df)
# %%
predicted_cell = (reg.predict(df)).tolist()
predicted_cell = list(map(lambda x: round(x,3), predicted_cell))
# %%
df['cells'] = predicted_cell
print(df)
# %%
df.to_csv("predicted_cells.csv")
# %%
plt.ylabel("cells")
plt.xlabel("time")
sns.scatterplot(df, x='time', y='cells', color='green', markers="*")
# %%
