import functools
import traceback
import os
from lib import image

tests = {}

def failt(fn, reason):
    i = 0
    p = str(fn.__name__) +"-"+ str(i)
    while p in tests.keys():
        i += 1
        p = str(fn.__name__) + "-" + str(i)
    tests[p] = traceback.format_exc()
    print('[FAIL] {}'.format(p))
    print('\t{}'.format(reason))

def passt(fn):
    i = 0
    p = str(fn.__name__) + "-" + str(i)
    while p in tests.keys():
        i += 1
        p = str(fn.__name__) + "-" + str(i)
    tests[p] = "PASS"
    print("[PASS] {}".format(p))

def test_output_file(method=None, output_file=None):
    if not callable(method):
        return functools.partial(test_output_file, output_file=output_file)
    method.gw_method = output_file or method.__name__
    def _decorate(funct):
        @functools.wraps(funct)
        def wrap(*args, **kwargs):
            try:
                os.remove(output_file)
            except:
                pass
            try:
                funct(*args, **kwargs)
                passt(funct)
            except:
                failt(funct, traceback.format_exc())
            finally:
                if output_file and not os.path.exists(output_file):
                    failt(funct, "OUTPUT")
        return wrap
    return _decorate(method)


testimagejpg = "test-data/test.jpg"
testimagecr2 = "test-data/test.CR2"

@test_output_file(output_file="test-output-resize.jpg")
def test_resize():
    image.resize(testimagejpg, "test-output-resize.jpg")

@test_output_file(output_file="test-output-resize.jpg")
def test_resize_vips():
    image._resize_vips(testimagejpg, "test-output-resize.jpg")

@test_output_file(output_file="test-output-resize.jpg")
def test_resize_pil():
    image._resize_pil(testimagejpg, "test-output-resize.jpg")

@test_output_file()
def test_rotate(angle):
    image.rotate_inplace("test-output-resize.jpg", angle)

@test_output_file()
def test_rotate_pil(angle):
    image._rotate_pil_inplace("test-output-resize.jpg", angle)

@test_output_file()
def test_rotate_vips(angle):
    image._rotate_vips_inplace("test-output-resize.jpg", angle)

@test_output_file(output_file="test-output-resize.tif")
def test_pyramid():
    image.pyramid(testimagejpg, "test-output-resize.tif")

if __name__ == "__main__":
    test_resize()
    test_resize_pil()
    test_resize_vips()

    test_rotate(0)
    test_rotate(90)
    test_rotate(270)

    test_rotate_vips(0)
    test_rotate_vips(90)
    test_rotate_vips(270)

    test_rotate_pil(0)
    test_rotate_pil(90)
    test_rotate_pil(270)

    test_pyramid()