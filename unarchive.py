#! /usr/bin/env python3

import os
import sys
import shutil


def get_from_archive(archive,
                     accepted_formats,
                     extract_dir='unpacked',
                     rename=False):
    """
    Get files from archive

    Args:
        archive: (str) archive path
        accepted_formats: (list of str) list of accepted formats
        unpacked: (str) directory in which archive is extracted

    Returns:
        list of paths of the files found
    """

    shutil.unpack_archive(archive, extract_dir=extract_dir)

    files = [os.path.join(root, f)
             for root, dirs, files in os.walk(extract_dir)
             for f in files if f.endswith(accepted_formats)]
    files.sort()

    if rename:
        for n, i in enumerate(files):
            j = i.replace(' ', '_')  # remove spaces
            j = j.replace('(', '').replace(')', '')  # remove parentheses
            if j != i:  # filename has been modified
                while os.path.exists(j):
                    j_path, j_ext = os.path.splitext(j)
                    j = j_path + '_again' + j_ext
                os.rename(i, j)
                files[n] = j  # replace i by j in the list

    return files


def cli():
    """
    Command line interface
    """

    import argparse

    note = 'The archive can be in one of the following archive formats: '
    for s, t in shutil.get_archive_formats(): note += s + ' (' + t + '), '
    note = note[:-2] + '.'

    p = argparse.ArgumentParser(description='Unarchive for IPOL demos. ' + note)
    p.add_argument('archive',
                   help="path to the archive")
    p.add_argument('--rename',
                   action='store_true', default=False,
                   help="rename files with spaces etc.")
    p.add_argument('--extract-dir',
                    help="directory in which to extract the archive")

    a = p.parse_args()

    accepted_formats = (
            '.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.tif', '.tiff',
            '.JPG', '.JPEG', '.PNG', '.PPM', '.BMP', '.TIF', '.TIFF')

    files = get_from_archive(archive=a.archive,
                             accepted_formats=accepted_formats,
                             rename=a.rename)

    print('\n'.join(files))


if __name__ == '__main__':
    cli()
