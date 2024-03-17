#prime number is evenly divisble by itself and 1
def is_prime(num):
    Ans = False
    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                Ans = True
                break
    if Ans == True:
        return True
    elif Ans == False:
        return False
def main():
    num = int(input('Enter a number: '))
    value = is_prime(num)
    if value == True:
        print('Number is not prime')
    else:
        print('Number is prime')
main()3