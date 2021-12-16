import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_shift(img, pixel):
  return 10

def read_this(image_file, gray_scale=False):
  output = cv2.imread(image_file)
  if gray_scale:
    output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
  else:
    output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
  return output

def shifter(vect, y, y_):
  if (y > 0):
    image_trans = pad_vector(vector=vect, how='lower', depth=y_)
  elif (y < 0):
    image_trans = pad_vector(vector=vect, how='upper', depth=y_)
  else:
    image_trans = vect
  return image_trans

def pad_vector(vector, how, depth, constant_value=0):
  vect_shape = vector.shape[:2]
  if (how == 'upper') or (how == 'top'):
    pp = np.full(shape=(depth, vect_shape[1]), fill_value=constant_value)
    pv = np.vstack(tup=(pp, vector))
  elif (how == 'lower') or (how == 'bottom'):
    pp = np.full(shape=(depth, vect_shape[1]), fill_value=constant_value)
    pv = np.vstack(tup=(vector, pp))
  elif (how == 'left'):
    pp = np.full(shape=(vect_shape[0], depth), fill_value=constant_value)
    pv = np.hstack(tup=(pp, vector))
  elif (how == 'right'):
    pp = np.full(shape=(vect_shape[0], depth), fill_value=constant_value)
    pv = np.hstack(tup=(vector, pp))
  else:
    return vector
  return pv

# pmat = pad_vector(vector=mat, how='left', depth=3)

def shift_image(image_src, at):
    x, y = at
    x_, y_ = abs(x), abs(y)
    if (x > 0):
        left_pad = pad_vector(vector=image_src, how='left', depth=x_)
        image_trans = shifter(vect=left_pad, y=y, y_=y_)
    elif (x < 0):
        right_pad = pad_vector(vector=image_src, how='right', depth=x_)
        image_trans = shifter(vect=right_pad, y=y, y_=y_)
    else:
        image_trans = shifter(vect=image_src, y=y, y_=y_)

    return image_trans


def translate(img, at, with_plot=False, gray_scale=False):
  if len(at) != 2: return False

  image_src = read_this(image_file=img, gray_scale=gray_scale)

  if not gray_scale:
    r_image, g_image, b_image = image_src[:, :, 0], image_src[:, :, 1], image_src[:, :, 2]
    r_trans = shift_image(image_src=r_image, at=at)
    g_trans = shift_image(image_src=g_image, at=at)
    b_trans = shift_image(image_src=b_image, at=at)
    image_trans = np.dstack(tup=(r_trans, g_trans, b_trans))
  else:
    image_trans = shift_image(image_src=image_src, at=at)

  if with_plot:
    cmap_val = None if not gray_scale else 'gray'
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 20))

    ax1.axis("off")
    ax1.title.set_text('Original')

    ax2.axis("off")
    ax2.title.set_text("Translated")

    ax1.imshow(image_src, cmap=cmap_val)
    ax2.imshow(image_trans, cmap=cmap_val)
    plt.show()
    output_name = "output" + str(at) + ".png"
    print("Saving aligned image : ", output_name)
    cv2.imwrite(output_name, image_trans)
    return True
  return image_trans

translate(
    img='/Users/natalka/PycharmProjects/image_registration_algorithm/lenna-black.png',
    at=(+63, 0),
    with_plot=True,
    gray_scale=False
)