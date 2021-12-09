import matplotlib.pyplot as plt
from PIL import Image
from registration_algorithm import download_image

#The best
# MAX_FEATURES = 10000
# GOOD_MATCH_PERCENT = 0.6

# MAX_FEATURES = 10000
# GOOD_MATCH_PERCENT = 0.6

img = "/Users/natalka/PycharmProjects/image_registration_algorithm/frame/frame-2.jpg"
img2 = "/Users/natalka/PycharmProjects/image_registration_algorithm/frame/frame-3.jpg"



def main():
  #MAX_FEATURES_array = [500]
  MAX_FEATURES_array = [100, 300, 50 ,500, 1000,2000, 3000, 4000, 5000,8000, 10000, 50000]
  GOOD_MATCH_PERCENT_array = [ 0.2, 0.4,0.5, 0.6,0.7, 0.8, 0.9]

  MAX_FEATURES = 0
  GOOD_MATCH_PERCENT = 0
  for max_f in MAX_FEATURES_array:
    MAX_FEATURES = max_f
    for good_match_p in GOOD_MATCH_PERCENT_array:
        GOOD_MATCH_PERCENT = good_match_p
        try:
          download_image(MAX_FEATURES,GOOD_MATCH_PERCENT)
        except:
          print("less:" + str(GOOD_MATCH_PERCENT_array))


main()






#