def isPrime(input_number):
    for n in range(2, input_number):
        if (input_number % n) == 0:
            return False
    return True


def define_number_of_trials(num):
    for num in range(2, num, 1):
        print(f'{num} {isPrime(num)}')

def try_me():
    return 'successful disintegration'
