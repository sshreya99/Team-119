import matplotlib.pyplot as plt
import seaborn as sns

# set figure size for better readability
plt.figure(figsize=(16, 8))

# Pie chart for inability to find specialists
plt.subplot(1, 2, 2)
wedges, texts, autotexts = plt.pie(percentages, labels=issues, autopct='%1.1f%%', 
                                   startangle=90, colors=colors_issues, 
                                   wedgeprops=dict(width=0.6, edgecolor='white'))

# Customize the appearance
plt.title('Patient Issues in Finding Specialists', fontsize=16, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=12)

# Add a circle at the center to create a donut chart effect
centre_circle = plt.Circle((0,0), 0.3, fc='white')
plt.gca().add_artist(centre_circle)

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
