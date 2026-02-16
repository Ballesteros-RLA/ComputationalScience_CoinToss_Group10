import matplotlib.pyplot as plt
import numpy as np

# Data for all tiles trials - cumulative heads and tails
tiles_data = {
    '1A': {
        'heads': [2, 3, 5, 7, 9, 11, 13, 15, 17, 20, 23, 25, 26, 27, 28, 29, 31, 32, 34, 35, 36, 39, 41, 43, 45, 48, 50, 51, 53, 53, 56, 56, 56, 58, 59, 59, 60, 62, 63, 64, 66, 68, 69, 71, 73, 74, 75, 76, 76, 77, 78, 79, 82, 82, 82, 84, 85, 86, 87, 89, 90, 92, 94, 96, 98, 99, 100, 101, 103, 104, 107, 108, 110, 110, 111, 113, 113, 114, 115, 116, 116, 116, 117, 120, 121, 121, 122, 122, 124, 125, 126, 127, 129, 130, 131, 131, 131, 132, 134, 134],
        'tails': [1, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 13, 15, 17, 19, 20, 22, 23, 25, 27, 27, 28, 29, 30, 30, 31, 33, 34, 37, 37, 40, 43, 44, 46, 49, 51, 52, 54, 56, 57, 58, 60, 61, 62, 64, 66, 68, 71, 73, 75, 77, 77, 80, 83, 84, 86, 88, 90, 91, 93, 94, 95, 96, 97, 99, 101, 103, 104, 106, 106, 108, 109, 112, 114, 115, 118, 120, 122, 124, 127, 130, 132, 132, 134, 137, 139, 142, 143, 145, 147, 149, 150, 152, 154, 157, 160, 162, 163, 166]
    },
    '1B': {
        'heads': [0, 0, 2, 4, 5, 6, 6, 7, 9, 10, 11, 13, 15, 17, 17, 17, 17, 19, 21, 23, 24, 26, 26, 26, 27, 28, 29, 29, 29, 31, 32, 34, 35, 37, 38, 38, 38, 39, 40, 42, 43, 44, 45, 46, 47, 49, 49, 49, 49, 50, 52, 54, 54, 56, 57, 58, 60, 62, 63, 63, 63, 63, 65, 67, 68, 69, 70, 70, 71, 72, 73, 74, 74, 75, 76, 77, 78, 80, 82, 82, 82, 83, 83, 85, 86, 88, 89, 89, 91, 91, 92, 94, 95, 95, 96, 96, 96, 98, 99, 100],
        'tails': [2, 4, 4, 4, 5, 6, 8, 9, 9, 10, 11, 11, 11, 11, 13, 15, 17, 17, 17, 17, 18, 18, 20, 22, 23, 24, 25, 27, 29, 29, 30, 30, 31, 31, 32, 34, 36, 37, 38, 38, 39, 40, 41, 42, 43, 43, 45, 47, 49, 50, 50, 50, 52, 52, 53, 54, 54, 54, 55, 57, 59, 61, 61, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76, 76, 76, 78, 80, 81, 83, 83, 84, 84, 85, 87, 87, 89, 90, 90, 91, 93, 94, 96, 98, 98, 99, 100]
    },
    '5B': {
        'heads': [3, 5, 9, 11, 13, 14, 15, 18, 21, 22, 25, 27, 29, 29, 30, 33, 35, 39, 41, 43, 46, 47, 49, 52, 53, 54, 56, 58, 58, 61, 65, 67, 70, 72, 75, 77, 79, 82, 83, 84, 85, 89, 93, 96, 100, 101, 101, 103, 105, 109, 110, 112, 115, 119, 121, 122, 125, 127, 129, 130, 131, 132, 134, 134, 136, 140, 142, 144, 144, 146, 147, 151, 151, 154, 156, 159, 162, 163, 166, 169, 170, 173, 175, 178, 179, 182, 185, 187, 190, 190, 193, 194, 194, 195, 197, 199, 200, 201, 203, 207],
        'tails': [1, 3, 3, 5, 7, 10, 13, 14, 15, 18, 19, 21, 23, 27, 30, 31, 33, 33, 35, 37, 38, 41, 43, 44, 47, 50, 52, 54, 58, 59, 59, 61, 62, 64, 65, 67, 69, 70, 73, 76, 79, 79, 79, 80, 80, 83, 87, 89, 91, 91, 94, 96, 97, 97, 99, 102, 103, 105, 107, 110, 113, 116, 118, 122, 124, 124, 126, 128, 132, 134, 137, 137, 141, 142, 144, 145, 146, 149, 150, 151, 154, 155, 157, 158, 161, 162, 163, 165, 166, 170, 171, 174, 178, 181, 183, 185, 188, 191, 193, 193]
    },
    '5A': {
        'heads': [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 11, 11, 11, 12, 12, 13, 14, 15, 15, 16, 16, 17, 18, 18, 19, 20, 20, 21, 21, 21, 22, 22, 23, 23, 24, 25, 25, 25, 26, 27, 27, 28, 28, 29, 29, 29, 29, 29, 30, 31, 32, 33, 33, 34, 35, 35, 35, 35, 35, 36, 36, 37, 37, 38, 38, 39, 40, 41, 42, 43, 43, 43, 44, 45, 46, 46, 46, 47, 48, 49, 49, 50, 50, 51, 51, 51, 52, 53, 54],
        'tails': [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 11, 12, 13, 13, 14, 14, 14, 14, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 19, 20, 20, 21, 21, 22, 22, 22, 23, 24, 24, 24, 25, 25, 26, 26, 27, 28, 29, 30, 30, 30, 30, 30, 31, 31, 31, 32, 33, 34, 35, 35, 36, 36, 37, 37, 38, 38, 38, 38, 38, 38, 39, 40, 40, 40, 40, 41, 42, 42, 42, 42, 43, 43, 44, 44, 45, 46, 46, 46, 46]
    },
    '20': {
        'heads': [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 15, 15, 15, 16, 17, 17, 17, 17, 18, 19, 19, 19, 20, 21, 22, 23, 23, 23, 24, 25, 25, 25, 26, 27, 27, 27, 28, 29, 30, 30, 31, 31, 31, 31, 32, 32, 32, 33, 33, 33, 34, 34, 35, 36, 37, 37, 37, 37, 38, 39, 39, 39, 40, 41, 42, 43, 44, 45, 45, 46, 47, 48],
        'tails': [2, 3, 3, 3, 3, 3, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 23, 24, 25, 26, 26, 27, 27, 28, 29, 29, 29, 30, 31, 32, 32, 32, 33, 34, 34, 34, 34, 34, 35, 36, 36, 36, 37, 38, 38, 38, 39, 40, 40, 40, 40, 41, 41, 42, 43, 44, 44, 45, 46, 46, 47, 48, 48, 49, 49, 49, 49, 50, 51, 52, 52, 52, 53, 54, 54, 54, 54, 54, 54, 54, 55, 55, 55, 55]
    },
    '10A': {
        'heads': [0, 0, 0, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 10, 11, 12, 13, 13, 14, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 18, 19, 20, 20, 20, 21, 22, 23, 24, 25, 26, 26, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 43, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49, 49, 50, 51, 52, 52, 52],
        'tails': [1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 9, 10, 10, 10, 11, 12, 12, 13, 13, 13, 13, 13, 14, 14, 14, 14, 15, 16, 17, 18, 19, 19, 20, 21, 22, 23, 23, 23, 23, 24, 25, 25, 25, 25, 25, 25, 25, 26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33, 34, 34, 35, 36, 37, 38, 39, 40, 40, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 45, 45, 46, 46, 46, 46, 47, 48]
    },
    '10B': {
        'heads': [2, 2, 4, 5, 6, 8, 8, 11, 13, 14, 16, 19, 20, 21, 21, 24, 25, 26, 28, 30, 32, 35, 35, 37, 39, 42, 42, 45, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 64, 66, 67, 70, 71, 72, 73, 74, 75, 77, 78, 80, 82, 83, 84, 86, 87, 89, 90, 90, 91, 92, 94, 95, 96, 96, 99, 100, 102, 102, 103, 104, 106, 108, 111, 112, 114, 116, 118, 118, 119, 120, 121, 123, 124, 124, 126, 126, 128, 129, 131, 132, 134, 135, 137, 138, 139, 140, 142, 142],
        'tails': [1, 4, 5, 7, 9, 10, 13, 13, 14, 16, 17, 17, 19, 21, 24, 24, 26, 28, 29, 30, 31, 31, 34, 35, 36, 36, 39, 39, 39, 41, 42, 44, 46, 48, 50, 52, 54, 56, 57, 59, 59, 60, 62, 62, 64, 66, 68, 70, 72, 73, 75, 76, 77, 79, 81, 82, 84, 85, 87, 90, 92, 94, 95, 97, 99, 102, 102, 104, 105, 108, 110, 112, 113, 114, 114, 116, 117, 118, 119, 122, 124, 126, 128, 129, 131, 134, 135, 138, 139, 141, 142, 144, 145, 147, 148, 150, 152, 154, 155, 158]
    }
}

