import numpy, sys
import mhd_utils_3d
import mhd_utils_2
import matplotlib.pyplot as plt
sys.path.append('./')

image_array, meta_header = mhd_utils_3d.load_raw_data_with_mhd('/home/dashy/Desktop/Gate_v8.2/simulations/Radiotherapy/photon_linac/py/output-full-Dose.mhd')
image_array.shape

image_array=image_array**2
def func(x):
    y=x**2+2*x+500
    return y
image_array=func(image_array)
meta_header
meta_header['ElementSpacing']


#mhd_utils_3d.write_meta_header('../output/output-full-Dose.mhd',meta_header)
#mhd_utils_3d.dump_raw_data('../output/output-full-Dose.raw',image_array)
plt.image(data[10,:,:])
plt.show()