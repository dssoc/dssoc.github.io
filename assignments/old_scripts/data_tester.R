


library('devtools')
library("rjson")
library("dplyr")
library('WikipediR')

# download data from here: https://github.com/unitedstates/congress-legislators

# Give the input file name to the function.
#lhist <- fromJSON(file = "C:\\Users\\Devin\\Downloads\\legislators-current.json") %>% as.data.frame


# last_name, first_name, middle_name, suffix, nickname, full_name, birthday, gender, type, state, district, senate_class, party, url, address, phone, contact_form, rss_url, twitter, facebook, youtube, youtube_id, bioguide_id, thomas_id, opensecrets_id, lis_id, fec_ids, cspan_id, govtrack_id, votesmart_id, ballotpedia_id, washington_post_id, icpsr_id, wikipedia_i, 

#congress_info <- read.csv("C:\\Users\\Devin\\Downloads\\legislators-current.csv", stringsAsFactors = FALSE)
#congress_info <- read.csv(url('https://theunitedstates.io/congress-legislators/legislators-historical.csv'), stringsAsFactors = FALSE)
congress_info <- read_excel('E:\\data\\legislators-current(1).xlsx')



congress <- congress_info %>% 
  select(last_name, full_name, birthday, gender, type, state, party, phone, twitter, 
         facebook, youtube, bioguide_id) %>% 
  mutate(birthyear=as.numeric(substr(birthday, 1, 4)))


congress_ids <- congress_info %>% 
  select(bioguide_id, youtube_id, thomas_id, opensecrets_id, lis_id, fec_ids, cspan_id, 
         govtrack_id, votesmart_id, ballotpedia_id, icpsr_id, wikipedia_id)

committees <- read.csv('C:\\Users\\Devin\\Downloads\\committee-membership-current.csv', stringsAsFactors = FALSE) %>% 
  select(!(date:chamber)) %>% 
  select(!(X)) %>% 
  relocate(committee, bioguide, before=name)

congress_wiki <- read.csv('C:\\Users\\Devin\\Downloads\\wikipedia_pages2.csv', stringsAsFactors = FALSE) %>% 
  select(bioguide_id,	wikipedia_id,	title,	content,	references,	categories,	url) %>% 
  rename(text=content)
  


save(congress, congress_ids, committees, file='congress.RData')
save(congress_wiki, file='congress_wiki.RData')
write.csv(congress_ids, file='congress_ids.csv')
write.csv(congress_wiki, file='congress_wiki.csv')

#a <- page_content("en", "wikipedia", page_name="Sherrod Brown", as_wikitext=TRUE, clean_response=TRUE)

