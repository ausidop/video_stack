from pathlib import Path
import os
import shutil
from moviepy.editor import VideoFileClip, clips_array

result = []


def stacking_video(vid1, vid2):
    clip1 = VideoFileClip(vid1).set_duration('15')
    clip1_duration = clip1.duration
    audio = clip1.audio
    clip2 = VideoFileClip(vid2).set_duration(clip1_duration)
    file_name = vid1.split('/')[-1].split('.')[0] + '_edited.mp4'
    result.append(file_name)
    final_clip = clips_array([[clip1], [clip2]]).set_audio(audio)
    final_clip.write_videofile(file_name)

source_dir = 'source_video'
target_dir = 'edited_video'
# shutil.move('my_stack.mp4', target_dir + '/my_stack.mp4')
stacking_video('test_video.mp4', 'test_video.mp4')