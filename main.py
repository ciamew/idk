# from PIL import Image
# pic = Image.open("fam.jpg")
# picnew = Image.new("RGB",pic.size,"white")
# pixel_out = pic.load()
# pixel_in = picnew.load()

# x = pic.read("fam.jpg")
# flipped = pic.flip(pic,-1)
# pic.show(flipped)

#otocenie obrazku podla y osi
# for x in range(pic.size[0]):
#     for y in range(pic.size[1]):
#         pixel_in[pic.size[0]-1-x,y] = pixel_out[x,y]
#
# picnew.show()

#zrusenie kazdeho druheho stlpca a riadku
# for x in range(0, pic.size[0],2):
#     for y in range(0, pic.size[1],2):
#         pixel_in[x//2,y//2] = pixel_out[x,y]
# picnew.show()



#zvacsanie obrazku 2x
#
# from PIL import Image
# pic = Image.open("fam.jpg")
# picnew = Image.new("RGB",(pic.size[0]*2,pic.size[1]*2),"white")
# pixel_out = pic.load()
# pixel_in = picnew.load()
#
# for x in range(pic.size[0]):
#     for y in range(pic.size[1]):
#         pixel_in[2*x,2*y] = pixel_out[x,y]
#         pixel_in[2*x+1,2*y+1] = pixel_out[x,y]
#         pixel_in[2*x+1,2*y] = pixel_out[x,y]
#         pixel_in[2*x,2*y+1] = pixel_out[x,y]
# picnew.show()

#zvacsanie obrazku 4x, dorobit

# from PIL import Image
# pic = Image.open("fam.jpg")
# picnew = Image.new("RGB",(pic.size[0]*4,pic.size[1]*4),"white")
# pixel_out = pic.load()
# pixel_in = picnew.load()
#
# for x in range(pic.size[0]):
#     for y in range(pic.size[1]):
#         pixel_in[2*x,2*y] = pixel_out[x,y]
#         pixel_in[2*x+1,2*y+1] = pixel_out[x,y]
#         pixel_in[2*x+1,2*y] = pixel_out[x,y]
#         pixel_in[2*x,2*y+1] = pixel_out[x,y]
#         pixel_in[2*x+2,2*y+2] = pixel_out[x,y]
#         pixel_in[2*x+2,2*y+1] = pixel_out[x,y]
#         pixel_in[2*x+1,2*y+2] = pixel_out[x,y]
#         pixel_in[2*x,2*y] = pixel_out[x,y]
#         pixel_in[2*x,2*y] = pixel_out[x,y]
# picnew.show()

# otocenie obrazku podla x a y osi, ????
# from PIL import Image
# pic = Image.open("fam.jpg")
# picnew = Image.new("RGB",pic.size,"white")
# pixel_out = pic.load()
# pixel_in = picnew.load()
#
# for x in range(pic.size[0]):
#     for y in range(pic.size[1]):
#         pixel_in[pic.size[0]-x,-y] = pixel_out[x,y]
#
# picnew.show()

# urob ciernobiely a

from PIL import Image, ImageOps
pic = Image.open("but.jpg")
pic1 = ImageOps.grayscale(pic)
pixels = pic1.load()
fw = open("vysledok.txt","w", encoding = "UTF-*")
fw.write(str(pic.size[0])+ "" +str(pic.size[1])+ "\n")

for y in range(pic1.size[1]):
    for x in range(pic1.size[1]):
        #TODO zapis do suboru
        print(hex(pixels[x,y])[2::]) #hex prevedie cislo do 16kovej sustavy
    fw.write("\n")
pic1.show()

#cierna 0, biela 1
