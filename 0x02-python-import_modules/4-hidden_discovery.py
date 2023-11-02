#!/usr/bin/python3
import hidden_4


def main():
    name_list = dir(hidden_4)
    for i in range(len(name_list)):
        if(name_list[i][0] != '_'):
            print(name_list[i])


if __name__ == "__main__":
    main()
