#Quiz 03

from random import *

id = range(1,21)
id = list(id)
shuffle(id)

win = sample(id,4)

print("-- 당첨자 발표 --\n")
print("치킨 당첨자 : " , win[0] )
print("커피 당첨자 : " , win[1:])
print("\n-- 축하합니다 --")