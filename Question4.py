def f(dict):
    ans = {}
    for i in dict:
        ans[dict[i]]= i
    return ans

dict = {
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}

print(f(dict))
