

# def ter(string):
#     return string[::-1]
#
# def ter_test():
#     string_test = "good"
#     return ter(string_test) == "doog"
#
#
# res = ter("love")
# print(res)


def reverse(string):
    return string[::-1]

def test_reverse():
    string = "good"
    assert reverse(string) == "doog"

    another_string = "itest"
    assert reverse(another_string) == "tseti"