#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of x below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competign both steps, commit and push your changes to GitHub
Alex = 'hello world! python line " + '1' 
print(Alex)

# second group member's error to fix
Negar = 'pizza' + 'beer' + 'wine'

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
Niro = '1' + '2' +'3'

#Katherine Bak fix this
Katherine = 'pizza' + 'icecream' + 'chocolate' + 'candy' 



# etc. until all group members have fixed and made 1 error



#%%  Part 2  find and remove the invalid response______________________________

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 410, 570]

# the -1 indicates missing data. Your job is to remove it
# use the index method to find the missing value 
missing_rt = rt[-3]

# and then use missing_rt to remove the trial from rt
clean_rt =rt.remove(missing_rt)


# now you have data with more than one missing value
rt_trouble = [400, 450, 500, 440, -1, 410, 570, -1, 400]

# try the same procedure. Does it work? 

# No

# use a comment to explain why or why not below in comments

#This procdeure removes one value at a time. 



# now write an if statement that you can use to remove the frist missing value 
x=-1
if x==-1:
    clean_rt_trouble = rt_trouble.remove(x)
    print(rt_trouble)
Out[18]: [400, 450, 500, 440, 410, 570, -1, 400]

# only when there is a missing value (-1) in a list 
# this statement should always generate a clean_rt list; if there's no missing
# data clean_rt is set to the original rt list.   



# for the last section, you will work with a list of lists:
rt_new = [400, 450, 500, 440, -1, 410, 570]
trial_num = [1,2,3,4,5,6,7]
accuracy = [0, 1, 0, 0, 1, 0]
data = [rt_new, trial_num, accuracy]

# this master list combines information about each trial in an experiment,
# where index 0 in each sublist refers to data from the first trial, etc.
# using the same appraoches as above, find the trial with missing rt data
# and remove it from all sublists in data 
# be sure to only work with the master data list, to practice indexing 
# lists of lists

data=[rt_new.remove(-1),trial_num.remove(5)]



data=[rt_new,trial_num,accuracy]

data
Out[26]: [[400, 450, 500, 440, 410, 570], [1, 2, 3, 4, 6, 7], [0, 1, 0, 0, 1, 0]]

