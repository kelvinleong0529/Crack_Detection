import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,11,11,dtype = np.int32)
#fx = [2505.098,2497.757,2529.163,2484.689,2492.547,2496.164,2499.709,2503.132,2485.935,2525.209,2496.967]
#fy = [2555.370,2560.021,2577.089,2369.049,2526.047,2562.163,2561.960,2559.220,2566.05,2572.036,2565.863]
#u0 =[372.370,357.155,335.7,395.366,438.548,365.247,379.429,352.153,422.833,477.981,360.938]
#v0 =[259.340,268.049,250.547,274.019,248.155,270.466,257.144,253.234,276.528,259.847,256.027]
#k1 = [-0.522459,-0.654239,-0.649547,-0.499760,-0.335888,-0.487500,-0.458604,-0.584696,-0.403204,-0.295241,-0.590039]
#k2 = [7.096578,8.448437,9.171360,7.213383,4.267550,6.698646,6.553896,7.455679,7.012862,3.485919,7.966020]
e = [0.113,0.12,0.11,0.102,0.105,0.110,0.112,0.111,0.107,0.102,0.124]
plt.plot(x,e,color="red",label="mean error")
leg = plt.legend()
plt.title('Mean Error in Pixels VS Group')
plt.xlabel('Group')
plt.xticks(np.arange(1,len(x)+1,1))
plt.ylabel('Mean Error in Pixels')
plt.show()