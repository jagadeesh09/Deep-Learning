


import skimage
from PIL import Image
import scipy.misc as m
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
                          
def resize(image,shape=None):
    if(shape == None):
        return image
    else:
        image = m.imresize(image,shape)
        return image
