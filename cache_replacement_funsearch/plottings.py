
"""
Created on Sat Apr 26 19:26:59 2025

@author: sohamgundewar
"""

import matplotlib.pyplot as plt


policies = ['Adaptive_Reuse', 'LRU', 'DRRIP', 'Random', 'SHIP', 'SRRIP']

# Workload-wise hit/miss
astar_hits = [27784, 104914, 40541, 35754, 41890, 44595]
astar_misses = [123307, 46175, 110553, 115338, 109205, 106497]

bwaves_hits = [18346,18367, 18374, 18357, 18364, 18246]
bwaves_misses = [20796, 20775, 20768, 20785, 20778, 20896]

calculix_hits = [0, 0, 0, 0, 0, 0]
calculix_misses = [1170, 1170, 1170, 1170, 1170, 1170]

tonto_hits = [209786, 384662, 233380, 189611, 248734, 235451]
tonto_misses = [300241, 127393, 276646, 320413, 261293, 274575]

fig, axs = plt.subplots(2, 2, figsize=(16, 10))
bar_width = 0.35
x = range(len(policies))

def plot_with_labels(ax, hits, misses, title):
    bars1 = ax.bar(x, hits, width=bar_width, label='Hits')
    bars2 = ax.bar([i + bar_width for i in x], misses, width=bar_width, label='Misses')
    ax.set_title(title)
    ax.set_xticks([i + bar_width / 2 for i in x])
    ax.set_xticklabels(policies)
    ax.set_ylabel('Count')
    ax.grid(True)
    

    for bar in bars1 + bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + max(height * 0.01, 500), 
                f'{int(height)}', ha='center', va='bottom', fontsize=8)


plot_with_labels(axs[0, 0], astar_hits, astar_misses, 'Astar')
plot_with_labels(axs[0, 1], bwaves_hits, bwaves_misses, 'Bwaves')
plot_with_labels(axs[1, 0], calculix_hits, calculix_misses, 'Calculix')
plot_with_labels(axs[1, 1], tonto_hits, tonto_misses, 'Tonto')


handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2, fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()


import matplotlib.pyplot as plt


policies = ['LRU', 'DRRIP', 'Random', 'SHIP', 'SRRIP']


astar_hits = [ 104914, 40541, 35754, 41890, 44595]
astar_misses = [ 46175, 110553, 115338, 109205, 106497]

bwaves_hits = [ 18367, 18374, 18357, 18364, 18246]
bwaves_misses = [ 20775, 20768, 20785, 20778, 20896]

# calculix_hits = [0, 0, 0, 0, 0, 0]
# calculix_misses = [1170, 1170, 1170, 1170, 1170, 1170]

tonto_hits = [ 384662, 233380, 189611, 248734, 235451]
tonto_misses = [ 127393, 276646, 320413, 261293, 274575]

bzip_hits= [ 350475,301801, 292512, 310217, 297473 ]
bzip_misses = [ 63570, 112321, 121507, 103716, 116483 ]


fig, axs = plt.subplots(2, 2, figsize=(16, 10))
bar_width = 0.35
x = range(len(policies))

def plot_with_labels(ax, hits, misses, title):
    bars1 = ax.bar(x, hits, width=bar_width, label='Hits')
    bars2 = ax.bar([i + bar_width for i in x], misses, width=bar_width, label='Misses')
    ax.set_title(title)
    ax.set_xticks([i + bar_width / 2 for i in x])
    ax.set_xticklabels(policies)
    ax.set_ylabel('Count')
    ax.grid(True)
    

    for bar in bars1 + bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + max(height * 0.01, 500), 
                f'{int(height)}', ha='center', va='bottom', fontsize=8)


plot_with_labels(axs[0, 0], astar_hits, astar_misses, 'Astar')
plot_with_labels(axs[0, 1], bwaves_hits, bwaves_misses, 'Bwaves')
# plot_with_labels(axs[1, 0], calculix_hits, calculix_misses, 'Calculix')
plot_with_labels(axs[1, 1], tonto_hits, tonto_misses, 'Tonto')
plot_with_labels(axs[1, 0],bzip_hits, bzip_misses, 'Bzip2')

handles, labels = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=2, fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()






























