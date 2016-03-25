import scipy.io.wavfile as scw
import numpy as np

num=0

while num>=1 and num<=2:
	num = raw_input("Please enter in the instrument number from the following menu: ")
	if num>2 or num<1 :
		print "Please Enter in a valid option"

path = raw_input("Please enter the correct path to the '.wav' file of your music track : ")

music_data = scw.read(path)

# First convert to many wavfiles of sample rates of the sound tracks