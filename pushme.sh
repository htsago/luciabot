# Pull Updates before push yours!
git pull
git fetch
commit=$1
git add *
git commit -m "$commit"
git push