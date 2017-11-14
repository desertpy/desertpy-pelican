DesertPy Conda Environment Update - `desertpy-2017-v1`
######################################################

:date: 2017-11-10 06:47
:tags: conda
:category: posts
:slug: conda-env-2017-v1
:author: Austin Godber
:summary: DesertPy Conda Environment Update - `desertpy-2017-v1`


For those who want to follow along with my upcoming `pyglet presentation <https://www.meetup.com/Phoenix-Python-Meetup-Group/events/244752711>`_
you can install my updated desertpy conda environment on macOS with the
following commands::

  conda env create godber/desertpy-2017-v1
  source activate desertpy-2017-v1

There may be additional updates to the environment, but I will increment the
version counter.

**Update**

Within 6 hours of my creating the `desertpy-2017-v1` conda environment the
pyglet library did its first release in over two years, go figure.  The new
version has improved Python 3 support.  You can read more in the
`Pyglet RELEASE_NOTES.txt <https://bitbucket.org/pyglet/pyglet/src/133d8703f0eb68571edd5613c079c417e417c628/RELEASE_NOTES?at=default&fileviewer=file-view-default>`_.

Of course this means that I had to create a new conda environment with the new
version.  So, here you go, `desertpy-2017-v2` contains `v1.3.0` of pyglet::

  conda env create godber/desertpy-2017-v2
  source activate desertpy-2017-v2
