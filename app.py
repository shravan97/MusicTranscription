import scipy.io.wavfile as scw
import numpy as np


instrument = raw_input("Please enter in the instrument number from the following menu: ")
path = raw_input("Please enter the correct path to the '.wav' file of your music track : ")

music_data = scw.read(path)

# First convert to many wavfiles of sample rates of the sound tracks