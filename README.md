# ScrapMetro

ScrapMetro is a Python script that uses Selenium to scrape product information from the METRO website, including the product title and promotional price. The scraped data is then saved to an Excel file.

## Usage

To use the ScrapMetro script, pass the URL of a METRO product page as a command line argument, like this:

./main.py <product_url>

For example:

linux
./main.py https://shop.metro.fr/shop/pv/BTY-X141114/0032/0021/Beurre-doux-en-rouleau-1-kg-METRO-Chef

The scraped data will be saved to an Excel file named "products.xlsx" in the current directory.

## Project Overview

The ScrapMetro project is built using Python 3 and Selenium. The script uses a pre-configured Chrome browser profile to handle cookie management, and regular expressions to extract the promotional price from the product page.

## Dependencies

To run the project, you'll need to have Python 3 installed on your system. You can download Python 3 from the [official website](https://www.python.org/downloads/).

You'll also need to install the following Python packages:

- selenium
- openpyxl
- python-dotenv

To install these packages, you can use pip:

pip install -r requirements

## Running the Script

To run the ScrapMetro script, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies (see above).
3. (optional) Create a `.env` file and set your METRO credentials in it using the following format:
   METRO_USERNAME=<your_username>
   METRO_PASSWORD=<your_password>
4. Open a terminal window and navigate to the project directory.
5. Run the script with the product URL as a command line argument (see above).

## Challenges

The ScrapMetro project presented some challenges that needed to be addressed during development. These challenges include:

### Cookie management

METRO's website requires cookies to be set in order to access certain pages, including product pages. To handle this, the project uses a Chrome browser profile that is pre-configured with the necessary cookies. This allows the script to bypass the login page and directly access the product page.

### Multiple types of promotions

METRO offers multiple types of promotions for their products, such as discounts, rebates, and bulk purchase deals. The project needed to be able to handle these different types of promotions and extract the correct promotional price for each product.

To handle this, the project uses regular expressions to match the promotional price on the product page. The regular expressions are customized to match the format of each type of promotion.

## Conclusion

The ScrapMetro project demonstrates how to use Selenium and Python to scrape data from a website. By using a Chrome browser profile and regular expressions, the project is able to handle cookie management and multiple types of promotions. With some additional improvements, the project could be extended to handle scraping multiple products and additional types of promotions.

## Author

This repository was created by Romain Dufourt.
