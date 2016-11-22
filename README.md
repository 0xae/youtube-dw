youtube-dw
======

a youtube (playlist specialized) resumer.

it depends on `youtube-dl` so install it first at [https://rg3.github.io/youtube-dl/](https://rg3.github.io/youtube-dl/)

# USAGE
    ./youtube-dw video [playlist-index]
youtube-dw will resume the last video of the playlist (if the url provided is a playlist)
and will keep trying for 100 times

# MOTIVATION

i used it to download a playlist containing +100 videos of anime music.
youtube-dl would fail and restart the whole thing from the start (skipping the already downloaded videos of course)
which would make the process a whole lot slower. so i wrote this and it resumes the download **exactly** where it was
thank you
