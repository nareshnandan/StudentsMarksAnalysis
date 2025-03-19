import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('students.csv')

print("here is the student data")
print(data)

avg_maths = np.mean(data['Maths'])
avg_science = np.mean(data['Science'])
avg_english = np.mean(data['English'])

print("\nAverage marks for each Subject")
print(f"Maths: {avg_maths}")
print(f"Science: {avg_science}")
print(f"English: {avg_english}")

data['Average'] = data[['Maths', 'Science', 'English']].mean(axis=1)

print("\nStudent data with averages:")
print(data)

plt.figure(figsize=(8, 5))
plt.bar(data['Name'], data['Average'], color='skyblue')
plt.title('Average Marks of Students')
plt.xlabel('Students Names')
plt.ylabel('Average Marks')
plt.show()