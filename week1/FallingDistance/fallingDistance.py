def falling_distance(x):
    d = 0.5*(9.8)*(pow(x, 2))
    d = round(d, 2)
    return d
def main():
    for i in range(1,11):
        distance = falling_distance(i)
        print(f'The distance in {i} secs: ',distance)
main()


