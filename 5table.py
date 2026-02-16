import matplotlib.pyplot as plt
import numpy as np

# Data for all trials - cumulative heads and tails
trials_data = {
    '1B': {
        'heads': [1, 3, 5, 5, 8, 10, 13, 14, 15, 15, 18, 18, 19, 20, 22, 24, 26, 29, 31, 33, 34, 37, 37, 38, 40, 40, 42, 43, 46, 46, 47, 49, 51, 53, 56, 57, 60, 62, 63, 63, 65, 67, 69, 71, 74, 77, 79, 80, 83, 84, 84, 87, 89, 91, 93, 94, 95, 97, 99, 99, 102, 103, 105, 107, 109, 111, 113, 115, 117, 119, 120, 123, 123, 125, 127, 129, 130, 132, 133, 136, 138, 138, 139, 140, 141, 142, 142, 142, 142, 143, 144, 144, 145, 146, 148, 149, 151, 152, 153, 154],
        'tails': [2, 3, 4, 7, 7, 8, 8, 10, 12, 15, 15, 18, 20, 22, 23, 24, 25, 25, 26, 27, 29, 29, 32, 34, 35, 38, 39, 41, 41, 44, 46, 47, 48, 49, 49, 51, 51, 52, 55, 57, 59, 59, 61, 61, 61, 61, 62, 64, 64, 66, 69, 69, 70, 71, 73, 74, 76, 77, 78, 81, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 93, 96, 97, 98, 99, 101, 102, 104, 104, 105, 108, 110, 112, 114, 116, 119, 122, 125, 127, 129, 132, 134, 136, 137, 139, 140, 142, 144, 146]
    },
    '1A': {
        'heads': [1, 4, 4, 7, 9, 10, 12, 13, 15, 17, 18, 19, 22, 23, 24, 27, 29, 30, 31, 34, 36, 39, 40, 42, 45, 47, 49, 51, 54, 57, 58, 59, 61, 62, 64, 65, 65, 68, 69, 69, 69, 70, 72, 73, 74, 75, 78, 81, 82, 83, 85, 87, 87, 90, 91, 92, 95, 97, 98, 99, 100, 101, 102, 105, 105, 107, 110, 112, 114, 115, 115, 117, 119, 120, 121, 123, 125, 127, 129, 129, 131, 133, 134, 136, 137, 140, 140, 143, 144, 145, 147, 149, 149, 151, 153, 154, 156, 157, 160, 161],
        'tails': [2, 2, 5, 5, 6, 8, 9, 11, 12, 13, 15, 17, 17, 19, 21, 21, 22, 24, 26, 26, 27, 27, 29, 30, 30, 31, 32, 33, 33, 33, 35, 37, 38, 40, 41, 43, 46, 46, 48, 51, 54, 56, 57, 59, 61, 63, 63, 63, 65, 67, 68, 69, 72, 72, 74, 76, 76, 77, 79, 81, 83, 85, 87, 87, 90, 91, 91, 92, 93, 95, 98, 99, 100, 102, 104, 105, 106, 107, 108, 111, 112, 113, 115, 116, 118, 118, 121, 121, 123, 125, 126, 127, 130, 131, 132, 134, 135, 137, 137, 139]
    },
    '5A': {
        'heads': [2, 4, 6, 7, 9, 11, 13, 15, 16, 19, 19, 22, 24, 25, 26, 27, 28, 29, 30, 32, 33, 36, 37, 39, 40, 42, 43, 44, 45, 47, 48, 48, 49, 50, 51, 52, 52, 54, 56, 57, 58, 59, 61, 61, 63, 64, 66, 68, 68, 70, 71, 74, 76, 78, 80, 81, 84, 87, 88, 90, 93, 95, 97, 98, 100, 102, 104, 106, 108, 110, 111, 112, 114, 117, 118, 118, 120, 121, 123, 125, 127, 130, 130, 133, 133, 135, 137, 139, 139, 140, 140, 143, 143, 145, 146, 149, 150, 153, 155, 158],
        'tails': [1, 2, 3, 5, 6, 7, 8, 9, 11, 11, 14, 14, 15, 17, 19, 21, 23, 25, 27, 28, 30, 30, 32, 33, 35, 36, 38, 40, 42, 43, 45, 48, 50, 52, 54, 56, 59, 60, 61, 63, 65, 67, 68, 71, 72, 74, 75, 76, 79, 80, 82, 82, 83, 84, 85, 87, 87, 87, 89, 90, 90, 91, 92, 94, 95, 96, 97, 98, 99, 100, 102, 104, 105, 105, 107, 110, 111, 113, 114, 115, 116, 116, 119, 119, 122, 123, 124, 125, 128, 130, 133, 133, 136, 137, 139, 139, 141, 141, 142, 142]
    },
    '5B': {
        'heads': [1, 3, 4, 5, 6, 7, 8, 9, 9, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 22, 24, 25, 26, 27, 27, 28, 29, 31, 31, 31, 31, 33, 35, 37, 37, 38, 39, 39, 40, 41, 41, 42, 43, 44, 44, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 56, 56, 58, 59, 59, 60, 62, 62, 63, 63, 65, 65, 66, 67, 68, 69, 70, 72, 73, 74, 76, 78, 79, 80, 81, 82, 83, 84, 84, 85, 86, 86, 88, 89, 91, 91, 92, 94, 95, 95, 95, 96, 96, 98, 99],
        'tails': [1, 1, 2, 3, 4, 5, 6, 7, 9, 9, 10, 11, 12, 13, 14, 14, 14, 15, 16, 18, 18, 19, 20, 21, 23, 24, 25, 25, 27, 29, 31, 31, 31, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 44, 46, 46, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 58, 58, 59, 61, 62, 62, 64, 65, 67, 67, 69, 70, 71, 72, 73, 74, 74, 75, 76, 76, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 88, 88, 89, 89, 91, 92, 92, 93, 95, 97, 97, 98, 100, 101]
    },
    '2': {
        'heads': [0, 1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7, 7, 8, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 14, 15, 15, 15, 15, 16, 16, 17, 18, 19, 19, 19, 20, 21, 22, 22, 23, 23, 23, 24, 24, 24, 25, 25, 26, 27, 28, 29, 29, 29, 29, 30, 31, 32, 32, 33, 34, 34, 34, 34, 34, 35, 35, 35, 36, 37, 38, 38, 39, 39, 40, 41, 42, 43, 43, 43, 44, 44, 44, 45, 45, 45, 45, 46, 47, 48, 49, 49, 49, 49, 50, 51, 52, 53, 54],
        'tails': [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 6, 7, 7, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 13, 14, 15, 15, 16, 16, 16, 16, 17, 18, 18, 18, 18, 19, 19, 20, 21, 21, 22, 23, 23, 24, 24, 24, 24, 24, 25, 26, 27, 27, 27, 27, 28, 28, 28, 29, 30, 31, 32, 32, 33, 34, 34, 34, 34, 35, 35, 36, 36, 36, 36, 36, 37, 38, 38, 39, 40, 40, 41, 42, 43, 43, 43, 43, 43, 44, 45, 46, 46, 46, 46, 46, 46]
    },
    '20': {
        'heads': [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 15, 15, 15, 16, 17, 17, 17, 17, 18, 19, 19, 19, 20, 21, 22, 23, 23, 23, 24, 25, 25, 25, 26, 27, 27, 27, 28, 29, 30, 30, 31, 31, 31, 31, 32, 32, 32, 33, 33, 33, 34, 34, 35, 36, 37, 37, 37, 37, 38, 39, 39, 39, 40, 41, 42, 43, 44, 45, 45, 46, 47, 48],
        'tails': [1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10, 11, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 20, 21, 22, 23, 23, 24, 24, 25, 26, 26, 26, 27, 28, 29, 29, 29, 30, 31, 31, 31, 31, 31, 32, 33, 33, 33, 34, 35, 35, 35, 36, 37, 37, 37, 37, 38, 38, 39, 40, 41, 41, 42, 43, 43, 44, 45, 45, 46, 46, 46, 46, 47, 48, 49, 49, 49, 50, 51, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52]
    },
    '10A': {
        'heads': [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 10, 11, 12, 13, 13, 14, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 26, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 51, 52, 52, 52],
        'tails': [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 9, 10, 10, 10, 11, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 15, 16, 17, 18, 19, 19, 20, 21, 22, 23, 23, 23, 23, 24, 25, 25, 25, 25, 25, 25, 25, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 34, 34, 35, 36, 37, 38, 39, 40, 40, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 46, 46, 47, 48]
    },
    '10B': {
        'heads': [0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 15, 15, 16, 17, 18, 18, 18, 19, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 25, 25, 26, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 31, 31, 32, 32, 33, 33, 34, 35, 35, 35, 36, 37, 37, 38, 39, 40, 40, 41, 42, 43, 44, 44, 44, 45, 46, 46, 47, 48, 49, 49, 50, 51, 51, 52, 53, 54, 54, 55, 56],
        'tails': [1, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 10, 10, 11, 12, 12, 13, 13, 14, 15, 16, 16, 16, 16, 17, 18, 18, 19, 20, 20, 21, 21, 21, 22, 23, 23, 23, 23, 24, 24, 24, 24, 25, 26, 26, 27, 28, 28, 29, 30, 31, 31, 32, 32, 33, 33, 34, 34, 34, 35, 36, 36, 36, 37, 37, 37, 37, 38, 38, 38, 38, 38, 39, 40, 40, 40, 41, 41, 41, 41, 42, 42, 42, 43, 43, 43, 43, 44, 44, 44]
    }
}

