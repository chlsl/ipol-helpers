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



Notes and documentation
=======================

Memos about the ipol demo system, and documentation for features and behaviors
missing in the official documentation.

official_documentation.txt
--------------------------

Useful links.

undocumented_ddl.txt
--------------------

Features not officially documented.

hidden_features.txt
-------------------

Features not officially documented, available from the run.sh

demo-system-structure.txt
-------------------------

[work in progress]

Files hierarchy.
If you're wondering were IPOL move your files in the "move" sections, or if
your "run.sh" can't find the executable, you may want to have a better idea of
how files are organized.


