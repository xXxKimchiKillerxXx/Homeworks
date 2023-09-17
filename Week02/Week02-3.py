import re

pattern = re.compile("[a-zA-Z0-9+-_]+@[a-zA-Z0-9-]+[.][a-zA-Z0-9-.]+")

prev = input("텍스트를 입력하세요: ")

next = pattern.findall(prev)

if len(next) == 0:
    print("이메일 주소가 발견되지 않았습니다.")
else:
    for x in next:
        print("추출된 이메일 주소:\n")
        print(x)
