import codewars_test as test

'''def loose_change(numb):
    coin_value = {'Quarters': 25,'Dimes': 10,'Nickels': 5,'Pennies': 1}
    change = {'Quarters': 0, 'Dimes': 0, 'Nickels': 0,'Pennies': 0}
    coin_value_items = coin_value.items()
    for key, value in coin_value_items:
        is_in = numb // value >= 1
        while is_in:
            change[key]+=1
            numb -= value
            is_in = numb // value >= 1
    return change
if __name__ == "__main__":
    print ("Testing")
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) ==  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    print ("Passed")
'''
def loose_change(cents):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while cents >= 25:
        quarters += 1
        cents -= 25

    while cents >= 10:
        dimes += 1
        cents -= 10

    while cents >= 5:
        nickels += 1
        cents -= 5

    while cents >= 1:
        pennies += 1
        cents -= 1

    return {
        'Pennies': pennies,
        'Nickels': nickels,
        'Dimes': dimes,
        'Quarters': quarters
    }


# Pennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢)
test.assert_equals(loose_change(29), {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
test.assert_equals(loose_change(91), {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
test.assert_equals(loose_change(0), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(-2), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
