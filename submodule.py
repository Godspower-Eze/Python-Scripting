import subprocess

"""
The subprocess module is used to run codes that should have been run on the terminal in python itself
"""
p1 = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE)
"""
This .run method is where the code is inputed
and the first could be a string but we need to add shell=True for it to work
for e.g subprocess.run('pip list', shell=True).
Also, the stdout=subprocess.PIPE helps it to be able to stored in varable rather it would store None as
its value.
"""

print(p1.stdout.decode())
# The decode changes this to string

with open('oupput.txt', 'w') as f:
    p1 = subprocess.run(['pip', 'list'], stdout=f)
    # This send the content of p1 to output.txt

p2 = subprocess.run(['ls', '-la', 'dne'], stdout=subprocess.PIPE)
print(p2.returncode)
# returncode is a number that shows if the code was run suceessfully or not. 0 represents successfully but every other number is an error
print(p2.stderr)
p3 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)
print(p3.stderr)

p4 = subprocess.run(['cat', 'oupput.txt'], stdout=subprocess.PIPE)
# print(p4.stdout.decode())

p5 = subprocess.run(['grep', '-n', 'pip'], stdout=subprocess.PIPE, input=p4.stdout)
print(p5.stdout)
# In this example, i used the output of p4 as the input of p5

p6 = subprocess.run('cat oupput.txt | grep -n pip', stdout=subprocess.PIPE, shell=True)
print(p6.stdout.decode())

subprocess.run('git init', shell=True)
# In this example, i used it to create a github initialization for this project
subprocess.run('touch .gitignore', shell=True)
# i created a gitignore file with it
with open('.gitignore', 'w') as f:
    f.write('venv')
    # Here, i added the venv folder to gitignore
