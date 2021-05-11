#Quiz 6

def std_weight(height, gender) :
    if gender == 'male' :
        height_m = height * 0.01
        std_weight = round((height_m * height_m * 22),2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height,std_weight))
    else :
        height_m = height * 0.01
        std_weight = round((height_m * height_m * 21),2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height,std_weight))
    return height , std_weight

std_weight(175,'male')

