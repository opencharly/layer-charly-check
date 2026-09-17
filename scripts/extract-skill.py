#!/usr/bin/env python3
# extract-skill.py — pull one of the jetkvm-skill method lists out of a
# layer-charly-check charly.yml, so it can be diffed against the plugin's sets.
#
#   usage: python3 extract-skill.py charly.yml {readonly|mutating|never}
import re
import sys

text = open(sys.argv[1]).read()
# The three lists, in order, each ending at the next heading (or a blank line).
patterns = {
    "readonly": r"Read-only \(no gate\):(.*?)\n\n",
    "mutating": r"Mutating \(need `allow_control: true`\):(.*?)\n\n",
    "never": r"Never autonomous:(.*?)\n\n",
}
block = re.search(patterns[sys.argv[2]], text, re.S)
if not block:
    sys.exit(f"could not find the {sys.argv[2]} section")
print("\n".join(sorted(set(re.findall(r"`([a-z-]+)`", block.group(1))))))
