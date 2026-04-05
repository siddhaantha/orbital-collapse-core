#!/bin/bash

set -e

echo "💣 Injecting chaos into repository..."

# -------------------------
# Normalize branch name
# -------------------------
CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" = "master" ]; then
    git branch -m master main
fi

git checkout main

# -------------------------
# DEV TELEMETRY BRANCH (Merge conflict)
# -------------------------
git checkout -b dev-telemetry

sed -i 's/Satellite data received/Telemetry stream unstable/' telemetry/parser.py
git add .
git commit -m "refactor telemetry parser output"

# -------------------------
# DEV AUTH BRANCH (Deep conflict)
# -------------------------
git checkout main
git checkout -b dev-auth

sed -i 's/Operator verified/Auth success: operator cleared/' auth/login.py
git add .
git commit -m "auth message updated"

# Modify same line differently → future conflict
sed -i 's/Auth success: operator cleared/Auth OK/' auth/login.py
git add .
git commit -m "simplified auth response"

# -------------------------
# DEV LAUNCH (Bad commits)
# -------------------------
git checkout main
git checkout -b dev-launch

echo "def dispatch_command():
    return '[DISPATCH] FAILED'" > launch-sequence/dispatcher.py

git add .
git commit -m "changed dispatch logic (broken)"

echo "# temporary debug" >> launch-sequence/dispatcher.py
git add .
git commit -m "debug commit"

# -------------------------
# DEV GROUND (File deletion)
# -------------------------
git checkout main
git checkout -b dev-ground

git rm ground-control/dashboard.py
git commit -m "removed unused dashboard (accidental)"

# Add misleading new file
echo "def display_status():
    return '[GROUND] UNKNOWN STATE'" > ground-control/status_view.py

git add .
git commit -m "new status view added"

# -------------------------
# HOTFIX (Old base → rebase conflict)
# -------------------------
git checkout main
OLD_COMMIT=$(git rev-list --max-parents=0 HEAD)

git checkout -b hotfix-critical $OLD_COMMIT

sed -i 's/Operator verified/Operator verified [HOTFIX]/' auth/login.py
git add .
git commit -m "critical hotfix applied"

# -------------------------
# EXPERIMENTAL REWRITE (Messy history)
# -------------------------
git checkout main
git checkout -b experimental-rewrite

echo "# rewrite attempt" >> telemetry/parser.py
git add .
git commit -m "wip"

echo "# more changes" >> telemetry/parser.py
git add .
git commit -m "wip2"

echo "# final tweak" >> telemetry/parser.py
git add .
git commit -m "final maybe"

# -------------------------
# Create divergence on main (for conflict)
# -------------------------
git checkout main

sed -i 's/Satellite data received/Data stream nominal/' telemetry/parser.py
git add .
git commit -m "main telemetry update"

echo "💥 Chaos successfully injected."
echo "Branches created:"
git branch
