import streamlit as st
import datetime
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo

tweets_list1 = []
st.title("Project Twitter Scraping")
with st.form("Twitter scraping", clear_on_submit=False):
    search_txt = st.text_input("Enter Your name search")
    tweet_count = st.number_input("Enter Your Tweet Count", min_value=0, max_value=5000, step=10)

    date_col1, date_col2 = st.columns(2)
    start_date = date_col1.date_input("Start Date", datetime.date(2015, 1, 1))
    end_date = date_col2.date_input('End date')
    # start_date = start_date.strftime("%Y-%m-%d")
    # search_string = search_txt + ' ' + 'since:' + start_date
    search_string =f'from:{search_txt} since:{start_date} until:{end_date}'

    button_col1, button_col2 = st.columns(2)
    search_submitted = button_col1.form_submit_button("search")
    if search_submitted:

        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_string).get_items()):
            if i > tweet_count:  # number of tweets you want to scrape
                break
            tweets_list1.append([tweet.date, tweet.id,
                                 tweet.content, tweet.user.username,
                                 tweet.replyCount, tweet.retweetCount,
                                 tweet.lang, tweet.source, tweet.likeCount])  # declare the attributes to be returned
    # Creating a dataframe from the tweets list above
    column_name =["Datetime", "Tweet Id", "Text", "Username", "reply count", "retweet count","language", "source", "like count"]
    tweets_df1 = pd.DataFrame(tweets_list1,columns=column_name)
    st.dataframe(tweets_df1)

    # Uploading the scraped data into database
    upload_submitted = button_col2.form_submit_button("upload")
    if upload_submitted:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["twitter_data"]
        mycollection = db[search_txt]
        res = {column_name[i]: tweets_list1[i] for i in range(len(column_name))}
        mycollection.insert_one(res)
        results = mycollection.find()
        df = pd.DataFrame(list(results))

        st.success("submitted")

    download_button1, dowmload_button2 = st.columns(2)
    download_CSV = download_button1.form_submit_button("Download as CSV")
    if download_CSV:
        # save the data as a CSV file
        df.to_csv("data.csv", index=False)
        st.success("submitted")
    download_JSON = dowmload_button2.form_submit_button("Download as JSON")
    if download_JSON:
        # save the data as a CSV file
        df.to_json("data.json")
        st.success("submitted")
st.write(search_string)
