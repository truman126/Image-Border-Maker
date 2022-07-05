from PIL import Image, ImageDraw, ImageOps
from screeninfo import get_monitors
import re , os, numpy
from os import listdir


### Variables

# Which monitor to use for the resolution template
monitor = 0 

# Set up edge margin to look for dominant color
me = 10

# Set up border margin to be added in dominant color
mb = 300

dir = 'Desktop Wallpapers/'

###

# get the screen resolution
m = get_monitors()

m = str(m[0])

mon_w = 2560  #int(re.search("width=(.*?)\,", m).group(1))
mon_h = 1400 #int(re.search("height=(.*?)\,", m).group(1))


# loop to get every image in the dir

for image in os.listdir(dir):
 
    # check if the image ends with png
    if (image.endswith(".png")) or (image.endswith(".jpg")) or (image.endswith(".jpeg")) :

        # Open image, enforce RGB with alpha channel
        img = Image.open(dir + image).convert('RGBA')
        img_w, img_h = img.size


        # Determine if the image is portrait or landscape
        if (img_w > img_h):
            # landscape
            img_w = (img_w // 5)*2
            img_h = (img_h // 5)*2

        else :
            # portrait
            img_w = (img_w // 6)*2
            img_h = (img_h // 6)*2

        img = img.resize((img_w,img_h))




        # Get the average color
        avg_color_per_row = numpy.average(img, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)
        avg_color = tuple(avg_color)



        #Create the border
        border = Image.new(mode="RGB", size=(mon_w, mon_h))

        draw = ImageDraw.Draw(border)
        draw.rectangle([(0, 0), (mon_w, mon_h)], (int(avg_color[0]),int(avg_color[1]),int(avg_color[2])))



        # Add border
        final_img = border.copy()
        final_img.paste(img,((mon_w - img_w) // 2 ,(mon_h - img_h) // 2))

        print("Bordering " + image + " complete!")

        final_img.save(dir + 'bordered_' + image)

