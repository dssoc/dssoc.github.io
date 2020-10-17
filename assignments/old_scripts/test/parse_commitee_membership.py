

import json
import pandas as pd

with open('committee-membership-current.json', 'r') as f:
    d = json.load(f)

print(d.keys())


rows = list()

for committee, members in d.items():
    for member in members:
        row = member.copy()
        row['committee'] = committee
        rows.append(row)

df = pd.DataFrame(rows)

df.to_csv('committee_membership.csv')


