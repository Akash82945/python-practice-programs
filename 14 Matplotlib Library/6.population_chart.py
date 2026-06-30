# # import pandas as pd
# # import numpy as np
# # import matplotlib.pyplot as plt

# ## This code is for machine learning

# # initla_population = 10
# # carrying_capacity = 1000
# # growth_rate = 0.25
# # time_steps = np.arange(0,50,1)

# # population = carrying_capacity/ (1+ ((carrying_capacity - initla_population) / initla_population)* np.exp(-growth_rate * time_steps))

# # df_population = pd.DataFrame({
# #     'Time' : time_steps,
# #     'Population' : population
# # }).set_index('Time')


# # plt.figure(figsize=(10,5))

# # plt.plot(df_population.index, df_population['Population'], color='blue', linewidth=2.5, label='Population')

# # plt.axhline(y=carrying_capacity, color='red', linestyle='--', alpha=0.7, label=f"Carrying Capacity (K = {carrying_capacity})")

# # plt.grid(True, linestyle=":", alpha=0.6)
# # plt.title('Population Chart')
# # plt.xlabel('Time(YEAR)')
# # plt.ylabel('Population')
# # plt.tight_layout()
# # plt.legend()
# # plt.show()




# import kagglehub
# import pandas as pd
# import matplotlib.pyplot as plt
# import os


# # Download latest version
# path = kagglehub.dataset_download("muhammedtausif/world-population-by-countries")

# print("Path to dataset files:", path)

# files = [f for f in os.listdir(path) if f.endswith('.csv')]
# csv_path = os.path.join(path, files[0])

# df = pd.read_csv(csv_path, encoding= 'latin1')

# df.columns = df.columns.str.strip()

# country_col = [col for col in df.columns if 'Country' in col][0]

# pop_col = [col for col in df.columns if 'Population' in col or 'Pop' in col][0]

# print(f"{country_col} , {pop_col}")

# df[pop_col] = 






# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

## This code is for machine learning

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

import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. डेटासेट डाउनलोड करना
path = kagglehub.dataset_download("muhammedtausif/world-population-by-countries")
print("Path to dataset files:", path)

# 2. CSV फाइल का रास्ता निकालना
files = [f for f in os.listdir(path) if f.endswith('.csv')]
csv_path = os.path.join(path, files[0])

# 3. डेटा लोड करना (latin1 एन्कोडिंग के साथ)
df = pd.read_csv(csv_path, encoding='latin1')
df.columns = df.columns.str.strip()  # कॉलम नामों से एक्स्ट्रा स्पेस हटाना

# 4. सही कॉलम नाम खुद ढूंढना (Dynamic Detection)
country_col = [col for col in df.columns if 'Country' in col][0]
# नाम में 'Population' शब्द वाला पहला कॉलम ढूंढें (जैसे Population 2024)
pop_col = [col for col in df.columns if 'Population' in col or 'Pop' in col][0]

print(f"\nचार्ट के लिए इस्तेमाल हो रहे कॉलम्स: Country -> '{country_col}', Population -> '{pop_col}'")

# 5. पापुलेशन कॉलम को नंबर (Float/Int) में बदलना (अगर उसमें कॉमा ',' या स्ट्रिंग हो तो)
df[pop_col] = pd.to_numeric(df[pop_col].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')
df = df.dropna(subset=[pop_col])

# 6. डेटा को सॉर्ट करके टॉप 10 सबसे ज्यादा आबादी वाले देश निकालना
df_sorted = df.sort_values(by=pop_col, ascending=False).head(10)

# 7. मैटप्लोटलिब से बार चार्ट प्लॉट करना
plt.figure(figsize=(12, 6))

# वैल्यूज को बिलियंस (Billions) में बदलना ताकि y-axis पर बड़ी संख्याएं (00000...) न दिखें
y_values = df_sorted[pop_col] / 1e9

plt.bar(df_sorted[country_col], y_values, color='dodgerblue', edgecolor='black', alpha=0.8)

# 8. ग्राफ की सजावट और लेबल्स
plt.title(f"Top 10 Most Populated Countries ({pop_col})", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Country", fontsize=12, labelpad=10)
plt.ylabel("Population (in Billions)", fontsize=12, labelpad=10)
plt.xticks(rotation=45, ha='right')  # देश के नामों को 45 डिग्री घुमाना ताकि साफ पढ़ें जा सकें
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 9. ग्राफ स्क्रीन पर दिखाना
plt.tight_layout()
plt.show()
