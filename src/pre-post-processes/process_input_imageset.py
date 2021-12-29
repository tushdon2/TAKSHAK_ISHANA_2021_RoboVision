# importing required libraries
import PIL.Image as I
import numpy as np

def __save(imgArr, destination, savedImgsAlready):
    pass
    img = I.fromarray(imgArr)
    savedImgsAlready += 1
    img.save(destination + "/" + str(savedImgsAlready) + ".jpeg")
    return savedImgsAlready

def splitterAndSaver(imgpath, destination):
    savedImgs = 0
    img = I.open(imgpath)
    width, height = img.size
    # divide into parts of size 256x256
    numrows = height // 256 + 1
    numcols = width // 256 + 1
    img = np.asarray(img)

    i = 0
    while i < numrows:
        j = 0
        while j < numcols:
            newImg = np.full((256, 256, 3), 255, dtype = np.uint8) # complete white
            row = 0
            while row < 256:
                x = i * 256 + row               
                if x == height: break
                col = 0
                while col < 256:
                    y = j * 256 + col
                    if y == width: break
                    newImg[row, col] = img[x, y]
                    col += 1
                row += 1
            j += 1
            # save newImg and update counter for number of images saved
            savedImgs = __save(newImg, destination, savedImgs) 
        i += 1
    return savedImgs    

def stichMask():
    pass