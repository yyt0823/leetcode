#!/bin/bash
# Switch VSCode to minimal mode for LeetCode practice

SETTINGS="$HOME/Library/Application Support/Code/User/settings.json"
BACKUP="$HOME/Library/Application Support/Code/User/settings.leetcode-backup.json"

if [ ! -f "$SETTINGS" ]; then
    echo "VSCode settings file not found: $SETTINGS"
    exit 1
fi

python3 - "$SETTINGS" "$BACKUP" << 'EOF'
import json, sys, shutil, os

settings_path = sys.argv[1]
backup_path = sys.argv[2]

with open(settings_path, 'r') as f:
    settings = json.load(f)

# Keys we will override — save originals for restore
keys_to_save = [
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

# Only write backup if one doesn't already exist
if not os.path.exists(backup_path):
    backup = {k: settings[k] for k in keys_to_save if k in settings}
    with open(backup_path, 'w') as f:
        json.dump(backup, f, indent=4)

# Apply minimal / no-assist settings
settings["editor.quickSuggestions"] = {"other": "off", "comments": "off", "strings": "off"}
settings["editor.suggestOnTriggerCharacters"] = False
settings["editor.inlineSuggest.enabled"] = False
settings["editor.parameterHints.enabled"] = False
settings["editor.wordBasedSuggestions"] = "off"
settings["editor.snippetSuggestions"] = "none"
settings["editor.acceptSuggestionOnEnter"] = "off"
settings["editor.tabCompletion"] = "off"
settings["editor.hover.enabled"] = False
settings["github.copilot.enable"] = {"*": False}

with open(settings_path, 'w') as f:
    json.dump(settings, f, indent=4)

print("VSCode → LeetCode mode (all suggestions off, Copilot off)")
EOF
