import numpy as np
from PIL import Image
from PIL import ImageFilter
import os
from shutil import rmtree
import matplotlib.pyplot as plt
import pandas as pd
from scipy.misc import toimage

def stitch(input_dir, output_dir, total_grid, name):
    images = []
    unique_name = []
    for img in os.listdir(input_dir):
        images.append(img)
        num, format = img.split('.')
        # num = num[1:]

    # # Sorting image list using 2nd occurance of _ to .png 
    images.sort(key=lambda x: int(x[x.find('_') + len('_'): x.rfind('.png')]))

    list_image = []
    for ii in range(len(images)):
        # Iterates through number of grid images for each image
        for jj in range(total_grid+1):
            num, format = img.split('.')
            if images[ii] == '_' + str(jj) + '.' + format:
                print('Image: {}'.format(images[ii]))
                list_image.append(os.path.join(input_dir, images[ii]))

    comb_width = int(513 * 52)
    comb_height = int(513 * 40)

    new_im = Image.new('RGB', (comb_width, comb_height))

    x_offset = 0
    y_offset = 0
    for img in list_image:
        image = Image.open(img)
        im = np.array(image)
        image = Image.fromarray(im)
        # image = toimage(image)
        new_im.paste(image, (x_offset, y_offset))
        x_offset += image.size[0]
        if x_offset == comb_width:
            x_offset = 0
            y_offset += image.size[0]
    
    new_im.save(output_dir + '/'+ name + '.' + format)


if __name__ == "__main__":

    district = 'Manikganj'
    input_org = f"BD/{district}/before_stitch/original"
    output_org = f"BD/{district}/after_stitch/original"
    input_pred = f"BD/{district}/before_stitch/prediction"
    output_pred = f"BD/{district}/after_stitch/prediction"
    
    if os.path.exists(output_org) and os.path.exists(output_pred):
        pass
    else:
        os.makedirs(output_org)
        os.makedirs(output_pred)

    stitch(input_dir, output_dir, 2080, district)