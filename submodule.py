import subprocess

p1 = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE)  # This helps to store the value of the expression
print(p1.stdout.decode())  # The decode changes this to string

with open('oupput.txt', 'w') as f:
    p1 = subprocess.run(['pip', 'list'], stdout=f)
    # This send the content of p1 to output.txt

p2 = subprocess.run(['ls', '-la', 'dne'], stdout=subprocess.PIPE)
print(p2.returncode)
print(p2.stderr)

p3 = subprocess.run(['ls', '-la', 'dne'], stderr=subprocess.DEVNULL)
print(p3.stderr)

p4 = subprocess.run(['cat', 'oupput.txt'], stdout=subprocess.PIPE)
# print(p4.stdout.decode())

p5 = subprocess.run(['grep', '-n', 'pip'], stdout=subprocess.PIPE, input=p4.stdout)
print(p5.stdout)

p6 = subprocess.run('cat oupput.txt | grep -n pip', stdout=subprocess.PIPE, shell=True)
print(p6.stdout.decode())

#subprocess.run('git init', shell=True)
subprocess.run('touch .gitignore', shell=True)

with open('.gitignore', 'w') as f:
    f.write('venv')