# Create attempts array (1 to 100)
attempts = list(range(1, 101))

# Calculate final statistics
final_stats = {}
for trial_name, data in tiles_data.items():
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
trial_names = list(tiles_data.keys())
positions = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0)
]

for idx, trial_name in enumerate(trial_names):
    if idx < len(positions):
        row, col = positions[idx]
        ax = fig.add_subplot(gs[row, col])
        
        data = tiles_data[trial_name]
        heads = data['heads']
        tails = data['tails']
        
        ax.plot(attempts, heads, 'b-', linewidth=2, label='Heads', alpha=0.7)
        ax.plot(attempts, tails, 'r-', linewidth=2, label='Tails', alpha=0.7)
        
        # Calculate expected line based on actual total
        expected = [(h + t) / 2 for h, t in zip(heads, tails)]
        ax.plot(attempts, expected, 'g--', linewidth=1, label='Expected (50%)', alpha=0.5)
        
        stats = final_stats[trial_name]
        ax.set_title(f'{trial_name}: {stats["heads"]}H, {stats["tails"]}T ({stats["percent_heads"]:.1f}%)', 
                    fontsize=11, fontweight='bold')
        ax.set_xlabel('Attempts', fontsize=9)
        ax.set_ylabel('Cumulative Count', fontsize=9)
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

