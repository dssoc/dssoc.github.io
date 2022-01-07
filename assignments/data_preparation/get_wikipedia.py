
import wikipedia
import pandas as pd

cdf = pd.read_csv('congress_ids.csv')



newrows = list()
for idx,row in cdf.iterrows():
    
    try:
        page = wikipedia.page(row['wikipedia_id'])

        newrows.append({
            'bioguide_id': row['bioguide_id'],
            'wikipedia_id': row['wikipedia_id'],
            'title': page.title,
            'summary': page.summary,
            'content': page.content,
            'references': '\n'.join(page.references),
            'categories': '\n'.join(page.categories),
            'url': page.url,
        })
        pd.DataFrame(newrows).to_csv('wikipedia_pages2.csv')
        print(f'downloaded {row["wikipedia_id"]}.')

    except wikipedia.exceptions.PageError:
        print(f'\t\tcouldn\'t find {row["wikipedia_id"]}..')



    
#page = "Sherrod Brown"
#summary = wikipedia.summary(page)
#full = wikipedia.page(page)

#print(full.content)

#print(df.head())
