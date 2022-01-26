def collatz(number):
    
    while number != 1:
        print(number)
        if number % 2 ==0:
            number = number//2
        elif number == 0:
            print("Invalid number")
            continue
        else: 
            number = number * 3 + 1
    print(number)

collatz(30)