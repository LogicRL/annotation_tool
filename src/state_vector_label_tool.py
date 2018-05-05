
import os
import sys

import shutil
#install python-editor
import editor



import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time


PROJ_PATH = os.path.abspath(os.path.dirname(os.getcwd()))
IMG_PATH = PROJ_PATH + '/data/imgLevel1Label_20180504_01/'
IMG_TYPE = '.png'
ANN_TYPE = '.txt'


KEY_SPACE = ord(' ') # 32
KEY_E = ord('e') #edit



def label(start_idx, end_idx):
	for cur_i in range(start_idx, end_idx + 1):
		cur_ann_file = IMG_PATH + str(cur_i) + ANN_TYPE
		if os.path.exists(cur_ann_file):
			sys.exit("Current annotation file " +str(cur_i) + ANN_TYPE + " exists, please check!")
		else:
			copyAnnotation(cur_i)
		showImg(cur_i)

def copyAnnotation(cur_i):
	pre_ann = IMG_PATH + str(cur_i - 1) + ANN_TYPE
	new_ann = IMG_PATH + str(cur_i) + ANN_TYPE
	if os.path.exists(pre_ann) == False:
		sys.exit("PreFrame annotation file " +str(cur_i - 1) + ANN_TYPE + " not exists, please check!")
	else:
		shutil.copy(pre_ann, new_ann)

def showImg(img_i):
	print str(img_i)
	ann_file = IMG_PATH + str(img_i) + ANN_TYPE
	f = open(ann_file, "r")
	ann_str = f.read()
	f.close()

	img_name = IMG_PATH + str(img_i) + IMG_TYPE
	img = mpimg.imread(img_name)

	plt.subplot(1, 2, 1)
	plt.axis('off') 
	plt.imshow(img)
	plt.title(str(img_i))
	plt.subplot(1, 2, 2)
	plt.axis('off') 
	plt.text(0, 0, ann_str)

	#plt.show()
	plt.ion()
	plt.pause(0.01)
	key = raw_input("Press Space to annotate next frame. Press E to edit annotation.")
	if key == "e":
		editor.edit(ann_file)
	elif key == " ":
		plt.close()
	else:
		sys.exit("Unknown key")
	plt.close()


#def load_annotation(img, ann):
	


if __name__ == '__main__':
	start_idx = int(sys.argv[1])
	end_idx = int(sys.argv[2])
	label(start_idx, end_idx)

	#message = input()
