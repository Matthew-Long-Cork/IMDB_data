# -*- coding: utf-8 -*-
"""
Created on fri Nov  30 11:40:00 2018

@author: R00050477
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

data = pd.read_csv('movie_metadata.csv')
data['movie_title'] = data['movie_title'].str.replace(u'\xa0', '')


def primary_menu():
    print("\n\n======================================")
    print("                Menu")
    print("======================================\n\n")
    print("1. Most successful directors or actors.")
    print("2. Film comparison.")
    print("3. Analyse the distribution of gross earnings.")
    print("4. Genre analysis.")
    print("5. Earnings and IMDB scores.")
    print("6. Exit")

    selected_function = int(input("Please select one of the above options (1-6): "))

    return selected_function


def secondary_menu1():
    print("\n\n======================================")
    print("          Most successful Menu")
    print("======================================\n\n")
    print("1. Top Directors.")
    print("2. Top Actors.")

    selected_option = int(input("Please select an option (1 or 2): "))

    return selected_option


def secondary_menu2():
    print("\n\n======================================")
    print("           Film Comparison Menu")
    print("======================================\n\n")
    print("1. IMDB Scores.")
    print("2. Gross Earnings.")
    print("3. Movie Facebook Likes.")

    selected_option = int(input("Please select a location (1-3): "))

    return selected_option


def validate_movie(movie_name):
    result = False

    # index = 0
    for x in data['movie_title']:
        if x == movie_name:
            # print("item at index " + str(index))
            result = True
        # index = index + 1

    return result


# ===================================================================================
#               FUNCTION ONE_ONE
# ===================================================================================


def top_directors():
    number_of_directors = 0

    while number_of_directors not in range(1, 5000):
        number_of_directors = int(input("Please enter the number of results you wish to have: "))

    directors = data[['director_name', 'gross']]
    directors.columns = ['Directors', 'Gross Movie Earnings In Billions']
    unique_directors = directors.groupby('Directors').sum().sort_values('Gross Movie Earnings In Billions',
                                                                        ascending=False)

    results = pd.DataFrame(unique_directors[:number_of_directors])
    print(results)

    results.plot.bar()
    #plt.ylabel('Movie Earnings')
    #plt.show()


# ===================================================================================
#               FUNCTION ONE_TWO
# ===================================================================================


def top_actors():
    number_of_actors = 0

    while number_of_actors not in range(1, 5000):
        number_of_actors = int(input("Please enter the number of results you wish to have: "))

    actor_1_name = data[['actor_1_name', 'gross']]
    actor_2_name = data[['actor_2_name', 'gross']]
    actor_3_name = data[['actor_3_name', 'gross']]

    actors = actor_1_name
    actors.add(actor_2_name)
    actors.add(actor_3_name)

    actors.columns = ['Actors', 'Gross Movie Earnings In Billions']
    unique_actors = actors.groupby('Actors').sum().sort_values('Gross Movie Earnings In Billions', ascending=False)

    results = pd.DataFrame(unique_actors[:number_of_actors])
    print(results)

    results.plot.bar()
    #plt.ylabel('Movie Earnings')
    #plt.show()


# ===================================================================================
#               FUNCTION TWO_ONE
# ===================================================================================
def imdb_scores(m1, m2):
    s1 = data.loc[data.movie_title == m1]['imdb_score']
    s2 = data.loc[data.movie_title == m2]['imdb_score']

    bar_width = 0.35

    #plt.bar(bar_width * 1, s1, bar_width, color='b')
    #plt.bar(bar_width * 2.5, s2, bar_width, color='g')
    #plt.ylabel('Rating Score')
    #plt.title('IMDB Ratings')

    #plt.xticks(np.arange(0, 1, step=0.2))
    #labels = [m1, m2]
    #plt.xticks([1, 2], labels)
    #plt.show()


# ===================================================================================
#               FUNCTION TWO_TWO
# ===================================================================================
def gross_earnings(m1, m2):
    s1 = data[['gross']][data['movie_title'] == m1]
    # s2 = data[['movie_title', 'gross']][data['movie_title'] == m2]
    print("test: " + str(s1))

    index = np.arange(0, 1)
    bar_width = 0.50

    #plt.bar(index, s1, bar_width, color='g')
    #plt.bar(index, s1, bar_width, color='r')

    #plt.ylabel('Movie Earnings')
    #plt.show()


# ===================================================================================
#               FUNCTION TWO_THREE
# ===================================================================================
def movie_facebook_likes(m1, m2):
    s1 = data.loc[data.movie_title == m1]['imdb_score']
    s2 = data.loc[data.movie_title == m2]['imdb_score']

    index = np.arange(1)
    bar_width = 0.10

    #plt.bar(index, s1, bar_width, color='b')
    #plt.bar(index + bar_width, s2, bar_width, color='b')
    #plt.xlabel
    #plt.show()


""""
    both_movies = [s1, s2]
    result = pd.concat(both_movies)
    result.columns = ['Movie', 'FaceBook Likes']
    result.plot.bar(x='Movie', y='FaceBook Likes')

    plt.ylabel('Likes')
    plt.show()
