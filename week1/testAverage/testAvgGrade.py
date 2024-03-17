def main():
    user1 = int(input('Enter first user test score: '))
    user2 = int(input(f'Enter second user test score: '))
    user3 = int(input(f'Enter third user test score: '))    
    user4 = int(input(f'Enter four user test score: '))
    user5 = int(input(f'Enter fifth user test score: '))
    print(calc_average(user1, user2, user3, user4, user5))
    determine_grade(user1)
    determine_grade(user2)
    determine_grade(user3)
    determine_grade(user4)
    determine_grade(user5)
def calc_average(num1, num2, num3, num4, num5):
    Avg = (num1 + num2 + num3 + num4 + num5) / 5
    return Avg
def determine_grade(score):
    if(score <= 100 and score >= 90):
        print('A')
    elif(score <= 89 and score >= 80):
        print('B')
    elif(score <= 79 and score >= 70):
        print('C')
    elif(score <= 69 and score >= 60):
        print('D')
    else:
        print('F')
main()