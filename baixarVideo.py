#import pytube
from pytube import YouTube

Url = input("Informe a URL do vídeo: ");
Resolucao = input("Informe a resolução(Use o formato 720p, 144p, 1080p...): ");
video = YouTube(Url);

stream = video.streams.filter(res=Resolucao).first()
try:
  stream.download("videos");
  print("Download realizado com sucesso!");
except:
  print("Não foi possível baixar o seu vídeo! Tente novamente!")
