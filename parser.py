import pandas as pd
import xml.etree.ElementTree as ET
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
with open("tracks.txt", "w") as f:
        for i in range(len(am_tracks)):
            if itr % 2 == 0:
                f.write("\r\n")
            try:
                f.write(am_tracks[itr] + " - " + am_tracks[itr+1])
            except:
                break
            itr += 2
print("Done")