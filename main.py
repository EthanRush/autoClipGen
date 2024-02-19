from clip_gen import clip_gen
from clip_paths import base_footage_path, outro_clip_path, output_path

CLIP_LENGTH = 30
if __name__ == '__main__':  
    clip_gen(base_footage_path, CLIP_LENGTH, outro_clip_path, output_path)