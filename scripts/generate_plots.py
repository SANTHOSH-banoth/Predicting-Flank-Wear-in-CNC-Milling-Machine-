import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.dpi'] = 130

train = pd.read_excel('data/Train_data_3.xlsx')
test = pd.read_excel('data/Test_data_3.xlsx')

# 1. VB wear progression over time, grouped by case (train)
fig, ax = plt.subplots(figsize=(8,5))
for case, grp in train.groupby('case'):
    grp = grp.sort_values('time')
    ax.plot(grp['time'], grp['VB'], marker='o', markersize=3, label=f'Case {case}')
ax.set_xlabel('Time (min)')
ax.set_ylabel('Flank Wear VB (mm)')
ax.set_title('Flank Wear Progression Over Time by Case (Train Data)')
ax.legend(fontsize=7, ncol=2)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('results/vb_wear_progression_by_case.png')
plt.close()

# 2. Correlation heatmap
fig, ax = plt.subplots(figsize=(6,5))
corr = train[['time','DOC','feed','material','VB','VIB','DC']].corr()
im = ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha='right')
ax.set_yticklabels(corr.columns)
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f'{corr.iloc[i,j]:.2f}', ha='center', va='center', fontsize=7,
                 color='white' if abs(corr.iloc[i,j])>0.5 else 'black')
ax.set_title('Feature Correlation Heatmap (Train Data)')
fig.colorbar(im, ax=ax, shrink=0.8)
plt.tight_layout()
plt.savefig('results/feature_correlation_heatmap.png')
plt.close()

# 3. VIB vs VB scatter
fig, ax = plt.subplots(figsize=(7,5))
ax.scatter(train['VIB'], train['VB'], alpha=0.6, label='Train', c='tab:blue')
ax.scatter(test['VIB'], test['VB'], alpha=0.6, label='Test', c='tab:orange')
ax.set_xlabel('Vibration (VIB)')
ax.set_ylabel('Flank Wear VB (mm)')
ax.set_title('Vibration Signal vs Flank Wear')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('results/vib_vs_vb_scatter.png')
plt.close()

# 4. DC vs VB scatter
fig, ax = plt.subplots(figsize=(7,5))
ax.scatter(train['DC'], train['VB'], alpha=0.6, label='Train', c='tab:green')
ax.scatter(test['DC'], test['VB'], alpha=0.6, label='Test', c='tab:red')
ax.set_xlabel('DC (Deflection/Current)')
ax.set_ylabel('Flank Wear VB (mm)')
ax.set_title('DC Signal vs Flank Wear')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('results/dc_vs_vb_scatter.png')
plt.close()

# 5. VB distribution train vs test
fig, ax = plt.subplots(figsize=(7,5))
ax.hist(train['VB'], bins=15, alpha=0.6, label='Train', color='tab:blue')
ax.hist(test['VB'], bins=15, alpha=0.6, label='Test', color='tab:orange')
ax.set_xlabel('Flank Wear VB (mm)')
ax.set_ylabel('Count')
ax.set_title('Flank Wear (VB) Distribution: Train vs Test')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('results/vb_distribution_train_test.png')
plt.close()

print("Done. Generated 5 plots in results/")
