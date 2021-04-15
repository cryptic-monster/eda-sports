import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic("matplotlib", " inline")


matches = pd.read_csv('data/matches.csv', parse_dates=['date'])
deliveries = pd.read_csv('data/deliveries.csv')


matches.head()


deliveries.head()


print('There are {} rows and {} columns on deliveries dataframe.'.format(deliveries.shape[0], deliveries.shape[1]))
print('There are {} rows and {} columns on matches dataframe.'.format(matches.shape[0], matches.shape[1]))


matches.isnull().sum()


matches.loc[matches['city'].isnull()]


matches.loc[matches.venue == 'Dubai International Cricket Stadium', 'city'] = 'Dubai'


matches.loc[matches['winner'].isnull()]


matches.loc[matches['player_of_match'].isnull()]


matches.loc[matches['result'] == 'no result']


matches.drop(matches[matches['result'] == 'no result'].index, inplace=True)


matches.to_csv('data/matches-cleaned.csv')


deliveries.isnull().sum()


deliveries.to_csv('data/deliveries-cleaned.csv')


data = matches.merge(deliveries, left_on='id', right_on='match_id')


data.head()


# different datatypes in the merged dataframe
dataTypes = data.dtypes 

# count of null values in each columns
nullCnt = data.isnull().sum().sort_values(ascending=False) 

# concatenate
dataProperty = pd.concat([dataTypes, nullCnt], axis=1)

# rename columns
columns = ['data type', 'count of nulls']
dataProperty.columns = columns

# sort by count of nulls
dataProperty.sort_values(by='count of nulls', ascending=False, inplace=True)
dataProperty


data.shape


data.to_csv('data/merged_data.csv')





# count the win by each team
sucTeam = matches['winner'].value_counts().to_frame()

# rename column
sucTeam.rename(columns={'winner':'Count of Wins'}, inplace=True)
sucTeam.head()


# visualize
sns.barplot(x=sucTeam.index, y='Count of Wins', data=sucTeam)
plt.xticks(rotation='vertical')
plt.show()


print('The most successful team is {}.'.format(sucTeam.index[0]))


# count how many times the player become the player of the match
playerOfMatch = matches['player_of_match'].value_counts().to_frame()

# rename column
playerOfMatch.rename(columns={'player_of_match':'Player of the Match Count'}, inplace=True)
playerOfMatch.head()


topPlayers = playerOfMatch.iloc[:10]


# visualize
sns.barplot(x=topPlayers.index, y='Player of the Match Count', data=topPlayers)
plt.xticks(rotation='vertical')
plt.show()


print('The most successful player is {}.'.format(playerOfMatch.index[0]))


batsmanGrp = deliveries.groupby(["match_id", "inning", "batting_team", "batsman"])
batsmen = batsmanGrp["batsman_runs"].sum().reset_index()
batsmen


















