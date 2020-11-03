import image_slicer
from PIL import Image, ImageDraw
def create_done(my_array,location):
    list_of_png = ["one","two","three","four","five","six","seven","eight","nine"]
    with Image.open(location).convert('RGBA') as base:
        txt = Image.new("RGBA",base.size,(255,255,255,0))
        draw = ImageDraw.Draw(txt)
        for x in range(9):
            for y in range(9):
                # num = 9*y + x
                if my_array[y][x] == " ":
                    continue
                if not (location := int(my_array[y][x])-1 < 10):
                    continue
                z = list_of_png[int(my_array[y][x])-1]
                # print(z)
                if z!= "one":
                    im = Image.open(r"D:\Python_Github\Image_processing\templates_processed" + f"\{z}.png" ).convert("RGBA").resize((30,30))
                    txt.paste(im,(x*67+20,y*67+20))
                else:
                    im = Image.open(r"D:\Python_Github\Image_processing\templates_processed" + f"\{z}.png" ).convert("RGBA").resize((20,30))
                    txt.paste(im,(x*67+25,y*67+20))
#                draw.ellipse([(x*67+25,y*67+25),(x*67+35,y*67+35)],fill=(255,0,0,100))
        out = Image.alpha_composite(base,txt)
        out.show()
if __name__ == "__main__":
    array = [1,2,3,4,3,6,8,8,9,1,2,7,4,5,6,7,4,9,1,2,6,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
    create_done(array,r"D:\Python_Github\sudokoFinal\blank.jpg")
