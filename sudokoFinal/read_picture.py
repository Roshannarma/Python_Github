import cv2
import numpy as np
import image_slicer
from os import system,name
from operator import itemgetter
from drawout import create_done
from solver import solvers,print_nicely
from PIL import Image,ImageChops
from cleanup import cleanup_image
def clear():
    if name == 'nt':
        _ = system('cls')
def read_sudoko(location):
    location = cleanup_image(location)
    mylist = []
    my_images = image_slicer.slice(location, 81,save=False)
    image_slicer.save_tiles(my_images, directory=r'D:\Python_Github\Image_processing\broken_images',prefix='slice', format='png')
    list_of_png = ["one","two","three","four","five","six","seven","eight","nine"]



    #making templates usable
    temp = []
    for z in range(0,9):
        temp.append(cv2.imread(r'D:\Python_Github\Image_processing\templates_processed\{}.png'.format(list_of_png[z]),0))
    # temp.append(cv2.imread(r"D:\Python_Github\Image_processing\templates_processed\blank.png"))






    for x in range(1,10):
        for y in range(1,10):
            img_rgb = cv2.imread(r"D:\Python_Github\Image_processing\broken_images\slice_0{}_0{}.png".format(x,y))
            skip = False
            for my_threshold in [.6,.7,.75,.8,.833,.866,.9,.925,.95,.975]:
                my_temp = []
                for z in range(0,9):
                    template = temp[z]
                    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
                    w, h = template.shape[::-1]
                    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
                    loc = np.where( res >= my_threshold)
                    if len(loc[0]) >= 1:
                        if z!=9:
                            my_temp.append(str(z+1))
                        else:
                            my_temp.append(" ")
                if len(my_temp) == 1:
                    mylist.append(my_temp[0])
                    break
                if len(my_temp) == 0:
                    mylist.append(" ")
                    break
    print(mylist)
    my_array = [mylist[0:9],mylist[9:18],mylist[18:27],mylist[27:36],mylist[36:45],mylist[45:54],mylist[54:63],mylist[63:72],mylist[72:81]]
    create_done(my_array,r"D:\Python_Github\sudokoFinal\blank.jpg")
    print(my_array)
    x = solvers(my_array)
    print(x)
    print_nicely(x)
    create_done(x,r"D:\Python_Github\sudokoFinal\blank.jpg")

if __name__ == "__main__":
    read_sudoko(r'D:\Python_Github\Image_processing\download.png')
