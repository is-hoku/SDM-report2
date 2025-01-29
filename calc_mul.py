#!/usr/bin/python3

def calc(A, B):
    if not isinstance(A, int) or not isinstance(B, int):
        return -1
    ai = int(A)
    bi = int(B)
    if 1 <= ai and ai <= 999 and 1 <= bi and bi <= 999:
        return ai*bi
    else:
        return -1


def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))


if __name__ == '__main__':
    main()
