import numpy as np
import math  # for Q7

orig_data1 = np.load('datalist1.npy')
orig_data2 = np.load('datalist2.npy')

data1 = np.load('data1.npy')
data2 = np.load('data2.npy')

# Q1
print("Q1:")

data1_ = np.absolute(data1)
np.save('data1_.npy', data1_)

data2_ = np.absolute(data2)
np.save('data2_.npy', data2_)

# Q2
print("Q2:")
# print(data1)
# print(data1_)
# print(orig_data1)
# print(checkData1)

boolData1 = True
checkData1 = orig_data1 - data1_
for lhs in checkData1:
    if lhs != 0:
        print("diff")
        boolData1 = False
        break
if boolData1:
    print("same")

boolData2 = True
checkData2 = orig_data2 - data2_
for lhs in checkData2:
    if lhs != 0:
        print("diff")
        boolData2 = False
        break
if boolData2:
    print("same")

# Q3
print("Q3:")

dictData1_ = {}
for num1 in data1_:
    if str(num1) in dictData1_:
        dictData1_[str(num1)] = dictData1_[str(num1)] + 1
    else:
        dictData1_[str(num1)] = 1

strListData1_ = list(dictData1_.keys())
listData1_ = []
for str1 in strListData1_:
    listData1_.append(int(str1))
listData1_.sort()
print(listData1_)


dictData2_ = {}
for num2 in data2_:
    if str(num2) in dictData2_:
        dictData2_[str(num2)] = dictData2_[str(num2)] + 1
    else:
        dictData2_[str(num2)] = 1

strListData2_ = list(dictData2_.keys())
listData2_ = []
for str2 in strListData2_:
    listData2_.append(int(str2))
listData2_.sort()
print(listData2_)

# Q4
print("Q4:")

fqData1_ = []
for num in listData1_:
    print(num, ":", dictData1_[str(num)])
    fqData1_.append(dictData1_[str(num)])
fqData1_.sort()
# print(fqData1_)


fqData2_ = []
for num in listData2_:
    print(num, ":", dictData2_[str(num)])
    fqData2_.append(dictData2_[str(num)])
fqData2_.sort()
# print(fqData2_)

# Q5
print("Q5:")

for num, fq in dictData1_.items():
    if fq == fqData1_[0]:
        print(num)

for num, fq in dictData2_.items():
    if fq == fqData2_[-1]:
        print(num)

# Q6
print("Q6:")

print("Data1 max:", listData1_[-1], "min:", listData1_[0])
print("R(range) =", listData1_[-1] - listData1_[0])

print("Data2 max:", listData2_[-1], "min:", listData2_[0])
print("R(range) =", listData2_[-1] - listData2_[0])

# Q7
print("Q7:")
# ref : http://highscope.ch.ntu.edu.tw/wordpress/?p=65479

sumData1 = 0
fqSumData1 = 0
amData1 = 0   # Arithmetic mean
varData1 = 0  # Variance
sdData1 = 0   # Standard Deviation，SD

for num, fq in dictData1_.items():
    sumData1 += int(num) * fq
    fqSumData1 += fq
# print(sumData1, fqSumData1)
amData1 = sumData1 / fqSumData1
# print(amData1)
for num, fq in dictData1_.items():
    varData1 += pow((int(num) - amData1), 2) * fq
varData1 /= fqSumData1
# print(varData1)
sdData1 = math.sqrt(varData1)
# print(sdData1)

sumData2 = 0
fqSumData2 = 0
amData2 = 0   # Arithmetic mean
varData2 = 0  # Variance
sdData2 = 0   # Standard Deviation，SD

for num, fq in dictData2_.items():
    sumData2 += int(num) * fq
    fqSumData2 += fq
# print(sumData2, fqSumData2)
amData2 = sumData2 / fqSumData2
# print(amData2)
for num, fq in dictData2_.items():
    varData2 += pow((int(num) - amData2), 2) * fq
varData2 /= fqSumData2
# print(varData2)
sdData2 = math.sqrt(varData2)
# print(sdData2)

if(sdData1 > sdData2):
    print("Dispersion of data: data1 > data2")
else:
    print("Dispersion of data: data2 > data1")
