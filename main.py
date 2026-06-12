# 파일이름 : 나의 카페 스마트 포스기
# 작 성 자 : 신지민
# 2차 + 3차 + 4 과제 
daily_total_revenue = 0.0 
daily_order_records = []

try :
    with open('daily_report.csv', 'r', encoding = 'utf-8') as f:
        print('\n 이전 영입 기록 파일을 성공적으로 인식했습니다.')
except FileNotFoundError:
    print('\n 기존 영업 기록이 없습니다. 새로운 영업을 시작합니다.')

def display_main_menu():
    print('=== 나의 카페 스마트 포스 시스템 ===')
    print('1. 새 주문 받기')
    print('2. 오늘의 마감 보고서 조회')
    print('0. 시스템 종료')
    print('\n' + '='*30)

    try :
        choice = int(input('원하시는 작업 번호를 선택하시오: '))
        return choice
    except ValueError :
        print('\n 문자가 아닌 숫자로만 입력해주세요!')
        return -1


def process_order(customer_name):
    global daily_total_revenue
    global daily_order_records

    
    print(f'\n--- {customer_name} 님의 주문을 시작합니다 ---')

    order_items = []
    order_prices = []

    try :
        discount_rate = float(input('손님의 맴버십 특별 할인율을 입력하세요 (실수형 입력, 예: 0.10): '))
    except ValueError :
        print('올바른 실수가 아닙니다. 할인율이 0.0으로 자동 적용됩니다.')
        discount_rate = 0.0

    for i in range(5):
        print(f'[{i+1}/5 번째 메뉴 선택]')
        try :
            menu_choice = int(input('메뉴 번호 선택 (1. 아메리카노:4000원 2. 카페라떼:4500원 3. 딸기스무디:5000원 4. 초코라떼:5500원 5. 녹차:4000원 0.선택취소):'))
        except ValueError :
            print('[오류] 숫자로만 입력해주세요. 이번 선택을 취소하고 다음 선택으로 스킵합니다.')
            continue

        if menu_choice == 0:
            print('이번 선택을 취소하고 다음 선택으로 스킵합니다.')
            continue 

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
            print('잘못된 번호입니다. 다시 선택해 주세요.')
            continue 

        order_items.append(menu_name)
        order_prices.append(price)
        print(f'장바구니에 [{menu_name}]({price}원) 추가 완료!')

    if len(order_items)== 0:
        print('담긴 메뉴가 없어 주문이 자동 취소됩니다.')
        return
    
    total_before_discount = sum(order_prices)
    expensive_price = max(order_prices)
    total_count = len(order_items)
    order_items.sort()

    final_discount = 0.0

    if total_before_discount >= 10000 and discount_rate >= 0.05:
        if total_before_discount >= 13000:
            print('13,000원 이상 고액 주문으로 5% 추가 특별 할인 자동 적용!')
            final_discount = total_before_discount * (discount_rate + 0.05)
        else:
            final_discount = total_before_discount * discount_rate
    elif total_before_discount >= 5000 or discount_rate > 0.0:
        final_discount = total_before_discount * discount_rate
    else:
        final_discount = 0.0

    final_price = total_before_discount - final_discount

    daily_total_revenue += final_price
    
    single_order_record = [customer_name, total_count, int(final_price)]

    daily_order_records.append(single_order_record)

    print('=======영수증=======')
    print(f'주문 고객명 : {customer_name}님')
    print(f'정렬된 메뉴 : {order_items}')
    print(f'총 주문 수량: {total_count}개 최고가 메뉴: {expensive_price}원')
    print(f'할인 전 금액: {total_before_discount}원')
    print(f'차감 할인액 : {int(final_discount)}원')
    print(f'최종 결제액 : {int(final_price)}원')
    print('='*30)

def show_daily_report():
    print('=======오늘의 마감 보고서=======')
    print(f'오늘 하루 최종 총 매출: {int(daily_total_revenue)}원')
    print('='*30)
    print('[상세 주문 내역 표]')

    if len(daily_order_records) == 0:
        print('오늘 판매된 내역이 없습니다.')
    else:
        for record in daily_order_records:
            print(f'고객명 : {record[0]:<5} | 수량 : {record[1]}개 | 결제금액 : {record[2]:<5}원')
    print('='*30)

def save_report_to_file():
    try :
        with open('daily_report.csv', 'w', encoding='utf-8') as file:
            file.write('고객명,총수량,결재금액,메뉴내역\n')
            for record in daily_order_records:
                file.write(f'{record[0]},{record[1]},{record[2]},{record[3]}\n')
        print("\n오늘의 마감 보고서가 'daily_report.csv' 파일로 안전하게 저장되었습니다.")
    except Exception as e:
        print(f'파일 저장 중 문제가 발생했습니다: {e}')

while True:
    menu_num = display_main_menu()

    if menu_num == 1:
        name = input('주문 손님의 닉네임을 입력하세요: ')
        process_order(name)

    elif menu_num == 2:
        show_daily_report()

    elif menu_num == 0:
        print('카페 스마트 포스가 종료됩니다.')
        save_report_to_file()
        break

    elif menu_num == -1:
        continue

    else:
        print('[오류] 잘못된 번호입니다. 0, 1, 2번 중에서 다시 입력해주세요.')