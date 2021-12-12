#!/bin/sh -x

python3 random-maplist.py maplist-ctf.json > baseq3/maprotation-ctf.cfg
cp baseq3/maprotation-ctf.cfg ~/.q3a/baseq3/
/usr/lib/ioquake3/ioq3ded +exec ctf.cfg
