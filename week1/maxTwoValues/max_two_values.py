def max(x,y):
    if(x < y):
        return y
    else:
        return x



def main():
    num1 = int(input('first num:'))
    num2 = int(input('second num:'))
    print('The maximum number of those two values: ', max(num1,num2)) 
main()