#! /usr/bin/env python3

import os
import sys
import shutil


def guess_file_extension(file):
    """
    Guess the extension of a file using libmagic

    Args:
        file (str): file path

    Returns:
        ext (str): guessed file extension (with leading ".")
    """
    import mimetypes
    try:
        import magic
    except ImportError:
        print('Missing python library "magic". '
              'Install with "python -m pip install python-magic".',
              file=sys.stderr)
        raise

    m = magic.from_file(file, mime=True)
    ext = mimetypes.guess_extension(m)

    # mimetypes.guess_extensions often fails (at least with archives) so here
    # are some guess from personal tests (not reliable but better than nothing).
    ext = '.zip' if (not ext and m == 'application/zip') else ext
    ext = '.tar.gz' if (not ext and m == 'application/gzip') else ext
    ext = '.tar.gz' if ext == '.gz' else ext  # might cause errors for true gz?

    if not ext:
        raise RuntimeError(f'Could not guess the extension of file {file}')

    return ext


def get_from_archive(archive,
                     archive_original_name=None,
                     accepted_formats=['.tif', '.tiff'],
                     extract_dir='unpacked',
                     rename=False):
    """
    Get files from archive

    Args:
        archive: (str) archive path. Archives without extensions are handled.
        archive_original_name: (str) original archive path, with the correct
        extension. If provided, this file's extension will be used if the input
        archive has no extension (or if it's a fake extension). Default is None
        accepted_formats: (list/tuple of str) list of accepted formats. It is
                better (but not mandatory) to include the leading dot.
                Comparison is case insensitive, so only the lowercase (or
                uppercase) version is needed. Default is ['.tif', '.tiff'].
        unpacked: (str) directory in which the archive is extracted.
                Default is 'unpacked'.
        rename: (bool) rename files with tricky names, e.g. with spaces or
                parenthesis. Default is False.

    Returns:
        list of paths of the files found
    """
    assert os.path.exists(archive), f'The file {archive} does not exist.'

    ext = os.path.splitext(archive)[1]  # empty string if no extension

    if ext == '.whatever' or ext == '.data': ext = None  # ipol's fake ext

    if not ext:  # the archive has no extension
        if archive_original_name is not None:
            ext = os.path.splitext(archive_original_name)[1]
        if not ext:  # if still not ext even after looking at original name
            ext = guess_file_extension(archive)
        shutil.copyfile(archive, 'tmp' + ext)
        archive = 'tmp' + ext

    shutil.unpack_archive(archive, extract_dir=extract_dir)

    accepted_formats = tuple(x.lower() for x in accepted_formats)

    files = [os.path.join(root, f)
             for root, dirs, files in os.walk(extract_dir)
             for f in files if f.lower().endswith(accepted_formats)]

    # remove hidden files (start by a dot)
    files = [f for f in files if not os.path.basename(f).startswith('.')]

    # sort them, so that the user can give files in a specific order
    files.sort()

    if rename:
        for n, i in enumerate(files):
            j = i.replace(' ', '_')  # replace spaces
            j = j.replace('(', '').replace(')', '')  # remove parentheses
            if j != i:  # filename has been modified
                while os.path.exists(j):
                    j_path, j_ext = os.path.splitext(j)
                    j = j_path + '_again' + j_ext
                os.rename(i, j)
                files[n] = j  # replace i by j in the list

    return files


def cli():
    """Command line interface"""
    import argparse

    note = 'The archive can be in one of the following archive formats: '
    for s, t in shutil.get_archive_formats(): note += s + ' (' + t + '), '
    note = note[:-2] + '.'

    p = argparse.ArgumentParser(description='Unarchive for IPOL demos. ' + note)
    p.add_argument('archive',
                   help="path to the archive")
    p.add_argument('--archive-orig',
                   help='original archive name, used to get correct extension',
                   type=str, default=None)
    p.add_argument('--rename',
                   action='store_true', default=False,
                   help="rename files with spaces etc.")
    p.add_argument('--extract-dir',
                   help="directory in which to extract the archive")

    a = p.parse_args()

    accepted_formats = ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.tif',
                        '.tiff', '.asc', '.pgm']

    files = get_from_archive(archive=a.archive,
                             archive_original_name=a.archive_orig,
                             accepted_formats=accepted_formats,
                             rename=a.rename)

    print('\n'.join(files))


if __name__ == '__main__':
    cli()
