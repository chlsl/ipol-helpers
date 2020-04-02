IPOL Helpers
============

Scripts to ease the creation of IPOL demos.

unarchive.py
------------

For demos that use an archive as input.

The unarchive script
- Guess the type of archive
- Unpack it
- finds and return all files matching a given list of extensions

tonemap.py
----------

For demos in which input or output images are not 8-bits/channel.

The tonemap script map the dynamic of each input to [0, 255] and save it in the
specified format (png by default).

