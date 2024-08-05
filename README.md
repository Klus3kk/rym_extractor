# rym_extractor
RYM Album Data Extractor is a Python tool designed to scrape and organize music album data from RateYourMusic (RYM) HTML files. This tool extracts album details and separates albums with ratings from those that are wishlisted.

## Features

- Extracts artist names, album titles, and ratings from an HTML file.
- Separates wishlisted albums (albums without ratings) into a separate file.
- Skips entries with missing artist or album information.

## Getting Started

### Prerequisites

- Python 3.x
- BeautifulSoup4
- pandas

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/rym-album-data-extractor.git
    cd rym-album-data-extractor
    ```

2. Install the required packages:
    ```bash
    pip install pandas beautifulsoup4
    ```

### How to get HTML RYM album ratings

### Usage

1. Place your `file.html` in the project directory.

2. Run the extraction script:
    ```bash
    python rym.py
    ```

3. The script will generate two CSV files:
    - `music_data.csv` for albums with ratings.
    - `wishlisted_music_data.csv` for albums without ratings (wishlisted albums).

