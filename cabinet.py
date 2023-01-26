cabinet = {1: "유재석", 3: "박명수", 5: "김종국"}

user_choice = int(input("락커번호를 선택해주세요 1~5: "))
empty_cabinet = user_choice in cabinet

while True:
    if empty_cabinet == False:
        print("사용 가능한 락커입니다.")
        customer = input("이름을 입력해주세요: ")
        cabinet[user_choice] = customer
        print(f"등록이 완료되었습니다. {customer}님")
        break
    else:
        print("이미 사용중인 락커입니다. 다시 선택해 주세요")
        user_choice = int(input("락커번호를 선택해주세요 1~5: "))
        empty_cabinet = user_choice in cabinet
        continue
