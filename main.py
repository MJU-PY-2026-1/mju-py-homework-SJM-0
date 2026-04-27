# 파일이름 : 나의 카페 스마트 포스기
# 작 성 자 : 신지민
# 2차 과제 
print('=== 나의 카페 스마트 포스 시스템 ===')
# 조건 : 자료형 3개 이상(str, int, float), 변수 5개 이상 사용
nickname = input('손님 닉네임을 입력하세요: ') # 변수 1(str)
order_count = int(input(f'어서오세요, {nickname}님! 몇 잔의 음료를 주문하시겠습니까?: ')) # 변수2 (int)

total_price = 0 #변수3 (int)
order_list = [] # 조건: 빈 리스트 선언

# 조건: for문과 range() 사용
for i in range(order_count):
    # 조건: 기능 5개 이상 (메뉴 5개 선택지)
    print('1. 아메리카노(4000원) 2. 카페라떼(4500원) 3. 딸기스무디(5000원) 4. 초코라떼(5500원) 5. 녹차(4000원)')
    menu_choice = int(input(f'{i+1}번째 메뉴 번호를 선택하세요 (1~5): '))

    #조건: 연속 if문(if~elif~else) 사용
    if menu_choice == 1:
        menu_name = '아메리카노'
        price = 4000
    elif menu_choice == 2:
        menu_name = '카페라떼'
        price = 4500
    elif menu_choice == 3:
        menu_name = '딸기스무디'
        price = 5000
    elif menu_choice == 4:
        menu_name = '초코라떼'
        price = 5500
    elif menu_choice == 5:
        menu_name = '녹차'
        price = 4000
    else:
        print('잘못된 번호입니다. 기본 메뉴(아메리카노)로 주문됩니다.')
        menu_name = '아메리카노'
        price = 4000

    order_list.append(menu_name) #조건: append()를 사용하여 리스트에 추가
    total_price += price #조건: 복합 대입 연산자(+=) 사용

print(f'주문하신 메뉴 확인: {order_list}')

#조건: 독립적인 if문 및 중첩 if문 사용
order_type = int(input('포장하시겠습니까? (1.포장 / 2.매장): '))
discount_rate = 0.0 #변수4 (float)

if order_type == 2:
    print('매장 이용 시 맴버십 할인이 가능합니다.')
    membership = int(input('맴버십 회원이신가요? (1.예 / 2.아니오): '))
    if membership == 1: #중첩 if문
        print('단골 손님! 10% 할인이 적용됩니다.')
        discount_rate = 0.1
else:
    print('포장 고객님은 할인이 적용되지 않습니다.')

#조건: 일반 사칙연산자 사용(*,-)ㄴㄴㄴㄴㄴㄴ
final_price = total_price * (1 - discount_rate) #변수5 (float)

print('='*30)
print(f'     [주문영수증]     ')
print(f' 손님: {nickname}')
print(f' 총 주문 수량: {order_count}잔')
print(f' 최종 결제 금액: {int(final_price)}원')
print('='*30)
print('이용해 주셔서 감사합니다!')