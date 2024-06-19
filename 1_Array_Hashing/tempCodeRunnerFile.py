 for i in range(sp, sp+count):
            word += s[i]
        decodedList.append(word)

        fp = fp + int(s[fp]) + 2

    print("***",decodedList)
    return False