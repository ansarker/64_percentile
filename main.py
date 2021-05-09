from utils.plot_percentile import plot_percentile
from utils.percentile import percentile
from utils.im2index import im2index
import os
import numpy as np

from PIL import Image
Image.MAX_IMAGE_PIXELS = 933120000*2


"""
    Step by step guide
    ------------------
    1. Stitch the images both Input and Prediction
        file: stitch.py
    2. Create index image and flatten the images
        file: im2index.py
    3. Then calculate the classes percentage
        file: percentile.py
    4. Visualize the images and show the percentiles
        file: plot_percentile.py
"""


def main():
    """
        All the arguments goes here
        district_name, image_name
    """
    district_name, image_name = 'Naogaon', 'Naogaon.png'
    print(f'Now processing {district_name}...\n')

    colors = ['#000000', '#00ffff', '#ff0000', '#0000ff', '#00ff00', '#ffff00']
    dict_ = {
        0: 'Unknown',
        1: 'Forest/Tree cover',
        2: 'Builtup',
        3: 'Water',
        4: 'Farmland',
        5: 'Meadow'
    }

    input_image_ = Image.open(f'BD/{district_name}/cropped/Input_{image_name}')
    predict_image_ = Image.open(
        f'BD/{district_name}/cropped/Predict_{image_name}')

    predict_image_ = np.array(predict_image_)
    predict_image_flatten = im2index(predict_image_)

    percentile_ = percentile(array=predict_image_flatten, num_classes=6)
    plot_percentile(input=input_image_,
                    predict=predict_image_,
                    percentile=percentile_,
                    colors=colors,
                    labels_dict=dict_,
                    name=district_name)


if __name__ == "__main__":
    main()
