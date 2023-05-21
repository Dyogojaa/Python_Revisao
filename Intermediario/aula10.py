# def double_number(number):
#     return number * 2

# def triple_number(number):
#     return number * 3

# def quadruple_number(number):
#     return number * 4

# # Usage examples:
# number = 5

# result_double = double_number(number)
# print(f"The double of {number} is {result_double}")

# result_triple = triple_number(number)
# print(f"The triple of {number} is {result_triple}")

# result_quadruple = quadruple_number(number)
# print(f"The quadruple of {number} is {result_quadruple}")


def createMulti(multi):
    def multiplicate(numero):
        return numero * multi
    return multiplicate


duplicate = createMulti(2)
triplicate = createMulti(3)
quadriplicate = createMulti(4)
print(duplicate(2))
print(triplicate(3))
print(quadriplicate(4))