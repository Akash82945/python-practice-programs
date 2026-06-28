import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Sales.csv')
print(df.head())

pay_mode = df['Payment Mode'].value_counts()

plt.pie(pay_mode.values, labels= pay_mode.index, autopct='%1.1f%%', startangle=90)
plt.title("Expense pie chart")
plt.tight_layout()
plt.show()


