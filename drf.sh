#!/bin/bash

if [[ -d /home/$USER/Pictures/dracula-factory ]]; then
  echo "AWESOME! dir [~/Pictures/dracula-factory/] already exists."
else
  mkdir /home/$USER/Pictures/dracula-factory
  echo "dir [~/Pictures/dracula-factory/] has been created successfully!"
fi

if [[ -z $1 ]]; then
  drfpy
else
  drfpy $1
fi
