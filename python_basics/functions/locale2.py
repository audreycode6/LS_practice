# Similar to the previous exercise, write a function that extracts
# the region code from a locale. (comes after _ and before .)


def extract_region(locale):
    # start slice at 3, i.e character after _
    # language code and ('_') seperator take up 3 indeces
    # stop at 5, i.e character after region code ('.')
    # region code is 2 characters
    return locale[3:5]


print(extract_region("en_US.UTF-8"))  # US
print(extract_region("en_GB.UTF-8"))  # GB
print(extract_region("ko_KR.UTF-16"))  # KR
