import tweepy
import pafy

url = ("https://www.youtube.com/watch?v=ctQJpfuhoN8")
video = pafy.new(url)
streams = video.streams
#for s in streams:
   # print(s.resolution, s.extension, s.get_filesize(), s.url)

#audiostreams = video.audiostreams
#for a in audiostreams:
 #   print(a.bitrate, a.extension, a.get_filesize())

def mycb(total, recvd, ratio, rate, eta):
    #print(recvd, ratio, eta)
    print(f"Em andamento...\n")

allstreams = video.allstreams
for s in allstreams:
    print(s.mediatype, s.extension, s.quality)

bestvideo = video.getbestvideo()
bestaudio = video.getbestaudio()
tituloVideo = video.title
op = str(input("Deseja baixar em audio ou video?\nSua opção: "))
if "audio" in op:
    filename = bestaudio.download(filepath=f"D:\Downloads\Vídeos\{tituloVideo}.mp3", meta=True, quiet=False, callback=mycb)
    print(f"audio")
if "video" in op:
    filename = bestvideo.download(filepath=f"D:\Downloads\Vídeos\{tituloVideo}", meta=True, quiet=False, callback=mycb)
    print(f"video")

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