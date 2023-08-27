import os
import xml.etree.ElementTree as ET
import requests
import re
def get_song_id(title, artist):
    api_key = '9d1d0e10066282ce0243bf88ee120070'
    base_url = 'https://api.deezer.com/search'
    print(f'Searching for "{title}" by "{artist}"...')
    # URL encode the title and artist
    title = title.replace(' ', '%20')
    artist = artist.replace(' ', '%20')

    # Construct the API request URL
    url = f'{base_url}?q=artist:"{artist}"%20track:"{title}"&limit=1&output=json'

    # Add the API key as a header (optional, but recommended)
    headers = {'user-key': api_key}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and len(data['data']) > 0:
                # Extract and return the song ID
                return data['data'][0]['id']
            else:
                print('No matching song found.')
        else:
            print(f'Error: {response.status_code} - {response.text}')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

    return None
folder_exists = False
lib = r"Library.xml"
tree = ET.parse(lib)
root = tree.getroot()
main_dict=root.findall('dict')
for item in list(main_dict[0]):    
    if item.tag=="dict":
        tracks_dict=item
        break
tracklist=list(tracks_dict.findall('dict'))
names=[]
artists = []
tempstr = ""
for item in tracklist:
    x=list(item)
    for i in range (len (x)):
        tempstr = ""
        if x[i].text=="Name":
            name=x[i+1].text
            names.append(name)
        if x[i].text=="Artist":
            artist=x[i+1].text
            artists.append(artist)
#remove all brackets and the text in them from the names
for each in names:
    tempstr = ""
    for i in range(len(each)):
        if each[i] == "(":
            break
        tempstr += each[i]
    names[names.index(each)] = tempstr
ids = []
for i in range(len(names)):
    ids.append(get_song_id(names[i], artists[i]))
for each in ids:
    if each == None:
        ids.remove(each)
for each in ids:
    os.system(f"deemix 320 --path downloads/ https://deezer.com/track/{each}")