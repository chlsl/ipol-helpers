#!/usr/bin/env python3

import os

import iio
import numpy as np


def tonemap(images, outdir='.', append='', outext='.png', pctbot=.5, pcttop=.5):
    """
    Apply a basic tone-mapping and save the images in the specified format.

    Args:
        images: (list of str) list of images (paths) to tonemap.
        outdir: (str) output directory. Default is '.'.
        append: (str) text appended to the tone-mapped images.
                Default is nothing.
        outext: (str) the extension to use for the output images (including the
                leading dot). Default is '.png'.
        pctbot: (float) percentage of clipping on the bottom of the dynamic
                range. Default is .5.
        pcttop: (float) percentage of slipping on the top of the dynamic range.
                Default is .5.

    Returns:
        (list of str) list of names of the output images.
    """

    out = [os.path.join(outdir, os.path.splitext(os.path.basename(i))[0]
           + append + outext) for i in images]
    ims = [iio.read(i).astype(np.float) for i in images]
    lum = [np.mean(i, axis=2) for i in ims]
    pct = [(np.percentile(i, pctbot),
            np.percentile(i, 100 - pcttop)) for i in lum]
    ims = [np.clip(255*(i - p[0])/(p[1] - p[0]), 0, 255).astype(np.uint8)
           for p, i in zip(pct, ims)]

    for i, o in zip(ims, out):
        iio.write(o, i)

    return out


def cli():
    """
    Command line interface
    """

    import argparse

    p = argparse.ArgumentParser(description="Tonemap images")
    p.add_argument('images',
                   nargs='+',
                   help="list of images to tonemap, in any format recognised "
                   "by iio")
    p.add_argument('--outdir',
                   default='.',
                   help="output directory. Default is current.")
    p.add_argument('--append',
                   default='',
                   help="text appended to the tone-mapped images. "
                   "Default is nothing.")
    p.add_argument('--outext',
                   default='.png',
                   help="extension of the output images. Default is '.png'")
    p.add_argument('--pctbot',
                   type=float,
                   default=.5,
                   help="percentage of clipping on the bottom of the dynamic "
                   "range. Default is 0.5.")
    p.add_argument('--pcttop',
                   type=float,
                   default=.5,
                   help="percentage of clipping on the top of the dynamic "
                   "range. Default is 0.5.")
    a = p.parse_args()

    tonemap(a.images, a.outdir, a.append, a.outext, a.pctbot, a.pcttop)


if __name__ == '__main__':
    cli()
