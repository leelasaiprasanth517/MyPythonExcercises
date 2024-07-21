def to_caml_case(text):
    capitalize = False
    arr = []
    for i in text:
        if i == '_' or i=='-':
            capitalize = True
        else:
            if capitalize:
                arr.append(i.upper())
                capitalize=False
            else:
                arr.append(i)
    return ''.join(arr)
text=input()
print(to_caml_case(text))