import pytube

url=input("enter link: ")
path=""

pytube.YouTube(url).streams.get_highest_resolution().download(path)



