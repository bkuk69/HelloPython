num = int(input("점수를 입력하세요"))

if num >100 or num < 0:
    print("성적을 잘못 입력하였습니다.")
elif num >= 90:
    print("A학점입니다.")
    print("축하합니다.")
elif num >= 80 :
    print("학점입니다.")
    print("축하합니다.")
elif num >= 70 :
    print("C학점입니다.")
elif num >= 60:
    print("D학점입니다.")
else :
    print("F학점입니다.")
print("꿈의학교")
