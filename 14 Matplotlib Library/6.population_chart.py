# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# initla_population = 10
# carrying_capacity = 1000
# growth_rate = 0.25
# time_steps = np.arange(0,50,1)

# population = carrying_capacity/ (1+ ((carrying_capacity - initla_population) / initla_population)* np.exp(-growth_rate * time_steps))

# df_population = pd.DataFrame({
#     'Time' : time_steps,
#     'Population' : population
# }).set_index('Time')


# plt.figure(figsize=(10,5))

# plt.plot(df_population.index, df_population['Population'], color='blue', linewidth=2.5, label='Population')

# plt.axhline(y=carrying_capacity, color='red', linestyle='--', alpha=0.7, label=f"Carrying Capacity (K = {carrying_capacity})")

# plt.grid(True, linestyle=":", alpha=0.6)
# plt.title('Population Chart')
# plt.xlabel('Time(YEAR)')
# plt.ylabel('Population')
# plt.tight_layout()
# plt.legend()
# plt.show()





import pandas as pd
df = pd.read_csv('world_population.csv')
print(df.head())