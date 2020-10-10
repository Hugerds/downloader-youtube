import tweepy
import pafy

#

url = ("https://www.youtube.com/watch?v=ctQJpfuhoN8")
video = pafy.new(url)
streams = video.streams
for s in streams:
    print(s.resolution, s.extension, s.get_filesize(), s.url)

audiostreams = video.audiostreams
for a in audiostreams:
    print(a.bitrate, a.extension, a.get_filesize())

allstreams = video.allstreams
for s in allstreams:
    print(s.mediatype, s.extension, s.quality)

bestaudio = video.getbestaudio()
nome = video.title
ext = str(input("Qual extensão?"))
filename = bestaudio.download(filepath=f"D:\Downloads\Vídeos\{nome}.{ext}")

""""
url = ("https://www.youtube.com/watch?v=ctQJpfuhoN8")
video = pafy.new(url)
print(f"{s.resolution},{s.get_filesize()}, {s.url}")
best = video.getbest()
bestaudio = video.getbestaudio()

print(f"{best.resolution}, {best.extension}")
print(f"URL: {best.url}")
#filename = audiostreams.download(filepath="D:\Downloads\Vídeos")
filename = bestaudio.download(filepath="D:\Downloads\Vídeos")
"""

