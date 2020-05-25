import os

print(os.getcwd())

os.chdir('/home/eminentfablous')

print(os.getcwd())

# os.mkdir('/home/eminentfablous/PycharmProjects/PythonScripting/NewFolder')
# os.rmdir('/home/eminentfablous/PycharmProjects/PythonScripting/NewFolder')

print(os.path.join('/home/eminentfablous/PycharmProjects/PythonScripting',
                   '/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))

print(os.path.split('/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))

print(os.path.exists('/home/eminentfablous/PycharmProjects/PythonScripting/sysmodule.py'))

pas = dir(os)
for i in pas:
    print(i)
