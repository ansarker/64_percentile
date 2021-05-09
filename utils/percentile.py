import numpy as np


def percentile(array, num_classes):
    percentile = np.zeros((num_classes), dtype=np.double)
    percentile_ = [0]
    for i in range(1, 6):
        percentile[i] = np.count_nonzero(array == i)
    whole = percentile.sum(axis=None)
    for i in range(1, 6):
        percentile_.append(round((percentile[i]/whole)*100, 2))

    print(f'Total pixels: {whole} (black excluded)')
    return percentile_
