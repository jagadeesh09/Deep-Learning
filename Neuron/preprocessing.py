


import skimage
from PIL import Image
import scipy.misc as m
import random
""" This python includes all the preprocessing requirements for images using skimage"""


def rotate2d(image, angle = None, resize=False):
    """
    Parameters : 
    image is a two dimensional array whose shape is (x,y) 
    angle is list of values in degrees, by default it is None
    
    """
    
    if(angle == None):
        angles = [0,90,180,270]
        images = []
        for angle in angles:
            images.append(skimage.transform.rotate(image,angle,resize)
    else:
        images = []
        for angl in angles:
            images.append(skimage.transform.rotate(image,angl,resize)
            
    return images
  
def rotate3d(image,angle=None,resize=False):
    """
    Parameters : 
    image is a three dimensional array whose shape is (x,y,3) i.e a 3 channel image 
    angle is list of values in degrees, by default it is None
    
    """
    if(angle == None):
        angles = [0,90,180,270]
        images =[]
        for angle in angles:
            im =[]
            for i in range(3):
                im.append(skimage.transform.rotate(image[:,:,i],angle,resize)
            images.append(im)
    else:
        images =[]
        for degree in angle:
            im =[]
            for i in range(3):
                im.sppend(skimage.transform.rotate(image[:,:,i],degree,resize)
            images.append(im)
    return images
                         
     
def random_patches(image,num_patches=1,patch_size=200):
    """
    Parameters :
    image is a three dimensional numpy array 
    num_patches is number of patches to generate
    patch_size is required patch size
    """
    (height,width) = image.shape
    half_size = patch_size/2
    (centre_x,centre_y) = (height/2,width/2)
    diffy = (patch_size - height)/2
    diffx = (patch_size - width)/2
    x_cood = []
    y_cood = []
    for i in range(num_patches):
        x_cood.append(random.randint(centre_y-diffy,centre_y + diffy)
        y_cood.append(random.randint(centre_x-diffx,centre_x + diffx)
    images = []
    for i in range(num_patches):
        slice = [image[x_cood[i]-half_size:x_cood+half_size,y_cood[i]-half_size:y_cood[i]+half_size,j] for j in range(3)]
        slice = np.asarray(slice)
        images.append(slice)
    images = np.asarray(image)
    return images                  
def resize(image,shape=None):
    if(shape == None):
        return image
    else:
        image = m.imresize(image,shape)
        return image
