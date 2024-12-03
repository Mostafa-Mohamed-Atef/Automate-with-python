import os 
from moviepy.editor import VideoFileClip, concatenate_videoclips
VIDS_LIST = []

def videos(path):
    for file in os.listdir(path):
        if file.endswith(".mp4"):
            full_path = os.path.join(path, file)
            VIDS_LIST.append(full_path)

def extract_order(filename):

    base_name = os.path.basename(filename).strip()
    return int(base_name.split('-')[0])


def files_sorted():
    VIDS_LIST.sort(key=extract_order)
    print(VIDS_LIST)

def merge():
    configured_vids = []
    for vid in VIDS_LIST:
        configured_vids.append(VideoFileClip(vid))
    result = concatenate_videoclips(configured_vids)
    result.write_videofile("ouput.mp4")


if __name__=="__main__":
    #sorting and accessing video files
    path = input("Enter Path: \n")
    videos(path)
    files_sorted()
    merge()
