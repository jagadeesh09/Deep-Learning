


import skimage





def rotate(image, angle, resize=False):

    if(angle == None):
        angles = [0,90,180,270]
        images = []
        for anfle in angles:
            images.append(skimage.transform.rotate(image,angle,resize)
    else:
        images = []
        for ang in angles:
            images.append(skimage.transform.rotate(image,ang,resize)
            
    return images
  
