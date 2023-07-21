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









def search_for_playlist(token, playlist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={playlist_name}&type=playlist&limit=1"

    query_url = url + query

    result = get(query_url, headers = headers)
    json_result_playlist = json.loads(result.content)["playlists"]["items"]
    if len(json_result_playlist) == 0:
        print("No playlist with this name found...")
        return None
    
    #pprint(json_result_playlist)
    return json_result_playlist[0]




def get_songs_in_playlist(token, artist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    #pprint(json_result)
    return json_result





'''
def get_song_features(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=CO"
    headers = get_auth_header(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)["tracks"]
    #pprint(json_result)
    return json_result
'''




token = get_token()
result = search_for_playlist(token, "Top 50: Global")
playlist_id = result["id"]
songs = get_songs_in_playlist(token, playlist_id)
#song_list = []






for idx, song in enumerate(songs):
    #song_list = song_list.append(song)
    print(f'{idx + 1}. {song["track"]["name"]}')    



'''
APUNTES:

Ya funciona para sacar los nombres de las canciones de una playist, en este caso para sacar los de Top 50: Global.
La función get_songs_in_playlist es donde se hace todo el desmadre de ir pidiendo los objetos dentro de la respuesta json del request con el url: https://api.spotify.com/v1/playlists/{playlist_id}.


Queda pendiente ver cómo pasar todos esos nombres a una lista que después pueda ser usada para pasar los nombres de canciones a la API de Genius.
Igual considerar que ya con la estructura que está podríamos pedir los ids de las canciones, en lugar del nombre, en caso de que Genius requiera que le pasemos los IDs.
'''


