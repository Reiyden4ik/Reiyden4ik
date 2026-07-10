def collatz_conjecture():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        k = 0
        while n != 1:
            if n % 2 != 0:
                print(int(n))
                n = n * 3 + 1
            else:
                print(int(n))
                n = n // 2
            k += 1
        print("end")
        print(k)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

collatz_conjecture()