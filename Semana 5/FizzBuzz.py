def fizzbuzz(numero):
    if numero % 5 == 0 and numero %3 == 0:
        return "FizzBuzz"
    else: 
        if numero % 5 == 0:
            return "Buzz"
        else:
            if numero % 3 == 0:
                return "Fizz"
            else:
                return numero