# Combined plot - all trials heads percentage
ax_combined = fig.add_subplot(gs[2, 1])
colors = plt.cm.tab10(np.linspace(0, 1, len(trial_names)))

for idx, trial_name in enumerate(trial_names):
    data = tiles_data[trial_name]
    heads = data['heads']
    tails = data['tails']
    percentages = [(h/(h+t))*100 if (h+t) > 0 else 50 for h, t in zip(heads, tails)]
    ax_combined.plot(attempts, percentages, linewidth=1.5, label=trial_name, alpha=0.7, color=colors[idx])

ax_combined.axhline(y=50, color='black', linestyle='--', linewidth=2, label='Expected (50%)', alpha=0.8)
ax_combined.set_xlabel('Attempts', fontsize=10)
ax_combined.set_ylabel('Heads Percentage (%)', fontsize=10)
ax_combined.set_title('All Trials: Heads Percentage Over Time', fontsize=12, fontweight='bold')
ax_combined.legend(fontsize=8, loc='best')
ax_combined.grid(True, alpha=0.3)
ax_combined.set_ylim([30, 70])

# Deviation from expected plot
ax_deviation = fig.add_subplot(gs[2, 2])

for idx, trial_name in enumerate(trial_names):
    data = tiles_data[trial_name]
    heads = data['heads']
    tails = data['tails']
    # Calculate deviation from 50%
    deviations = [h - t for h, t in zip(heads, tails)]
    ax_deviation.plot(attempts, deviations, linewidth=1.5, label=trial_name, alpha=0.7, color=colors[idx])

ax_deviation.axhline(y=0, color='black', linestyle='--', linewidth=2, label='Perfect Balance', alpha=0.8)
ax_deviation.set_xlabel('Attempts', fontsize=10)
ax_deviation.set_ylabel('Heads - Tails', fontsize=10)
ax_deviation.set_title('Deviation from Balance (H-T)', fontsize=12, fontweight='bold')
ax_deviation.legend(fontsize=8, loc='best')
ax_deviation.grid(True, alpha=0.3)

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
    ax_summary.text(i, max(h, t) + 5, f'{p:.1f}%', ha='center', fontsize=9, fontweight='bold')

ax_summary.set_xlabel('Trial', fontsize=11)
ax_summary.set_ylabel('Final Count', fontsize=11)
ax_summary.set_title('Final Results Summary - All Tiles Trials', fontsize=13, fontweight='bold')
ax_summary.set_xticks(x)
ax_summary.set_xticklabels(trial_labels)
ax_summary.legend(fontsize=10)
ax_summary.grid(True, alpha=0.3, axis='y')

# Add a horizontal line at 50% mark
expected_line = [stats['total']/2 for stats in final_stats.values()]
ax_summary.plot(x, expected_line, 'g--', linewidth=2, label='Expected (50%)', alpha=0.7)

plt.suptitle('Tiles - Coin Flip Analysis', fontsize=16, fontweight='bold', y=0.995)

# Save the figure
plt.savefig('graph5TILES.png', dpi=300, bbox_inches='tight')
print("Comprehensive tiles graph saved successfully!")

# Print detailed statistics
print("\n" + "="*80)
print("FINAL STATISTICS FOR ALL TILES TRIALS")
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

# Print some interesting observations
print("\n" + "="*80)
print("INTERESTING OBSERVATIONS")
print("="*80)

# Find most balanced trial
most_balanced = min(final_stats.items(), key=lambda x: abs(x[1]['percent_heads'] - 50))
print(f"Most balanced trial: {most_balanced[0]} ({most_balanced[1]['percent_heads']:.1f}%)")

# Find most biased trial
most_biased = max(final_stats.items(), key=lambda x: abs(x[1]['percent_heads'] - 50))
print(f"Most biased trial: {most_biased[0]} ({most_biased[1]['percent_heads']:.1f}%)")

# Find trial with most flips
most_flips = max(final_stats.items(), key=lambda x: x[1]['total'])
print(f"Trial with most flips: {most_flips[0]} ({most_flips[1]['total']} flips)")

# Find trial with least flips
least_flips = min(final_stats.items(), key=lambda x: x[1]['total'])
print(f"Trial with least flips: {least_flips[0]} ({least_flips[1]['total']} flips)")

print("="*80)

plt.show()