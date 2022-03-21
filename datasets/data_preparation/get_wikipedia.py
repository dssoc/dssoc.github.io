
import wikipedia
import pandas as pd
import tqdm

if __name__ == '__main__':

    cdf = pd.read_csv('raw_data/legislators-current.csv')

    #print(cdf.head())

    newrows = list()
    for idx,row in tqdm.tqdm(cdf.iterrows()):
        
        try:
            page = wikipedia.page(row['wikipedia_id'])

            newrows.append({
                'bioguide_id': row['bioguide_id'],
                'wikipedia_id': row['wikipedia_id'],
                'summary': page.summary,
                'text': page.content,
                #'url': page.url,
                #'title': page.title,
                #'references': '\n'.join(page.references),
                #'categories': '\n'.join(page.categories),
                
            })
            print(f'downloaded {row["wikipedia_id"]}.')

        except wikipedia.exceptions.PageError:
            print(f'\t\tcouldn\'t find {row["wikipedia_id"]}..')


        pd.DataFrame(newrows).to_csv('raw_data/wikipedia_pages.csv')
        
    #page = "Sherrod Brown"
    #summary = wikipedia.summary(page)
    #full = wikipedia.page(page)

    #print(full.content)

    #print(df.head())
