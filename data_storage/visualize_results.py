import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
data = pd.read_csv('data_storage/experiment_results.csv')

# Step 2: Calculate the value counts for the 'category' column
counts = data['category'].value_counts().reset_index()
counts.columns = ['Category', 'Count']

# Step 3: Create a professional Bar Chart using seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Count', data=counts, palette='viridis')

# Step 4: Add a title
plt.title("Attack Success Rate by Category")

# Step 5: Save the figure
plt.savefig('data_storage/attack_success_rate.png')

# Step 6: Use plt.tight_layout() to ensure nothing is clipped
plt.tight_layout()
plt.show()