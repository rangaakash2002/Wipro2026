import subprocess
result=subprocess.run("echo welcome to python",shell=True,capture_output=True,text=True)
print(result.stdout)
