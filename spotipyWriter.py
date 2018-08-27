import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError
import csv

# Get the username from terminal
username = sys.argv[1]
# Define nessisary scope
scope = 'user-read-private user-library-read' 

#erase cache and prompt for user permission
try:
	token = util.prompt_for_user_token(username, scope)
except (AttributeError, JSONDecodeError):
	os.remove(f".cache-{username}")
	token = util.prompt_for_user_token(username, scope)


#create spotify object
spotifyObject = spotipy.Spotify(auth=token)

#get the current user
user = spotifyObject.current_user()
displayName = user['display_name']

startingOffset = 0

outfile = open("./savedTracks.csv", "w")
writer = csv.writer(outfile)

# loop to iterate through saved tracks (nessisary as limit of tracks to pull at once is 50)
while True:
	try:
		savedTracks = spotifyObject.current_user_saved_tracks(limit=50, offset=startingOffset)
		total_tracks = savedTracks['total']
		# if there are no more items to import, break out of the while loop
		if savedTracks['items'] == []:
			break
		for item in savedTracks['items']:
			track = item['track']
			writer.writerow([track['name'], track['artists'][0]['name']])

		startingOffset+=50
	except:
		break


print("Written to file \'savedTracks.csv\'")
