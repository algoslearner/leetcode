# https://leetcode.com/discuss/interview-question/866230/Asana-or-Software-Engineer-or-Reject
'''
Program an ASCII printer. I think this was OOP related question which I thought is as simple as ''.join(str(ord(c)) for c in s)
I searched this question online but couldn't find an answer. I would love to know what the potential answer looks like.
'''

# Do you know what was ascii printer question? something like this? http://memex.cc/Technical_interview#print-out-an-ascii-art-piece
# My one hour coding challenge onsite was to program an ASCII printer. There were several functions of the program to implement, if you know OOP, linked lists, and 2d matrices you'll be fine. 



#################################################################################################################
# https://levelup.gitconnected.com/python-ascii-art-generator-60ba9eb559d7

#Python ASCII Art Generator.

# Steps to convert image to ASCII character
#   1.  Load an image
#   2.  Resize Image
#   3.  Convert image to GreyScale
#   4.  Convert GreyScale data of each pixel into respective ASCII character
#   5.  Loading an Image using PIL image Library
#   6.  To load the image we will be using PIL library.

import PIL.Image
def main():
    path = input("Enter the path to the image fiel : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ");
        
# The above code reads the image from the path given by the user. If the image doesn’t exist on the given path then, we will show an error message.

# Define ASCII list
# Let’s create a list of ASCII characters,

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
# The ASCII characters are arranged from the darkest to the lightest. This means the darkest pixel will be replaced with @ and lightest with .

# Resize Image
# We need to convert the image to some small width and height so that it doesn’t result in large size text. To find the new_height, multiply new_width with old_height then divide by old_width.

def resize(image, new_width = 100):
    width, height = image.size
    new_height = new_width * height / width
    return image.resize((new_width, new_height))
  
# Convert Image to GreyScale
# We can use convert method on image with L option to get GreyScale image

def to_greyscale(image):
    return image.convert("L")
  
# Convert GreyScale Image to ASCII character
# To convert the image to ASCII character first, get each pixel value(0-255). Get the corresponding ASCII character and join them as a string

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "";
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25];
    return ascii_str
  
# Now we have a to_greyscale method to convert image to GreyScale image, pixel_to_ascii method to convert GreyScale image to ASCII string, once we get the ASCII string of the image we need to split the string based on the width of the image and save it in a file.

import PIL.Image
def main():
    path = input("Enter the path to the image fiel : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")
    #resize image
    image = resize(image);
    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    #save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img);
main()
