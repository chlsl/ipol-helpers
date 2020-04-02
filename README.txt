IPOL Helpers
============

Scripts to ease the creation of IPOL demos.

unarchive.py
------------

For demos that use an archive as input.

The unarchive script
- guesses the type of archive
- unpacks it
- finds and returns all files matching a given list of extensions.

tonemap.py
----------

For demos in which input or output images are not 8-bits/channel.

The tonemap script
- maps the dynamic of each input to [0, 255] by clipping 0.5% on each side
- saves it in the specified format (png by default).

