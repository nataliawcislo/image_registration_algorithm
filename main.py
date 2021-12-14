import matplotlib.pyplot as plt
from PIL import Image
from registration_algorithm import download_image

#The best
# MAX_FEATURES = 10000
# GOOD_MATCH_PERCENT = 0.6

# MAX_FEATURES = 10000
# GOOD_MATCH_PERCENT = 0.6
refFilename = '/Users/natalka/PycharmProjects/image_registration_algorithm/output-2.jpg'
imFilename = '/Users/natalka/PycharmProjects/image_registration_algorithm/output-3.jpg'

def main(refFilename, imFilename):
  #MAX_FEATURES_array = [500]
  MAX_FEATURES_array = [8000]
  GOOD_MATCH_PERCENT_array = [0.8, 0.6, 0.4]

  MAX_FEATURES = 0
  GOOD_MATCH_PERCENT = 0
  for max_f in MAX_FEATURES_array:
    MAX_FEATURES = max_f
    for good_match_p in GOOD_MATCH_PERCENT_array:
        GOOD_MATCH_PERCENT = good_match_p
        try:
          download_image(MAX_FEATURES,GOOD_MATCH_PERCENT, refFilename, imFilename)
        except:
          print("less:" + str(GOOD_MATCH_PERCENT_array))

main(refFilename, imFilename)
