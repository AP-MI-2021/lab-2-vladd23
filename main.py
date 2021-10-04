import datetime


def prim(x):
    if x < 2:
        return 0
    for d in range(2, x // 2):
        if (x % d == 0):
            return 0
    return 1


def get_largest_prime_below(n):
    '''
    functie care cauta primul numar prim mai mic decat n
    :param n:
    :return: cel mai mare numar prim mai mic decat n, sau 2 (cel mai mic numar prim) in caz ca n < 0
    '''
    n = n - 1
    while n > 0:
        if prim(n) == 1:
            return n
        else:
            n = n - 1
    return 2


def test_get_largest_prime_below(n):
    assert get_largest_prime_below(76) == 73
    assert get_largest_prime_below(6) == 5
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(33) == 31


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
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(111) == True
    assert is_palindrome(125) == False
    assert is_palindrome(12521) == True


def get_age_in_days(birthday):
    prezent = datetime.datetime.now()
    diferenta = prezent - birthday

    return diferenta.days


def test_get_age_in_days():
    zi1 = datetime.datetime(2002, 2, 23)
    zi2 = datetime.datetime(2010, 1, 3)
    zi3 = datetime.datetime(2005, 11, 30)
    assert get_age_in_days(zi1) == 7163
    assert get_age_in_days(zi2) == 4292
    assert get_age_in_days(zi3) == 5787

def main():
    while True:

        print("1. Găsește ultimul număr prim mai mic decât un număr dat.")
        print("2. Determină dacă un număr dat este palindrom.")
        print("3. Varsta unei persoane in zile")
        print("x. Exit")
        optiune = input("Selecteaza optiunea dorita: ")
        if optiune == "1":
            n = int(input("Introduceti un numar: "))
            print("Cel mai mare numar prim mai mic decat", n, "este: ", get_largest_prime_below(n))
        elif optiune == "2":
            n = int(input("Introduceti un numar: "))
            if is_palindrome(n) is True:
                print("Numarul ", n, "este palindrom")
            else:
                print("Numarul", n, "nu este palindrom")
        elif optiune == "3":
            an = int(input("Introduceti anul nasterii: "))
            luna = int(input("Introduceti luna nasterii: "))
            zi = int(input("Introduceti ziua nasterii: "))
            data_nasterii = datetime.datetime(an, luna, zi)
            print("Varsta este de", get_age_in_days(data_nasterii), "zile")
        elif optiune.lower() == "x":
            break
        else:
            print("Optine invalida, selectati alta!")


if __name__ == '__main__':
    main()
