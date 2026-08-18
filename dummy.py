import subprocess

user_input = input("Command: ")
# should block & comment on the below
subprocess.run(user_input, shell=True)