import matplotlib.pyplot as plt
import numpy as np


def plotWPMGraph(wpm):
    height = [wpm]
    bars = ['Your WPM=' + str(wpm)]
    y_pos = np.arange(1)
    fig = plt.figure()
    ax = fig.gca()
    ax.set_aspect('equal')
    ax.grid(True, which='both', alpha=0.4)
    ax.bar(y_pos, height,  width=10, color='green', align='center', alpha=0.4)
    plt.xticks(y_pos, bars)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    scale = 130
    if wpm <= 130:
        scale += 10
    elif wpm > 130:
        scale = wpm
    ax.set_ylim([0,scale])

    # ax.set_aspect('auto')
    ax.axvline(100, 130, color='black', alpha=0.0)
    ax.text(0, 115, 'average WPM')
    ax.text(0, 100, '100')
    ax.text(0, 130, '130')
    ax.annotate(s='', xy=(0, 100), xytext=(0, 130), arrowprops=dict(arrowstyle='<->'))
    fig.savefig('outputFiles\\wpmGraph.png')
#     plt.show()

# if __name__ == "__main__":
#     plotWPMGraph(160)