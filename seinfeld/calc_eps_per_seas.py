# First pyandcoffee homework
# Apr 2018, C. Muhs
# Read seinfeld data, write function that calculates number of episodes per season as a dict

import os
from collections import defaultdict # see page 64. Get defaultdicts from collections library
import pprint # for pretty printing data structures

'''
Function: given an episode file path, parse each line
and return a nested dictionary
which maps season -> episode -> episode info
'''
def index_episodes(file_path):
    with open(file_path) as f:  
        lines = f.readlines()
        eps_by_season = defaultdict(dict)
        # iterate over lines, skipping the file header
        for line in lines[1:]:
            # throw away the first column (a row index)
            # see page 54. '_' means ditch the first column. 'season' defines the 2nd column as a main key. 'ep' defines the 3rd column as a nested key. '*rest' means all other columns are the values for each key.
            _, season, ep, *rest = line.split(sep=',') 
            eps_by_season[season][ep] = rest
    # f.close() # close the file. Not needed since using 'with'
    return eps_by_season

'''
given a nested dictionary of seasons to episodes
return a dictionary of season number to episode count
'''
def count_episodes(episode_index):
    eps_per_season = defaultdict(dict)
    for season in episode_index:
        eps_per_season[season] = len(episode_index[season].keys())
    return eps_per_season

os.chdir('/Users/Chisto/Dropbox/data_science/repos/pyandcoffee/seinfeld/') # Change to directory where the csv is
# os.getcwd()
# Define file name
mypath = 'episode_info.csv'
# Run the functions
myindex = index_episodes(mypath)
mycount = count_episodes(myindex)
# Print the result - # episodes per season
pprint.pprint(mycount)