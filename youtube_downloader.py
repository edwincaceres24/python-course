import pytube
# var=input('Your name is: ')
# print(var)

link = input('Enter the link: ')
destinationFolder= '/Users/administrador/Downloads'
yt = pytube.YouTube(link)

videoWithSound=yt.streams.filter(progressive=True).order_by('resolution').desc().first()
videoWithoutSound= yt.streams.filter( file_extension='mp4').order_by('resolution').desc().first()

# videoFHD = yt.streams.filter( mime_type="video/mp4", res="1080p").first()
# videoHD = yt.streams.filter( mime_type="video/mp4", res="7720p").first()
# def downloadVideo ():
#     if len(videoFHD)==1:
#         videoFHD.download(destinationFolder)
#         print('Se descargó el video en formato FHD en la carpeta ' + destinationFolder)
#     else:
#         videoHD.download(destinationFolder)

# print(firstVideo)
# firstVideo.download(destinationFolder)
# print(yt.streams.filter(progressive=True))
# print(firstVideo)
videoWithSound.download(destinationFolder)
print('Felicidades, eres un crack')
# print('Se descargó el video en formato HD en la carpeta ' + destinationFolder)
