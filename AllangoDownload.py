import requests
import xml.etree.ElementTree as ET
import subprocess
import os
import argparse

parser = argparse.ArgumentParser(description='Download MP3 Files from Allango')
parser.add_argument("inputURL", help="URL of the page you want to download")
args = parser.parse_args()

session = requests.Session() # Cookie Storage

# Fetch Info for Files
inputISBN = args.inputURL.rpartition('/')[2]

x = session.get(f"https://www.allango.net/api/augmented/{inputISBN}")
r = x.json()

# Create Output Folder
isbn = r["book"]["isbn"]
if not os.path.exists(f"./{isbn}/"):
    os.makedirs(f"./{isbn}/")

for page in r["pages"]:
    if not page["audios"]: continue
    for audio in page["audios"]:
        # Fetch URL of MPD file
        assetRequest = session.get(f"https://www.allango.net/api/asset/access/public/dasha/{audio['assetId']}")
        url = assetRequest.json()["url"]

        # Fetch and parse MPD file
        mpdRequest = session.get(f"https://www.allango.net/{url}")
        tree = ET.ElementTree(ET.fromstring(mpdRequest.text))

        # Get all BaseURLS and Download Content
        mpdUrls = tree.findall("./*/*/*/{urn:mpeg:dash:schema:mpd:2011}BaseURL")
        for murl in mpdUrls:
            dashStreamUrl = f"{f"https://www.allango.net/{url}".rpartition('/')[0]}/{murl.text}"
            
            # Download and write content to "./stream.tmp"
            streamDataRequest = session.get(dashStreamUrl)
            with open('./stream.tmp', 'wb') as f:
                f.write(streamDataRequest.content)

            # Convert to MP3 file with FFMPEG
            print(f"Converting \"{audio["originalFilename"]}\"")
            subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", "./stream.tmp", "-c:v", "copy", "-c:a", "libmp3lame", "-q:a", "4", f"./{isbn}/{audio["originalFilename"]}"]) 

# Remove temporary file
os.remove("./stream.tmp")                  



