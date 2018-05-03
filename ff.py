from pathlib import Path
import sys

from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

currentFolder = Path(".")
folders = [".."]
for entry in currentFolder.iterdir():
  if not entry.is_dir(): continue
  if entry.name.startswith("."): continue
  folders.append(entry)

folder = prompt(
  message="> ", 
  auto_suggest=AutoSuggestFromHistory(),
  completer=WordCompleter(str(f) for f in folders),
  history=FileHistory("c:/temp/ff_history.txt")
)

with open("c:/temp/ff.txt", "wt", encoding="utf8") as f:
  print(folder, file=f)

sys.exit(0)
