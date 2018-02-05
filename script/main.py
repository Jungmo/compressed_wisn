import preprocessing as pp
import os
import cv2

ROOT = os.getcwd()
DIRS = ["swallow", "bluebird", "egg", "empty", "child"]
K = [32, 16, 8]

for k in K:
	try:
		os.mkdir(str(k))
	except OSError:
		pass
	for directory in DIRS:
		try:
			os.mkdir(os.path.join(str(k),directory))
		except OSError:
			pass	
 		target = os.path.join(ROOT, directory)
		filelist = os.listdir(target)
		for name in filelist:
			if 'DS' in name:
				continue
			target_image = os.path.join(target, name)
			image = cv2.imread(target_image, 0)
			quantized_image = pp.drop_image_quality(image, k)
			cv2.imwrite(os.path.join(ROOT, str(k),directory,name[:-4]+"_"+str(k)+".bmp"),quantized_image)
