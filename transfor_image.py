import PIL
import image_slicer
import os.path
from PIL import Image


def split_img(namedir,nameimage, p):
  path = '/Users/natalka/PycharmProjects/image_registration_algorithm'
  path_dir = os.path.join(path, namedir)
  try:
    os.mkdir(path_dir)
    print("folder created")
  except FileExistsError:
    print("file already exists.")
  tiles = image_slicer.slice(nameimage, p, save=False)
  image_slicer.save_tiles(tiles, directory=path_dir, prefix=namedir, format='png')

def merge_img(namedir):
  path = '/Users/natalka/PycharmProjects/image_registration_algorithm'
  path_dir = os.path.join(path, namedir)
  for i in list:
    path_img = os.path.join(namedir, i)
    image = PIL.Image.open(path_img)
    image_new = Image.new('RBG', (path_img.width))
  return


def generator_tiff(img):
  im = Image.open(img)
  im.save("frame-2.tiff", 'TIFF')
  return "Done"

# generator_tiff(img)
#test
split_img("f3","frame-3.jpg", 4)
list_f2 = ['f2_01_01.png', 'f2_01_02.png', 'f2_02_01.png', 'f2_02_02.png']
list_f3 = ['f3_01_01.png', 'f3_01_02.png', 'f3_02_01.png', 'f3_02_02.png']
merge_img("f2", list_f2)
