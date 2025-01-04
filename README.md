# Allango Downloader
Download MP3 Files from the Klett Allango Platform (https://www.allango.net) using Python and FFMPEG (for re-encoding)

# Usage
1. You need to either have [ffmpeg](https://www.ffmpeg.org/download.html) in your PATH or put the executable (`ffmpeg.exe`) next to the script
2. Go to https://www.allango.net and find your book, select "Go to the media" (where you can play the media corresponding to your book in the browser)
3. Copy the page URL, something like "https://www.allango.net/product/MAXP-123456/aug/123-4-56-789101-1"
4. Call the script with `python AllangoDownload.py <url>`
   * `python AllangoDownload.py https://www.allango.net/product/MAXP-123456/aug/123-4-56-789101-1` in our example above
5. It will create a folder and convert all files into that folder

# License of the downloaded files
All licenses of the content still applies. This script just downloads all openly available stream files for the books that you own. As the page states on the top:
> I confirm that I am using this content with the print book, digital book, or copy I have accessed legally. This confirmation is required for licensing purposes.

__This still applies!__
