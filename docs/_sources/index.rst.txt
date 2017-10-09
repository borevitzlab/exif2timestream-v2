.. exif2timestream-v2 documentation master file

.. toctree::
   :name: mastertoc
   :titlesonly:
   :hidden:

   ansible
   py-modindex


exif2timestream-v2
==================

Credits/License
---------------

The goal of this project is to create a robust image processing and structuring.

This project is open source but please `contact us <https://github.com/borevitzlab>`_ before using the code so we can know who is using it and please make sure to link back here in any code you use. This project is in active development but we are happy to work with other groups to develop new features so drop us a line if you are interested.

This code was developed for the TraitCapture project at ANU.

Please cite: *Brown, Tim B., et al.* `TraitCapture : genomic and environment modelling of plant phenomic data. Current opinion in plant biology 18 (2014): 73-79 <http://www.sciencedirect.com/science/article/pii/S1369526614000181>`_. when using the code.


Instructions
------------
Run from command line with specific arguments/batch mode from yaml file


Command line help:

`./cli.py --help`

batch mode:

`./batch.py example.yml`




Options
-------

:depth:
   how many levels under the source directory to scan for images

:rotation:
   90 degree increment to rotate the source images, removes the orientation exif tag.

:pyramid:
   whether to also create tiled pyramidal tiffs for each image.

:resolutions:
   the output resolutions to write

:output_image_type:
   the output image types to write


Archive Modes
-------------

:copy:
   leave source images in their original location

:move:
   remove source images after processing

:archive:
   create a new tarball of the source images for this time range
      overwrites any previous archives
      leaves the source images in their original location

:archive-rm:
   updates a tarball (creates if it doesn't exist) with the source images
      removes the source images after processing


Env Vars
--------

:FORCE_PIL:
   options: "true", unset
   forces exif2timestream-v2 to use PIL instead of libvips, can be helpful if debugging etc.

:NO_RAWKIT:
   options: "true", unset
   forces exif2timestream-v2 to not use rawkit to convert images first to tiffs temporarily.
   using rawkit allows skipping of vips magickload (which isnt very good)



Requirements
------------

These requirements are specified and provide installation methods within the ansible playbook.

*os:*
 * exiv2
 * exifread
 * libvips with python bindings (see :doc:`ansible` )

*python/aur/extra*
 * piexif
 * pillow `[pip] <https://pypi.python.org/pypi/Pillow/3.1.1>`__