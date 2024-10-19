import matplotlib.pyplot as plt
import seaborn as sns

# Set figure size for better readability
plt.figure(figsize=(16, 8))

# Pie chart for wait times in days
plt.subplot(1, 2, 1)
wedges, texts = plt.pie(wait_times, labels=specialties, 
                        startangle=90, colors=colors_specialties, 
                        wedgeprops=dict(width=0.6, edgecolor='white'))

# Add text labels for wait times inside the pie slices
for i, p in enumerate(wedges):
    x, y = p.center
    theta = (p.theta2 - p.theta1) / 2. + p.theta1
    x = np.cos(np.deg2rad(theta))
    y = np.sin(np.deg2rad(theta))
    plt.text(x*0.6, y*0.6, f'{wait_times[i]:.1f} days', ha='center', va='center', color='white', fontsize=10, weight='bold')

plt.title('Distribution of Average Wait Times by Specialty (in Days)', fontsize=16, fontweight='bold', pad=20)
plt.setp(texts, size=12)

# Add a circle at the center to create a donut chart effect
centre_circle = plt.Circle((0,0), 0.3, fc='white')
plt.gca().add_artist(centre_circle)

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
