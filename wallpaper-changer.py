import os
import argparse

def set_wallpaper(file):
    os.system("sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db \"update data set value = '" + file + "'\" && killall Dock")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='wallpaper image file')
    args = parser.parse_args()
    set_wallpaper(args.wallpaper)

main()