#!Python3 
# nameChanger - a simple program to change the names of annoying names Offliberty files

import os

print('Name Changer 0.0.1a')

# navigate to the directory
os.chdir('/Users/poisonarena/Desktop/target')

join = os.path.join




# This is fucked up and janky, but you have to use A, run the script, then B, 
# commenting the other out, also cuz stupid mac there are DS Store files that need 
# to be removed with 'rm -f .DS_Store' in target directory

for file in os.listdir("."):
	old = file
	os.rename(join(file), join(file[:-19]))
	#os.rename(join(file), join(old + ".mp3"))

print('...done')