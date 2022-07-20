def isPalindrome(bigStr):
    onlyAlpha=""
    result=False
    for char in bigStr.lower():
        if ord(char) >= 97 and ord(char) <=122 or ord('0') <= ord(char) <= ord('9'):
            onlyAlpha += char
    revString=reverseAString(onlyAlpha)
    print(onlyAlpha)
    print(revString)
    if onlyAlpha == revString:
        result=True

    print(result)
    return result

def reverseAString(a_string):
    new_string=""
    index=len(a_string)
    while index:
        index -= 1
        new_string += a_string[index]
    return new_string
s = "A man, a plan, a canal: Panama"
isPalindrome(s)