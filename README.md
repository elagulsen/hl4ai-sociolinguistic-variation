# hl4ai-sociolinguistic-variation

Code for an assignment on sociolinguistic variation for 11-324: Human Language for AI.
Takes Reddit data from the top 50 posts of a given subreddit and uses NLTK to tag words with their types of speech, then provides analysis.

Syntax:
python subreddit-data.py output-file subreddit-name
ex.
python subreddit-data.py nyc.txt nyc

Sample output (condensed):
{'DT': 37606, 'RB': 29555, 'VBZ': 13841}
total number of words: 422333
proportionally: 
type: DT proportion: 0.08904347990803466
type: IN proportion: 0.10409084774336838
type: NN proportion: 0.14555812593380105

Needs to be given valid Reddit account credentials in subreddit-data.py.
