from PIL import Image, ImageChops
import cv2
def crop_image_only_outside(img,tol=0):
    # img is 2D image data
    # tol  is tolerance
    mask = img>tol
    print(img.shape)
    m,n,z = img.shape
    mask0,mask1 = mask.any(0),mask.any(1)
    col_start,col_end = mask0.argmax(),n-mask0[::-1].argmax()
    row_start,row_end = mask1.argmax(),m-mask1[::-1].argmax()
    return img[row_start:row_end,col_start:col_end]
def crop_until_white(img):
    if img.getpixel((0,0))[1] > 150 and img.getpixel((0,0))[2] > 150:
        print(img.getpixel((0,0))[1])
        print(img.getpixel((0,0))[2])
        return img
    else:
        try:
            width, height = img.size
        except:
            z,width,height = img.size
        return crop_until_white(img.crop((1,1,width-1,height-1)))
def cleanup_image(location):
    im = cv2.imread(location)
    im = cv2.bitwise_not(im)
    im = crop_image_only_outside(im)
    im = cv2.bitwise_not(im)
    newloc = r"D:\Python_Github\Image_processing\test.png"
    cv2.imwrite(newloc,im)
    imp = Image.open(newloc)
    imp = crop_until_white(imp)
    imp.save(r"D:\Python_Github\Image_processing\test2.png")
    return r"D:\Python_Github\Image_processing\test2.png"
if __name__ == "__main__":
    cleanup_image(r"D:\Python_Github\Image_processing\download2.png")
