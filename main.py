import subprocess
import os

executedCommands = []

def execute(command):
  try:
    subprocess.run(command)
    executedCommands.append(command)
  except Exception:
    print("pyshell: Comando no encontrado")


def history():
  stdout = ""
  for command in executedCommands:
    stdout = f"{command}\n"
    print(stdout)
def cd(path):
  try:
    os.chdir(path)
  except Exception:
    print(f"pyshell: Error cambiando de directorio")

def main():
  while True:
    terminalPath = f"{os.getcwd()} > "
    command = input(terminalPath)
    if command == "exit":
      exit(-1)
    elif command[:3] == "cd ":
      cd(command[3:])
    elif command[:3] == "cd":
      pass
    elif command == "history":
      history()
    else:
      execute(command)

if __name__ == "__main__":
  main()
