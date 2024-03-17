def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0 :
            return False
    if prime:
      return num
           
        
        
def main():
    print(25%5)
    for i in range(1,100):
        value = is_prime(i)
        if value == 1 or value == False or value == 0:
            continue
        else:
             print(value)
main()