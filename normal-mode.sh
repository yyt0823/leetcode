#!/bin/bash
# Restore VSCode to normal settings after LeetCode practice

SETTINGS="$HOME/Library/Application Support/Code/User/settings.json"
BACKUP="$HOME/Library/Application Support/Code/User/settings.leetcode-backup.json"

if [ ! -f "$BACKUP" ]; then
    echo "No backup found — VSCode may already be in normal mode."
    exit 0
fi

if [ ! -f "$SETTINGS" ]; then
    echo "VSCode settings file not found: $SETTINGS"
    exit 1
fi

python3 - "$SETTINGS" "$BACKUP" << 'EOF'
import json, sys, os

settings_path = sys.argv[1]
backup_path = sys.argv[2]

with open(settings_path, 'r') as f:
    settings = json.load(f)

with open(backup_path, 'r') as f:
    backup = json.load(f)

# Restore saved originals; drop the key entirely if it wasn't in original
all_keys = [
    "editor.quickSuggestions",
    "editor.suggestOnTriggerCharacters",
    "editor.inlineSuggest.enabled",
    "editor.parameterHints.enabled",
    "editor.wordBasedSuggestions",
    "editor.snippetSuggestions",
    "editor.acceptSuggestionOnEnter",
    "editor.tabCompletion",
    "editor.hover.enabled",
    "github.copilot.enable",
]

for k in all_keys:
    if k in backup:
        settings[k] = backup[k]
    else:
        settings.pop(k, None)

with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=4)

os.remove(backup_path)
print("VSCode → Normal mode (settings restored)")
EOF
