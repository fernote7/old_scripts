__author__ = 'fernando.ormonde'


import numpy as np


# criterios

c11 = 1
c12 = 1./7
c13 = 1./3
c14 = 1./2
c22 = 1
c23 = 5
c24 = 5
c33 = 1
c34 = 3
c44 = 1

# preferencias


e11 = 1
e12 = 6
e21 = 8
e22 = 1
e31 = 1
e32 = 5
e41 = 4
e42 = 1



c21 = (c12)**(-1)
c31 = (c13)**(-1)
c32 = (c23)**(-1)
c41 = (c14)**(-1)
c42 = (c24)**(-1)
c43 = (c34)**(-1)


mat_crit = np.array([[c11,c12,c13,c14], [c21,c22,c23,c24], [c31,c32,c33,c34], [c41,c42,c43,c44]])

mc0 = mat_crit[:,0]
mc1 = mat_crit[:,1]
mc2 = mat_crit[:,2]
mc3 = mat_crit[:,3]

lista = [sum(mc0), sum(mc1), sum(mc2), sum(mc3)]


a = mc0/lista[0]


b = mc1/lista[1]


c = mc2/lista[2]


d = mc3/lista[3]


mat_crit2 = np.array([[a], [b], [c], [d]])

mat_crit3 = mat_crit2.T




m1 = sum(mat_crit3[0]/len(mat_crit3))
m11 = sum(m1)
m2 = sum(mat_crit3[1]/len(mat_crit3))
m21 = sum(m2)
m3 = sum(mat_crit3[2]/len(mat_crit3))
m31 = sum(m3)
m4 = sum(mat_crit3[3]/len(mat_crit3))
m41 = sum(m4)

mx1 = [m11, m21, m31, m41]




# parte de preferencias

#pref1 = w1/wi
#pref2 = w2/wi
#pref3 = w3/wi
#pref4 = w4/wi


pref1 = np.array([[float(e11)/e11,float(e11)/e12], [float(e12)/e11, float(e12)/e12]])
pref11 = np.array([[pref1[0, 0]/(pref1[0, 0] + pref1[1, 0]), pref1[0, 0]/(pref1[0, 0] + pref1[1, 0]) ], [pref1[1, 0]/(pref1[0, 0] + pref1[1, 0]), pref1[1, 0]/(pref1[0, 0] + pref1[1, 0])]])

print 0.14285714+0.85714286

print pref11
print pref1

pref2 = np.array([[float(e21)/e21,float(e21)/e22], [float(e22)/e21, float(e22)/e22]])

print pref2
pref3 = np.array([[float(e31)/e31,float(e31)/e32], [float(e32)/e31, float(e32)/e32]])
pref4 = np.array([[float(e41)/e41,float(e41)/e42], [float(e42)/e41, float(e42)/e42]])

print pref3
print pref4