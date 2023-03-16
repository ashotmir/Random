def gcd(*args):
    if len(args) < 2:
        return None
    if len(args) == 2:
        a, b = args
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    else:
        return gcd(args[0], gcd(*args[1:]))



# def gcd(*args):
#     """
#     Returns the greatest common divisor of a list of numbers.
#     """
#     if len(args) == 2:
#         a, b = args
#         if b == 0:
#             return a
#         else:
#             return gcd(b, a % b)
#     elif len(args) > 2:
#         result = gcd(args[0], args[1])
#         for i in range(2, len(args)):
#             result = gcd(result, args[i])
#         return result
#     else:
#         raise ValueError("At least two arguments are required.")
#

print(gcd(11))
