# Scraping-Twitter-Data
This project demonstrates a simple Twitter scraping application using Python. It allows you to search for tweets based on specific criteria such as a username, date range, and tweet count. The scraped tweets can be displayed, uploaded to a MongoDB database, and downloaded as CSV or JSON files.

## Dependencies
Make sure you have the following libraries installed:
- streamlit
- datetime
- snscrape
- pandas
- pymongo

You can install these dependencies using `pip`:
```bash
pip install streamlit datetime snscrape pandas pymongo
```

## Usage
1. Run the script, which will launch a Streamlit application.
2. Enter the search criteria:
   - **Enter Your name search**: Input the username you want to search for.
   - **Enter Your Tweet Count**: Specify the number of tweets you want to scrape (between 0 and 5000, in increments of 10).
   - **Start Date** and **End Date**: Define the date range for the search.
3. Click the **Search** button to start scraping the tweets based on the provided criteria. The tweets will be displayed in a table.
4. If desired, click the **Upload** button to upload the scraped tweets to a MongoDB database. The data will be stored in a collection named after the entered username.
5. To download the scraped data, click either the **Download as CSV** or **Download as JSON** button. The data will be saved in the respective file format.

Note: Ensure that you have a running MongoDB instance on `localhost:27017` for successful data uploading.

## Database Structure
The scraped tweet data will be stored in a MongoDB database with the following collection structure:
- Collection Name: [username] (e.g., if the username is "john123", the collection name will be "john123")
- Document Structure:
  - Datetime
  - Tweet Id
  - Text
  - Username
  - Reply Count
  - Retweet Count
  - Language
  - Source
  - Like Count

**Important Note:** Twitter has implemented restrictions on data scraping. If you intend to scrape data from Twitter, it is essential to use the official Twitter API, which provides authorized access to their data. Please ensure you comply with Twitter's API terms of service and usage policies to avoid any potential violations.

Thank you for checking out this Twitter scraping project!
