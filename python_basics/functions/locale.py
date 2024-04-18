# Write a function that extracts the language code from a locale.
# A locale is a combination of a language code, a region,
# and usually also a character set, e.g en_US.UTF-8.


# knowing language code will be the first 2 letters in locale
# print back 1st 2 letters of locale
def locale_language(locale):
    return locale[0:2]  # OR locale.split("_")[0]


print(locale_language("en_US.UTF-8"))  # en
print(locale_language("en_GB.UTF-8"))  # en
print(locale_language("ko_KR.UTF-16"))  # ko
print(locale_language("en_KR.UTF-16"))  # en


# OR not very useful or reusable
# but if locale is specififed as a case it will return language code
# includes error message
def extract_language(locale):
    match locale:
        case "en_US.UTF-8":
            return "en"
        case "en_GB.UTF-8":
            return "en"
        case "ko_KR.UTF-16":
            return "ko"
        case _:
            return "Language code not found."


# TEST
print(extract_language("en_US.UTF-8"))  # en
print(extract_language("en_GB.UTF-8"))  # en
print(extract_language("ko_KR.UTF-16"))  # ko
print(extract_language("en_KR.UTF-16"))  # Language code not found
