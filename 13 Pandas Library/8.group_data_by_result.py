import pandas as pd

df = pd.read_csv('Student_marksheet.csv')
# print(df.info())

# Group data by result

# result_category = df.groupby('Result')['StudentID'].count()
# print(result_category)



# Pivot table according subject wise average marks
# pivot_table = df.pivot_table(
#     values= ['Maths', 'English', 'C lang', 'Python', 'Java', 'Percentage'],
#     index= 'Stream',
#     aggfunc= 'mean',
# ).round(2)

# pivot_table['Grade'] = pivot_table.sum(axis=1)
# print(pivot_table.reset_index())





# Pivot tabel according stream or result
pass_fail_pivot = df.pivot_table(
    values= 'StudentID',
    index= 'Stream',
    columns= 'Result',
    aggfunc= 'count',
    fill_value= 0
)

pass_fail_pivot['Total Student'] = pass_fail_pivot.sum(axis = 1)
print(pass_fail_pivot.reset_index())

# Pandas


