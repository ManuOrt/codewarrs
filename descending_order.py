import codewars_test as test


def descending_order(num):
    my_list = [int(x) for x in str(num)]
    my_list = sorted(my_list)

    my_list.reverse()

    my_list_string = [str(i) for i in my_list]

    complete_string = "".join(my_list_string)

    return int(complete_string)


test.assert_equals(descending_order(0), 0)
test.assert_equals(descending_order(15), 51)
test.assert_equals(descending_order(123456789), 987654321)
test.assert_equals(descending_order(69050), 96500)

# stra = str(num)
# my_list = []
#
# for char in stra:
#     my_list.append(int(char))