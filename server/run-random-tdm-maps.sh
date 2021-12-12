#!/bin/sh -x

python3 random-maplist.py maplist-tdm.json > baseq3/maprotation-tdm.cfg
cp baseq3/maprotation-tdm.cfg ~/.q3a/baseq3/
/usr/lib/ioquake3/ioq3ded +exec tdm.cfg
