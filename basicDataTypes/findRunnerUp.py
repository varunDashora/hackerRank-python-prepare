if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if(n==2) :
        print(arr[0])
    else :
        print(sorted(set(arr))[-2])
        # print(list(set(sorted(arr)))[-2])
