def func():
    first = []
    second = []
    third = []
    fourth = []
    while(True):
        print("Введіть ім*я:(Для виходу ввести !)")
        name = input()
        if name == "!":
            break
        print("Введіть вік:")
        birthDay = int(input())
        if birthDay < 7:
            first = funcForTest(name, list)
        elif birthDay == 7:
            second.append(name)
        elif birthDay == 8:
            third.append(name)
        else:
            fourth.append(name)
        n = 0
        print("First: ", end="")
        while(n < len(first)):
            print(" ", first[n], end="")
            n = n + 1
        print("\n")
        n = 0
        print("Second: ", end="")
        while(n < len(second)):
            print(" ", second[n], end="")
            n = n + 1
        print("\n")
        n = 0
        print("Third: ", end="")
        while(n < len(third)):
            print(" ", third[n], end="")
            n = n + 1
        print("\n")
        n = 0
        print("Fourth: ", end="")
        while(n < len(fourth)):
            print(" ", fourth[n], end="")
            n = n + 1
        print("\n")

def funcForTest(name, list):
    list.append(name)
    return list
    

    

if __name__ == '__main__':
    func()