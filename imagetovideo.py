import imageio.v2
import os
from PIL import Image
def imagetovideo(nm):
    try:
        images = []
        for i in os.listdir(f"image{nm}"):
            with Image.open(fr"image{nm}/{i}") as img:
                img.load()
                cropimg = img.crop((0 , 0, 1000, 1000))
                cropimg.save(fr"image{nm}/{i}", "JPEG")
                images.append(f"image{nm}/"+i)
        with imageio.get_writer(f'{nm}.mp4', mode='I', format='FFMPEG', fps = 1) as writer:
            for img in images:
                writer.append_data(imageio.v2.imread(img))
    except ValueError:
        pass