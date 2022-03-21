

# get data from here:
# https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/UIVHQR

library(tidyverse)
library(rtweet)

all_status_ids <- read_lines('assignments/data_preparation/senators-1.txt')
senator_tweet_ids <- all_status_ids %>% sample(500)

lookup_status_ids <- all_status_ids %>% sample(1000)
#lookup_status_ids <- senator_tweet_sample$status_id

statuses <- lookup_tweets(lookup_status_ids)

senator_tweet_sample <- statuses %>% 
  select(status_id, user_id, screen_name, created_at, is_quote, is_retweet, favorite_count, retweet_count, text)

save(senator_tweet_ids, senator_tweet_sample, file='datasets/senator_tweets.RData')

