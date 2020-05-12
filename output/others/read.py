import SimpleITK as sitk
import numpy as np
'''
This funciton reads a '.mhd' file using SimpleITK and return the image array, origin and spacing of the image.
'''

def load_itk_image(output_Edep):
    # Reads the image using SimpleITK
    itkimage = sitk.ReadImage(output_Edep)

    # Convert the image to a  numpy array first and then shuffle the dimensions to get axis in the order z,y,x
    npImage = sitk.GetArrayFromImage(itkimage)
    return npImage
