import matplotlib.pyplot as plt
import pandas as pd


# df = pd.read_csv('Sales.csv')


# 1. Line Plot
plt.plot([12,13,14],[32,43,54])
plt.show()


# 2. Bar Plot
plt.bar(['A','B'],[20,34])
plt.show()


# 3. Pie chart
plt.pie([30,30,40])
plt.show()


# 4. Title
plt.title('Sales Data')


# 5. Labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')


# 6. Grid
plt.grid(True)



# 7. Scatter plot 
a = [1,2,3] 
b = [12,13,141]
plt.scatter(a,b)
plt.title('Scatter Plot')
plt.legend()
plt.xlabel(a)
plt.ylabel(b)
plt.grid(True)
plt.show()



# 9. Multiple lines
plt.plot([1,2,3],[10,20,30])
plt.plot([1,2,3],[30,20,10])
plt.title('Multiple lines')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.savefig('Chart.png')
plt.show()


# Save plot as PNG