# TV Show Summary

this program download tv shows and sumarize the information.

## Data source

[The URL](https://api.tvmaze.com/shows?page=0), tv sHOW, and roughly 240 records it returns.

## Setup

python -m venv .venv

source .venv/bin/activate # Windows: .venv\Scripts\activate

pip install -r requirements.txt

## Run

python records.py

## Example output
summary.json

{
  "source_url": "https://api.tvmaze.com/shows?page=0",
  "record_count": 240,
  "language_counts": {
    "English": 236,
    "Japanese": 4
  },
  "average_rating": 7.584745762711866,
## Data quirks
some records does not have avg. rating so I checked the rating is valid #.
## Design choices
I used dictionary for language_counts as each language connected to its cunt
I used set for genre as set keep the uniques

## Known limitations
N/A