<h1> Spotipy Writer </h1>

a simple python/spotipy script used to write the user's saved songs to a csv file

<h3> Usage: </h3>

Download the spotipyWriter.py to any location on your computer

Set environment variables for CLIENT_ID and SECRET_ID retrieved from: https://developer.spotify.com/dashboard/login
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='http://google.com/'
```
Run the script using 
```
python spotipyWriter.py [YOUR_SPOTIFY_URI]
```

You should then see a csv output file titled 'savedTracks.csv' located in the same folder as the script
