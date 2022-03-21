

import json
import pandas as pd
import pprint

if __name__ == '__main__':

    with open('committees-current.json', 'r') as f:
        committee_data = json.load(f)

    with open('committee-membership-current.json', 'r') as f:
        membership_data = json.load(f)

    # will output to this file
    writer = pd.ExcelWriter('committees.xlsx', engine='xlsxwriter')

    ########### Parse Committee Information ###########
    committees = list()
    subcommittees = list()
    for committee in committee_data:

        if 'subcommittees' in committee:
            subcomms = committee['subcommittees']
            del committee['subcommittees']
            print(f'{len(subcomms)} committees')

            for subcomm in subcomms:
                subcomm['committee_thomas_id'] = committee['thomas_id']
                subcommittees.append(subcomm)

        committees.append(committee)

    df_c = pd.DataFrame(committees)
    df_c.to_excel(writer, sheet_name='committees', index=False)
    
    
    df_sc = pd.DataFrame(subcommittees)
    df_sc.to_excel(writer, sheet_name='subcommittees', index=False)
    
    ########### Parse Committee Memberships ###########

    memberships = list()

    for committee, members in membership_data.items():
        for member in members:
            row = member.copy()
            row['committee'] = committee
            memberships.append(row)

    df_m = pd.DataFrame(memberships)
    df_m.to_excel(writer, sheet_name='committee_memberships', index=False)
    
    # print information and save
    print(df_c.info())
    print(df_sc.info())
    print(df_m.info())
    print(f'found {len(committees)} committees and {len(subcommittees)} subcommittees')
    print(f'total of {df_m.shape[0]} memberships found')

    writer.save()
    
    


    