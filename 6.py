import matplotlib.pyplot as plt
import numpy as np

# Combined data from all groups flipping together
attempts = list(range(1, 101))

# Cumulative heads and tails for each attempt (from the table)
cumulative_heads = [12, 28, 46, 64, 82, 97, 111, 129, 146, 162, 179, 195, 212, 224, 237, 255, 271, 289, 304, 320,
                    340, 361, 371, 386, 403, 419, 435, 452, 468, 482, 498, 512, 528, 544, 559, 572, 585, 602, 615, 625,
                    638, 659, 678, 693, 708, 725, 740, 757, 767, 786, 803, 821, 839, 859, 873, 885, 904, 926, 940, 949,
                    965, 980, 994, 1009, 1023, 1042, 1059, 1073, 1089, 1105, 1117, 1136, 1150, 1167, 1184, 1200, 1218, 1232, 1251, 1264,
                    1278, 1295, 1306, 1324, 1337, 1355, 1368, 1381, 1396, 1409, 1422, 1440, 1453, 1466, 1480, 1495, 1507, 1524, 1543, 1561]

cumulative_tails = [19, 34, 47, 60, 73, 89, 106, 119, 133, 148, 162, 177, 191, 210, 228, 241, 256, 269, 285, 300,
                    311, 321, 342, 358, 372, 387, 402, 416, 431, 448, 463, 480, 495, 510, 526, 544, 562, 576, 595, 615,
                    634, 643, 656, 671, 687, 701, 717, 731, 752, 764, 778, 791, 804, 815, 833, 851, 863, 872, 889, 911,
                    926, 942, 959, 975, 992, 1004, 1018, 1035, 1050, 1065, 1084, 1096, 1113, 1127, 1141, 1156, 1169, 1186, 1198, 1216,
                    1233, 1247, 1267, 1280, 1298, 1311, 1329, 1347, 1363, 1381, 1399, 1412, 1430, 1448, 1465, 1481, 1500, 1514, 1526, 1539]

# Group information for reference
groups_info = {
    '1B': ['G1', 'G2', 'G3', 'G5', 'G9', 'G15'],
    '1A': ['G5', 'G8', 'G11', 'G13', 'G14'],
    '5A': ['G2', 'G4', 'G7', 'G12'],
    '5B': ['G4', 'G6', 'G9', 'G10', 'G12', 'G15'],
    '2': ['G1'],
    '20': ['G6', 'G9', 'G14'],
    '10A': ['G3', 'G7', 'G13'],
    '10B': ['G8', 'G10', 'G11']
}

# Calculate statistics
total_heads = cumulative_heads[-1]
total_tails = cumulative_tails[-1]
total_flips = total_heads + total_tails
percent_heads = (total_heads / total_flips) * 100

# Calculate per-attempt data
heads_per_attempt = [cumulative_heads[0]] + [cumulative_heads[i] - cumulative_heads[i-1] for i in range(1, len(cumulative_heads))]
tails_per_attempt = [cumulative_tails[0]] + [cumulative_tails[i] - cumulative_tails[i-1] for i in range(1, len(cumulative_tails))]
total_per_attempt = [h + t for h, t in zip(heads_per_attempt, tails_per_attempt)]

# Calculate percentages
percentages = [(h/(h+t))*100 for h, t in zip(cumulative_heads, cumulative_tails)]

# Calculate deviation
deviations = [h - t for h, t in zip(cumulative_heads, cumulative_tails)]

# Calculate expected 50% line
expected_heads = [(h+t)/2 for h, t in zip(cumulative_heads, cumulative_tails)]

# Create comprehensive visualization
fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(3, 2, height_ratios=[1.2, 1, 1], hspace=0.35, wspace=0.3)

# Title
fig.suptitle('Table and Tiles Combined Experiment: Complete Analysis\nAll Groups (31 coins × 100 attempts = 3,100 total flips)', 
             fontsize=18, fontweight='bold', y=0.98)

# Plot 1: Main cumulative graph with label box
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(attempts, cumulative_heads, 'b-', linewidth=3, label='Total Heads', alpha=0.8)
ax1.plot(attempts, cumulative_tails, 'r-', linewidth=3, label='Total Tails', alpha=0.8)
ax1.plot(attempts, expected_heads, 'g--', linewidth=2, label='Expected (50%)', alpha=0.7)

