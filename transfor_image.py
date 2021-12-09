import image_slicer
import os.path
from PIL import Image


def split_img(namedir,nameimage, p):
  path = '/Users/natalka/PycharmProjects/image_registration_algorithm'
  path_dir = os.path.join(path, namedir)
  print(path_dir)
  try:
    os.mkdir(path_dir)
    print("folder created")
  except FileExistsError:
    print("file already exists.")
  tiles = image_slicer.slice(nameimage, 4, save=False)
  image_slicer.save_tiles(tiles, directory=path_dir, prefix=nameimage, format='png')

def merge_img(namedir):
  return


def generator_tiff(img):
  im = Image.open(img)
  im.save("frame-2.tiff", 'TIFF')
  return "Done"

# generator_tiff(img)
#test
split_img("f3","frame-3.jpg", 4)
merge_img("f3")