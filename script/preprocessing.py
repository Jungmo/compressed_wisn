# -*- coding: utf-8 -*-
import numpy as np
import cv2
import collections
#import globalvariable as gv



def get_centroid(k):
    ret_centroid = []
    if k == 8:
        ret_centroid = [15, 47, 79, 111, 143, 175, 207, 239]
    elif k == 16:
        ret_centroid = [7, 23, 39, 55, 71, 87, 103, 119, 135, 151, 167, 183, 199, 215, 231, 247]
    elif k == 32:
	ret_centroid = [3 + 8*num for num in range(32)] 
    return ret_centroid


def drop_image_quality(image, k):
    centroid = []
    if k == 8:
        centroid = [15, 47, 79, 111, 143, 175, 207, 239]
    elif k == 16:
        centroid = [7, 23, 39, 55, 71, 87, 103, 119, 135, 151, 167, 183, 199, 215, 231, 247]
    elif k == 32:
	centroid = [3 + 8*num for num in range(32)] 
    x = 0
    y = 0
    dropped_image = image.copy()

    centroid_length = len(centroid)
    k = 0
    while(1):
	centroid_length = centroid_length >> 1
        k += 1
        if centroid_length == 1:
		break


    for i in dropped_image:
        for j in i:
            nearest_index = get_nearest_centroid(j, k)
            try:
		dropped_image[x][y] = centroid[nearest_index]
            except IndexError:
		print nearest_index				 
	        div = 256 >> k
	        sub = 2 << ((8-k-1)) - 1

	        ret = (j-sub) / div

	        if (j-sub)% div > sub+1:
		    ret = ret + 1
    		print j, div, sub, ret, (j-sub)%div
		exit()
	    y += 1
        x += 1
        y = 0
    return dropped_image


# TODO:O(log n)
def get_nearest_centroid(pixel, k):
    
    div = 256 >> k
    sub = 2 << ((8-k-1)) - 1

    ret = (pixel-sub) / div

    if (pixel-sub)% div > sub+1:
	ret = ret + 1
    return ret


def get_feature_for_make_model(cropped_image):
    area = [0] * gv.numofcentroid
    centroid = get_centroid(gv.numofcentroid)
    for x in range(gv.width):
        for y in range(gv.width):
            i = centroid.index(cropped_image[x][y])
            area[i] += 1
    return area


def pop_image(image):
    cv2.namedWindow("POP_IMAGE", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("POP_IMAGE", image)
    cv2.waitKey(0)
