import os
from datetime import datetime

print(os.getcwd())

os.chdir('/home/eminentfablous')

print(os.getcwd())

# os.mkdir('/home/eminentfablous/PycharmProjects/PythonScripting/NewFolder')
# os.rmdir('/home/eminentfablous/PycharmProjects/PythonScripting/NewFolder')

print(os.path.join('/home/eminentfablous/PycharmProjects/PythonScripting',
                   '/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))

print(os.path.split('/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))

print(os.path.exists('/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))
"""
pas = dir(os)
for i in pas:
    print(i)

"""

# os.mkdir('OSDD')
# os.makedirs('opp/hhh/iiii')

# os.rmdir('OSDD')
# os.removedirs('opp/hhh/iiii')

# os.rename('Videos', 'vid')
print(os.listdir())
print(os.stat('vid').st_mtime)
mod_time = os.stat('vid').st_mtime
print(datetime.fromtimestamp(mod_time))