"""
There is a road consisting of N segments, numbered from 0 to N-1, represented by a string S.

Segment S[K] of the road may contain a pothole, denoted by a single uppercase "x" character, or may be a good segment without any potholes, denoted by a single dot,".".

For example, string".X. .X" means that there are two potholes in total in the road: one is located in segment S[1] and one in segment S[4].

All other segments are good. The road fixing machine can patch over three consecutive segments at once with asphalt and repair all the potholes located within each of these segments. Good or already repaired segments remain good after patching them. Your task is to compute the minimum number of patches required to repair all the potholes in the road.

Write a function: def solution(s) that, given a string S of length N, returns the minimum number of patches required to repair all the potholes.

Examples: 1. Given S=".X..x", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 2-4. 2.

Given S = "x.xxxxx.x", your function should return 3. The road fixing machine could patch, for example, segments 0-2, 3-5 and 6-8. 3.

Given S = "xx.xxx", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 3-5. 4. Given S = "xXxx", your function should return 2.
"""


def get_minimum_patches(road):
    road_patch_map = {}
    for i, block in enumerate(road):
        if block.lower() != 'x':
            continue
        if (i-1 in road_patch_map) or (i-2) in road_patch_map:
            continue
        road_patch_map[i] = 1
    return sum(road_patch_map.values())


if __name__ == '__main__':
    roads = ['.X..x', 'x.xxxxx.x', 'xx.xxx']
    for road in roads:
        print(get_minimum_patches(road))
