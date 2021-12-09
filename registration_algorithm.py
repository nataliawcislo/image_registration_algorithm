from __future__ import print_function
import cv2
import numpy as np
import imutils



def alignImages(im1, im2, MAX_FEATURES, GOOD_MATCH_PERCENT):
  # Convert images to grayscale
  im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
  im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

  # Detect ORB features and compute descriptors.
  orb = cv2.ORB_create(MAX_FEATURES)
  keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
  keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

  # Match features.
  matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matches = matcher.match(descriptors1, descriptors2, None)

  # Sort matches by score
  # matches.sort(key=lambda x: x.distance, reverse=False)
  #
  # # Remove not so good matches
  # numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
  # matches = matches[:numGoodMatches]

  matches = sorted(matches, key=lambda x: x.distance)
  # keep only the top matches
  numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
  matches = matches[:numGoodMatches]

  # Draw top matches
  imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
  imMatches = imutils.resize(imMatches, width=1000)
  cv2.imshow = ("Matched Keypoints", imMatches)
  cv2.imwrite("frame_match_" + str(MAX_FEATURES) + "_" + str(GOOD_MATCH_PERCENT) + ".jpg", imMatches)

  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)

  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt

  # Find homography
  h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

  # Use homography
  height, width, channels = im2.shape
  im1Reg = cv2.warpPerspective(im1, h, (width, height))

  return im1Reg, h

def download_image(MAX_FEATURES,GOOD_MATCH_PERCENT):
  MAX_FEATURES = MAX_FEATURES
  GOOD_MATCH_PERCENT = GOOD_MATCH_PERCENT
  # Read reference image
  refFilename = '/Users/natalka/PycharmProjects/image_registration_algorithm/f2/frame-2.jpg_01_02.png'

  print("Reading reference image : ", refFilename)
  imReference = cv2.imread(refFilename,cv2.IMREAD_COLOR)
  # imReference = cv2.cvtColor(imReference,  cv2.COLOR_BGR2GRAY)

  # Read image to be aligned
  imFilename = '/Users/natalka/PycharmProjects/image_registration_algorithm/f3/frame-3.jpg_01_02.png'
  print("Reading image to align : ", imFilename);
  im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
  # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  #   im = cv2.cvtColor(im, cv2.IMREAD_COLOR)
  print(type(im))

  print("Aligning images ...")
  # Registered image will be resotred in imReg.
  # The estimated homography will be stored in h.
  imReg, h = alignImages(im, imReference, MAX_FEATURES, GOOD_MATCH_PERCENT)

  # Write aligned image to disk.
  outFilename = "output_" + str(MAX_FEATURES) + "_" + str(GOOD_MATCH_PERCENT) + ".jpg"
  print("Saving aligned image : ", outFilename)
  cv2.imwrite(outFilename, imReg)

  # Print estimated homography
  print("Estimated homography : \n",  h)

#Test
#download_image( MAX_FEATURES = 10000, GOOD_MATCH_PERCENT = 0.6)
#download_image(MAX_FEATURES=1000, GOOD_MATCH_PERCENT=0.8)