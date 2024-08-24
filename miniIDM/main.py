from pytubefix import YouTube
from tqdm import tqdm

progress_bar = None
def download():
    global progress_bar
    try:
       #yd = yt.streams.get_highest_resolution()
       video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', res="1080p").order_by('resolution').desc().first()
       audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()
       print(yt.title)
       print(video_stream)
    #    x = input("which stream \n")
       progress_bar = tqdm(total=video_stream.filesize, unit='0', unit_scale=True, desc="Downloading")
       video_stream.download(path)
       audio_stream.download(path, filename='audio.mp4')
       progress_bar.close()
       print('completed')
    except Exception as e:
        print(e)
def progress(stream, chunk, bytes_remaining):
    global progress_bar
    file_size = stream.filesize
    bytes_downloaded = file_size - bytes_remaining
    progress_bar.update(len(chunk))

url = input("import your link: \n")
# path = input("path: \n")
path = "/home/mostafa/Downloads"
yt = YouTube(url, on_progress_callback=progress)
download()
