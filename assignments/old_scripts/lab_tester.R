

library(tidytext)
library(dplyr)
library(tm)
library(topicmodels)


ptm <- proc.time()
dtm <- congress_wiki %>% 
  select(bioguide_id, summary) %>% 
  #mutate(summary=summary[[1]]) %>% 
  unnest_tokens('word', 'summary') %>% 
  anti_join(stop_words) %>% 
  count(bioguide_id, word) %>% 
  cast_dtm(bioguide_id, word, n)

proc.time() - ptm
ptm <- proc.time()

tm <- LDA(dtm, k=10, control=list(seed=0))

proc.time() - ptm
ptm <- proc.time()
topics <- tm %>% tidy(matrix='beta')

proc.time() - ptm
ptm <- proc.time()
topwords <- topics %>% group_by(topic) %>% top_n(10, beta) %>% ungroup() %>% arrange(topic, -beta)
proc.time() - ptm
ptm <- proc.time()



