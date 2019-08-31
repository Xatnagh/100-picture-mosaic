def pixilImg(imagename, l, h):  # high def image -> 5 images of lower quality/ file names from order from highest quatity to lowest - YOUR_FILENAME1, ... YOUR_FILENAME5 by pixels/4
    from PIL import Image
    im = Image.open(imagename)
    x = imagename
    for i in range(5):
        im.thumbnail([h/2, l/2])  # shrink image
        y = x.split('.')  # y[0] is the name y[1] is file type
        y[0] = y[0] + i + "." + y[1]  # to get the pixelized img do imagename+#
        print(y[0])
        print(y[1])
        if y[1] != 'jpg':
            raise(NameError('in 5imgs.py input file is not type jpg --raised error'))
        else:
            im.save(y, 'JPEG')  # saves image as type jpg


    """ for testing purposes
python
import procimage
procimage.pixilImg('test.jpg', 500, 500)
    """
