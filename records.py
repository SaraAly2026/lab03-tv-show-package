import json
from pathlib import Path

import requests

SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
OUTPUT = Path("summary.json")

def fetch_shows(url):
    """Download TV show records and return them."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        raise SystemExit(f"Download failed: {error}")

def count_shows_by_language(records):
    """Count the number of shows for each language."""
    language_counts = {}

    for show in records:
        language = show.get("language")
        if isinstance(language, str):
            language_counts[language] = language_counts.get(language, 0) + 1

    return language_counts


def calculate_average_rating(records):
    """Calculate the average rating from valid ratings."""
    total_rating = 0
    rating_count = 0

    for show in records:
        rating_info = show.get("rating")

        if isinstance(rating_info, dict):
            rating = rating_info.get("average")

            if isinstance(rating, (int, float)):
                total_rating += rating
                rating_count += 1

    if rating_count > 0:
        return total_rating / rating_count

    return None

def get_show_names(records):
    """Build a list of valid show names."""
    return [
        show["name"]
        for show in records
        if isinstance(show.get("name"), str)
    ]


def get_unique_genres(records):
    """Build a set of unique genres."""
    return {
        genre
        for show in records
        if isinstance(show.get("genres"), list)
        for genre in show["genres"]
        if isinstance(genre, str)
    }

def build_summary(records):
    """Combine the aggregations into one summary dictionary."""
    language_counts = count_shows_by_language(records)
    average_rating = calculate_average_rating(records)
    genres = get_unique_genres(records)

    return {
        "source_url": SOURCE_URL,
        "record_count": len(records),
        "language_counts": language_counts,
        "average_rating": average_rating,
        "genres": sorted(genres)
    }




def write_summary(summary, path):
    """Write the summary to a JSON file."""
    with path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)


def main():
    """Run the TV show summary program."""
    shows = fetch_shows(SOURCE_URL)

    print(f"Downloaded {len(shows)} records.")
    print(shows[0].keys())

    show_names = get_show_names(shows)
    print(show_names[:5])

    summary = build_summary(shows)

    print(summary["language_counts"])
    print(f'Average rating: {summary["average_rating"]}')
    print(summary["genres"])

    write_summary(summary, OUTPUT)





if __name__ == "__main__":
    main()