


def my_method():
    print("hello i am in my_method")
    input_str = 'cmhuemmbbauir#'
    # Type your code here
    message1 = input_str[::2]
    message2 = input_str[1::2]
    print(message1.lstrip('#').rstrip('#') + ',' + message2.lstrip('#').rstrip('#'))

    n = input('enter a number')
    n = int(n)
    print(type(n))

    for i in range(n):
        if i == 2:
            print('print special number')
        else:
            print('normal number')

    while n != 0:
        n = n - 1
        print("hello")


def new_method_recursive(x):
    if x == 0:
        return
    x = x - 1
    print(x)
    new_method_recursive(x)


def method_array():
    n = input()
    n = int(n)
    array = list(map(int, input().strip().split()))[:n]
    print(array)
    array.sort()
    array.pop()
    print(array)
    array.remove(2)
    print(array)
    array.reverse()
    print(array)


def mark_student():
    marks = input("Enter mark of student")
    marks = int(marks)
    if marks >= 75:
        print('hurray')
    else:
        print('you need to work hard')


def method_tuple():
    group = (2, 'hello')
    print(type(group))


if __name__ == '__main__':
    # my_method()
    # new_method_recursive(3)
    # method_array()
    # mark_student()
    method_tuple()
