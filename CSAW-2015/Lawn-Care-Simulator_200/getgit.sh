#!/bin/bash

# Curls the generic files within a .git folder for structure
mkdir -p .git/
cd .git/;
mkdir -p {hooks,info,objects/{info,pack},refs/{heads,tags}};
for file in HEAD config description info/exclude refs/heads/master; do
  curl "http://54.175.3.248:8089/.git/${file}" > "${file}";
done;
cd ..;