ax1.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax1.set_ylabel('Cumulative Count', fontsize=12, fontweight='bold')
ax1.set_title('Cumulative Results: All Groups Combined Over 100 Attempts', 
             fontsize=14, fontweight='bold', pad=10)
ax1.legend(fontsize=11, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xlim([0, 100])

# Add final total label box in center
textstr = f'Final Total:\nH={total_heads}\nT={total_tails}'
props = dict(boxstyle='round,pad=0.6', facecolor='lightblue', edgecolor='black', linewidth=2, alpha=0.9)
ax1.text(50, (cumulative_heads[-1] + cumulative_tails[-1])/2, textstr, 
        fontsize=13, fontweight='bold', ha='center', va='center', bbox=props)

# Add corner info box
corner_text = f'Groups: 1B, 1A, 5A, 5B, 2, 20, 10A, 10B\nTotal: {total_flips:,} flips\nHeads: {percent_heads:.2f}%'
corner_props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax1.text(0.02, 0.98, corner_text, transform=ax1.transAxes, fontsize=10,
        verticalalignment='top', bbox=corner_props)

# Plot 2: Percentage over time
ax2 = fig.add_subplot(gs[1, 0])
ax2.plot(attempts, percentages, 'purple', linewidth=3, alpha=0.8)
ax2.axhline(y=50, color='green', linestyle='--', linewidth=2, label='Expected (50%)', alpha=0.7)
ax2.fill_between(attempts, percentages, 50, where=(np.array(percentages) >= 50), 
                 color='blue', alpha=0.2, label='Heads ahead')
ax2.fill_between(attempts, percentages, 50, where=(np.array(percentages) < 50), 
                 color='red', alpha=0.2, label='Tails ahead')
ax2.set_xlabel('Attempt Number', fontsize=11, fontweight='bold')
ax2.set_ylabel('Percentage of Heads', fontsize=11, fontweight='bold')
ax2.set_title('Heads Percentage Convergence', fontsize=12, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_xlim([0, 100])
ax2.set_ylim([38, 62])

# Plot 3: Deviation from balance
ax3 = fig.add_subplot(gs[1, 1])
colors = ['blue' if d > 0 else 'red' for d in deviations]
ax3.bar(attempts, deviations, color=colors, alpha=0.6, edgecolor='black', linewidth=0.3)
ax3.axhline(y=0, color='black', linestyle='-', linewidth=2, label='Perfect Balance')
ax3.set_xlabel('Attempt Number', fontsize=11, fontweight='bold')
ax3.set_ylabel('Heads - Tails', fontsize=11, fontweight='bold')
ax3.set_title('Deviation from Perfect Balance', fontsize=12, fontweight='bold')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3, axis='y')
ax3.set_xlim([0, 101])

# Add max deviation info
max_dev = max(abs(d) for d in deviations)
max_dev_idx = [i for i, d in enumerate(deviations) if abs(d) == max_dev][0]
textstr = f'Max deviation: {max_dev}\nat attempt {max_dev_idx + 1}'
props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
ax3.text(0.98, 0.98, textstr, transform=ax3.transAxes, fontsize=9,
        verticalalignment='top', horizontalalignment='right', bbox=props, fontweight='bold')

# Plot 4: Flips per attempt
ax4 = fig.add_subplot(gs[2, 0])
x = np.arange(len(attempts))
width = 0.35

bars1 = ax4.bar(x - width/2, heads_per_attempt, width, label='Heads', color='blue', alpha=0.7)
bars2 = ax4.bar(x + width/2, tails_per_attempt, width, label='Tails', color='red', alpha=0.7)

ax4.set_xlabel('Attempt Number', fontsize=11, fontweight='bold')
ax4.set_ylabel('Number of Outcomes', fontsize=11, fontweight='bold')
ax4.set_title('Heads vs Tails Distribution per Attempt', fontsize=12, fontweight='bold')
ax4.set_xticks([0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99])
ax4.set_xticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax4.legend(fontsize=10)
ax4.grid(True, alpha=0.3, axis='y')

# Plot 5: Statistical summary
ax5 = fig.add_subplot(gs[2, 1])
ax5.axis('off')

# Statistical analysis
expected_heads_count = total_flips / 2
deviation_from_expected = total_heads - expected_heads_count
std_dev = np.sqrt(total_flips * 0.5 * 0.5)
z_score = deviation_from_expected / std_dev

# Create text summary
summary_text = f"""
STATISTICAL SUMMARY
{'='*45}

Total Flips: {total_flips:,}
Total Heads: {total_heads:,} ({percent_heads:.3f}%)
Total Tails: {total_tails:,} ({100-percent_heads:.3f}%)
Difference: {abs(total_heads - total_tails)} flips

EXPECTED VALUES
Expected Heads/Tails: {expected_heads_count:.1f} each
Deviation: {deviation_from_expected:+.1f} heads
Percentage Deviation: {(deviation_from_expected/expected_heads_count)*100:+.3f}%

STATISTICAL MEASURES
Standard Deviation: {std_dev:.2f}
Z-score: {z_score:.4f}
Sigma Distance: {abs(z_score):.4f}σ

INTERPRETATION
Status: {"✓ Within normal range" if abs(z_score) < 1.96 else "Unusual result"}
Confidence: 95% interval

GROUPS INVOLVED
1B: G1, G2, G3, G5, G9, G15 (6 coins)
1A: G5, G8, G11, G13, G14 (5 coins)
5A: G2, G4, G7, G12 (4 coins)
5B: G4, G6, G9, G10, G12, G15 (6 coins)
2: G1 (1 coin)
20: G6, G9, G14 (3 coins)
10A: G3, G7, G13 (3 coins)
10B: G8, G10, G11 (3 coins)
Total: 31 coins per attempt
"""

ax5.text(0.1, 0.95, summary_text, transform=ax5.transAxes, fontsize=9,
        verticalalignment='top', family='monospace',
        bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))

