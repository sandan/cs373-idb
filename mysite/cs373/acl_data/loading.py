# python3 manage.py shell

# from cs373.models import *

def load_stages () :
	with open("stages_raw_data.txt") as stagesf :
		stiter = iter(stagesf)
		numberOfStages = int(next(stiter).split()[1])
		stageData = dict()

		for line in stiter :
			data = line.split(': ')	 
			assert(len(data) == 2)

			if (data[1] == "NULL\n") :
				continue

			stageData[data[0]] = data[1]

			if (data[0] == "Twitter") :
				loadDBstage(stageData)
				stageData = dict()

def loadDBstage (stageDict) :
	print(stageDict)
	print()
	# s = Stage(name = stageDict["Name"], )

def load_artists () :
	with open("artist_raw_data.txt") as af :
		aiter = iter(af)
		numberOfArtists = int(next(aiter).split()[1])
		artistData = dict()

		for line in aiter :
			data = line.split(': ')	 
			assert(len(data) == 2)

			artistData[data[0]] = data[1]

			if (data[0] == "Webpage") :
				loadDBartist(artistData)
				artistData = dict()
				
def loadDBartist (artistDict) :
	print(artistDict)
	print()
	# a = Artist(name = artistDict["Name"], )

def load_sponsors () :
	with open("sponsor_raw_data.txt") as sponsorsf :
		spiter = iter(sponsorsf)
		numberOfSponsors = int(next(spiter).split()[1])
		sponsorData = dict()

		for line in spiter :
			data = line.split(': ')	 
			assert(len(data) == 2)

			sponsorData[data[0]] = data[1]

			if (data[0] == "Twitter") :
				loadDBsponsor(sponsorData)
				sponsorData = dict()
				
def loadDBsponsor (sponsorDict) :
	print(sponsorDict)
	print()
	# a = Artist(name = artistDict["Name"], )

load_stages()
load_artists()
load_sponsors()