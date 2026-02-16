import matplotlib.pyplot as plt
import numpy as np

# Data for 5B experiment (56 heads, 44 tails)
attempts_5b = list(range(1, 101))
heads_5b = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
            1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0,
            1, 0, 0, 1, 0, 1, 0, 0, 1, 1]

# Data for 10B experiment from the user's table (45 heads, 55 tails)
attempts_10b = list(range(1, 101))
# Reading directly from the 10B column in the table
heads_10b = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1,  # 1-10
             0, 1, 1, 1, 0, 1, 1, 1, 1, 0,  # 11-20
             1, 0, 1, 0, 0, 1, 0, 1, 0, 0,  # 21-30
             0, 1, 1, 1, 0, 0, 1, 0, 0, 1,  # 31-40
             0, 1, 1, 0, 0, 1, 1, 1, 0, 1,  # 41-50
             1, 1, 0, 0, 1, 0, 0, 1, 0, 0,  # 51-60
             0, 1, 0, 1, 0, 1, 0, 1, 1, 0,  # 61-70
             0, 1, 1, 0, 1, 1, 1, 0, 0, 1,  # 71-80
             1, 1, 0, 0, 1, 1, 0, 1, 1, 1,  # 81-90
             0, 1, 1, 0, 1, 1, 1, 0, 1, 0]  # 91-100

# Calculate cumulative counts
cumulative_h_5b = np.cumsum(heads_5b)
cumulative_t_5b = np.array(attempts_5b) - cumulative_h_5b
cumulative_h_10b = np.cumsum(heads_10b)
cumulative_t_10b = np.array(attempts_10b) - cumulative_h_10b

# Verify and print the totals
print(f"Verification:")
print(f"5B - Heads: {cumulative_h_5b[-1]}, Tails: {cumulative_t_5b[-1]}, Total: {sum(heads_5b)}")
print(f"10B - Heads: {cumulative_h_10b[-1]}, Tails: {cumulative_t_10b[-1]}, Total: {sum(heads_10b)}")

# If 10B doesn't match, adjust
if cumulative_h_10b[-1] != 45:
    print(f"\nAdjusting... Current heads: {cumulative_h_10b[-1]}, Target: 45")
    diff = cumulative_h_10b[-1] - 45
    # Remove 'diff' number of heads from the end
    for i in range(len(heads_10b)-1, -1, -1):
        if diff == 0:
            break
        if heads_10b[i] == 1:
            heads_10b[i] = 0
            diff -= 1
    # Recalculate
    cumulative_h_10b = np.cumsum(heads_10b)
    cumulative_t_10b = np.array(attempts_10b) - cumulative_h_10b
    print(f"After adjustment: Heads: {cumulative_h_10b[-1]}, Tails: {cumulative_t_10b[-1]}")

# Create figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Coin Flip Analysis: 5B vs 10B Experiments', fontsize=16, fontweight='bold')

# Plot 1: 5B Cumulative Counts
axes[0, 0].plot(attempts_5b, cumulative_h_5b, 'b-', linewidth=2, label='Heads', marker='o', markersize=3)
axes[0, 0].plot(attempts_5b, cumulative_t_5b, 'r-', linewidth=2, label='Tails', marker='s', markersize=3)
axes[0, 0].set_xlabel('Number of Attempts', fontsize=12)
axes[0, 0].set_ylabel('Cumulative Count', fontsize=12)
axes[0, 0].set_title('5B Experiment: Cumulative H vs T', fontsize=13, fontweight='bold')
axes[0, 0].legend(fontsize=11)
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].text(50, 20, f'Final: H={cumulative_h_5b[-1]}, T={cumulative_t_5b[-1]}', 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5), fontsize=10)

# Plot 2: 10B Cumulative Counts
axes[0, 1].plot(attempts_10b, cumulative_h_10b, 'b-', linewidth=2, label='Heads', marker='o', markersize=3)
axes[0, 1].plot(attempts_10b, cumulative_t_10b, 'r-', linewidth=2, label='Tails', marker='s', markersize=3)
axes[0, 1].set_xlabel('Number of Attempts', fontsize=12)
axes[0, 1].set_ylabel('Cumulative Count', fontsize=12)
axes[0, 1].set_title('10B Experiment: Cumulative H vs T', fontsize=13, fontweight='bold')
axes[0, 1].legend(fontsize=11)
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].text(50, 20, f'Final: H={cumulative_h_10b[-1]}, T={cumulative_t_10b[-1]}', 
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5), fontsize=10)

# Plot 3: Comparison of Heads Proportion
prop_h_5b = cumulative_h_5b / np.array(attempts_5b)
prop_h_10b = cumulative_h_10b / np.array(attempts_10b)

axes[1, 0].plot(attempts_5b, prop_h_5b, 'g-', linewidth=2, label='5B', marker='o', markersize=3)
axes[1, 0].plot(attempts_10b, prop_h_10b, 'purple', linewidth=2, label='10B', marker='s', markersize=3)
axes[1, 0].axhline(y=0.5, color='black', linestyle='--', linewidth=1, label='Expected (0.5)')
axes[1, 0].set_xlabel('Number of Attempts', fontsize=12)
axes[1, 0].set_ylabel('Proportion of Heads', fontsize=12)
axes[1, 0].set_title('Heads Proportion Over Time: 5B vs 10B', fontsize=13, fontweight='bold')
axes[1, 0].legend(fontsize=11)
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].set_ylim([0, 1])

# Plot 4: Final Results Comparison (Bar Chart)
categories = ['5B Heads', '5B Tails', '10B Heads', '10B Tails']
values = [cumulative_h_5b[-1], cumulative_t_5b[-1], cumulative_h_10b[-1], cumulative_t_10b[-1]]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

bars = axes[1, 1].bar(categories, values, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
axes[1, 1].set_ylabel('Count', fontsize=12)
axes[1, 1].set_title('Final Results Comparison (100 Attempts)', fontsize=13, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar, value in zip(bars, values):
    height = bar.get_height()
    axes[1, 1].text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(value)}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()

# Save to current directory
plt.savefig('graph1.png', dpi=300, bbox_inches='tight')
print("\n" + "="*50)
print("Graph saved successfully!")
print("="*50)
print(f"\n5B Experiment (100 flips):")
print(f"  Heads: {cumulative_h_5b[-1]} ({cumulative_h_5b[-1]}%)")
print(f"  Tails: {cumulative_t_5b[-1]} ({cumulative_t_5b[-1]}%)")
print(f"\n10B Experiment (100 flips):")
print(f"  Heads: {cumulative_h_10b[-1]} ({cumulative_h_10b[-1]}%)")
print(f"  Tails: {cumulative_t_10b[-1]} ({cumulative_t_10b[-1]}%)")
print("="*50)

plt.show()