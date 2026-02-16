import matplotlib.pyplot as plt
import numpy as np

# Individual experiment data - 16 experiments total
experiments = {
    '1A': {
        'heads': [0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0],
        'color': '#e74c3c',
        'group': '1A'
    },
    '1A_2': {
        'heads': [1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0],
        'color': '#c0392b',
        'group': '1A'
    },
    '1A_3': {
        'heads': [0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,1],
        'color': '#e67e22',
        'group': '1A'
    },
    '1B': {
        'heads': [0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0],
        'color': '#3498db',
        'group': '1B'
    },
    '1B_2': {
        'heads': [1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,1],
        'color': '#2980b9',
        'group': '1B'
    },
    '1B_3': {
        'heads': [0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,0],
        'color': '#1abc9c',
        'group': '1B'
    },
    '5B': {
        'heads': [1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1],
        'color': '#2ecc71',
        'group': '5B'
    },
    '5B_2': {
        'heads': [0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0],
        'color': '#27ae60',
        'group': '5B'
    },
    '5B_3': {
        'heads': [1,1,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1],
        'color': '#16a085',
        'group': '5B'
    },
    '5B_4': {
        'heads': [0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0],
        'color': '#138d75',
        'group': '5B'
    },
    '5A': {
        'heads': [1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1],
        'color': '#9b59b6',
        'group': '5A'
    },
    '20': {
        'heads': [0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1],
        'color': '#f39c12',
        'group': '20'
    },
    '20_2': {
        'heads': [1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0],
        'color': '#d68910',
        'group': '20'
    },
    '10A': {
        'heads': [0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0],
        'color': '#16a085',
        'group': '10A'
    },
    '10B': {
        'heads': [1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1],
        'color': '#d35400',
        'group': '10B'
    },
    '10B_2': {
        'heads': [0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0],
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

# Combined cumulative data from your table
attempts = list(range(1, 101))
combined_heads = [5,16,23,31,41,49,52,64,75,82,93,104,112,118,122,131,139,148,157,166,177,187,191,198,205,214,221,231,238,245,257,264,271,280,288,295,302,311,317,323,332,344,353,365,373,382,385,391,395,406,414,421,433,442,449,457,467,476,483,488,493,499,509,515,523,531,539,544,551,558,566,574,580,588,598,606,614,621,631,637,642,649,654,665,672,680,689,692,703,708,716,723,732,737,745,751,754,762,771,779]

combined_tails = [10,21,25,31,39,47,60,64,69,78,83,88,96,106,118,125,133,140,147,154,159,165,177,186,195,202,211,217,226,235,239,248,257,264,272,281,290,297,307,317,324,328,335,339,347,354,367,377,389,394,402,411,415,422,431,439,445,452,461,472,483,493,499,509,517,525,533,544,553,562,570,578,588,596,602,610,618,627,633,643,654,663,674,679,688,696,703,716,721,732,740,749,756,767,775,785,798,806,813,821]

total_heads = combined_heads[-1]
total_tails = combined_tails[-1]
total_flips = total_heads + total_tails
percent_heads = (total_heads / total_flips) * 100

# Create comprehensive visualization with 4x4 grid for 16 experiments
fig = plt.figure(figsize=(24, 20))
gs = fig.add_gridspec(5, 4, height_ratios=[1.2, 1, 1, 1, 1], hspace=0.35, wspace=0.3)

# Title
fig.suptitle('Coin Flip Experiment: Complete Analysis of All 16 Individual Trials\n16 experiments × 100 flips = 1,600 total flips', 
             fontsize=22, fontweight='bold', y=0.98)

# TOP: Combined results
ax_top = fig.add_subplot(gs[0, :])
ax_top.plot(attempts, combined_heads, 'b-', linewidth=3, label='Total Heads', alpha=0.8)
ax_top.plot(attempts, combined_tails, 'r-', linewidth=3, label='Total Tails', alpha=0.8)
expected = [(h+t)/2 for h, t in zip(combined_heads, combined_tails)]
ax_top.plot(attempts, expected, 'g--', linewidth=2, label='Expected (50%)', alpha=0.7)

ax_top.set_xlabel('Flip Number', fontsize=13, fontweight='bold')
ax_top.set_ylabel('Cumulative Count', fontsize=13, fontweight='bold')
ax_top.set_title('ALL EXPERIMENTS COMBINED: Cumulative Results', fontsize=16, fontweight='bold', pad=12)
ax_top.legend(fontsize=12, loc='upper left')
ax_top.grid(True, alpha=0.3)
ax_top.set_xlim([0, 100])

# Add final total box
textstr = f'Final Total:\nHeads = {total_heads}\nTails = {total_tails}\n\nProportion: {percent_heads:.2f}%'
props = dict(boxstyle='round,pad=0.8', facecolor='lightblue', edgecolor='black', linewidth=2, alpha=0.9)
ax_top.text(50, (combined_heads[-1] + combined_tails[-1])/2, textstr, 
           fontsize=14, fontweight='bold', ha='center', va='center', bbox=props)

# MIDDLE/BOTTOM: Individual experiment plots (16 plots in 4 rows x 4 columns)
positions = []
for row in range(1, 5):  # rows 1-4
    for col in range(4):  # cols 0-3
        positions.append((row, col))

for idx, (exp_name, exp_data) in enumerate(experiments.items()):
    row, col = positions[idx]
    ax = fig.add_subplot(gs[row, col])
    
    # Plot lines
    ax.plot(attempts, exp_data['cumulative_h'], 
            color=exp_data['color'], linewidth=2.5, label='Heads', alpha=0.8)
    ax.plot(attempts, exp_data['cumulative_t'], 
            color='gray', linewidth=2, label='Tails', alpha=0.6)
    ax.axhline(y=50, color='black', linestyle='--', linewidth=1, alpha=0.4, label='Expected (50)')
    
    # Labels
    ax.set_xlabel('Flip #', fontsize=9)
    ax.set_ylabel('Count', fontsize=9)
    ax.set_title(f'{exp_name} (Group {exp_data["group"]})', fontsize=11, fontweight='bold')
    ax.legend(fontsize=7, loc='upper left')
    ax.grid(True, alpha=0.2)
    ax.set_xlim([0, 100])
    ax.set_ylim([0, 100])
    
    # Add final count with percentage
    h, t = exp_data["final_h"], exp_data["final_t"]
    pct_h = (h / (h + t)) * 100
    textstr = f'{h}H / {t}T\n({pct_h:.1f}%)'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8, edgecolor='black', linewidth=1)
    ax.text(0.95, 0.05, textstr, transform=ax.transAxes, fontsize=8,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=props, fontweight='bold')

plt.tight_layout()
plt.savefig('graph6TILES.png', dpi=300, bbox_inches='tight')
print("="*80)
print("✓ SUCCESS! Graph saved as 'graph6TILES.png'")
print("="*80)

# Print detailed summary
print("\n" + "="*80)
print("COIN FLIP EXPERIMENT - INDIVIDUAL TRIAL RESULTS (16 EXPERIMENTS)")
print("="*80)

# Group experiments by group name
groups = {}
for exp_name, exp_data in experiments.items():
    group = exp_data['group']
    if group not in groups:
        groups[group] = []
    groups[group].append((exp_name, exp_data))

# Print by group
for group_name in sorted(groups.keys()):
    print(f"\n--- GROUP {group_name} ---")
    for exp_name, exp_data in groups[group_name]:
        h, t = exp_data['final_h'], exp_data['final_t']
        pct = (h / (h + t)) * 100
        print(f"  {exp_name:8s}: Heads={h:2d}, Tails={t:2d}, Total={h+t:3d} flips, Proportion={pct:5.1f}%")

print("\n" + "="*80)
print(f"COMBINED TOTAL ACROSS ALL 16 EXPERIMENTS:")
print(f"  Heads = {total_heads:4d}")
print(f"  Tails = {total_tails:4d}")
print(f"  Total = {total_flips:4d} flips")
print(f"  Overall Proportion: {percent_heads:.2f}% Heads ({100-percent_heads:.2f}% Tails)")
print(f"  Difference from 50%: {abs(50-percent_heads):.2f}%")
print("="*80)

plt.show()