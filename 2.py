import matplotlib.pyplot as plt

# Data from the table
data = {
    'No. of Attempts': list(range(1, 101)),
    '5B_H': [1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,0,1,1],
    '10B_H': [0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0],
    '5B_T': [0,0,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,0],
    '10B_T': [1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1]
}

# Calculate cumulative sums for 5B experiment
cumulative_5b_h = []
cumulative_5b_t = []
h_sum_5b = 0
t_sum_5b = 0

for i in range(100):
    h_sum_5b += data['5B_H'][i]
    t_sum_5b += data['5B_T'][i]
    cumulative_5b_h.append(h_sum_5b)
    cumulative_5b_t.append(t_sum_5b)

# Calculate cumulative sums for 10B experiment
cumulative_10b_h = []
cumulative_10b_t = []
h_sum_10b = 0
t_sum_10b = 0

for i in range(100):
    h_sum_10b += data['10B_H'][i]
    t_sum_10b += data['10B_T'][i]
    cumulative_10b_h.append(h_sum_10b)
    cumulative_10b_t.append(t_sum_10b)

# Calculate combined cumulative sums (5B + 10B)
cumulative_combined_h = []
cumulative_combined_t = []

for i in range(100):
    cumulative_combined_h.append(cumulative_5b_h[i] + cumulative_10b_h[i])
    cumulative_combined_t.append(cumulative_5b_t[i] + cumulative_10b_t[i])

# Create single plot
plt.figure(figsize=(10, 6))
plt.plot(data['No. of Attempts'], cumulative_combined_h, color='#4472C4', linewidth=2.5, label='Heads')
plt.plot(data['No. of Attempts'], cumulative_combined_t, color='#ED7D31', linewidth=2.5, label='Tails')

plt.title('Coin Flip Analysis: 5B vs 10B Experiments', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Number of Attempts', fontsize=10)
plt.ylabel('Cumulative Count', fontsize=10)
plt.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
plt.legend(loc='upper left', fontsize=10)
plt.xlim(0, 100)
plt.ylim(0, 120)

# Add final count annotation
plt.text(70, 25, f'Final: H={cumulative_combined_h[-1]}, T={cumulative_combined_t[-1]}', 
         fontsize=9, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('graph2.png', dpi=300, bbox_inches='tight')
plt.show()

print("Combined (5B + 10B) - Final counts:")
print(f"  Heads: {cumulative_combined_h[-1]}")
print(f"  Tails: {cumulative_combined_t[-1]}")
print("\nGraph saved successfully!")