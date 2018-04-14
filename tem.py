import numpy as np

orig_data1 = np.load('datalist1.npy')
orig_data2 = np.load('datalist2.npy')

data1 = np.load('data1.npy')
data2 = np.load('data2.npy')

# Q1
data1_ = np.absolute(data1)
np.save('data1_.npy', data1_)

data2_ = np.absolute(data2)
np.save('data2_.npy', data2_)

# Q2
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

dictData1_ = {}
for num1 in data1_:
    if str(num1) in dictData1_:
        dictData1_[str(num1)] = dictData1_[str(num1)] + 1
    else:
        dictData1_[str(num1)] = 1

listData1_ = list(dictData1_.keys())
print(listData1_)


dictData2_ = {}
for num2 in data2_:
    if str(num2) in dictData2_:
        dictData2_[str(num2)] = dictData2_[str(num2)] + 1
    else:
        dictData2_[str(num2)] = 1

listData2_ = list(dictData2_.keys())
print(listData2_)
