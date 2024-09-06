from pytubefix import YouTube
from tqdm import tqdm

progress_bar = None

def download():
    global progress_bar
    try:
       audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()
       print(yt.title)
       progress_bar = tqdm(total=audio_stream.filesize, unit='0', unit_scale=True, desc="Downloading")
       audio_stream.download(filename=f"{yt.title}.mp3")
       progress_bar.close()
       print('completed')
    except Exception as e:
        print(e)

def progress(stream, chunk, bytes_remaining):
    global progress_bar
    file_size = stream.filesize
    bytes_downloaded = file_size - bytes_remaining
    progress_bar.update(len(chunk))

url = input("Import your link: \n")
yt = YouTube(url, on_progress_callback=progress)
download()