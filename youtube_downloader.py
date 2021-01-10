import pytube


link = input('Enter the link: ')
destinationFolder= '/Users/administrador/Downloads'
yt = pytube.YouTube(link)

videoName=yt.title

videoWithSound=yt.streams.filter(progressive=True).order_by('resolution').desc().first()
videoWithoutSound= yt.streams.filter( file_extension='mp4').order_by('resolution').desc().first()

# videoWithSound.download(destinationFolder)
print(f"El video '{videoName}' se descargó en la carpeta '{destinationFolder}'")
# print('Se descargó el video en formato HD en la carpeta ' + destinationFolder)
