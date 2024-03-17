#Write a Python program to find the index of an element in a list.
#lst = ['A','P','B','Q','C','D']
""" def main():
    lst = ['A','P','B','Q','C','D']
    for i in range(0,len(lst)):
        print(f"The index of {lst[i]} is {i}")
main() """

# second way
def main():
    lst = ['A','P','B','Q','C','D']
    for i in range(0,len(lst)):
        print(f"The index of {lst[i]} is {lst.index(lst[i])}")
main()