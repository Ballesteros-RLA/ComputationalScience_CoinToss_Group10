import matplotlib.pyplot as plt
import numpy as np

# Data for combined experiment - all groups flipping together
# This represents cumulative results across all groups per attempt
attempts = list(range(1, 101))

# Cumulative heads and tails for each attempt (reading from the table)
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

# Calculate total flips and percentages
total_heads = cumulative_heads[-1]
total_tails = cumulative_tails[-1]
total_flips = total_heads + total_tails
percent_heads = (total_heads / total_flips) * 100

# Calculate running percentages
percentages = [(h/(h+t))*100 for h, t in zip(cumulative_heads, cumulative_tails)]

# Calculate deviation from 50%
deviations = [h - t for h, t in zip(cumulative_heads, cumulative_tails)]

# Calculate expected 50% line
expected_heads = [(h+t)/2 for h, t in zip(cumulative_heads, cumulative_tails)]

# Create comprehensive visualization
fig = plt.figure(figsize=(20, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Plot 1: Cumulative Heads vs Tails
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(attempts, cumulative_heads, 'b-', linewidth=3, label='Cumulative Heads', alpha=0.8)
ax1.plot(attempts, cumulative_tails, 'r-', linewidth=3, label='Cumulative Tails', alpha=0.8)
ax1.plot(attempts, expected_heads, 'g--', linewidth=2, label='Expected (50%)', alpha=0.7)
ax1.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax1.set_ylabel('Cumulative Count', fontsize=12, fontweight='bold')
ax1.set_title('Combined Group Experiment: Cumulative Heads vs Tails\n(All Groups Flipping Together)', 
             fontsize=14, fontweight='bold')
ax1.legend(fontsize=11, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xlim([1, 100])

# Add text box with final stats in upper left
textstr = f'Final Results:\nHeads: {total_heads} ({percent_heads:.2f}%)\nTails: {total_tails} ({100-percent_heads:.2f}%)\nTotal: {total_flips} flips'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax1.text(0.02, 0.98, textstr, transform=ax1.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

# Add final totals label box in the center of the graph (like the uploaded image)
final_label_text = f'Final Total:\nH={total_heads}\nT={total_tails}'
bbox_props = dict(boxstyle='round,pad=0.5', facecolor='lightblue', edgecolor='black', linewidth=2, alpha=0.9)
ax1.text(50, (cumulative_heads[-1] + cumulative_tails[-1])/2, final_label_text, 
        fontsize=12, fontweight='bold', ha='center', va='center', bbox=bbox_props)

# Plot 2: Percentage of Heads Over Time
ax2 = fig.add_subplot(gs[1, 0])
ax2.plot(attempts, percentages, 'purple', linewidth=3, alpha=0.8)
ax2.axhline(y=50, color='green', linestyle='--', linewidth=2, label='Expected (50%)', alpha=0.7)
ax2.fill_between(attempts, percentages, 50, where=(np.array(percentages) >= 50), 
                 color='blue', alpha=0.2, label='Heads ahead')
ax2.fill_between(attempts, percentages, 50, where=(np.array(percentages) < 50), 
                 color='red', alpha=0.2, label='Tails ahead')
ax2.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax2.set_ylabel('Percentage of Heads', fontsize=12, fontweight='bold')
ax2.set_title('Heads Percentage Over Time', fontsize=13, fontweight='bold')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.set_xlim([1, 100])
ax2.set_ylim([45, 55])

# Plot 3: Deviation from Perfect Balance
ax3 = fig.add_subplot(gs[1, 1])
colors = ['blue' if d > 0 else 'red' for d in deviations]
ax3.bar(attempts, deviations, color=colors, alpha=0.6, edgecolor='black', linewidth=0.5)
ax3.axhline(y=0, color='black', linestyle='-', linewidth=2, label='Perfect Balance')
ax3.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax3.set_ylabel('Heads - Tails', fontsize=12, fontweight='bold')
ax3.set_title('Deviation from Perfect Balance', fontsize=13, fontweight='bold')
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3, axis='y')
ax3.set_xlim([0, 101])

# Add text for max deviation
max_dev = max(abs(d) for d in deviations)
max_dev_idx = [i for i, d in enumerate(deviations) if abs(d) == max_dev][0]
ax3.text(0.98, 0.98, f'Max deviation: ±{max_dev}\nat attempt {max_dev_idx + 1}', 
        transform=ax3.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right', bbox=props)

# Plot 4: Flips per Attempt Analysis
ax4 = fig.add_subplot(gs[2, :])
heads_per_attempt = [cumulative_heads[0]] + [cumulative_heads[i] - cumulative_heads[i-1] for i in range(1, len(cumulative_heads))]
tails_per_attempt = [cumulative_tails[0]] + [cumulative_tails[i] - cumulative_tails[i-1] for i in range(1, len(cumulative_tails))]
total_per_attempt = [h + t for h, t in zip(heads_per_attempt, tails_per_attempt)]

x = np.arange(len(attempts))
width = 0.35

bars1 = ax4.bar(x - width/2, heads_per_attempt, width, label='Heads', color='blue', alpha=0.7)
bars2 = ax4.bar(x + width/2, tails_per_attempt, width, label='Tails', color='red', alpha=0.7)

# Add a line showing total flips per attempt
ax4_twin = ax4.twinx()
ax4_twin.plot(attempts, total_per_attempt, 'g-o', linewidth=2, markersize=4, 
             label='Total Flips', alpha=0.7)
ax4_twin.set_ylabel('Total Flips per Attempt', fontsize=11, fontweight='bold', color='green')
ax4_twin.tick_params(axis='y', labelcolor='green')

ax4.set_xlabel('Attempt Number', fontsize=12, fontweight='bold')
ax4.set_ylabel('Number of Outcomes', fontsize=12, fontweight='bold')
ax4.set_title('Heads and Tails Distribution per Attempt', fontsize=13, fontweight='bold')
ax4.set_xticks([0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99])
ax4.set_xticklabels([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
ax4.legend(loc='upper left', fontsize=10)
ax4_twin.legend(loc='upper right', fontsize=10)
ax4.grid(True, alpha=0.3, axis='y')

plt.suptitle('Comprehensive Analysis: Combined Group Coin Flip Experiment\n3,100 Total Flips (31 coins × 100 attempts)', 
            fontsize=16, fontweight='bold', y=0.995)

# Save the figure
plt.savefig('graph4.png', dpi=300, bbox_inches='tight')
print("Comprehensive graph saved successfully!")

# Print detailed statistics
print("\n" + "="*80)
print("COMBINED GROUP COIN FLIP EXPERIMENT - FINAL STATISTICS")
print("="*80)
print(f"Total Flips: {total_flips:,}")
print(f"Total Heads: {total_heads:,} ({percent_heads:.3f}%)")
print(f"Total Tails: {total_tails:,} ({100-percent_heads:.3f}%)")
print(f"Difference: {abs(total_heads - total_tails)} flips")
print("="*80)

# Statistical analysis
print("\n" + "="*80)
print("STATISTICAL ANALYSIS")
print("="*80)

# Calculate expected values
expected_heads_count = total_flips / 2
expected_tails_count = total_flips / 2
deviation_from_expected = total_heads - expected_heads_count

print(f"Expected Heads: {expected_heads_count:.1f}")
print(f"Expected Tails: {expected_tails_count:.1f}")
print(f"Deviation from Expected: {deviation_from_expected:+.1f} heads")
print(f"Percentage Deviation: {(deviation_from_expected/expected_heads_count)*100:+.3f}%")

# Calculate standard deviation for binomial distribution
# For n flips with p=0.5, standard deviation = sqrt(n * p * (1-p))
std_dev = np.sqrt(total_flips * 0.5 * 0.5)
z_score = deviation_from_expected / std_dev

print(f"\nStandard Deviation (expected): {std_dev:.2f}")
print(f"Z-score: {z_score:.4f}")
print(f"Number of standard deviations from expected: {abs(z_score):.4f}")

# Interpretation
if abs(z_score) < 1.96:
    interpretation = "Within normal range (95% confidence interval)"
elif abs(z_score) < 2.58:
    interpretation = "Slightly unusual but still reasonable (99% confidence interval)"
else:
    interpretation = "Very unusual result"

print(f"Interpretation: {interpretation}")

# Attempt-by-attempt statistics
print("\n" + "="*80)
print("ATTEMPT-BY-ATTEMPT STATISTICS")
print("="*80)
print(f"Average flips per attempt: {np.mean(total_per_attempt):.2f}")
print(f"Minimum flips in an attempt: {min(total_per_attempt)}")
print(f"Maximum flips in an attempt: {max(total_per_attempt)}")
print(f"Standard deviation of flips per attempt: {np.std(total_per_attempt):.2f}")

# Find turning points
heads_lead_count = sum(1 for d in deviations if d > 0)
tails_lead_count = sum(1 for d in deviations if d < 0)
tied_count = sum(1 for d in deviations if d == 0)

print("\n" + "="*80)
print("LEAD CHANGES")
print("="*80)
print(f"Attempts where Heads led: {heads_lead_count}")
print(f"Attempts where Tails led: {tails_lead_count}")
print(f"Attempts with perfect tie: {tied_count}")

# Find longest streaks
current_streak = 0
longest_heads_streak = 0
longest_tails_streak = 0
current_leader = None

for i, d in enumerate(deviations):
    if d > 0:  # Heads leading
        if current_leader == 'heads':
            current_streak += 1
        else:
            current_leader = 'heads'
            current_streak = 1
        longest_heads_streak = max(longest_heads_streak, current_streak)
    elif d < 0:  # Tails leading
        if current_leader == 'tails':
            current_streak += 1
        else:
            current_leader = 'tails'
            current_streak = 1
        longest_tails_streak = max(longest_tails_streak, current_streak)
    else:  # Tied
        current_streak = 0
        current_leader = None

print(f"Longest streak with Heads leading: {longest_heads_streak} attempts")
print(f"Longest streak with Tails leading: {longest_tails_streak} attempts")

print("="*80)
print("\nThis experiment beautifully demonstrates the Law of Large Numbers!")
print(f"With {total_flips:,} flips, we're only {abs(deviation_from_expected):.1f} flips away from perfect 50/50.")
print(f"That's a deviation of just {abs(deviation_from_expected)/total_flips*100:.3f}%!")
print("="*80)

plt.show()