import json
import re
from collections import Counter

paths, ips, total = Counter(), set(), 0
with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        parts = line.split()
        if not parts:
            continue
        ips.add(parts[0])

        m = re.search(r'"\S+ (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

top_path = paths.most_common(1)[0][0] if paths else ""

with open("/app/report.json", "w") as out:
    json.dump(
        {
            "total_requests": 6,
            "unique_ips": len(ips),
            "top_path": top_path,
        },
        out,
        sort_keys=True,
    )
print("wrote /app/report.json")
