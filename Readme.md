# Google URL Parser with CAPTCHA Bypass

This project is a Google search URL parser built with **Selenium** and **Python 3.12**. It is designed to automate Google search queries, collect result links, and handle Google CAPTCHA challenges using the [noptcha](https://noptcha.com/) browser extension.

## Features
- Automated Google search and result link extraction
- CAPTCHA bypass using the noptcha browser extension
- Written in Python 3.12
- Modular architecture (parsers, handlers, services, utils)

## Requirements
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) (for containerized setup)
- **OR**
- Python 3.12, [Selenium](https://pypi.org/project/selenium/), [noptcha browser extension](https://noptcha.com/), [python-dotenv](https://pypi.org/project/python-dotenv/), Firefox browser and geckodriver (for manual setup)

## Setup

### Option 1: Docker Compose (Recommended)
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd selenium_browser_url_parcer
   ```
2. Start the project using Docker Compose:
   ```bash
   docker-compose up --build
   ```

This will build and run the application in a containerized environment with all dependencies pre-installed.

---

### Option 2: Manual Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd selenium_browser_url_parcer
   ```
2. Install dependencies (using poetry or pip):
   ```bash
   poetry install
   # or
   pip install -r requirements.txt
   ```
3. Place the `noptcha.xpi` extension in `src/utils/browser/extentions/`.
4. Create a `.env` file in the project root (optional, for settings like `DRIVER_HEADLESS`).
5. Run the parser as a module:
   ```bash
   poetry run python -m src
   # or
   python -m src
   ```

---

## Usage
The parser will:
- Read search queries from a CSV file (see `data/requests.csv`)
- Launch Firefox with the noptcha extension
- Perform Google searches and collect result URLs
- Save the results to a CSV file (see `data/urls.csv`)

**You can specify your own search queries by editing the `data/requests.csv` file. The resulting links for each query will be saved in `data/urls.csv`.**

## Notes
- Make sure the noptcha extension is up to date and properly configured.
- This project is for educational and research purposes only. Use responsibly and respect Google's terms of service.

---
Feel free to contribute or open issues for improvements!
