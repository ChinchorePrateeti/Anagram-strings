# checking if the given strings are an anagram
# anagrams are different words made out of same letters

string1 = "HEART"
string2 = "EARTH"

# sorting the strings to set letters in an order

string1_ordered = sorted(string1)
string2_ordered = sorted(string2)

#checking if the strings ordered are in the same manner

if string1_ordered == string2_ordered:
    print("Yes! strings are anagrams")
else:
    print("No! strings are not anagrams")

# if strings are combination of upper and lowercase characters, change them all to upper/lower