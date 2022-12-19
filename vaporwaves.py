import codewars_test as test


def vaporcode(s):
        s = s.upper()
        s = s.replace(" ", "")
        s = s.replace("", "  ")
        s = s.strip("  ")
        return s




test.assert_equals(vaporcode("Lets go to the movies"),"L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
test.assert_equals(vaporcode("Why isn't my code working?"),"W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")
'''return "  ".join(s.replace(" ", "").upper())'''