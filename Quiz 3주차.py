#Quiz 04

from random import *

id = range(1,21)
id = list(id)
shuffle(id)

win = sample(id,4)

print("-- 당첨자 발표 --\n")
print("치킨 당첨자 : " , win[0] )
print("커피 당첨자 : " , win[1:])
print("\n-- 축하합니다 --")

 #Quiz 05

from random import *

count = 0 

for i in range(1,51) :
    time = randrange(5,51)
    if time >= 5 and time <= 15:
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else :
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) 
print("총 탑승 승객 : {}".format(count))