import os
import time
os.environ['MAGICK_AREA_LIMIT'] = "100MB"
os.environ['MAGICK_TEMPORARY_PATH'] = "."
os.environ['MAGICK_TMPDIR'] = "."

import gi
gi.require_version('Vips', '8.0')
from gi.repository import Vips
Vips.cache_set_max_mem(204857600)

def print_mems():
    print("mem {}/{}".format(Vips.tracked_get_mem(), Vips.cache_get_max_mem()))
    print("files {}/{}".format(Vips.tracked_get_files(), Vips.cache_get_max_files()))
    print("ops {}/{}".format(Vips.cache_get_size(), Vips.cache_get_max()))

def load_img_magick(p):
    im = Vips.Image.magickload(p)
    im = im.resize(0.1)
    im.write_to_file("output.jpg")
    print_mems()
    time.sleep(1)

def load_img(p):
    im = Vips.Image.new_from_file(p)
    im = im.resize(0.1)
    im.write_to_file("output.jpg")
    print_mems()
    time.sleep(1)

if __name__ == "__main__":
    for x in range(0, 5):
        load_img_magick("test-data/6308.CR2".format(x))
    print("loading non-magick...")
    for x in range(0, 5):
        load_img("test-data/test.tiff".format(x))
