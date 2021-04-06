import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


matches = pd.read_csv('data/matches.csv')
deliveries = pd.read_csv('data/deliveries.csv')


deliveries.head()


matches.head()


deliveries.shape


matches.shape


data = matches.merge(deliveries, left_on='id', right_on='match_id')


data.head()


data.dtypes


data.shape


data.isnull().sum().sort_values(ascending=False)


# count the win by each team
sucTeam = matches['winner'].value_counts().to_frame()

# rename column
sucTeam.rename(columns={'winner':'Count of Wins'}, inplace=True)
sucTeam.head()


print('The most successful team is {}.'.format(sucTeam.index[0]))


# count how many times the player become the player of the match
playerOfMatch = matches['player_of_match'].value_counts().to_frame()

# rename column
playerOfMatch.rename(columns={'player_of_match':'Player of the Match Count'}, inplace=True)
playerOfMatch.head()


print('The most successful player is {}'.format(playerOfMatch.index[0]))


batsmanGrp = deliveries.groupby(["match_id", "inning", "batting_team", "batsman"])
batsmen = batsmanGrp["batsman_runs"].sum().reset_index()
batsmen



