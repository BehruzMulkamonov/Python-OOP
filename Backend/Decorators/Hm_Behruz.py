# HM_one
# def add_one():
#     return ()
#
# def plus_one(number):
#     return number +1
# add_one = plus_one
# print(add_one(4))

# HM_two
# def uppercase_dec(func):
#     def word():
#         print('My name is Behruz')
#         print(f"{func()}".upper())
#     print(word())
#
# # @uppercase_dec
# def say_hi():
#     return 'here there'
# say_hi = uppercase_dec(say_hi)
# print(say_hi)


def standartize(func):
    def wrapper(*args):
        func(args)
        print(f'+998{func(args)}')
        return
    return wrapper
@standartize
def nine(args):
    return args
print(nine('906458545'))
