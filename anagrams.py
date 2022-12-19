import codewars_test as test


def anagrams(word, words):
    ana = []
    word_sorted = ''.join(sorted(word))

    for ele in words:
        if word_sorted == ''.join(sorted(ele)):
            ana.append(ele)

    return ana


@test.describe("Example Tests")
def example_tests():
    @test.it("Tests")
    def _():
        cases = [
            ('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbb', 'aaab'], ['aabb', 'bbaa']),
            ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'], ['carer', 'racer']),
            ('laser', ['lazing', 'lazy', 'lacer'], []),
            ('a', ['a', 'b', 'c', 'd'], ['a']),
            ('big', ['gig', 'dib', 'bid', 'biig'], []),
            ('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer'], ['ab', 'ba']),
            ('abba',
             ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa',
              'babaa'], ['aabb', 'bbaa', 'abab', 'baba', 'baab']),
        ]
        for word, words, expected in cases:
            msg = f"Incorrect answer for:\n  word = {repr(word)}\n  words = {repr(words)}\n"
            test.assert_equals(anagrams(word, words), expected, msg)
