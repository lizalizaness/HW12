!pip install numpy
!pip install pandas

import numpy as np
import pandas as pd
income = np.array([1032, 12032, 1432, 1344, 5200, 1999, 53567, 4739, 54658, 0])
income_without_tax = income * 0.7
expenses = np.array([800, 802, 1000, 95, 1800, 1900, 980, 1000, 1200, 1300])
data = {
    'Income Without Tax': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data, index=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"])
print(df)
print("First Quarter Data:")
print(df.loc[["Jan", "Feb", "Mar"]])
