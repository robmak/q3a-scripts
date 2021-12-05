#!/bin/sh -x

python3 ./maplist-ctf.py

/usr/lib/ioquake3/ioq3ded +exec ctf.cfg
