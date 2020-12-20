import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import praw
import sys
import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

#User provides their own login information for Reddit.
CLIENT_ID=''
CLIENT_SECRET=''
PASSWORD=''
USERNAME=''
USER_AGENT=''

r = praw.Reddit(client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                password=PASSWORD,
                user_agent=USER_AGENT,
                username=USERNAME)

speech_types = dict()
bad_types = ("$","#",".","\'\'","(",",","``",")",":")

h = open(sys.argv[1], 'w')
sub = r.subreddit(sys.argv[2])

for submission in sub.top('year',limit=50):
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()
    for comment in comments:
        text = nltk.word_tokenize(str(comment.body))
        nltkwords = nltk.pos_tag(text)
        for word in nltkwords:
            if word[1] not in bad_types:
                if word[1] in speech_types:
                    speech_types[word[1]] += 1
                else:
                    speech_types[word[1]] = 1


w_count2 = 0
for key in speech_types:
    w_count2 += speech_types[key]

h.write(str(speech_types))
h.write("\ntotal number of words: " + str(w_count2))
h.write("\nproportionally: ")

speech_types_list = [(key, float(speech_types[key]/w_count2)) for key in speech_types]

def sort_key(key):
    return key[1]
speech_types_list.sort(key=sort_key)

for st in speech_types_list:
    h.write("\ntype: " + st[0])
    h.write(" proportion: " + str(st[1]))
h.close()


