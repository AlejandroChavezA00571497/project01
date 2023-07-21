#https://www.youtube.com/watch?v=WAmEZBEeNmg


from dotenv import load_dotenv
#pip install python-dotenv
import os
import base64
from requests import post, get
#pip install requests
import json
from pprint import pprint



load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

#print(client_id, client_secret)


#CLIENT CREDENTIALS WORKFLOW (No se acceden a datos de usuario ni se controla el Spotify del usuario, solo se accede a los datos de Spotify)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {"grant_type" : "client_credentials"}

    result = post(url, headers = headers, data = data)
    json_response = json.loads(result.content)
    token = json_response["access_token"]
    return token


def get_auth_header(token):
    return{"Authorization" : "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query

    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name found...")
        return None
    
    return json_result[0]


def get_songs_by_artists(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=CO"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)["tracks"]
    #pprint(json_result)
    return json_result


def get_song_features(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=CO"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)["tracks"]
    #pprint(json_result)
    return json_result


token = get_token()
result = search_for_artist(token, "Bad Bunny")
artist_id = result["id"]
songs = get_songs_by_artists(token, artist_id)
song_list = []




for idx, song in enumerate(songs):
    #song_list = song_list.append(song)
    print(f"{idx + 1}. {song['name']}")    
