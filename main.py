from PIL import Image
import os

imgFiles = []
imgFilesP = []
files = os.listdir('/home/virgil/Downloads/usbData/')
print(files)
directory = '/home/virgil/Downloads/usbData/'
for i in files:
    if '.webp' in i:
        imgFilesP.append(directory+ i)
    elif 'png' in i:
        imgFiles.append(directory + i)
    elif 'jpg' in i:
        imgFiles.append(directory + i)
#This code is for webp files which have different length extensions
for i in imgFilesP:
    im = Image.open(i)
    os.remove(i)
    i = i[:-5]
    im.save(i + '.png', 'PNG')
for i in imgFiles:
    im = Image.open(i)
    os.remove(i)
    i = i[:-4]
    im.save(i + '.png', 'PNG')



print(imgFiles)

