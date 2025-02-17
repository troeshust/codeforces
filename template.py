from os import path
import sys
import random


RANDOM = random.getrandbits(32)
LOCAL_OUTPUT = 'output.txt'
LOCAL_INPUT = 'input.txt'

input = sys.stdin.buffer.readline # for numerican inputs
# input=lambda: sys.stdin.readline().rstrip("\r\n") # for text inputs

if(path.exists(LOCAL_OUTPUT)):
    sys.stdout = open(LOCAL_OUTPUT,'w')
if(path.exists(LOCAL_INPUT)):
    sys.stdin = open(LOCAL_INPUT,'r')


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        n, k = map(int, input().split())
        a = list(map(int, input().split()))


main()

    



