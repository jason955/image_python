from PIL import Image
picture = Image.open("marp.jpg")

# Get the size of the image
width, height = picture.size
#print(picture.size)
# Process every pixel
for x in range(width):
   for y in range(height):
       current_color = picture.getpixel( (x,y) )
       ####################################################################
       # Do your logic here and create a new (R,G,B) tuple called new_color
       ####################################################################
       #picture.putpixel( (x,y), new_color)
       #print(current_color)


       if(current_color[0] >200):            
            picture.putpixel( (x,y), 232)

picture.save('1_mod.jpg')