# def is_leap():
#     if year%4==0 or year%400==0 and yaer%100!=0:
#         return True
#     else:
#         return False
# year=int(input("enter year"))
# print(is_leap())

def is_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
year = int(input("enter "))
print(is_leap(year))