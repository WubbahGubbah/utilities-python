from PIL import Image, ImageStat
from functools import reduce

thisimagepath = 'C:/Users/mwilson/Documents/python/Lambda/Images/white.jpg'
thisimagepath = 'C:/Users/mwilson/Documents/python/Lambda/Images/black.jpg'
thisimagepath = 'C:/Users/mwilson/Documents/python/Lambda/Images/whiteblack.jpg'


def main():
    thisimagepath = 'C:/Users/mwilson/Documents/python/Lambda/Images/12519932_574062_1940_0 - Copy.tif'
    thisimagepath = 'C:/Users/mwilson/Documents/python/Lambda/Images/whiteblack.jpg'

    im = Image.open(thisimagepath)
    width, height = im.size   # Get dimensions
    new_width = width * 0.125
    new_height = width * 0.125

    left = (width / 2) - new_width
    top = (height / 2) - new_height
    right = (width / 2) + new_width
    bottom = (height / 2) + new_height

    im2 = im.crop((left, top, right, bottom))

    thisimagepath='C:/Users/mwilson/Documents/python/Lambda/Images/testoutput1.jpg'
    im2.save(thisimagepath)

    if(ismonochrome(thisimagepath) == 1):
        print('is one color')
    else:
        print('not monochrome')
		
    print ('done')
	

def ismonochrome(infilename):
    MONOCHROMATIC_MAX_VARIANCE = 0.005
    v = ImageStat.Stat(Image.open(infilename)).var
    if(reduce(lambda x, y: x and y < MONOCHROMATIC_MAX_VARIANCE, v, True)):
        print('mono')
        return 1
    else:
        print('more')
        return 0
		
if __name__ == "__main__":
    main()
