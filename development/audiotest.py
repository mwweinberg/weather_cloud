import simpleaudio as sa
import time

#wave_obj = sa.WaveObject("sounds/calm.wav", 2, 2, 44100)
wave_obj = sa.WaveObject.from_wave_file("sounds/calm.wav")
play_obj = wave_obj.play()

i = 0
while i < 2:
    i = i+1
    print("i is " + str(i))
    time.sleep(2)
#play_obj.wait_done()

play_obj = wave_obj.play()
i = 0
while i < 2:
    i = i+1
    print("i is " + str(i))
    time.sleep(2)
