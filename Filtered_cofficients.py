# Provide the path for the ITSG file for the variable 'file' in the code below:
# 'mat1' is the list containing raw cofficients read directly from ITSG file
# 'new_mat' is the full normal matrix read from ITSG file
# 'filtered_field' is the list of filtered cofficients
def upper2full(mat):
    other_half=[]
    new_mat=[]
    for i in range(len(mat)):
        for j in range(i):
            other_half.append(mat[j][i-j])
        new_mat.append(other_half+mat[i])
        other_half=[]
    return new_mat

file=open('/home/raghavsg/Downloads/grace/ITSG-Grace2018_n96_2002-04.snx', 'r')
flag1=''
flag2=''
for line in file:

    line=line.split()
    if line[0]=='+SOLUTION/ESTIMATE':

        print('Process started')
        flag1='+SOLUTION/ESTIMATE'
#        temp1=[]
        mat1=[]
    elif line[0]=='-SOLUTION/ESTIMATE':
        flag1='-SOLUTION/ESTIMATE'
        for m in mat1:
            print(m)
        print('Process ended')
    if flag1=='+SOLUTION/ESTIMATE' and line[0].isdigit():

        mat1.append(float(line[8]))
#        temp1=[]
    elif line[0]=='+SOLUTION/NORMAL_EQUATION_MATRIX':
        print('\n\nProcess started')
        flag2='+SOLUTION/NORMAL_EQUATION_MATRIX'
        temp2=[]
        mat2=[]
        first=1
    elif line[0]=='-SOLUTION/NORMAL_EQUATION_MATRIX':
        flag2='-SOLUTION/NORMAL_EQUATION_MATRIX'
        mat2.append(temp2)
        final_mat2=upper2full(mat2)
        print('mat2=',len(final_mat2), 'x', len(final_mat2[1]))

#        for m in final_mat2:
#            print(m)
        print('Process ended')
    if flag2=='+SOLUTION/NORMAL_EQUATION_MATRIX' and line[0].isdigit():
        if int(line[0])==first+1:
            first+=1
            mat2.append(temp2)
            temp2=[]
        try:
            temp2.append(float(line[2]))
            temp2.append(float(line[3]))
            temp2.append(float(line[4]))
        except IndexError:
            continue

file.close()

#import pandas as pd
import numpy as np
from numpy import array
import math
ser=mat1
i=0
sigma= []
for l in range(2, 96):
    for j in range(0,2*l +1):
        sum=0
        sum=sum + ser[i]*ser[i]
        i=i+1
    sigma.append(sum)
log_sigma = np.log(sigma)
# finding the minimum value of the set of squared sigmas
#mi= min(log_sigma)
#it = np.where(log_sigma==mi)
#log_ml=np.log(it[0][0])
# Assuming the minimum at 40th element after visualization
it=40
log_ml =np.log(40)
mi = log_sigma[40]

slope= (mi-log_sigma[0])/(log_ml - np.log(2))
intercpt= log_sigma[0]- slope*(np.log(2))
mat_S =np.zeros(shape=(9405,9405))
p=0
corrected_sigma_square_values=[]
for l in range(2,96):
    s= slope*(np.log(l)) + intercpt
    corrected_sigma_square_values.append(s)
    exp_s=np.exp(s)
    div_exp_s = exp_s/(2*l +1)
    inv_sigma = 1/div_exp_s
    for i in range(0, 2*l +1):
        mat_S[p,p]= inv_sigma
        p=p+1
# finding sigma squared values of the filtered coefficients
i=0
F_sigma= []
for l in range(2, 96):
    for j in range(0,2*l +1):
        sum=0
        sum=sum + filtered_field[i]*filtered_field[i]
        i=i+1
    F_sigma.append(sum)
F_log_sigma = np.log(F_sigma)
#print(F_log_sigma)
ser=np.squeeze(ser)
ser=ser.reshape(9405,1)
final_mat2 = np.matrix(final_mat2)
filtered_field = (np.linalg.inv(final_mat2 + mat_S))*(final_mat2)*ser
print(((np.linalg.inv(final_mat2 + mat_S))*final_mat2*ser).shape)
print(filtered_field)