# Create attempts array (1 to 100)
attempts = list(range(1, 101))

# Calculate final statistics
final_stats = {}
for trial_name, data in trials_data.items():
    final_h = data['heads'][-1]
    final_t = data['tails'][-1]
    total = final_h + final_t
    percent_h = (final_h / total) * 100 if total > 0 else 0
    final_stats[trial_name] = {
        'heads': final_h,
        'tails': final_t,
        'total': total,
        'percent_heads': percent_h
    }

# Create comprehensive visualization
fig = plt.figure(figsize=(20, 14))
gs = fig.add_gridspec(4, 3, hspace=0.3, wspace=0.3)

# Plot individual trials
trial_names = list(trials_data.keys())
positions = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1)
]

for idx, trial_name in enumerate(trial_names):
    if idx < len(positions):
        row, col = positions[idx]
        ax = fig.add_subplot(gs[row, col])
        
        data = trials_data[trial_name]
        heads = data['heads']
        tails = data['tails']
        
        ax.plot(attempts, heads, 'b-', linewidth=2, label='Heads', alpha=0.7)
        ax.plot(attempts, tails, 'r-', linewidth=2, label='Tails', alpha=0.7)
        ax.plot(attempts, [i/2 for i in attempts], 'g--', linewidth=1, label='Expected (50%)', alpha=0.5)
        
        stats = final_stats[trial_name]
        ax.set_title(f'{trial_name}: {stats["heads"]}H, {stats["tails"]}T ({stats["percent_heads"]:.1f}%)', 
                    fontsize=11, fontweight='bold')
        ax.set_xlabel('Attempts', fontsize=9)
        ax.set_ylabel('Cumulative Count', fontsize=9)
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

