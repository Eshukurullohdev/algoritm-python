def reverse_number(num):
    return int(str(num)[::-1])

num = 9839032898348932 
print(f"sonalrning teslarisi {reverse_number(num)}")

print(f"{num} ning teskarisi {reverse_number(num)}")
def notogri_sanash(a):
    return int(str(a)[::-1])

a = 3428782375323875
print(f"{a} ning teskari soni {notogri_sanash(a)}")

def word_count(text):
    words = text.split()
    return len(words)


text = "Hello, world! This is a sample text."
print(f"matn sozlarini soni: {word_count(text)}")

def sozlarni_sonini_aniqlash(x):
    karim = x.split()
    return len(karim)

x = "qaleysan hello whatsapp kjdsnk dksnkl kjsnakln klasndib kdsnkls xskdbnks ksdksd ks"
print(f"jami matini soni {sozlarni_sonini_aniqlash(x)} ")




def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
        return True

user_input = input("Raqamni kiriting: ")

if user_input.isdigit():
    num = int(user_input)
    if is_prime(num):
        print(f"{num} tub son")
    else:
        print(f"{num} tub son emas butun sondir")
else:
        print("Iltimos faqat butun son kiriting!!")
print(f"sonlarning yigindisi {is_prime(num)}")