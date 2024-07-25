#!/bin/bash

# Example script to switch between GitHub repositories

REPO_A="https://github.com/user/repo_a.git"
REPO_B="https://github.com/user/repo_b.git"

case "$1" in
  "a")
    git remote set-url origin $REPO_A
    echo "Switched to Repo A"
    ;;
  "b")
    git remote set-url origin $REPO_B
    echo "Switched to Repo B"
    ;;
  *)
    echo "Usage: $0 {a|b}"
    exit 1
    ;;
esac