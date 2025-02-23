# n, x0 = map(int, input().split())  
# current_camera_man_track = [x0, x0]
# moves = 0

# def check_intersection(camera_range, left, right):
#     return not (right < camera_range[0] or left > camera_range[1])

# for _ in range(n):
#     ai, bi = map(int, input().split())
#     left, right = min(ai, bi), max(ai, bi)
    
#     if check_intersection(current_camera_man_track, left, right):
#         continue
#     if left < current_camera_man_track[0]:
#         moves += current_camera_man_track[0] - left
#         current_camera_man_track[0] = left
#     if right > current_camera_man_track[1]:
#         moves += right - current_camera_man_track[1]
#         current_camera_man_track[1] = right

# print(moves)


n, x0 = map(int, input().split())
current_camera_man_track = [x0, x0]
moves = 0

def check_intersection(camera_range, left, right):
    return not (right < camera_range[0] or left > camera_range[1])

for _ in range(n):
    ai, bi = map(int, input().split())
    left, right = min(ai, bi), max(ai, bi)
    
    if check_intersection(current_camera_man_track, left, right):
        continue
    
    elif left < current_camera_man_track[0]:
        moves += current_camera_man_track[0] - left
        current_camera_man_track[0] = left
    elif right > current_camera_man_track[1]:
        moves += right - current_camera_man_track[1]
        current_camera_man_track[1] = right

if current_camera_man_track[0] > current_camera_man_track[1]:
    print(-1)
else:
    print(moves)