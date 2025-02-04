# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        command = list(input().split())
        if command[0] ==  'insert':
            result.insert(int(command[1]),int(command[2]))
        elif command[0] ==  'print':
            print(result)
        elif command[0] ==  'remove':
            result.remove(int(command[1]))
        elif command[0] ==  'append':
            result.append(int(command[1]))
        elif command[0] ==  'sort':
            result.sort()
        elif command[0] ==  'pop':
            result.pop()
        elif command[0] ==  'reverse':
            result.reverse()