#!/usr/bin/python
import sys
import os
import subprocess

MAX_TRIES = 100

if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv
    tries = 1

    if argc < 2:
        print "usage: getv.py <video-url> [<playlist-idx>]"
        sys.exit(1)

    video_url = argv[1]
    if argc == 3:
        is_playlist = True
        last_pl_index = int(argv[2])
    else:
        is_playlist = None
        last_pl_index = 1

    while True:
        if is_playlist:
            print "RESUMING AT %d" % last_pl_index
            command = ['youtube-dl', 
                        '%s --playlist-start %s' % (video_url, str(last_pl_index))]
        else:
            command = ['youtube-dl', video_url]

        p = subprocess.Popen(command, 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
        text = p.stdout.read()
        print text

        retcode = p.wait()
        if is_playlist is None:
            is_playlist = text.find('[download] Downloading playlist:') > -1

        tries += 1

        # An error ocurred, lets try again
        if retcode > 0 and tries < MAX_TRIES:
            if is_playlist:
                # the last time we downloaded a video
                idx = text.rfind('[download] Downloading video')
                if idx > -1: 
                    idx = idx + len('[download] Downloading video ')
                    print text[idx:-1]
                    end = text.rfind(' of ')
                    last_pl_index = int(text[idx:end])
                else:
                    last_pl_index += 1
        else:
            break



