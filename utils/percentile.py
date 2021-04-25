# import os
import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.font_manager import FontProperties

# from PIL import Image
# Image.MAX_IMAGE_PIXELS = 933120000

# from utils.im2index import im2index
# from utils.plot_percentile import plot_percentile

# name = 'narayan_.png'

# input_image = Image.open('narayan.png')
# predict_image = np.array(Image.open(name))
# predict_image_ = im2index(predict_image)

# colors = ['#000000', '#00ffff', '#ff0000', '#0000ff', '#00ff00', '#ffff00']
# dict_ = {
#     0 : 'Unknown',
#     1 : 'Forest',
#     2 : 'Builtup',
#     3 : 'Water',
#     4 : 'Farmland',
#     5 : 'Meadow'
#     }

def percentile(array, num_classes):
    percentile = np.zeros((num_classes), dtype=np.double)
    percentile_ = [0]
    for i in range(1, 6):
        percentile[i] = np.count_nonzero(array == i)
    whole = percentile.sum(axis=None)
    for i in range(1, 6):
        percentile_.append(round((percentile[i]/whole)*100, 2))
    
    print(f'Output: {percentile}')
    print(f'Total pixels: {whole} (black excluded)')
    return percentile_

# percentile_ = percentile(array=predict_image_, num_classes=6)
# plot_percentile(input=input_image, 
#                 predict=predict_image, 
#                 percentile=percentile_, 
#                 colors=colors, 
#                 labels_dict=dict_,
#                 name='Narayanganj')
