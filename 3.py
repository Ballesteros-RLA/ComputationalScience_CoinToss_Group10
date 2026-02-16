import matplotlib.pyplot as plt
import numpy as np

# Define all experiments with their complete data
experiments = {
    '1B': {
        'groups': ['G1', 'G2', 'G3', 'G5', 'G9', 'G15'],
        'heads_data': [0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,
                       0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,
                       1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,
                       0,0,0,1,1,0,1,1,0,1],
        'final': (297, 303),
        'color': '#e74c3c'
    },
    '1A': {
        'groups': ['G5', 'G8', 'G11', 'G13', 'G14'],
        'heads_data': [0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,
                       1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,
                       0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,
                       1,1,0,1,1,0,1,0,1,0],
        'final': (245, 255),
        'color': '#3498db'
    },
    '5A': {
        'groups': ['G2', 'G4', 'G7', 'G12'],
        'heads_data': [1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,
                       1,0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,
                       1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,
                       1,1,0,0,0,1,0,1,0,1],
        'final': (212, 188),
        'color': '#2ecc71'
    },
    '5B': {
        'groups': ['G4', 'G6', 'G9', 'G10', 'G12', 'G15'],
        'heads_data': [0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,
                       0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,
                       0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,
                       0,1,1,0,1,1,1,0,1,0],
        'final': (306, 294),
        'color': '#9b59b6'
    },
    '2': {
        'groups': ['G1'],
        'heads_data': [0,1,0,1,1,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,0,
                       1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,
                       1,1,0,0,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,
                       1,1,0,0,0,1,1,1,1,1],
        'final': (54, 46),
        'color': '#f39c12'
    },
    '20': {
        'groups': ['G6', 'G9', 'G14'],
        'heads_data': [0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,
                       1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,
                       1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,
                       1,1,1,1,1,1,0,1,1,1],
        'final': (142, 158),
        'color': '#1abc9c'
    },
    '10A': {
        'groups': ['G3', 'G7', 'G13'],
        'heads_data': [0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,
                       0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,
                       0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,
                       0,1,0,1,0,1,1,1,0,0],
        'final': (150, 150),
        'color': '#e67e22'
    },
    '10B': {
        'groups': ['G8', 'G10', 'G11'],
        'heads_data': [0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,
                       0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,
                       0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,
                       0,1,1,0,1,1,1,0,1,0],
        'final': (155, 145),
        'color': '#34495e'
    }
}

# Calculate cumulative data
for exp_name, exp_data in experiments.items():
    heads = exp_data['heads_data']
    tails = [1 - h for h in heads]
    cumulative_h = np.cumsum(heads)
    cumulative_t = np.cumsum(tails)
    exp_data['cumulative_h'] = cumulative_h
    exp_data['cumulative_t'] = cumulative_t

# Calculate combined totals for summary
attempts = list(range(1, 101))
all_heads_combined = [sum(exp['heads_data'][i] for exp in experiments.values()) for i in range(100)]
cumulative_all_h = np.cumsum(all_heads_combined)
cumulative_all_t = np.cumsum([8 - h for h in all_heads_combined])

# Create the figure WITHOUT the top combined graph
fig = plt.figure(figsize=(24, 14))
gs = fig.add_gridspec(3, 4, height_ratios=[1, 1, 0.8], hspace=0.35, wspace=0.3)

# Title
fig.suptitle('Complete Coin Flip Analysis: All Experiments', 
             fontsize=20, fontweight='bold', y=0.98)

# TOP & MIDDLE: 8 individual experiment graphs (2 rows x 4 columns)
positions = [(0, 0), (0, 1), (0, 2), (0, 3), 
             (1, 0), (1, 1), (1, 2), (1, 3)]

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
    groups_str = ', '.join(exp_data['groups'])
    ax.set_title(f'{exp_name}\n({groups_str})', fontsize=10, fontweight='bold')
    ax.legend(fontsize=7, loc='upper left')
    ax.grid(True, alpha=0.2)
    ax.set_xlim(0, 100)
    
    # Add final count
    final_h, final_t = exp_data['final']
    textstr = f'{final_h}H\n{final_t}T'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.7, edgecolor='black', linewidth=1)
    ax.text(0.95, 0.05, textstr, transform=ax.transAxes, fontsize=8,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=props, fontweight='bold')

# BOTTOM LEFT: Bar chart of final results
ax_bar = fig.add_subplot(gs[2, :2])
exp_names = list(experiments.keys())
heads_counts = [experiments[exp]['final'][0] for exp in exp_names]
tails_counts = [experiments[exp]['final'][1] for exp in exp_names]

x = np.arange(len(exp_names))
width = 0.35

bars1 = ax_bar.bar(x - width/2, heads_counts, width, label='Heads', 
                   color=[experiments[exp]['color'] for exp in exp_names], 
                   alpha=0.8, edgecolor='black', linewidth=1)
bars2 = ax_bar.bar(x + width/2, tails_counts, width, label='Tails', 
                   color='gray', alpha=0.6, edgecolor='black', linewidth=1)

ax_bar.axhline(y=50, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Expected (50)')
ax_bar.set_ylabel('Count', fontsize=11, fontweight='bold')
ax_bar.set_title('Final Results: All Experiments (100 flips each)', 
                 fontsize=12, fontweight='bold')
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(exp_names, fontsize=10, fontweight='bold')
ax_bar.legend(fontsize=10)
ax_bar.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax_bar.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

# BOTTOM RIGHT: Proportion convergence
ax_prop = fig.add_subplot(gs[2, 2:])

for exp_name, exp_data in experiments.items():
    proportion = exp_data['cumulative_h'] / (exp_data['cumulative_h'] + exp_data['cumulative_t'])
    ax_prop.plot(attempts, proportion, linewidth=1.5, label=exp_name, 
                 color=exp_data['color'], alpha=0.7)

# Combined proportion
prop_combined = cumulative_all_h / (cumulative_all_h + cumulative_all_t)
ax_prop.plot(attempts, prop_combined, 'black', linewidth=3, label='Combined', 
             linestyle='--', alpha=0.9)

ax_prop.axhline(y=0.5, color='red', linestyle='--', linewidth=2, label='Expected (0.5)')
ax_prop.set_xlabel('Attempt Number', fontsize=11, fontweight='bold')
ax_prop.set_ylabel('Proportion of Heads', fontsize=11, fontweight='bold')
ax_prop.set_title('Heads Proportion Convergence: All Experiments', 
                  fontsize=12, fontweight='bold')
ax_prop.legend(fontsize=8, ncol=3, loc='upper right')
ax_prop.grid(True, alpha=0.3)
ax_prop.set_xlim(0, 100)
ax_prop.set_ylim(0.3, 0.7)

plt.tight_layout()
plt.savefig('graph3.png', dpi=300, bbox_inches='tight')
print("="*90)
print("✓ SUCCESS! Graph saved as 'graph3.png'")
print("="*90)

# Print summary
total_h = cumulative_all_h[-1]
total_t = cumulative_all_t[-1]

print("\nCOMPREHENSIVE SUMMARY")
print("="*90)
for exp_name, exp_data in experiments.items():
    h, t = exp_data['final']
    print(f"{exp_name:5s} ({', '.join(exp_data['groups']):30s}): H={h:3d}, T={t:3d}")

print("\n" + "="*90)
print(f"GRAND TOTAL: Heads={total_h:4d}, Tails={total_t:4d}, Total={total_h + total_t:4d} flips")
print(f"Overall Proportion: {total_h/(total_h + total_t):.4f}")
print("="*90)

plt.show()