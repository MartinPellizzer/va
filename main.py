from datetime import datetime
from pygame import mixer
import time

import gtts  
from playsound import playsound  
import os
  
# t1 = gtts.gTTS("Tweet 10 Times")
# t1.save("welcome.mp3")
# playsound("welcome.mp3")  

mixer.init()

def twitter():
	mixer.music.load('codec.mp3')
	mixer.music.set_volume(1)
	mixer.music.play()
	time.sleep(2)
	mixer.music.stop()
	mixer.music.load('codec.mp3')
	mixer.music.set_volume(1)
	mixer.music.play()
	time.sleep(2)
	mixer.music.stop()
	mixer.music.load('codec-open.wav')
	mixer.music.set_volume(1)
	mixer.music.play()
	time.sleep(1)
	mixer.music.set_volume(1)
	mixer.music.load('tts/twitter-tasks.wav')
	mixer.music.play()
	while mixer.music.get_busy():
		time.sleep(1)
	mixer.music.load('codec-close.wav')
	mixer.music.set_volume(1)
	mixer.music.play()
	time.sleep(1)


def training():
	mixer.music.set_volume(1)
	mixer.music.load('battle.mp3')
	mixer.music.play()
	time.sleep(60)
	mixer.music.set_volume(1)
	mixer.music.load('victory.mp3')
	mixer.music.play()

def alert():
	mixer.music.set_volume(1)
	mixer.music.load('alert.mp3')
	mixer.music.play()
	time.sleep(1)
	mixer.music.stop()
	mixer.music.load('duel.mp3')
	mixer.music.set_volume(0.2)
	mixer.music.play()
	time.sleep(1500)
	mixer.music.stop()
	mixer.music.load('complete.mp3')
	mixer.music.play()
	while mixer.music.get_busy():
		time.sleep(1)


times = [
	[14, 2, 0],
	[14, 30, 0],
	[17, 00, 0],
	[17, 30, 0],
]

while True:
	now = datetime.now()
	hour = now.hour
	minute = now.minute
	second = now.second

	if (hour == 13 or hour == 14 or hour == 15 or hour == 16 or hour == 17) and minute == 56:
		training()

	if (hour == 8 or hour == 11) and (minute == 30 or minute == 0):
		alert()

	if (hour == 14 or hour == 17) and (minute == 30 or minute == 0):
		twitter()
		alert()

	continue

	for t in times:
		# if hour == t[0] and minute == t[1] and second == t[2]:
		# 	# if (hour == 17 and minute == 25) or (hour == 16 and minute == 55):
		# 	mixer.music.load('codec.mp3')
		# 	mixer.music.set_volume(1)
		# 	mixer.music.play()
		# 	while mixer.music.get_busy():
		# 		time.sleep(1)
		# 	time.sleep(60)

		# if hour == t[0] and minute == t[1] and second == t[2]:
		# elif (hour == 17 and minute == 30) or (hour == 17 and minute == 00):
		if minute == 0 or minute == 30: 
			twitter()
			alert()

			


	time.sleep(1)
