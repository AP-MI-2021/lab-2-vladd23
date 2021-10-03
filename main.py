def prim(x):
    if x < 2:
        return 0
    for d in range(2, x // 2):
        if(x % d == 0) :
            return 0
    return 1

assert prim(-2) == 0
assert prim(2) == 1
assert prim(79) == 1

def get_largest_prime_below(n):
    '''
    functie care cauta primul numar prim mai mic decat n
    :param n:
    :return: cel mai mare numar prim mai mic decat n, sau 2 (cel mai mic numar prim) in caz ca n < 0
    '''

    while n > 0:
        if prim(n) == 1:
            return n
        else: n = n - 1
    return 2

def test_get_largest_prime_below(n):
    print("cel mai mare numar prim mai mic decat", n," este :" ,get_largest_prime_below(n-1))

def is_palindrome(n):
    '''

    :param n:
    :return: True daca numarul este palindrom si False in caz contrar
    '''
    cn = n
    m = 0
    while cn != 0:
        m = m * 10 + cn % 10
        cn = cn // 10
    if n == m:
        return True
    else : return False

def test_is_palindrome(n):
    if is_palindrome(n) is True:
        print("Numarul", n, "este palindrom")
    else:
        print("Numarul", n, "nu este palindrom")

while True:
    print("1. Găsește ultimul număr prim mai mic decât un număr dat.")
    print("2. Determină dacă un număr dat este palindrom.")
    print("x. Exit")
    optiune = input("Selecteaza optiunea dorita: ")
    if optiune == "1":
        n = int(input("Introduceti un numar: "))
        test_get_largest_prime_below(n)
    elif optiune == "2":
        n = int(input("Introduceti un numar: "))
        test_is_palindrome(n)
    elif optiune.lower() == "x":
        break
    else:
        print("Optine invalida, selectati alta!")
