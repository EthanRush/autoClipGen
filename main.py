from clip_gen import clip_gen, clip_gen_parallel, last_clip
from clip_paths import base_footage_path, outro_clip_path, output_path
from moviepy.editor import *
import multiprocessing as mp
CLIP_LENGTH = 30
if __name__ == '__main__':  
    
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
    base_length = (CLIP_LENGTH - outro_clip.duration)

    # how many clips can be greated evenly
    clip_count = int(base_footage.duration / base_length)
    process_ct = min(max(mp.cpu_count() - 2, 1), clip_count)
    ind = 0
    #loop through and create clips
    outro_clip = outro_clip.resize((1080,1092))
    base_footage.close()
    outro_clip.close()

    if process_ct > 1:
        pool = mp.Pool(process_ct) 
        for x in range(0, clip_count):
            res = pool.apply_async(clip_gen_parallel, args=(base_footage_path, x, outro_clip_path, base_length, base_filename, base_fps))
        pool.close()
        pool.join()
        last_clip(base_footage_path, clip_count, outro_clip_path, base_length, base_filename, base_fps)
    else:
        clip_gen(base_footage_path, clip_count, outro_clip_path, base_length, base_filename, base_fps)