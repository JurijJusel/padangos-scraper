# Padangos Scraper

A Python web scraper for extracting tire product information from e-commerce websites.
Built with BeautifulSoup, Requests, and Pydantic for data modeling.

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


# Supabase Connection from VSCode (SQLTools)

## Prerequisites
Install these VSCode extensions:
- `SQLTools`
- `SQLTools PostgreSQL/Cockroach Driver` (driver.pg)

## Getting Connection String from Supabase
1. Go to your Supabase project
2. Click the **Connect** button in the top centee of the dashboard
3. A modal window will appear: **Connect to your project — Choose how you want to use Supabase**
4. Select **Session Pooler** (recommended — Direct connection may be blocked by your ISP on port 5432)
5. Copy the **Connection string** shown below the options — it looks like this:

## Notes
  - Use **Session Pooler** connection string — Direct connection (port 5432)
    may be blocked by your ISP

```
postgresql://postgres.YOUR-PROJECT-ID:YOUR-PASSWORD@aws-0-eu-central-1.pooler.supabase.com:5432/postgres
```

6. Replace `YOUR-PASSWORD` with your actual database password
 - This is the same password you entered when creating the Supabase project
7. Replace `YOUR-PROJECT-ID` with your actual project ID
 - Go ot Project Settings → General settings → Project ID to find your project ID

## Setup in VSCode
1. open SQL Tools → Press `Add New Connection`
2. Select **PostgreSQL**
3. Set **Connect using** → **Connection String**
4. Paste the connection string from the previous step
5. SSL settings:
   - SSL: **Enabled**
   - rejectUnauthorized: **unchecked**
6. Use password → **Save as plaintext in settings**
7. Click **Save Connection**

## Viewing Data
1. Click **SQLTools icon** (cylinder) in the left sidebar
2. Expand your connection → **postgres → public → tables**
3. You will see your tables: `tires_base` and `technical_info`
4. Right-click on a table and select **Show Table Records** to run queries


## Dependencies

- `bs4` - BeautifulSoup for HTML parsing
- `requests` - HTTP client for web requests
- `pydantic` - Data validation and modeling
- `rich` - Rich console output
- `supabase` - Supabase Python client
- `python-dotenv` - Environment variable management


## License
This project is licensed under the MIT License.
