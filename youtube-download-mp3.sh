#!/usr/bin/env bash
set -e

child_script=$(dirname $(realpath $0))/youtube_download_mp3.py
echo "child_script=$child_script"

export XDG_CONFIG_HOME="$HOME/.config"
export config_dir="$XDG_CONFIG_HOME/yt-dlp/mp3.d"
echo "config_dir=$config_dir"

$child_script
nemo "$HOME/Videos" &
