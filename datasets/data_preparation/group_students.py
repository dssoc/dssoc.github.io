'''
author: Devin J. Cornell
date: 03-21-2022
description: Use this file to randomly assign students to groups.
'''



import pandas as pd
import random

if __name__ == '__main__':
    random.seed(0)
    n_groups = 5
    #workshop_dates = ['January 19', 'February 2', 'February 16', 'March 2', 'March 23']
    workshop_dates = ['September 5', 'September 12', 'September 19', 'September 26', 'October 3', 
        'October 12', 'October 17', 'October 24', 'October 31', 'November 7', 'November 14']
    
    
    csv_fname = 'raw_data/Class Roster - 2022 Fall Term - SOCIOL 367S (3165).csv'
    roster = list(pd.read_csv(csv_fname, index_col=False)['Name'].dropna())
    print(f'{len(roster)} Students assigned to {n_groups} groups on {len(workshop_dates)} days.')
    
    for date in workshop_dates:
        print(f'{"="*15} Class {date} {"="*15}\n')
        groups = [[] for _ in range(n_groups)] # list of lists

        randomized_roster = list(roster)
        random.shuffle(randomized_roster)
        
        for i, student in enumerate(randomized_roster):
            # parse name of student
            l,f = student.split(',')
            groups[i % n_groups].append(f'{f} {l}'.strip())
            #print(i % n_groups, [len(g) for g in groups], groups[i % n_groups])

        #print(f'placed {sum([len(g) for g in groups])} students into {len(groups)} groups.')

        for i, group in enumerate(groups):
            print('\t' + f'{"-"*5} Group {i+1} {"-"*5}')
            for name in group:
                print(f'\t{name}')
            print()
        
        print('\n')
        
        #for i in range(n_groups):
        #    print(f'{"_"*5} Group {i+1} {"_"*5}')
        #    
        #    # make actual sample
        #    extra = 1 if roster.shape[0]%n_groups != 0 and i == (n_groups-1) else 0
        #    n = min(roster.shape[0]//n_groups + extra, len(remaining_students))
        #    sel = set(random.sample(remaining_students, n))
        #    remaining_students -= sel
        #    
        #    # print names
        #    for name in sel:
        #        #print(name)
        #        l,f = name.split(',')
        #        print(f'{f} {l}')
        #    
        #    print()
            
            

            








