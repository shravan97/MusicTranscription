import scipy.io.wavfile as scw
import numpy as np

path = raw_input("Please enter the correct path to the '.wav' file of your music track : ")

music_data = scw.read(path)
''' Now , music_data[0] will give you the sample rate in samples/sec , 
 and , music_data[1] will give you the samples as a list . Now , to 
 read the samples of first 'n' seconds , music_data[1][0:44100*n]  ,and to 
 get the samples of 'n'th second , music_data[1][44100*(n-1) : 44100*n]
'''
''' Then , store the '.wav' files of each piano note (with accurate time) ,
 in the piano_notes folder and then convert each of those notes to raw data 
 similar to the input file (as shown above) . Then find the total time of 
 each sample and compare those samples within that time of the input sample 
 by find the cost . Then find the least cost among all . OR , instead of the
 cost method , use a logistic classifier for each time period and find out 
 the probabilities . Then find the maximum probability among the lot
'''