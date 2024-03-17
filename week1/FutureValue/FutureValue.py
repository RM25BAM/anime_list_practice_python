def future_value(x, y, z):
    value = (x) * pow((1 + y), z)
    return value
def main():
    pValue = float(input('Enter the present value of account: '))
    interest = float(input('Enter the monthly interest of account: '))
    months = int(input('Enter the number of months: '))
    futureV = future_value(pValue, interest, months)
    print(f'Future value is ${futureV}')
main()