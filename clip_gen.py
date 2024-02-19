# Import everything needed to edit video clips
from moviepy.editor import *

# length of desired clips in seconds

crossfade = 2


def clip_gen(base_footage_path, clip_count, outro_clip_path, base_length, base_filename, base_fps):
    ind = 0
    base_footage = VideoFileClip(base_footage_path)
    # Create object for outro clip
    outro_clip = VideoFileClip(outro_clip_path)
    for i in range(clip_count):
        # Create object for outro clip
       

        start_time = i*base_length
        end_time = start_time + base_length
        # getting subclip from base footage
        base_clip = base_footage.subclip(start_time, end_time)
        base_clip = base_clip.audio_fadeout(crossfade)
        base_clip = base_clip.resize((1080,1920))


        # creating a composite video
        final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                       method="compose",
                                       padding=-crossfade)
       
        
        # showing final clip
        final.write_videofile(base_filename + str(i) + ".mp4", base_fps)
        base_clip.close()
        final.close()
        
        ind += 1
    if(base_footage.duration % base_length != 0):
        # Create object for outro clip
        base_clip = base_footage.subclip((ind)*base_length)
        base_clip = base_clip.audio_fadeout(crossfade)
        base_clip = base_clip.resize((1080,1920))

        
        # creating a composite video
        final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                       method="compose",
                                       padding=-crossfade)
        
        
        # showing final clip
        final.write_videofile(filename= base_filename + str(ind+1) + ".mp4", fps=base_fps)
        base_clip.close()
        final.close()
    return
    


def clip_gen_parallel(base_footage_path, clip_index, outro_clip_path, base_length, base_filename, base_fps):
    base_footage = VideoFileClip(base_footage_path)
    # Create object for outro clip
    start_time = clip_index*base_length
    end_time = start_time + base_length
    # getting subclip from base footage
    base_clip = base_footage.subclip(start_time, end_time)
    base_clip = base_clip.audio_fadeout(crossfade)
    base_clip = base_clip.resize((1080,1920))

    outro_clip = VideoFileClip(outro_clip_path)
    # creating a composite video
    final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                    method="compose",
                                    padding=-crossfade)
    
    
    # showing final clip
    final.write_videofile(base_filename + str(clip_index) + ".mp4", base_fps)
    base_clip.close()
    final.close()
    return

def last_clip(base_footage_path, clip_index, outro_clip_path, base_length, base_filename, base_fps):
    base_footage = VideoFileClip(base_footage_path)
    # Create object for outro clip
    base_clip = base_footage.subclip((clip_index)*base_length)
    base_clip = base_clip.audio_fadeout(crossfade)
    base_clip = base_clip.resize((1080,1920))

    outro_clip = VideoFileClip(outro_clip_path)

    # creating a composite video
    final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                    method="compose",
                                    padding=-crossfade)
    
    
    # showing final clip
    final.write_videofile(filename= base_filename + str(clip_index) + ".mp4", fps=base_fps)
    base_clip.close()
    final.close()