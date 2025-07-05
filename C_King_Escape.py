n = int(input())
ax, ay = map(int,input().split())
bx, by = map(int,input().split())
cx, cy = map(int,input().split())

arr = [[ax,ay], [bx,by], [cx,cy]]
queen_centered = []

def get_coordinate(x,y):
    if x>=0 and y>=0:
        return 1
    elif x<0 and y>=0:
        return 2
    elif x<0 and y<0:
        return 3
    else:
        return 4

for x,y in arr:
    queen_centered.append([x-ax, y-ay])
same_cord = get_coordinate(*queen_centered[1])==get_coordinate(*queen_centered[2])
print("YES" if same_cord else "NO")