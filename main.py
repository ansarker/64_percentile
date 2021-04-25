import os
import numpy as np

from PIL import Image
Image.MAX_IMAGE_PIXELS = 933120000

from utils.im2index import im2index
from utils.percentile import percentile
from utils.plot_percentile import plot_percentile

"""
    Step by step guide
    ------------------
    1. Stitch the images both Input and Prediction
        file: stitch.py
    2. Crop to initial size
        file: crop_to_initial.py
    3. Create index image and flatten the images
        file: im2index.py
    4. Then calculate the classes percentage
        file: percentile.py
    5. Visualize the images and show the percentiles
        file: plot_percentile.py
"""

def main():
    """
        All the arguments goes here
        district_name, image_name
        crop_right, crop_bottom
    """
    district_name, image_name = 'Manikganj', 'Manikganj.png'
    crop_right, crop_bottom = 26645, 20434
    colors = ['#000000', '#00ffff', '#ff0000', '#0000ff', '#00ff00', '#ffff00']
    dict_ = {
                0 : 'Unknown',
                1 : 'Forest',
                2 : 'Builtup',
                3 : 'Water',
                4 : 'Farmland',
                5 : 'Meadow'
            }

    input_path = os.path.join('BD', f'{district_name}/after_stitch/original/{image_name}')
    predict_path = os.path.join('BD', f'{district_name}/after_stitch/prediction/{image_name}')

    input_image = Image.open(input_path)
    predict_image = Image.open(predict_path)

    input_image_ = input_image.crop((0, 0, crop_right, crop_bottom))
    predict_image_ = predict_image.crop((0, 0, crop_right, crop_bottom))

    # input_image_.save(os.path.join('BD', f'{district_name}/cropped/Input_{image_name}'))
    # predict_image_.save(os.path.join('BD', f'{district_name}/cropped/Predict_{image_name}'))
    
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