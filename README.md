# Yelp Reviews Scraper (Python Scripting Project)

## Overview

This is a simple python project that was designed to scrape reviews from a specific Yelp business page and generate a CSV report containing the extracted data. The script fetches the content from the page, parses the HTML to extract review information, and saves it into a structured CSV file, that can be furthur used with data visualization tools like Tableau, PowerBI, etc.

## Author

William Hellems-Moody

## Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup` from `bs4` library
- `pandas` library

## Installation

To run this script, ensure you have the required libraries installed. You can install them using pip:

```sh
pip install requests
pip install beautifulsoup4
pip install pandas
```

## Usage

1. Set the `url` variable in the script to the Yelp business page you want to scrape. For example:
   ```python
   url = "https://www.yelp.com/biz/bowlero-san-antonio-san-antonio"
   ```
2. Run the script. It will scrape the reviews, including the reviewer's name, review content, and rating, and save the data into a CSV file named `yelp_reviews.csv`.

```sh
python yelp_reviews_scraper.py
```

## How It Works

1. **Fetch the Page Content**: The script sends a GET request to the Yelp page and retrieves the HTML content.
2. **Parse HTML with BeautifulSoup**: It uses BeautifulSoup to parse the HTML and locate the elements containing review data.
3. **Extract Data**:
   - **Names**: Extracts the names of the reviewers.
   - **Reviews**: Extracts the review text.
   - **Ratings**: Extracts the rating given by each reviewer.
4. **Store Data in a DataFrame**: The extracted data is stored in a pandas DataFrame.
5. **Save to CSV**: The DataFrame is then saved to a CSV file named `yelp_reviews.csv`.

## Example Output

The resulting CSV file, `yelp_reviews.csv`, will have the following columns:

- **Name**: The name of the reviewer.
- **Review**: The text of the review.
- **Rating**: The rating given by the reviewer, parsed from the aria-label attribute of the rating element.

## Notes

- The script assumes that the structure of the Yelp page does not change. If Yelp updates their HTML structure, the script might need adjustments.
- The script currently processes the first page of reviews. For multiple pages, additional logic will be needed to handle pagination (not included in this simple project).
