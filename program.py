import json
import os
import r
from mpi4py import MPI

# uncomment when run this on spartan - because on spartan it is a superlink
# path1 = os.readlink('./tinyTwitter.json')
# path2 = os.readlink('./bigTwitter.json')
PATH_TINY = './tinyTwitter.json'
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



def do_work(data: json) -> (float, str):
	tweet = 
	coordinate = 
	return (compute_score(afinn, tweet), compute_region(melbGrid, coordinate))




def main():

	nproc = MPI.COMM_WORLD.Get_size()
	iproc = MPI.COMM_WORLD.Get_rank()
	inode = MPI.Get_processor_name()

	# one node one core
	if nproc

	tweet_file_stats = os.stat(PATH_TINY)


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