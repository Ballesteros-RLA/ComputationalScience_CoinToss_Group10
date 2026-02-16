import matplotlib.pyplot as plt
import numpy as np

# Individual experiment data
experiments = {
    '1B': {
        'heads': [0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1],
        'color': '#e74c3c',
        'group': '1B'
    },
    '1B_2': {
        'heads': [0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,0],
        'color': '#c0392b',
        'group': '1B'
    },
    '1B_3': {
        'heads': [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        'color': '#e67e22',
        'group': '1B'
    },
    '1A': {
        'heads': [0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0],
        'color': '#3498db',
        'group': '1A'
    },
    '1A_2': {
        'heads': [1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1],
        'color': '#2980b9',
        'group': '1A'
    },
    '1A_3': {
        'heads': [0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,1],
        'color': '#1abc9c',
        'group': '1A'
    },
    '5A': {
        'heads': [1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1],
        'color': '#2ecc71',
        'group': '5A'
    },
    '5B': {
        'heads': [0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0],
        'color': '#9b59b6',
        'group': '5B'
    },
    '2': {
        'heads': [0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1],
        'color': '#f39c12',
        'group': '2'
    },
    '20': {
        'heads': [0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1],
        'color': '#16a085',
        'group': '20'
    },
    '10A': {
        'heads': [0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0],
        'color': '#d35400',
        'group': '10A'
    },
    '10B': {
        'heads': [0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0],
        'color': '#34495e',
        'group': '10B'
    }
}

# Calculate cumulative data for each experiment
for exp_name, exp_data in experiments.items():
    heads = exp_data['heads']
    tails = [1 - h for h in heads]
    cumulative_h = np.cumsum(heads)
    cumulative_t = np.cumsum(tails)
    exp_data['cumulative_h'] = cumulative_h
    exp_data['cumulative_t'] = cumulative_t
    exp_data['final_h'] = cumulative_h[-1]
    exp_data['final_t'] = cumulative_t[-1]

# Combined cumulative data from table
attempts = list(range(1, 101))
combined_heads = [5, 16, 23, 31, 41, 48, 58, 65, 71, 81, 88, 94, 102, 108, 116, 125, 134, 143, 150, 157,
                  167, 178, 184, 192, 201, 208, 216, 224, 233, 239, 244, 250, 259, 267, 274, 279, 285, 293, 300, 304,
                  308, 317, 327, 331, 338, 347, 359, 370, 376, 384, 392, 404, 411, 421, 428, 432, 441, 454, 460, 464,
                  474, 484, 489, 498, 504, 515, 525, 534, 544, 552, 557, 567, 575, 583, 590, 599, 608, 615, 624, 631,
                  640, 650, 655, 662, 667, 676, 679, 689, 693, 701, 706, 716, 721, 729, 736, 745, 754, 762, 773, 782]

combined_tails = [10, 14, 22, 29, 34, 42, 47, 55, 64, 69, 77, 86, 93, 102, 109, 115, 121, 127, 135, 143,
                  148, 152, 161, 168, 174, 182, 189, 196, 202, 211, 221, 230, 236, 243, 251, 261, 270, 277, 286, 296,
                  308, 313, 319, 329, 337, 343, 346, 350, 359, 366, 373, 376, 384, 389, 398, 408, 414, 416, 425, 436,
                  441, 446, 456, 462, 471, 475, 480, 486, 491, 498, 508, 513, 520, 527, 535, 541, 547, 555, 561, 569,
                  575, 580, 590, 598, 608, 614, 626, 631, 642, 649, 659, 664, 674, 681, 689, 695, 701, 708, 712, 718]

total_heads = combined_heads[-1]
total_tails = combined_tails[-1]
total_flips = total_heads + total_tails
percent_heads = (total_heads / total_flips) * 100

# Create comprehensive visualization
fig = plt.figure(figsize=(24, 16))
gs = fig.add_gridspec(4, 4, height_ratios=[1.2, 1, 1, 1], hspace=0.35, wspace=0.3)

# Title
fig.suptitle('Table Experiment: Complete Analysis of All Individual Trials\n15 coins × 100 attempts = 1,500 total flips', 
             fontsize=20, fontweight='bold', y=0.98)

# TOP: Combined results
ax_top = fig.add_subplot(gs[0, :])
ax_top.plot(attempts, combined_heads, 'b-', linewidth=3, label='Total Heads', alpha=0.8)
ax_top.plot(attempts, combined_tails, 'r-', linewidth=3, label='Total Tails', alpha=0.8)
expected = [(h+t)/2 for h, t in zip(combined_heads, combined_tails)]
ax_top.plot(attempts, expected, 'g--', linewidth=2, label='Expected (50%)', alpha=0.7)

ax_top.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax_top.set_ylabel('Cumulative Count', fontsize=12, fontweight='bold')
ax_top.set_title('ALL EXPERIMENTS COMBINED: Cumulative Results', fontsize=14, fontweight='bold', pad=10)
ax_top.legend(fontsize=11, loc='upper left')
ax_top.grid(True, alpha=0.3)
ax_top.set_xlim([0, 100])

# Add final total box
textstr = f'Final Total:\nH={total_heads}\nT={total_tails}'
props = dict(boxstyle='round,pad=0.6', facecolor='lightblue', edgecolor='black', linewidth=2, alpha=0.9)
ax_top.text(50, (combined_heads[-1] + combined_tails[-1])/2, textstr, 
           fontsize=13, fontweight='bold', ha='center', va='center', bbox=props)

# MIDDLE: Individual experiment plots (12 plots in 3 rows x 4 columns)
positions = [(1, 0), (1, 1), (1, 2), (1, 3),
             (2, 0), (2, 1), (2, 2), (2, 3),
             (3, 0), (3, 1), (3, 2), (3, 3)]

for idx, (exp_name, exp_data) in enumerate(experiments.items()):
    row, col = positions[idx]
    ax = fig.add_subplot(gs[row, col])
    
    # Plot lines
    ax.plot(attempts, exp_data['cumulative_h'], 
            color=exp_data['color'], linewidth=2, label='Heads', alpha=0.8)
    ax.plot(attempts, exp_data['cumulative_t'], 
            color='gray', linewidth=2, label='Tails', alpha=0.6)
    ax.axhline(y=50, color='black', linestyle='--', linewidth=1, alpha=0.4)
    
    # Labels
    ax.set_xlabel('Attempts', fontsize=9)
    ax.set_ylabel('Count', fontsize=9)
    ax.set_title(f'{exp_name} ({exp_data["group"]})', fontsize=10, fontweight='bold')
    ax.legend(fontsize=7, loc='upper left')
    ax.grid(True, alpha=0.2)
    ax.set_xlim([0, 100])
    
    # Add final count
    textstr = f'{exp_data["final_h"]}H\n{exp_data["final_t"]}T'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.7, edgecolor='black', linewidth=1)
    ax.text(0.95, 0.05, textstr, transform=ax.transAxes, fontsize=8,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=props, fontweight='bold')

plt.tight_layout()
plt.savefig('graph6TABLE.png', dpi=300, bbox_inches='tight')
print("="*80)
print("✓ SUCCESS! Graph saved as 'graph6TABLE.png'")
print("="*80)

# Print summary
print("\n" + "="*80)
print("TABLE EXPERIMENT - INDIVIDUAL TRIAL RESULTS")
print("="*80)
for exp_name, exp_data in experiments.items():
    h, t = exp_data['final_h'], exp_data['final_t']
    pct = (h / (h + t)) * 100
    print(f"{exp_name:8s} ({exp_data['group']:3s}): H={h:2d}, T={t:2d}, Total={h+t:3d}, Heads={pct:5.1f}%")

print("\n" + "="*80)
print(f"COMBINED TOTAL: Heads={total_heads:4d}, Tails={total_tails:4d}, Total={total_flips:4d} flips")
print(f"Overall Proportion: {percent_heads:.3f}% Heads")
print("="*80)

plt.show()