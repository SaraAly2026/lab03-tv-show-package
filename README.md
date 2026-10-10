
# TVMaze TV Show Summary — Lab 03

## Project Overview

This project refactors my Lab 02 TVMaze data aggregation script into an installable Python package using Object-Oriented Programming (OOP).

The application downloads TV show data, processes the records, calculates summary statistics, and saves the results as a JSON file.

## Data Source

TVMaze API:

https://api.tvmaze.com/shows?page=0

The application retrieves TV show records from page 0 of the API.

## Setup

Python 3.11 or newer is required.

Create a virtual environment:

```powershell
python -m venv .venv
```

Install the project and its dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
```

Alternatively, install the pinned dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

A Conda environment configuration is also provided in `environment.yml`.

## Run

Run the application:

```powershell
.\.venv\Scripts\python.exe main.py
```

The summary is saved to:

`data/processed/summary.json`

## Test

Run the offline unit tests:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

The tests cover language counts, average ratings, unique genres, and missing values. They do not require an internet connection.

## Project Layout

```text
lab03-tv-show-package/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   └── tvsummary/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── sources.py
│       ├── aggregations.py
│       └── report.py
├── tests/
│   └── test_tvsummary.py
├── main.py
├── pyproject.toml
├── environment.yml
├── requirements.txt
├── records.py
├── summary.json
└── README.md
```

## What Moved Where

| Lab 02 Functionality | Lab 03 Location |
|---|---|
| API URL and configuration | `config.py` |
| Downloading TV show records | `sources.py` |
| Cleaning and representing TV shows | `models.py` |
| Language counts | `aggregations.py` |
| Average rating | `aggregations.py` |
| Unique genres | `aggregations.py` |
| Building and saving JSON | `report.py` |
| Running the application | `main.py` |

## Design Choices

- **Encapsulation:** The `TVShow` class stores cleaned TV show attributes.
- **Inheritance:** Aggregation classes inherit from the abstract `Aggregation` class.
- **Method overriding:** Each aggregation implements its own `compute()` method.
- **Polymorphism:** The report builder processes different aggregation objects through a common interface.
- **Separation of concerns:** Data retrieval, modeling, aggregation, and reporting are separated into modules.
- **Editable installation:** The package uses a `src` layout and can be installed with `pip install -e .`.

## Known Limitations

- The application retrieves only page 0 of the TVMaze API.
- An internet connection is required to download live records.
- API data may change over time, affecting summary values.
- The application reports download errors rather than automatically retrying.
- The original Lab 02 files are retained for reference.
