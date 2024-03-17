#reate a list of characters. Write a program to reverse the order of the elements in the list without using built-in functions. Use indexing method.
#lst = ['A','P','B','Q','C','D']
# indexing method [::-1]
def main():
    lst = ['A','P','B','Q','C','D']
    reverse = lst[::-1]
    print(reverse)
main()