#!/usr/bin/env bash

echo "Please type the video url:"
read url
#if [[ ! -n "$url" ]]
#	then
#		echo "You must type a video url"
#		exit 1
#fi
		
executable=/home/schlangenbrut/.local/bin/yt-dlp
export XDG_CONFIG_HOME="$HOME/.config"
export config_dir="$XDG_CONFIG_HOME/yt-dlp/mp3.d"
cmd="$executable --config-locations $config_dir -- $url"
echo $cmd
eval $cmd
nemo "$HOME/Videos" &
