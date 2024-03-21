#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    call = dir(hidden_4)
    for item in call:
        if item[:2] != "__":
            print(item)
