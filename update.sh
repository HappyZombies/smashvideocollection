#!/bin/bash
while true; do
git pull origin gh-pages
git status
git add --all
git status
#git status for debugging
git commit -m "Updated site with new content."
git push origin gh-pages
echo "Done updating....Now Waiting..."
sleep 86405
#not that long of a wait
clear
done