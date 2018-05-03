ff () {
  winpty -- python $DROPBOX/util/git_helpers/ff.py
  FOLDER=`cat /c/temp/ff.txt` 
  cd "$FOLDER"
}

gg () {
  winpty -- python $DROPBOX/util/git_helpers/gg.py
}
