mkdir codeops-portfolio && cd codeops-portfolio
Creates a new folder named codeops-portfolio and immediately navigates inside it.

git init
Initializes a brand-new, empty local Git repository in your current folder so Git can start tracking changes.

echo "# CodeOps Portfolio" > README.md
Creates a file named README.md and writes the header # CodeOps Portfolio inside it.

git add README.md
Stages the new README file, telling Git to include it in the next commit.

git commit -m "Add README"
Saves your staged changes to your local Git history with the descriptive message "Add README".

git remote add origin <your-repo-url>
Links your local repository to a remote server (like GitHub or GitLab) and names that link origin.

git push -u origin main
Uploads your local commits to the main branch of your remote repository. The -u flag sets it as the default upstream branch, meaning next time you can just type git push.