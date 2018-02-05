import os
import cv2

def dot_name(k, size):
	return str(k)+"_"+str(size)+"_DOT"
CURRENT_DIR = os.getcwd()

K = ["256","32", "16", "8"]
SIZE = [150,140,130,120,110, 100]
CLASS = ["bluebird", "child", "egg", "empty", "swallow"]

for k in K:
	origin_root = os.path.join(CURRENT_DIR , dot_name(k, 200))
	for size in SIZE:
		os.mkdir(os.path.join(CURRENT_DIR, dot_name(k,size)))
		target_root = os.path.join(CURRENT_DIR, dot_name(k, size))
		for c in CLASS:
			os.mkdir(os.path.join(target_root,c))
			c_list = os.listdir(os.path.join(origin_root, c))
			for f in c_list:
				if not "bmp" in f:
					continue
				image = cv2.imread(os.path.join(origin_root, c, f), 0)
				resized = cv2.resize(image, (size, size)) #Bilinear rescaling algorithm
				save_path = os.path.join(target_root, c, f)
				cv2.imwrite(save_path, resized)
				
