import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Student_Attendance_Report.csv')
print(df.head())


total_day = df['Total Present'] + df['Total Absent']
persent = df['Total Present']
students = df['Roll No']

plt.plot(students, persent, marker='o', markersize=4)
plt.title('Line Chart of Students Attendance')
plt.xlabel("Students")
plt.ylabel('Marks')
plt.legend()
plt.tick_params(axis='x', rotation=45)


plt.tight_layout()
plt.show()




import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Student_Attendance_Report.csv')

# रोल नंबर को टेक्स्ट (String) में बदलें ताकि हर एक रोल नंबर अलग से दिखे
students = df['Roll No'].astype(str)
present_days = df['Total Present']

# सभी स्टूडेंट्स को जगह देने के लिए चार्ट की ऊँचाई (Height) बढ़ा दें 
# (अगर 50 से ज़्यादा स्टूडेंट्स हैं तो 12 को बढ़ाकर 15 या 18 कर सकते हैं)
plt.figure(figsize=(10, 12))

# plt.barh का मतलब है Horizontal Bar Chart
plt.barh(students, present_days, color='teal', edgecolor='black', label='Present Days')

plt.title('Attendance Report for All Students', fontsize=14, fontweight='bold')
plt.xlabel('Attendance Count (Days)', fontsize=12)
plt.ylabel('Students (Roll No)', fontsize=12)
plt.legend()
plt.grid(True, axis='x', linestyle=':', alpha=0.6) # केवल खड़ी ग्रिड लाइनें

plt.tight_layout()
plt.show()
