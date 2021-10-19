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

democli.py
----------

Upload a ddl file and demoextras archive to the demo system. Requires to be logged to the system from firefox.


Notes and documentation
=======================

Memos about the ipol demo system, and documentation for features and behaviors
missing in the official documentation.

- [official documentation](documentation/official_documentation.md)
  Useful links.

- [undocumented ddl](documentation/undocumented_ddl.md)
  Features not officially documented.

- [hidden features](documentation/hidden_features.md)
  Features not officially documented, available from the run.sh

- [demo-system-structure](documentation/demo-system-structure.md)
  (work in progress)
  Files hierarchy.
  If you're wondering were IPOL move your files in the "move" sections, or if
  your "run.sh" can't find the executable, you may want to have a better idea
  of how files are organized.

