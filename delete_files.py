from path import Path


d = Path('./unknown_images')

files = d.walkfiles('*.gif')

for file in files :
	file.remove()


files2 = d.walkfiles('*.svg')

for file in files2 :
	file.remove()

print('deleted svg and gifs')