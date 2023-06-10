def find_common_and_different_elements(listA, listB):
    common = []
    different = []

    for element in listA:
        if element in listB:
            common.append(element)
        else:
            different.append(element)

    for element in listB:
        if element not in listA:
            different.append(element)

    return list(set(common)), list(set(different))


Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

common, different = find_common_and_different_elements(Mainstream, must_watch)


print("Common elements:", common)
print("Different elements:", different)












