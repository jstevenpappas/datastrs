

"""

    URLify
    Write a method to replace all spaces in a string with its URL escaped equiv (i.e., %20).
    You may assume that the string has sufficient space at the end of the string to hold the addt'l
    characters, and that you are given the "true" length of the string.
    (NOTE: if implementing in Java, please use a character array so that you can perform this operation
    in place.)

"""
class Urlify(object):

    def __init__(self):
        pass


    def esc_spaces(self, string):
        uri_str = string.strip()
        return uri_str.replace(' ', '%20')






def main():

    test_str = 'Mr John Smith    '

    url_esc = Urlify()

    print(url_esc.esc_spaces(test_str))



if __name__ == "__main__":
    main()