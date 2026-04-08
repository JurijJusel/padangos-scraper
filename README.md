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

### Supabase Integration
Scraped tire data is automatically saved to a Supabase (PostgreSQL) database.
Database Schema
Two tables are used:
- tires_base — main product information:
- technical_info — technical specifications:

## Setup

1.Create a project at supabase.com
2. Create the tables `tires_base` and `technical_info` with the appropriate schema.

tires_base (
    id                 int8 (PRIMARY KEY GENERATED ALWAYS AS IDENTITY),
    brand              TEXT NOT NULL,
    model              TEXT NOT NULL,
    product_class      TEXT,
    price              NUMERIC,
    wet_grip           TEXT,
    fuel_effect        TEXT,
    noise              TEXT,
    remaining_quantity INT2,
    url                TEXT
);

technical_info (
    tires_id          int8 REFERENCES tires_base(id) foreign key,
    width             INT2,
    height            INT2,
    diameter          INT2,
    product_code      TEXT,
    product_season    TEXT,
    load_index        INT2,
    speed_index       TEXT,
    reinforced        TEXT,
    runflat           TEXT,
    transport_type    TEXT,
    construction_type TEXT
);

3. Obtain your Supabase URL and API key from the project settings.
4. Create a `.env` file in the project root with the following content:
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_api_key
```

How It Works
Before inserting, the scraper checks if a tire with the same product_code
already exists in technical_info
If found, the insert is skipped to avoid duplicates
If not found, data is inserted into both tires_base and technical_info tables


## Dependencies

- `bs4` - BeautifulSoup for HTML parsing
- `requests` - HTTP client for web requests
- `pydantic` - Data validation and modeling
- `rich` - Rich console output
- `supabase` - Supabase Python client
- `python-dotenv` - Environment variable management


## License
This project is licensed under the MIT License.
