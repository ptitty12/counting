#!/bin/bash
# Run by a Dokploy schedule inside the "counting" compose container.
# Keeps its own clone of the repo under /data/repo (persistent bind mount) and pushes from there
# with the deploy key in /data/ssh (add its .pub to GitHub -> repo Settings -> Deploy keys, "Allow write access").
set -e
REPO_PATH=${REPO_PATH:-/data/repo}
if [ ! -d "$REPO_PATH/.git" ]; then
  git clone git@github.com:ptitty12/counting.git "$REPO_PATH"
fi
cd "$REPO_PATH"
git config user.name  "${GIT_USER_NAME:-ptitty12}"
git config user.email "${GIT_USER_EMAIL:-PatrickTaylorUNL@gmail.com}"
git pull --rebase -q origin main || true
REPO_PATH="$REPO_PATH" python /app/update_counter.py
