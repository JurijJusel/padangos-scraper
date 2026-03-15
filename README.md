# Padangos Scraper

A Python web scraper for extracting tire product information from e-commerce websites. Built with BeautifulSoup, Requests, and Pydantic for data modeling.

## Features

- Scrapes tire product data including names, prices, dimensions, and availability
- Supports multiple tire brands and seasons
- Structured data output using Pydantic models
- Rich console output for better user experience
- Modular architecture with separate crawlers, utilities, and models

## Installation

### Prerequisites

- Python 3.12 or higher
- uv (recommended) or pip

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd padangos-scraper
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install uv and dependencies:

"https://docs.astral.sh/uv/getting-started/installation/#standalone-installer"

```bash
pip install uv
```

```bash
uv sync
# or with pip:
pip install -r requirements.txt
```

## Usage

Run the main scraper:

```bash
python main.py
```

This will:
- Build URLs for tire products based on configured dimensions, brands, and seasons
- Scrape product information from the target website
- Save data to JSON files in the `data/` directory
- Display progress using Rich console output

## Project Structure

```
padangos-scraper/
├── crawlers/           # Web scraping logic
├── models/            # Pydantic data models
├── utils/             # Utility functions
├── data/              # Output data files
├── constants.py       # Configuration constants
├── main.py           # Main entry point
└── pyproject.toml    # Project configuration
```

## Configuration

Modify `config_url_builder.py` to adjust:
- Target URLs
- Tire brands to scrape
- Seasons
- Dimensions
- Tire features and selections


## Dependencies

- `bs4` - BeautifulSoup for HTML parsing
- `requests` - HTTP client for web requests
- `pydantic` - Data validation and modeling
- `rich` - Rich console output

## License
This project is licensed under the MIT License.
