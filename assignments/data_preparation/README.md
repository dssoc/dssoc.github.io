
author: Devin J. Cornell
date: 03-21-2022
description: I describe the datasets and the scripts used to compile them into Rdata files.

NOTE: See Lab Instructions doc for more info about the source and details of these datasets.


## `congress.Rdata`

1. Download the "legislators-current.csv" file from the [congress-legislators](https://github.com/unitedstates/congress-legislators) repository.
2. run "compile_congress.Rmd" to output congress.RData

## `congress_committees.RData`

1. Download "committees-current.json" and "committee-membership-current.json" from the [congress-legislators](https://github.com/unitedstates/congress-legislators) repository.
2. Run the script "parse_committees.py" to convert those json files into "committees.xlsx", an excel file containing all committee information.
3. Run the script "compile_commitees.Rmd" to convert the xls file to an RData file - the output is "committees.RData".

## `senator_tweets.RData`

1. Download "senators-1.txt" from the [Harvard dataverse page](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/UIVHQR).
2. Run the script "prepare_senator_tweets.R" to generate samples of ids and pull a subset of those Tweets from the Twitter API. The output is "senator_tweets.RData"

## 