# Combined plot - all trials heads percentage
ax_combined = fig.add_subplot(gs[2, 2])
colors = plt.cm.tab10(np.linspace(0, 1, len(trial_names)))

for idx, trial_name in enumerate(trial_names):
    data = trials_data[trial_name]
    heads = data['heads']
    tails = data['tails']
    percentages = [(h/(h+t))*100 for h, t in zip(heads, tails)]
    ax_combined.plot(attempts, percentages, linewidth=1.5, label=trial_name, alpha=0.7, color=colors[idx])

ax_combined.axhline(y=50, color='black', linestyle='--', linewidth=2, label='Expected (50%)', alpha=0.8)
ax_combined.set_xlabel('Attempts', fontsize=10)
ax_combined.set_ylabel('Heads Percentage (%)', fontsize=10)
ax_combined.set_title('All Trials: Heads Percentage Over Time', fontsize=12, fontweight='bold')
ax_combined.legend(fontsize=8, loc='best')
ax_combined.grid(True, alpha=0.3)
ax_combined.set_ylim([30, 70])

# Summary statistics plot
ax_summary = fig.add_subplot(gs[3, :])
trial_labels = list(final_stats.keys())
heads_counts = [final_stats[t]['heads'] for t in trial_labels]
tails_counts = [final_stats[t]['tails'] for t in trial_labels]
percentages = [final_stats[t]['percent_heads'] for t in trial_labels]

x = np.arange(len(trial_labels))
width = 0.35

bars1 = ax_summary.bar(x - width/2, heads_counts, width, label='Heads', color='blue', alpha=0.7)
bars2 = ax_summary.bar(x + width/2, tails_counts, width, label='Tails', color='red', alpha=0.7)

# Add percentage labels on top
for i, (h, t, p) in enumerate(zip(heads_counts, tails_counts, percentages)):
    ax_summary.text(i, max(h, t) + 2, f'{p:.1f}%', ha='center', fontsize=9, fontweight='bold')

ax_summary.set_xlabel('Trial', fontsize=11)
ax_summary.set_ylabel('Final Count', fontsize=11)
ax_summary.set_title('Final Results Summary - All Trials', fontsize=13, fontweight='bold')
ax_summary.set_xticks(x)
ax_summary.set_xticklabels(trial_labels)
ax_summary.legend(fontsize=10)
ax_summary.grid(True, alpha=0.3, axis='y')

# Add a horizontal line at 50% mark
expected_line = [stats['total']/2 for stats in final_stats.values()]
ax_summary.plot(x, expected_line, 'g--', linewidth=2, label='Expected (50%)', alpha=0.7)

plt.suptitle('TABLE - Coin Flip Analysis', fontsize=16, fontweight='bold', y=0.995)

# Save the figure
plt.savefig('graph5TABLE.png', dpi=300, bbox_inches='tight')
print("Comprehensive graph saved successfully!")

# Print detailed statistics
print("\n" + "="*80)
print("FINAL STATISTICS FOR ALL TRIALS")
print("="*80)
for trial_name in trial_names:
    stats = final_stats[trial_name]
    print(f"{trial_name:6s}: {stats['heads']:3d} Heads, {stats['tails']:3d} Tails, "
          f"Total: {stats['total']:3d}, Heads %: {stats['percent_heads']:5.1f}%")

# Calculate overall statistics
total_heads = sum(stats['heads'] for stats in final_stats.values())
total_tails = sum(stats['tails'] for stats in final_stats.values())
total_flips = total_heads + total_tails
overall_percent = (total_heads / total_flips) * 100 if total_flips > 0 else 0

print("="*80)
print(f"OVERALL: {total_heads:4d} Heads, {total_tails:4d} Tails, "
      f"Total: {total_flips:4d}, Heads %: {overall_percent:5.1f}%")
print("="*80)

plt.show()