def encodeString(nums):
    encodestr = ""
    for num in nums:
        encodestr += str(len(num))+"#"+num

    print(encodestr)
    return encodestr

def decodeString(encodeStr):
    output, i = [], 0
    while i<len(encodeStr):
        j=i
        while encodeStr[j] != '#':
            j += 1
        length=int(encodeStr[i:j])
        output.append(encodeStr[j+1:j+1+length])
        i=j+1+length
    print(output)
    return output


nums=["lint","code","love","you"]
inputStr=encodeString(nums)
decodeString(inputStr)