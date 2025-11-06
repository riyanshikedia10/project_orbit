# Project ORBIT - Private Equity Intelligence for Forbes AI 50

Automated system for tracking and analyzing Forbes AI 50 startups using web scraping, RAG, and structured data extraction.

## Project Structure

```
project_orbit/
├── cloud_functions/        # Cloud Functions (Lab 2 & 3 - Scraping automation)
│   ├── main.py            # Function entry points
│   ├── requirements.txt   # Function dependencies
│   └── src/               # Scraper and GCS utilities
├── dags/                  # DEPRECATED: Old Airflow DAGs (kept for reference)
├── src/                   # Source code (scraper, RAG, API, etc.)
├── data/                  # Data files (seed JSON, scraped data)
├── scripts/               # Setup and deployment scripts
└── notebooks/             # Jupyter notebooks for development
```

## Quick Start

### Lab 2 & 3: Cloud Functions + Cloud Scheduler

For detailed setup instructions, see [QUICK_START_FUNCTIONS.md](QUICK_START_FUNCTIONS.md) or [CLOUD_FUNCTIONS_SETUP.md](CLOUD_FUNCTIONS_SETUP.md)

**Quick steps:**
1. Enable APIs: `bash scripts/enable_apis.sh`
2. Copy source code: `cp -r src cloud_functions/src`
3. Set bucket config: `echo 'BUCKET_NAME="project-orbit-data-12345"' > .gcs_config`
4. Deploy functions: `bash scripts/deploy_functions.sh`
5. Create schedulers: `bash scripts/create_schedulers.sh`

## Functions

- **full_ingest**: Full-load scraping for all 50 companies (manual trigger)
- **daily_refresh**: Daily refresh of key pages (runs at 3 AM UTC)

## Requirements

- `requirements.txt` - For local development (FastAPI, Streamlit, etc.)
- `cloud_functions/requirements.txt` - For Cloud Functions deployment

## Development

### Local Testing
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Test scraper locally
python src/scraper.py --companies anthropic abridge
```

### Test Cloud Functions Locally
```bash
# Install functions framework
pip install functions-framework

# Run function locally
cd cloud_functions
functions-framework --target=main_full_ingest --debug
```

## Labs Progress

- ✅ Lab 0: Project bootstrap & seed data
- ✅ Lab 1: Scraper implementation
- ✅ Lab 2: Full-load Cloud Function
- ✅ Lab 3: Daily refresh Cloud Function
- ⏳ Lab 4+: Vector DB, RAG, Structured extraction (coming next)

## Architecture

- **Cloud Scheduler** → Triggers Cloud Functions via HTTP (cron)
- **Cloud Functions** → Scrape companies and upload to GCS
- **Cloud Storage** → Stores scraped data (`project-orbit-data-12345`)

## License

Academic project for DAMG7245.
