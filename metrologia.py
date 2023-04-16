import math
di = [0.02,0.02,0.01,0.01,0.01,0.01,0.01]
i_d = [0.5,0.45,0.4,0.35,0.3,0.25,0.2]
for i in range (0,7):
    deltai = (di[i]/i_d[i]) * 100
    print (deltai)