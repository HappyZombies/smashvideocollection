#!/bin/bash
while true; do
git status
git add --all
git status
#git status for debugging
git commit -m "Updated voting page."
git push origin gh-pages
echo "Done updating....Now Waiting..."
sleep 86405
clear
done
