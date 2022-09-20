# TikTok Discordbot
Someone from your discord server always sending URLs of funny TikTok videos but you don't want to open that god-forsaken, privacy-violating piece of shit chinese-state website?
Well this bot is perfect for you!

It uses the YT-DLP fork of YT-DL to download TikTok videos in specified discord channels and send them.

# Installation
Execute:
```
pip install -r /path/to/requirements.txt
```
Run:
```
python main.py
```

# Config
A config.ini file is used to set configs:
- DISCORDBOT_TOKEN: Discord bot API token
- CHANNELS: Definded list of channels the bot monitors for TikTok links

# Usage
In the definded channels send a url of a TikTok video with the base url https://vm.tiktok.com/ or https://www.tiktok.com/
The bot then downloads the video and saves it to the output folder "videos", which should be located in the root directory of the project.
Currently the bot doesn't delete these downloaded videos.