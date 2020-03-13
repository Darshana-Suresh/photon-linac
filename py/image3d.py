import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt

'''
This funciton reads a '.mhd' file using SimpleITK and return the image array, origin and spacing of the image.
'''

def load_itk(filename):
    # Reads the image using SimpleITK
    itkimage = sitk.ReadImage(filename)

    # Convert the image to a  numpy array first and then shuffle the dimensions to get axis in the order z,y,x
    ct_scan = sitk.GetArrayFromImage(itkimage)

    # Read the origin of the ct_scan, will be used to convert the coordinates from world to voxel and vice versa.
    origin = np.array(list(reversed(itkimage.GetOrigin())))

    # Read the spacing along each dimension
    spacing = np.array(list(reversed(itkimage.GetSpacing())))
   # print(ct_scan)
    return ct_scan, origin, spacing

file = '/home/dashy/Desktop/Gate_v8.2/simulations/Radiotherapy/photon_linac/py/output-full-Dose.mhd'
print(load_itk(file))