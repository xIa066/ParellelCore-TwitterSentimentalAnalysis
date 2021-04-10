import json
import ijson
import os
import re
import collections
from mpi4py import MPI
import pdb

# uncomment when run this on spartan - because on spartan it is a superlink
# path1 = os.readlink('./tinyTwitter.json')
# path2 = os.readlink('./bigTwitter.json')
PATH_TINY = './tinyTwitter.json'
PATH_SMALL = './smallTwitter.json'
PATH_BIG = './bigTwitter.json'
PATH_MELBGRID = './melbGrid.json'
PATH_AFINN = './AFINN.txt'

def find_score(afinn: dict, tweet : str) -> float:
	tweet = tweet.lower()
	tweet = tweet.split()
	tweet = list(map(lambda token: re.sub(r'[\!\?\,\.\'\"]','',token), tweet))
	scores = [afinn[token] for token in tweet if token in afinn.keys()]
	return sum(scores)

# this function takes a json object return two list
# 1) a list of latitude intervals
# 2) a list of longtitude intervals
def parse_regions(melbGrid:json) -> (list, list):

	latitudes = []
	longtitudes = []

	for item in melbGrid['features']:
		latitudes.append(item['properties']['xmin'])
		latitudes.append(item['properties']['xmax'])
		longtitudes.append(item['properties']['ymin'])
		longtitudes.append(item['properties']['ymax'])

	latitudes = sorted(list(set(latitudes)))
	longtitudes = sorted(list(set(longtitudes)))

	return latitudes, longtitudes

# this function takes a list of latitude/longtitude interval and match it with a given
# coordinate, and then return a string of region/grid name
def find_region(latitudes: list, longtitudes: list, coordinate: (float, float)) -> str:

	LATITUIDE = 0
	LONGTITUDE = 1
	offset = -1

	grid_latitude = ['D', 'C', 'B', 'A']
	grid_longtitude = ['1', '2', '3', '4', '5']

	assert(len(longtitudes)== len(grid_latitude)+1)
	assert(len(latitudes)==len(grid_longtitude)+1)

	latitudes_indices = binary_search(latitudes, 0, len(latitudes)-1, coordinate[LATITUIDE])
	longtitudes_indices = binary_search(longtitudes, 0, len(longtitudes)-1, coordinate[LONGTITUDE])
	# print(longtitudes_indices)
	# find region of latitude
	if latitudes_indices > 0:
		name_latitude = grid_latitude[latitudes_indices+offset]
	# index out of bound
	else:
		name_latitude = grid_latitude[0]

	# find region of longtitude
	if longtitudes_indices > 0:
		name_longtitude = grid_longtitude[longtitudes_indices+offset]
	else:
		name_longtitude = grid_longtitude[0]

	return (name_latitude+name_longtitude)

# Returns index of x in arr if present, else return the index that its value is the supremum 
def binary_search(arr: list, low: int, high: int, x: float):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return low

# This function do the following job
# 1. read melb grid file into desired data structure
# 2. read afinn file into defsired data structure
# 3. call find_score() and find_region, at last return two Counter(), one count the total
# tweets, the other counts the sentimental scores
def do_work(tweets: list, coordinates: list) -> (collections.Counter, collections.Counter):

	with open(PATH_MELBGRID) as f:
		melbGrid = json.load(f)

	latitudes, longtitudes =  parse_regions(melbGrid)

	with open(PATH_AFINN) as f:
		word_score_pair = f.readlines()

	afinn = {}
	for line in word_score_pair:
		word, score =line.split('\t')
		afinn[word] = float(score)

	sentiment_score = collections.Counter()
	total_tweet = collections.Counter()

	assert(len(tweets) == len(coordinates))
	for tweet, coordinate in zip(tweets, coordinates):
		region = find_region(latitudes,longtitudes, coordinate)
		sentiment_score[region] += find_score(afinn, tweet)
		total_tweet[region] += 1
	return sentiment_score, total_tweet

def main():

	comm = MPI.COMM_WORLD
	nproc = comm.Get_size()
	iproc = comm.Get_rank()
	# inode = comm.Get_processor_name()
	isOneCore = True if nproc == 1 else False

	if isOneCore:

		with open(PATH_TINY) as f:
			tweets =[]
			coordinates = []
			rows = ijson.items(f, 'rows.item.value')
			for row in rows:
				tweets.append(row['properties']['text'])
				coordinates.append((row['geometry']['coordinates'][0], row['geometry']['coordinates'][1]))

		sentiment_score, total_tweet = do_work(tweets, coordinates)
		print(sentiment_score)
		print(total_tweet)

	# master-worker design pattern
	else:
		print("you are beautiful")
	if iproc == 0:
		print("you are beautiful")
	# print(inode)
	MPI.Finalize()


if __name__ == "__main__":
    main()