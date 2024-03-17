import random
def main():
    even = []
    odd = []
    #to generate random int number must import and also use the random.randint(num, num)
    for i in range (0,100):
        num = random.randint(0, 100)
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print('The count of Even numbers: ', len(even))
    print('The count of Odd numbers: ', len(odd))
main()