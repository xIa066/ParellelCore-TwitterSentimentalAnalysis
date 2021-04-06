import json
import os

# uncomment when run this on spartan - because on spartan it is a superlink
# path1 = os.readlink('./tinyTwitter.json')
# path2 = os.readlink('./bigTwitter.json')
PATH_TINY = './tinyTwitter.json'
PATH_BIG = './bigTwitter.json'
PATH_AFINN = './AFINN.txt'
PATH_MELBGRID = './melbGrid.json'

with open(PATH_TINY) as f:
  twitter_data = json.load(f)

with open(PATH_MELBGRID) as f:
	grid_data = json.load(f)

with open(PATH_AFINN) as f:
	word_score_pair = f.readlines()

lexicon = {}
for line in word_score_pair:
	word, score =line.split('\t')
	lexicon[word] = float(score)