plt.tight_layout()
plt.savefig('graph6.png', dpi=300, bbox_inches='tight')
print("="*80)
print("✓ SUCCESS! Graph saved as 'graph6.png'")
print("="*80)

# Print detailed statistics
print("\n" + "="*80)
print("TABLE AND TILES COMBINED EXPERIMENT - FINAL STATISTICS")
print("="*80)
print(f"Total Flips: {total_flips:,}")
print(f"Total Heads: {total_heads:,} ({percent_heads:.3f}%)")
print(f"Total Tails: {total_tails:,} ({100-percent_heads:.3f}%)")
print(f"Difference: {abs(total_heads - total_tails)} flips")
print("="*80)

print("\n" + "="*80)
print("STATISTICAL ANALYSIS")
print("="*80)
print(f"Expected Heads: {expected_heads_count:.1f}")
print(f"Expected Tails: {expected_heads_count:.1f}")
print(f"Deviation from Expected: {deviation_from_expected:+.1f} heads")
print(f"Percentage Deviation: {(deviation_from_expected/expected_heads_count)*100:+.3f}%")
print(f"\nStandard Deviation (expected): {std_dev:.2f}")
print(f"Z-score: {z_score:.4f}")
print(f"Number of standard deviations from expected: {abs(z_score):.4f}σ")

if abs(z_score) < 1.96:
    interpretation = "✓ Within normal range (95% confidence interval)"
elif abs(z_score) < 2.58:
    interpretation = "Slightly unusual but still reasonable (99% confidence interval)"
else:
    interpretation = "Very unusual result"

print(f"Interpretation: {interpretation}")

print("\n" + "="*80)
print("ATTEMPT-BY-ATTEMPT STATISTICS")
print("="*80)
print(f"Average coins flipped per attempt: {np.mean(total_per_attempt):.2f}")
print(f"Minimum flips in an attempt: {min(total_per_attempt)}")
print(f"Maximum flips in an attempt: {max(total_per_attempt)}")
print(f"Standard deviation of flips per attempt: {np.std(total_per_attempt):.2f}")

print("\n" + "="*80)
print("GROUPS PARTICIPATING")
print("="*80)
for exp_name, groups in groups_info.items():
    print(f"{exp_name:5s}: {', '.join(groups):30s} ({len(groups)} coins)")

print("\n" + "="*80)
print("CONCLUSION")
print("="*80)
print(f"With {total_flips:,} flips, we achieved {percent_heads:.3f}% heads.")
print(f"This is only {abs(deviation_from_expected):.1f} flips away from perfect 50/50!")
print(f"Deviation of just {abs(deviation_from_expected)/total_flips*100:.3f}% demonstrates")
print("the Law of Large Numbers beautifully! 🎲")
print("="*80)

plt.show()