import random

quiz_list = {
    '불닭볶음면이 땡길 때가 많다 (A) / 절대 못 먹는다 (B)':'매운맛', '디저트',
    ('고기 없이 식사는 상상할 수 없다 (A) / 채식도 괜찮다 (B)', '고기', '채소')
}

result = {'매운맛' : 0, '고기' : 0, '채소' : 0, '디저트' : 0}

random_quiz = random.choice(quiz_list) 

def questions(question, type1, type2):
    while True:
        print(questions)
        answer = input(f'A 또는 B를 선택하세요: {random_quiz}').upper()
        if answer == 'A':
            return type1
        elif answer == 'B':
            return type2
        else:
            print('잘못된 입력입니다. 다시 입력해주세요')

    def food_test():
        print('음식 취향 테스트를 시작합니다')
        print('각 질문에 A 또는 B로 답변해주세요')

        for q, a, b in quiz_list:
            result[questions(q, a, b)] =+ 1

        final_type = max(result, key=result.get)

    print('테스트 완료!')
    print(f'당신의 음식 취향은: {final_type} 입니다')