# Encore_Challenge
Coding Challenge for  Encore interview

Both coding challenges are included in this repository.

The code for question 4 is in the function flatten() in the arrayOps module.
The code for question 5 is in the class TempTracker, located in the rfClasses module.

The test code for both solutions is in the tests/unit/test_challenges.py
If you want to run the tests, you'll need to run them in a python 2.7 environment with the pytest module installed.
You can install pytest by opening a command line or terminal window and typing:

*python -m pip install pytest'*

Once pytest is installed, cd to the Encore_Challenge project, and type:

*pytest tests -v*

# Solutions
# flatten()
will flatten an array of arbitrarily nested arrays of integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4]. 

# TempTracker Class
has these methods:

•	insert()—records a new temperature.

•	get_max()—returns the highest temp we've seen so far.

•	get_min()—returns the lowest temp we've seen so far.

•	get_mean()—returns the mean of all temps we've seen so far.

get_mean() returns a float, but the rest of the getter functions return integers. Temperatures are inserted as integers. Fahrenheit scale is assumed. 
