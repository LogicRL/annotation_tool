import sys
import shutil

FILE_PATH = '/Users/wangwei/Desktop/10703DeepRL/proj/imgLevel1Label/'
FILE_TYPE = '.txt'

def copy_file(src_idx, goal_start, goal_end):
	old_file = FILE_PATH + str(src_idx) + FILE_TYPE
	for i in range(goal_start, goal_end+1):
		new_file = FILE_PATH + str(i) + FILE_TYPE
		shutil.copy(old_file, new_file)


if __name__ == '__main__':
	src_idx = int(sys.argv[1])
	goal_start = int(sys.argv[2])
	goal_end = int(sys.argv[3])
	copy_file(src_idx, goal_start, goal_end)