# youtube-downloader
The video downloader script is a command-line tool built in Python that allows users to easily download videos or audio from YouTube.

With support for specifying the YouTube URL, desired file name, and optional settings like audio-only downloads and custom file extensions, it provides flexibility and convenience. Utilizing the Pytube library, it offers progress tracking during downloads and seamlessly saves the media files to the specified local directory, making it a handy tool for fetching multimedia content from YouTube.

if the url includes '&' and some other symbols. encapsulate the url in "". 
e.g python wiredvideodownloader.py "youtubelink&&&" desired file name (-a for audio only)
change the desired location for video download in the .ENV file
