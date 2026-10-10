"""Entry point for the TVMaze summary application."""

from tvsummary.config import TVMAZE_URL
from tvsummary.models import TVShow
from tvsummary.sources import TVMazeSource
from tvsummary.aggregations import (
    LanguageCount,
    AverageRating,
    GenreList,
)
from tvsummary.report import build_summary, save_summary


def main():
    """Fetch, clean, aggregate, and save TV show data."""

    source = TVMazeSource()
    raw_records = source.fetch()

    shows = [TVShow(record) for record in raw_records]

    aggregations = {
        "language_counts": LanguageCount(),
        "average_rating": AverageRating(),
        "genres": GenreList(),
    }

    results = build_summary(shows, aggregations)

    summary = {
        "source_url": TVMAZE_URL,
        "record_count": len(raw_records),
        **results,
    }

    save_summary(summary)

    print(f"Downloaded {len(raw_records)} records.")
    print("Summary saved successfully.")


if __name__ == "__main__":
    main()