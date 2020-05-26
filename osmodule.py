import os
from datetime import datetime

print(os.getcwd())
# This prints out the current working directory where getcwd means " get current working directory"

os.mkdir('/home/eminentfablous/PycharmProjects/PythonScripting/NewFolder')
# This makes a directory
os.makedirs('opp/hhh/iiii')
# This makes multiple directories at once
os.rmdir('/home/eminentfablous/PycharmProjects/PythonScripting/NewFolder')
# This removes a directory
os.removedirs('opp/hhh/iiii')
# This removes multiple directories at once

print(os.path.join('/home/eminentfablous/PycharmProjects/PythonScripting',
                   '/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))
# This joins directories to be one path

print(os.path.split('/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))
# This splits directiories into seperate parts

print(os.path.exists('/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))
# This prints true or false depending whether file or directory exists

pas = dir(os)
for i in pas:
    print(i)
# This prints out all the methods under the os module


os.rename('Videos', 'vid')
# This renames a file or directory
print(os.listdir())
# This lists the files and directories of a path
print(os.stat('vid').st_mtime)
# This prints necessary informations about a file or directory
mod_time = os.stat('vid').st_mtime
# This is the modification time of the vid directory
print(datetime.fromtimestamp(mod_time))
# Using the datatime module, the mod_time is converted to human readable format

for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directory:', dirname)
    print('Files:', filename)
"""
This is a generator that yeilds a tuple of tree values as its walking the directory.
For each directory it sees, it yeilds the directory path, directories within that path 
and the files within that path. These can be useful if you want to search through path for files and
directories
"""

print(os.environ)
# This prints out the environment variables. Environment variables are variables that store the path of directories
print(os.environ.get('HOME'))
# This gets a particular path using its environmental variable
file_name = os.path.join(os.environ.get('HOME'), 'text.py')
# This joins the path of the environment variables and the 'text.py' file. Note that joining does not create the file
print(file_name)
