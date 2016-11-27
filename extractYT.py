import urllib.request
import re
import sys

iteration = 0
playlist = input("Enter Playlist URL: ")
response = urllib.request.urlopen(playlist)
play_data = response.read()


for i in re.findall(b"/watch\?v=[a-zA-Z0-9\-_]+", play_data):
    i = str(i)
    strip_chars = i[2:-1]

    new_url = "http://www.youtube.com" + str(strip_chars)
    print(new_url)
    iteration = iteration + 1


print()
print('%s videos found \n' % iteration)
