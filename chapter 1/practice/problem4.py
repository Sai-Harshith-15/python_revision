# write a python program to print the contents of a directory using the os module. 
# the program should print the name of each file and subdirectory in the directory. 
import os
# specify the directory you want to print the contents of
directory = '/Git Repo'
# use the listdir() function to get a list of all files and subdirectories in the directory
files_and_subdirectories = os.listdir(directory)
# print the contents of the directory
for file_or_subdirectory in files_and_subdirectories:
  print(file_or_subdirectory)
  