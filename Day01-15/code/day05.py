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
""" num = int(input('输出个数:'))
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
        break """

"""
百钱百鸡问题
说明：源于《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

解：设公鸡x只，母鸡y只，小鸡（100-x-y）只，故问题可简化为求满足5x+3y+(100-x-y)/3=100，（x,y全为整数）的方程的解
"""

""" 
for x in range(0,101):
        for y in range(0,101):
                if 5*x+3*y+(100-x-y)/3==100:
                        print('公鸡%d只，母鸡%d只，小鸡%d只'%(x,y,100-x-y),end='\n') 
"""

"""
生成斐波那契数列

"""

"""
counter = int(input('请输入数列项数：'))

variable_a = 1;
variable_b = 0;

for i in range(0,counter):
        if(i%2==0):
                variable_a+=variable_b
                print(variable_a,end="\t")
        else:
                variable_b+=variable_a
                print(variable_b,end="\t")
"""

"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

"""

from random import randint
money = 1000
count = 1

while True:
        if money<=0:
                print('游戏结束，庄家胜!')
                break
        elif money>=2000:
                print('游戏结束，玩家胜!')
                break
        else:
                print('第%d回合，玩家总资产为%d' % (count, money))
                current = randint(1, 6) + randint(1, 6)
                if count == 1:
                        first = current     # 存储第一次掷骰子结果
                        if first == 7 or first == 11:
                                money += 1000
                                print('你摇出的点数为%d，玩家胜：你的总资产+1000' % current)
                        elif first == 2 or first == 3 or first == 12:
                                money -= 1000
                                print('你摇出的点数为%d，庄家胜，你的总资产-1000' % current)
                        else:
                                print('你摇出的点数为%d，平局，游戏继续...' % current)
                else:
                        bet = int(input('请下注:'))
                        if current == 7:
                                print('你摇出的点数为%d，庄家胜，你的总资产-%d' % (current, bet))
                                money -= bet
                        elif current == first:
                                money += bet
                                print('你摇出的点数为%d，玩家胜，你的总资产+%d' % (current, bet))
                        else:
                                print('你摇出的点数为%d，平局，游戏继续...'% current)
                count+=1
                print('**************************************')