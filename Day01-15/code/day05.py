"""
寻找水仙花数
说明：水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
"""
"""
print('100-999内的水仙花数有：')
for i in range(100,1000):
    a = i//100 
    b = (i-a*100)//10 
    c = i-a*100-b*10
    if a**3+b**3+c**3 == i:
        print(i,end='\t')
"""

"""
寻找“完美数”。
"""
num = int(input('输出个数:'))
i = 1                          # 从1开始向后遍历
counter=0                      # 已输出的完美数个数
while True:
    if counter < num:
        sum = 0                # 除自身外的公约数求和
        for j in range(1,i):
            if i%j == 0:
                sum+=j
        if sum == i:
            counter+=1
            print(i,end='\t')
        i+=1
    else:
        break