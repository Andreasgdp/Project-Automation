cd C:\Users\<your username>\Documents\create-repositories\
python create.py %1
cd C:\Users\<your username>\Documents\Projects\%1
git init
git remote add origin https://github.com/Andreasgdp/%1.git
type NUL > README.md
git add .
git commit -m "Initial commit"
git push -u origin master
code-insiders .