"""


# ===================================================================================
#               FUNCTION THREE
# ===================================================================================
def dist_of_gross_earnings(x, y):
    results = data[['title_year', 'gross']]
    results.fillna(0)

    minimum = results.groupby('title_year').min().sort_values(['title_year', 'gross'], ascending=[False, False])
    mean = results.groupby('title_year').mean().sort_values(['title_year', 'gross'], ascending=[False, False])
    maximum = results.groupby('title_year').max().sort_values(['title_year', 'gross'], ascending=[False, False])

    print('\nMinimum - ', minimum)
    print('Mean - ', mean)
    print('Maximum - ', maximum)


# ===================================================================================
#               FUNCTION FOUR
# ===================================================================================
def gene_analysis():
    print("\nGenre Analysis:")


# ===================================================================================
#               FUNCTION FIVE
# ===================================================================================
def earnings_and_imdb_scores():
    print("\nEarnings and IMDB Scores:")


def main():
    selected_function = 0

    while selected_function != 6:

        # ask for function input and validate it
        # =================================================================
        selected_function = primary_menu()
        while selected_function not in range(1, 7):
            print("\n\nInvalid option! Select again:")
            selected_function = primary_menu()

        # =================================================================
        # if choice is 1
        if selected_function == 1:
            option = secondary_menu1()
            while option not in range(1, 3):
                print("\n\nInvalid option! Select again:")
                option = secondary_menu1()

            if option == 1:
                top_directors()
            # =================================================================
            if option == 2:
                top_actors()

        # =================================================================
        # if choice is 2
        if selected_function == 2:

            validation_working = True

            if validation_working:
                valid1 = False
                valid2 = False

                while not valid1:
                    movie1 = input("\nPlease enter the name of the first movie(messy): ")
                    valid1 = validate_movie(movie1)
                while not valid2:
                    movie2 = input("\nPlease enter the name of the second movie(messy): ")
                    valid2 = validate_movie(movie2)
            else:

                movie1 = input("\nPlease enter the name of the first movie: ")
                movie2 = input("\nPlease enter the name of the second movie: ")

            option = secondary_menu2()

            while option not in range(1, 4):
                print("\n\nInvalid option! Select again:")
                option = secondary_menu2()

            if option == 1:
                imdb_scores(movie1, movie2)
            # =================================================================
            if option == 2:
                gross_earnings(movie1, movie2)
            # =================================================================
            if option == 3:
                movie_facebook_likes(movie1, movie2)

        # =================================================================
        # if choice is 3
        if selected_function == 3:
            x = 1999
            y = 2016
            dist_of_gross_earnings(x, y)

        # =================================================================
        # if choice is 4
        if selected_function == 4:
            gene_analysis()

        # =================================================================
        # if choice is 5
        if selected_function == 5:
            earnings_and_imdb_scores()

        # =================================================================
        # if choice is 6 then exit program
        if selected_function == 6:
            print("\n\nGood bye... ")
            exit()


main()
