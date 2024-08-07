 dictP = {")":"(", "}":"{", "]":"["}
    stackP = []

    for i in s:
        if i in dictP:
            if stackP and stackP[-1] == dictP[i]:
                stackP.pop()
            else:
                return False
        else:
            stackP.append(i)


    return len(stackP) == 0