import math
import os
import random
import re
import sys



if __name__ == '__main__':
    while True:

        n = int(input().strip())
        if not n:
            break
        else:
            binary = []
            while n > 0:
                r = n % 2
                binary.append(r)
                n = n // 2

            binary = binary[::-1]

            binary_count = 0
            consecutive_binary = []
            for b in binary:
                if b:
                    binary_count += 1

                else:
                    consecutive_binary.append(binary_count)
                    binary_count = 0

            print(max(consecutive_binary))
