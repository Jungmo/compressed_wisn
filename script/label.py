import os

def dot_name(k, size):
	return str(k)+"_"+str(size)+"_DOT"
CURRENT_DIR = os.getcwd()
LABEL = {"swallow":4, "bluebird":0, "egg":2, "empty":3, "child":1}

SIZE = [150,140,130,120,110, 100, 90, 80, 70, 60, 50]
K = [8,16,32,256]
for size in SIZE:
	for k in K:
		f = open(dot_name(k, size)+".txt", "w")
		IMG_ROOT = os.path.join(CURRENT_DIR, dot_name(k, size)) 
		for directory, label in LABEL.iteritems() :
			TARGET_DIR = os.path.join(IMG_ROOT, directory)
			image_list = os.listdir(TARGET_DIR)
			for image in image_list:
				f.write(os.path.join(TARGET_DIR, image) + " "+str(label)+"\n")	
