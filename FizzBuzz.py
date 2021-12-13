def Fizz():
    num1=int(input("Nhap so bat ki: "))
    num2=int(input("Nhap so bat ki: "))

    if num2<num1:
        print("Số sau cần lớn hơn số đầu")
    else:
        for i in range(num1,num2):
            if i%3== 0 and i%5==0:
                print("FizzBuzz")
            elif i%3==0:
                print("Fizz")
            elif i%5==0:
                print("Buzz")
            else:
                print(i)

    Fizz()