def fizz(x):
    if x % 3 == 0 and x % 5 != 0:
        return True
    else:
        return False

def buzz(x):
    if x % 5 == 0 and x % 3 != 0:
        return True
    else:
        return False

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0 and x % 5 != 0:
        return "Fizz"
    elif x % 3 != 0 and x % 5 == 0:
        return "Buzz"
    else:
        return x


def teste_fb():
    if fizzbuzz(3) == "Fizz":
        print("ok")
    if fizzbuzz(5) == "Buzz":
        print("ok")
    if fizzbuzz(15) == "FizzBuzz":
        print("ok")
    if fizzbuzz(4) == 4:
        print("ok")

teste_fb()

