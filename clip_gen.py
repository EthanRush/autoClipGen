# Import everything needed to edit video clips
from moviepy.editor import *

# length of desired clips in seconds

crossfade = 2


def clip_gen(base_footage_path, clip_count, outro_clip_path, base_length, base_filename, base_fps):
    # Create object for base footage
    base_footage = VideoFileClip(base_footage_path)
    # Create object for outro clip
    outro_clip = VideoFileClip(outro_clip_path)
    outro_clip = outro_clip.resize((1080,1920))
    for i in range(clip_count):
        # Create object for outro clip
       

        start_time = i*base_length
        end_time = start_time + base_length
        # getting subclip from base footage
        base_clip = base_footage.subclip(start_time, end_time)
        base_clip = base_clip.audio_fadeout(crossfade)

        #resize to instagram reel dimensions
        base_clip = base_clip.resize((1080,1920))


        # creating a composite video
        final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                       method="compose",
                                       padding=-crossfade)
       
        splitFileName = base_filename.split("___")
        filename = splitFileName[0] + "_" + str(i) + "_" + splitFileName[1] + ".mp4"
        
        # showing final clip
        final.write_videofile(filename, base_fps)
        base_clip.close()
        final.close()
    if(base_footage.duration % base_length != 0):
        # Create object for outro clip
        base_clip = base_footage.subclip((clip_count-1)*base_length)
        base_clip = base_clip.audio_fadeout(crossfade)

        # Resize to Instagram Reel dimensions
        base_clip = base_clip.resize((1080,1920))

        
        # creating a composite video through negative padding in the concatenate
        final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                       method="compose",
                                       padding=-crossfade)
        
        # Insert Clip number
        filename = base_filename.replace("___",  "_" + str(clip_index) + "_") + ".mp4"
        
        # write final clip
        final.write_videofile(filename= filename, fps=base_fps)
        base_clip.close()
        final.close()
    return
    


def clip_gen_parallel(base_footage_path, clip_index, outro_clip_path, base_length, base_filename, base_fps):
    # Create object for base footage
    base_footage = VideoFileClip(base_footage_path)

    # Get the start time for the clip
    start_time = clip_index*base_length
    end_time = start_time + base_length

    # getting subclip from base footage
    base_clip = base_footage.subclip(start_time, end_time)

    # fade out the audio for smoother transition to outro
    base_clip = base_clip.audio_fadeout(crossfade)

    # Resize to Instagram Reel dimensions
    base_clip = base_clip.resize((1080,1920))

    # Create object for outro clip
    outro_clip = VideoFileClip(outro_clip_path)

    #Resize to Instagram Reel dimensions
    outro_clip = outro_clip.resize((1080,1920))
    # creating a composite video
    final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                    method="compose",
                                    padding=-crossfade)
    
    # Insert Clip number
    filename = base_filename.replace("___",  "_" + str(clip_index) + "_") + ".mp4"

    # write final clip
    final.write_videofile(filename, base_fps)

    # close files
    base_clip.close()
    final.close()
    base_footage.close()
    outro_clip.close()
    return

def last_clip(base_footage_path, clip_index, outro_clip_path, base_length, base_filename, base_fps):
    
    base_footage = VideoFileClip(base_footage_path)
    
    # Create clip from base footage
    base_clip = base_footage.subclip((clip_index)*base_length)
    
    # Fade out base footage for better transition to outro
    base_clip = base_clip.audio_fadeout(crossfade)
    # Resize for Instagram Dimensions
    base_clip = base_clip.resize((1080,1920))
    
    # Create object for outro clip
    outro_clip = VideoFileClip(outro_clip_path)
    outro_clip = outro_clip.resize((1080,1920))

    # creating a composite video
    final = concatenate_videoclips(clips=[base_clip.fx(transfx.crossfadeout,crossfade), outro_clip.set_start(base_clip.duration-crossfade).fx(transfx.crossfadein,crossfade)],
                                    method="compose",
                                    padding=-crossfade)
    # Insert Clip number
    filename = base_filename.replace("___",  "_" + str(clip_index) + "_") + ".mp4"
    # showing final clip
    final.write_videofile(filename=filename, fps=base_fps)
    
    # close files
    base_clip.close()
    final.close()
    base_footage.close()
    outro_clip.close()