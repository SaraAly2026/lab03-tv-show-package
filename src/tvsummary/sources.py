"""Fetch TV show data from TVMaze."""

import requests

from .config import TVMAZE_URL, REQUEST_TIMEOUT


class TVMazeSource:
    """Download TV show records from the TVMaze API."""

    def __init__(self, url=TVMAZE_URL):
        self.url = url

    def fetch(self):
        """Return raw TV show records from the API."""
        try:
            response = requests.get(
                self.url,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()

            data = response.json()

            if not isinstance(data, list):
                raise ValueError("Expected a list of TV shows.")

            return data

        except (requests.RequestException, ValueError) as error:
            raise RuntimeError(
                f"Failed to download TV shows: {error}"
            ) from error