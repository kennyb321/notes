# working with github through command line

### adding files to repository 
First need to 
-create repository on Github
-Cloned repository locally on your computer

##### Cloning repository
When you create a repo on GitHub, it exists as a remote reposiotry. You can clone your repo to create a local copy on your computer and sync between the two locations
1)On github, navigate to the main page of the repo.
2)Under repo name, click **Clone or Download**.
3)Copy the clone URL.
4) Open Terminal
5) Change the cwd (current working directory) to the location where you want the cloned directory to be made.
6) type `` git clone``, then paste URL you copied from before.
7)Press Enter, Your local Clone will be created.
you should see
```
Cloning into 'notes'...
remote: Enumerating objects: 48, done.
remote: Counting objects: 100% (48/48), done.
remote: Compressing objects: 100% (45/45), done.
remote: Total 48 (delta 19), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (48/48), done.
```

### Adding files to repo (cont)
1) Move file youde like to upload into the direcotry that you cloned the repo into.
2) Open Terminal
3) Change cwd to local repo.
4)stage the file for commit to your local repo.
``` 
git add
```
this adds the file to your local repo and stages it for commit. To unstage a file, use
```
git reset HEAD YOUR-FILE'
```

5) Commit the file youve staged in your local repo.
```
git commit  -m "add existing file"
```
this commits the tracked changes and prepares them to be pusged to a remote repo.

6)

**Push the changes** in your local repo to GitHub
```
git push origin *your-branch*
```
this pushes the changes in your local repo up to the remote repo
you specified as the origin.

 
