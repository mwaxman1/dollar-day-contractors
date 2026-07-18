
import re

file_path = '/home/mike/projects/dollar-day-contractors/index.html'
with open(file_path, 'r') as f:
    content = f.read()

# Replacing #pricing anchors with the specific Gumroad URLs in order of appearance
urls = [
    "https://threadmaster47.gumroad.com/l/wa-hvac-starter-weekly",
    "https://threadmaster47.gumroad.com/l/wa-hvac-pro",
    "https://threadmaster47.gumroad.com/l/wa-hvac-backlog"
]

matches = list(re.finditer(r'href="#pricing"', content))
if len(matches) >= 3:
    offset = 0
    for i, match in enumerate(matches):
        start = match.start() + offset
        end = match.end() + offset
        content = content[:start] + f'href="{urls[i]}"' + content[end:]
        offset += len(urls[i]) - len("#pricing")
    
    with open(file_path, 'w') as f:
        f.write(content)
    print("SUCCESS: Replaced 3 pricing anchors with real Gumroad URLs.")
else:
    print(f"FAILURE: Found {len(matches)} anchors, expected 3.")
