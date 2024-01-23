#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    list_str = dir(hidden_4)
    for i in range(0, len(list_str)):
        str = list_str[i]
        if str[:2] != "__" != str[-2:]:
            print(str)
