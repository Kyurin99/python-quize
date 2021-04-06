#Quiz

site = "http://naver.com"
s_1 = site[7:]              #규칙1
s_1 = s_1[0:5]              #규칙2
# print(s_1)

password = s_1[0:3] + str(len(s_1)) + str(s_1.count("e")) + "!"

print("{}의 비밀번호는 {}입니다".format(site, password))



