import pandas as pd

df = pd.read_csv('Student_marksheet.csv')
# print(df.info())

# Group data by result

# result_category = df.groupby('Result')['StudentID'].count()
# print(result_category)


pivot_table = df.pivot_table(
    values= ['Maths', 'English', 'C lang', 'Python', 'Java', 'Percentage'],
    index= 'Stream',
    aggfunc= 'mean',
).round(2)

pivot_table['Grade'] = pivot_table.sum(axis=1)
print(pivot_table.reset_index())