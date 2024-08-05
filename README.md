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
1. On the home page of RateYourMusic click on your profile picture.
<p align="center">
  <img width="1280" height="480" src="https://github.com/user-attachments/assets/1824880a-b9a1-4e51-ba6e-eaae28872bb4">
</p>

2. Scroll down, click on the "Music" button. You'll find it above your rated albums.
<p align="center">
  <img width="1280" height="480" src="https://github.com/user-attachments/assets/4df0539d-ac03-4be3-a835-effee8552d69">
</p>

3. After that click on the "Print this page" button.
<p align="center">
  <img width="1280" height="480" src="https://github.com/user-attachments/assets/07fe5fe4-51e9-40d6-b6f4-0582c7903406">
</p>

4. Right click on the shown page and click "Save as..."
<p align="center">
  <img width="1280" height="480" src="https://github.com/user-attachments/assets/b7946079-b064-49a4-9199-bad32fc9dc6f">
</p>

5. Save the file as "Webpage, HTML Only" with the reccomended name "file".
<p align="center">
  <img width="1280" height="480" src="https://github.com/user-attachments/assets/1a75b5e4-0c96-461e-830a-558b9bf5449d">
</p>

6. After that paste the HTML file to the folder, where the rym.py is located **and you're ready to go!**

### Usage

1. Place your `file.html` in the project directory.

2. Run the extraction script:
    ```bash
    python rym.py
    ```

3. The script will generate two CSV files:
    - `music_data.csv` for albums with ratings.
    - `wishlisted_music_data.csv` for albums without ratings (wishlisted albums).

