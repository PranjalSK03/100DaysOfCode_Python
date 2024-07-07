
test_variable = 10

def ap_natural_numbers(n):
    if n == 0:
        return 0
    return n + ap_natural_numbers(n-1)