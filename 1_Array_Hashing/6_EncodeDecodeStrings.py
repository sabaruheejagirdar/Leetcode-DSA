""" 
LEETCODE: 271- Encode and Decode Strings
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Example
Input: dummy_input = ["neet","code"]
Output: ["neet","code"]


APPROACH:
Encoding:
   -For each string in the list, concatenate the string's length, a delimiter (#), and the string itself.
   Example: ["hello", "world"] -> "5#hello5#world"
Decoding:
   -Parse the encoded string by finding the delimiter to get the length of each string.
   -Extract the string using the length and continue until the end.
   Example: "5#hello5#world" -> ["hello", "world"]

"""

def encode(strs):
    encodedStr = "";
    for perStr in strs:
        encodedStr = encodedStr + str(len(perStr)) + "#" + perStr
    
    return encodedStr
# encodedStr-> 5#saba#5#ru#ee5#54321

def decode(str):
    res, i = [], 0

    while i<len(str):
        j = i
        while str[j] != "#":
            j+=1

        length = int(str[i:j])
        word = str[j+1: j+1+length]
        res.append(word)

        i = j + 1 + length

    return res

# dummy_input = ["saba#","ru#ee","54321"]
dummy_input = ["Hello","World"]

result1 = encode(dummy_input);
result2 = decode(result1)
print(result1)
print(result2)









# def decode(s):
#     fp, sp, idx = 0, 0, 0
#     decodedList = []

#     while fp < len(s):
#         word = ""
#         count = int(s[fp])
#         sp = fp + 2
#         for i in range(sp, sp+count):
#             word += s[i]
#         decodedList.append(word)

#         fp = fp + int(s[fp]) + 2

#     print("***",decodedList)
#     return False