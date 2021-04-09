import json
import ijson
import os
import r
from mpi4py import MPI

# uncomment when run this on spartan - because on spartan it is a superlink
# path1 = os.readlink('./tinyTwitter.json')
# path2 = os.readlink('./bigTwitter.json')
PATH_TINY = './tinyTwitter.json'
PATH_SMALL = './smallTwitter.json'
PATH_BIG = './bigTwitter.json'
PATH_AFINN = './AFINN.txt'
PATH_MELBGRID = './melbGrid.json'

# for i in range(len(grid_data['features'])):
# 	print(grid_data['features'][i]['properties'])
# {'id': 'A1', 'xmin': 144.7, 'xmax': 144.85, 'ymin': -37.65, 'ymax': -37.5}


def find_score(afinn: dict, tweet : str) -> float:
	tweet = tweet.lower()
	tweet.split()
	tweet = list(map(lambda token: re.sub(r'[\!\?\,\.\'\"]','',token), tweet))
	scores = [afinn[token] if token in afinn.keys() for token in tweet]
	return sum(scores)

def find_region(melbGrid: json, coordinate: (float, float)) -> str:
	LONGTITUDE = 0
	LATITUIDE = 1

	latitudes = []
	longtitudes = []
	regions = []

	for item in melbGrid['features']:
		regions.append(item['properties']['id'])
		latitudes.append(item['properties']['xmin'])
		latitudes.append(item['properties']['xmax'])
		longtitudes.append(item['properties']['ymin'])
		longtitudes.append(item['properties']['ymax'])

	latitudes = sort(list(set(latitudes)))
	longtitudes = sort(list(set(longtitudes)))

	latitudes_indices = binary_search(latitudes, 0, len(latitudes)-1, coordinate[LATITUIDE])
	longtitudes_indices = binary_search(longtitudes, 0, len(longtitudes)-1, coordinate[LONGTITUDE])

# Returns index of x in arr if present, else return a list of left index, right index contain value x
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
        return (high, low)


def do_work(data: list) -> (float, str):

	tweet = 
	coordinate = 
	return (compute_score(afinn, tweet), compute_region(melbGrid, coordinate))

def main():

	comm = MPI.COMM_WORLD
	nproc = comm.Get_size()
	iproc = comm.Get_rank()
	# inode = comm.Get_processor_name()

	isOneCore = True if nproc == 1 else False

	# 
	if isOneCore:



	# master-worker design pattern
	else:

	tweet_file_stats = os.stat(PATH_TINY)


	with open('./tinyTwitter.json') as f:
		rows = ijson.items(f, 'rows.item.value')
		for row in rows:
			tweet = row['properties']['text']
			coordinate = (row['geometry']['coordinates'][0], row['geometry']['coordinates'][1])

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

	nproc = MPI.COMM_WORLD.Get_size()
	iproc = MPI.COMM_WORLD.Get_rank()
	inode = MPI.Get_processor_name()
	# print(nproc)
	if iproc == 0 :
		print("you are beautiful")
	# print(inode)
	MPI.Finalize()


if __name__ == "__main__":
    main()