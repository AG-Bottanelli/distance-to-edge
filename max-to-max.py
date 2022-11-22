import numpy as np 
import pandas as pd

A = pd.read_excel (r'C:/Users/Luis/Nextcloud/Wong et al., 2021/ARF Paper 2021/Quantification/ARF1-Halo Shift Control.xlsx')
#INTRODUCE THE CSV WITH THE LINE PROFILE INFORMATION HERE IN THE GREEN PART 
#THE ORDER OF COLUMNS SHOULD BE DISTANCE CHANNEL1-INTENSITY CHANNEL 1- D ch2 - i CH2 - D CH1 NEXT IMAGES... 
# lineprofiles = np.genfromtxt('Line Porfiles Side View ARF1+COPI.csv', delimiter = ',',  invalid_raise = False)  

'''
	Odd columns - intensity values 
    - I Ch1 (ARF): 4n+1 starting in 0 
    - I ch2 (marker): 4n-1 starting at 1 
  Even columns - distances 
'''

def distance_max_to_max(df): 
    lineprofiles = np.array(df)
    lineprofiles = lineprofiles[2:,:]
    n = int(np.shape(lineprofiles)[1])
    numberprofiles = int(np.shape(lineprofiles)[1]/4)
    D=np.array(np.zeros(numberprofiles))
    #loop that extracts the distance and intensity values
    for i in range(0, n, 4): 
        j = int(abs(i/4)) 
        ch1 = lineprofiles[:, i+1] 
        ch2 = lineprofiles[:,i+3]
        np.nan_to_num(ch2, 0)
        centerch1 = np.argmax(ch1)
        centerch2 = np.argmax(ch2)
        D[j] = (centerch2 - centerch1)*30
    return(D)



Dmax = distance_max_to_max(A)
print('distance between maxs', Dmax)