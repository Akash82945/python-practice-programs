



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. डेटा लोड करें
df = pd.read_csv('Student_marksheet.csv')

# --- चार्ट 1: स्ट्रीम के अनुसार पास/फेल छात्र ---
# पिवट टेबल बनाएं
pass_fail_pivot = df.pivot_table(
    values='StudentID',
    index='Stream',
    columns='Result',
    aggfunc='count',
    fill_value=0
)

# सुंदर रंगों के साथ बार चार्ट प्लॉट करें
pass_fail_pivot.plot(kind='bar', stacked=True, color=['#e74c3c', '#2ecc71'], figsize=(8, 5))

plt.title('Stream-wise Pass and Fail Students Count', fontsize=14, fontweight='bold')
plt.xlabel('Streams', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.xticks(rotation=0) # टेक्स्ट को सीधा रखने के लिए
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Result')
plt.tight_layout()
plt.show() # चार्ट स्क्रीन पर देखने के लिए


# --- चार्ट 2: विषयों का औसत प्रदर्शन (Seaborn की मदद से) ---
# डेटा को ग्रुप करें
stream_avg = df.groupby('Stream')[['Maths', 'Python', 'Java']].mean().reset_index()

# डेटा को सही फॉर्मेट में बदलें (Melt करें) ताकि ग्राफ़ आसानी से बने
melted_df = pd.melt(stream_avg, id_vars=['Stream'], var_name='Subject', value_name='Average Marks')

plt.figure(figsize=(9, 5))
sns.barplot(data=melted_df, x='Stream', y='Average Marks', hue='Subject', palette='Set2')

plt.title('Average Marks by Stream and Subject', fontsize=14, fontweight='bold')
plt.xlabel('Streams', fontsize=12)
plt.ylabel('Average Marks', fontsize=12)
plt.ylim(0, 100) # y-axis की सीमा 0 से 100 तक फिक्स करने के लिए
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
