from moviepy.editor import VideoFileClip, AudioFileClip


output_name = input("Enter file name: \n")

video_clip = VideoFileClip('video.mp4')
audio_clip = AudioFileClip('audio.mp4')

final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile(f'{output_name}.mp4', codec='libx264')