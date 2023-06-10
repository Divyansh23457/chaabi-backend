def f(x , input):
    dict = {}
    x=x.split(';')
    for i in x:
        j = i.split(',')
        dict[j[0]] = j[1]
    output = {}
    for i in input:
        j = i.split('.')
        if len(j)<2:
            output[i] = "unknown"
        elif j[1] in dict:
            output[i] = dict[j[1]]
        else:
            output[i] = "unknown"
    return output

print(f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
"xyz.xls", "text.csv", "123"]))
