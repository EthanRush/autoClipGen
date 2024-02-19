# Import everything needed to edit video clips
from moviepy.editor import *

# length of desired clips in seconds

crossfade = 2


def clip_gen(base_footage_path, clip_len, outro_clip_path, output_path=None):
    
    # Create object for base footage
    base_footage = VideoFileClip(base_footage_path)
    # Create object for outro clip
    outro_clip = VideoFileClip(outro_clip_path)

    #collect attributes for use in final
    base_fps = base_footage.fps
    base_filename = base_footage.filename.split(".")[0]
    if(output_path is not None):
        base_filename = base_filename.split("/")[-1]
        base_filename = base_filename.split("\\")[-1]
        base_filename = output_path + base_filename
    #how long from base footage to cut for each clip
    base_length = (clip_len - outro_clip.duration)

    # how many clips can be greated evenly
    clip_count = int(base_footage.duration / base_length)
    
    ind = 0
    #loop through and create clips
    base_footage.close()
    outro_clip.close()
    for i in range(clip_count):
        base_footage = VideoFileClip(base_footage_path)
        # Create object for outro clip
        outro_clip = VideoFileClip(outro_clip_path)
        start_time = i*base_length
        end_time = start_time + base_length
        # getting subclip from base footage
        base_clip = base_footage.subclip(start_time, end_time)
       
        

        # creating a composite video
        final = CompositeVideoClip([base_clip.crossfadeout(crossfade+1), outro_clip.set_start(base_clip.duration-crossfade).crossfadein(crossfade)])
       
        
        # showing final clip
        final.write_videofile(base_filename + str(i) + ".mp4", base_fps)
        base_clip.close()
        final.close()
        base_footage.close()
        outro_clip.close()
        ind += 1
    print(ind)
    if(base_footage.duration % base_length != 0):
        base_footage = VideoFileClip(base_footage_path)
        # Create object for outro clip
        outro_clip = VideoFileClip(outro_clip_path)
        base_clip = base_footage.subclip((ind)*base_length)
          

        # creating a composite video
        final = CompositeVideoClip([base_clip.crossfadeout(crossfade+1), outro_clip.set_start(base_clip.duration-crossfade).crossfadein(crossfade)])
        
        
        # showing final clip
        final.write_videofile(filename= base_filename + str(ind+1) + ".mp4", fps=base_fps)
        base_clip.close()
        final.close()
        base_footage.close()
        outro_clip.close()
    