def pubKey_ggt(a, icm):
    while icm > 0:
        a, icm = icm, a % icm
    return a


def output_of_e(a, icm):
    while pubKey_ggt(a, icm) != 1:
        a = a + 1
    else:
        return a



e = 13
print(output_of_e(3, 235560))
print(output_of_e(13, 59592))
print(pubKey_ggt(17, 235560))

