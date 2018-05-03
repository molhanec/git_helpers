import os

from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

from colorama import init
init()

commands = {
  "Status": "git status",
  "Confirm changes in all modified files": "git commit -a",
  "Confirm all already stages changes": "git commit",
  "Stage all new and changed files": "git add --all",
  "Create repository": "git init",
} 

try:
  command = prompt(
    message="> ", 
    auto_suggest=AutoSuggestFromHistory(),
    completer=WordCompleter(commands.keys()),
    history=FileHistory("c:/temp/gg_history.txt")
  )
  print("\n\t\033[33m", commands[command], "\033[0m\n")
  os.system(commands[command])
except KeyboardInterrupt:
  print("Cancelling...")
  pass
  
