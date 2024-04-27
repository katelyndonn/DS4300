"""
filename: twitter_timelines.py

This file uses the UserAPI to display user data such as
(1) follower list, (2) following list, (3) tweets posted, and (4) home timeline

Homework 1: TwitterDB
Avril Mauro & Katelyn Donn
"""

from twitter_mysql import UserAPI
import random
import pandas as pd
import time



follow_file = 'follows.csv'


def get_random_user(users_list):
    unique_users = list(set(users_list))
    random.shuffle(unique_users)
    return unique_users.pop()


def main():

    # make into a for loop to check how many timelines per second we can get
    # maybe for one user?
    # our timestamps are static
    # build speed tester


    # log into the database
    api = UserAPI("T_USER", "T_PASS", "TwitterDB", host="localhost")

    start_time = time.time()
    count = 0
    while time.time() - start_time < 60:


        # select a random user
        df_follows = pd.read_csv('follows.csv')
        random_user = get_random_user(df_follows.USER_ID)

        # display user data
        print(api.get_followers(random_user))
        print(api.get_following(random_user))
        print(api.get_tweets(random_user))

        # display home timeline
        print(api.get_timeline(random_user))
        count += 1

    timeline_count = count/60
    print(f"Timelines per second: {timeline_count:.2f}")

if __name__ == '__main__':
    main()
