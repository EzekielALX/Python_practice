def uppercase(str):
    result = ""
    for (i) in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            result += chr(ord(i) - 32)
        else:
            result += ord(i)
    print(result)

uppercase("gi")
