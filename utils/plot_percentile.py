import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

"""
    function: plot_percentile
    params:
        input       (an input image or array)
        predict     (a predict image or array)
        percentile  (a list of classes percentage)
        colors      (a list of colors)
        labels_dict (a dictionay of index_values with class_label)
        name        (output_name)
    

    gdrive upload to google_drive link
    parent_folder_id: 1S_f81itbNO-0ZJDw3crWcDDh0D2woAxN
    command: gdrive upload -r DIR_PATH -p 1S_f81itbNO-0ZJDw3crWcDDh0D2woAxN
"""


def plot_percentile(input, predict, percentile, colors, labels_dict, name):
    fp_suptitle = FontProperties(
        family="monospace", size="large", weight="bold")
    fp_title = FontProperties(family="monospace", size=11, weight="normal")
    fig, axes = plt.subplots(ncols=2, figsize=(14, 5.8))

    axes[0].imshow(input)
    axes[0].set_title('Input', fontproperties=fp_title)
    axes[0].set_xticks([])
    axes[0].set_yticks([])

    axes[1].imshow(predict)
    axes[1].set_title('Prediction', fontproperties=fp_title)
    axes[1].set_xticks([])
    axes[1].set_yticks([])

    for i in range(1, 6):
        per = f'{percentile[i] : .2f}'
        legend = f"{labels_dict[i] : <18}{per:>6}%"
        print(legend)
        axes[i//3].plot([], [], color=colors[i], label=legend)

    fig.suptitle(name, fontproperties=fp_suptitle)
    leg = fig.legend(loc=7, prop={'family': 'monospace'})

    for legobj in leg.legendHandles:
        legobj.set_linewidth(6.0)

    fig.tight_layout()
    fig.subplots_adjust(right=0.82)

    if os.path.exists(f'BD/{name}/result'):
        pass
    else:
        os.makedirs(f'BD/{name}/result')

    plt.savefig(os.path.join(f'BD/{name}/result', f'plot_{name}.png'), dpi=300)
