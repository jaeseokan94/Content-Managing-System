# Content Managing System for Android app
cms - paragon , Django + Android project
Git merge (Branch into master) http://stackoverflow.com/questions/5601931/best-and-safest-way-to-merge-a-git-branch-into-master

    git checkout master
    git pull origin master
    git merge test
    git push origin master

Remove pyc file in git https://yuji.wordpress.com/2010/10/29/git-remove-all-pyc/

    find . -name "*.pyc" -exec git rm -f {} \;

Going back to certain commit http://stackoverflow.com/questions/4114095/revert-git-repo-to-a-previous-commit

    git reset 56e05fced (commit name)
    git reset --soft HEAD@{1}
    git commit -m "Revert to 56e05fced"
    git reset --hard

Git new branch - Local 

    git checkout -b your_branch
    

and then push it to remote. 

    git push origin <branch-name>
