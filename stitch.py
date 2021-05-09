import pandas as pd
import matplotlib.pyplot as plt
from shutil import rmtree
import os
from PIL import ImageFilter
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS = 9331200001


def stitch(input_dir, output_dir, total_grid, col, row, crop_right, crop_bottom, name):
    images = []
    for img in os.listdir(input_dir):
        images.append(img)
        img_ = img.split('_', 1)[1]
        num, format = img_.split('.')

    images.sort(key=lambda x: int(x[x.find('_') + len('_'): x.rfind('.png')]))

    list_image = []
    for ii in range(len(images)):
        # Iterates through number of grid images for each image
        for jj in range(total_grid+1):
            img__ = img.split('_', 1)[0] or ""
            num, format = img.split('.')
            if images[ii] == f'{img__}_{jj}.{format}':
                print('Image: {}'.format(images[ii]))
                list_image.append(os.path.join(input_dir, images[ii]))

    comb_width = int(513 * col)
    comb_height = int(513 * row)

    new_im = Image.new('RGB', (comb_width, comb_height))

    x_offset = 0
    y_offset = 0
    for img in list_image:
        image = Image.open(img)
        im = np.array(image)
        image = Image.fromarray(im)
        new_im.paste(image, (x_offset, y_offset))
        x_offset += image.size[0]
        if x_offset == comb_width:
            x_offset = 0
            y_offset += image.size[0]

    new_im = new_im.crop((0, 0, crop_right, crop_bottom))
    new_im.save(output_dir + '/' + name + '.' + format)
    print(f"finish stitching {name}...")


if __name__ == "__main__":

    district = 'Naogaon'
    num_image = 4830
    col, row = 70, 69
    crop_right, crop_bottom = 35781, 34973

    input_org = f"BD/{district}/before_stitch/original"
    input_pred = f"BD/{district}/before_stitch/prediction"
    output_dir = f'BD/{district}/cropped/'

    if os.path.exists(output_dir):
        pass
    else:
        os.makedirs(output_dir)

    stitch(input_org, output_dir, num_image, col, row,
           crop_right, crop_bottom, f'Input_{district}')
    stitch(input_pred, output_dir, num_image, col, row,
           crop_right, crop_bottom, f'Predict_{district}')
