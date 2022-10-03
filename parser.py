import pandas as pd
import spotdl
import os
import xml.etree.ElementTree as ET
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
am_tracks=[]
artists = []
combined = []
tempstr = ""
for item in tracklist:
    x=list(item)
    for i in range (len (x)):
        tempstr = ""
        if x[i].text=="Name":
            name=x[i+1].text
            am_tracks.append(name)
        if x[i].text=="Artist":
            artist=x[i+1].text
            am_tracks.append(artist)
itr = 0
try:
    fp = open('tracks.txt', 'x')
    fp.close()
except:
    pass
with open("tracks.txt", "w") as f:
        for i in range(len(am_tracks)):
            if itr % 2 == 0:
                f.write("\r\n")
            try:
                f.write(am_tracks[itr+1] + " - " + am_tracks[itr])
            except:
                break
            itr += 2
with open("tracks.txt", 'r') as f:
    os.mkdir("output")
    os.chdir("output")
    for line in f:
        os.system("python3 -m spotdl --output-format mp3 --lyrics-provider genius '" + line + "\'")
        print("Downloaded " + line)
os.remove(".spotdl-cache")
os.chdir("..")
os.remove("tracks.txt")
print("Done")