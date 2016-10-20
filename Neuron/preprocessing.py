


import skimage


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
        for anfle in angles:
            images.append(skimage.transform.rotate(image,angle,resize)
    else:
        images = []
        for angl in angles:
            images.append(skimage.transform.rotate(image,angl,resize)
            
    return images
  
def rotate3d():
                          
     
def random_patches(image,num_patches=1,patch_size=200):
                          
