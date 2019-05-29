def upper2full(mat):
    other_half=[]
    new_mat=[]
    for i in range(len(mat)):
        for j in range(i):
            other_half.append(mat[j][i-j])
        new_mat.append(other_half+mat[i])
        other_half=[]
    return new_mat

file=open('ITSG-Grace2018_n96_2002-04.snx', 'r')
flag1=''
flag2=''
for line in file:
    line=line.split()
    if line[0]=='+SOLUTION/ESTIMATE':
        print('Process started')
        flag1='+SOLUTION/ESTIMATE'
        temp1=[]
        mat1=[]
    elif line[0]=='-SOLUTION/ESTIMATE':
        flag1='-SOLUTION/ESTIMATE'
        for m in mat1:
            print(m)
        print('Process ended')
    if flag1=='+SOLUTION/ESTIMATE' and line[0].isdigit():
        temp1.append(line[1])
        temp1.append(int(line[2]))
        temp1.append(int(line[4]))
        temp1.append(float(line[8]))
        mat1.append(temp1)
        temp1=[]
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
        for m in final_mat2:
            print(m)
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
