import pygame
import random
import sys
import time

# Constants
SCREEN_WIDTH = 910
SCREEN_HEIGHT = 750
arrSize = 130
rectSize = 7

arr = [0] * arrSize
Barr = [0] * arrSize

# Initialize pygame
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

complete = False

def visualize(x=-1, y=-1, z=-1):
    window.fill((0, 0, 0))  # Fill the screen with black

    for i in range(arrSize):
        color = (170, 183, 184)  # Default color
        if complete:
            color = (100, 180, 100)  # Completed sorting
        elif i == x or i == z:
            color = (100, 180, 100)  # Green for comparison
        elif i == y:
            color = (165, 105, 189)  # Purple for swaps
        
        pygame.draw.rect(window, color, (i * rectSize, 0, rectSize, arr[i]))

    pygame.display.update()

def partition_array(a, si, ei):
    count_small = sum(1 for i in range(si + 1, ei + 1) if a[i] <= a[si])
    c = si + count_small
    a[c], a[si] = a[si], a[c]
    visualize(c, si)

    i, j = si, ei
    while i < c and j > c:
        if a[i] <= a[c]:
            i += 1
        elif a[j] > a[c]:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            visualize(i, j)
            time.sleep(0.07)
            i += 1
            j -= 1
    return c

def quick_sort(a, si, ei):
    if si >= ei:
        return
    c = partition_array(a, si, ei)
    quick_sort(a, si, c - 1)
    quick_sort(a, c + 1, ei)

def merge_sorted_arrays(a, si, ei):
    size_output = (ei - si) + 1
    output = [0] * size_output

    mid = (si + ei) // 2
    i, j, k = si, mid + 1, 0
    while i <= mid and j <= ei:
        if a[i] <= a[j]:
            output[k] = a[i]
            i += 1
        else:
            output[k] = a[j]
            j += 1
        k += 1
        visualize(i, j)

    while i <= mid:
        output[k] = a[i]
        i += 1
        k += 1
    while j <= ei:
        output[k] = a[j]
        j += 1
        k += 1

    for l in range(si, ei + 1):
        a[l] = output[l - si]
        visualize(l)
        time.sleep(0.015)

def merge_sort(a, si, ei):
    if si >= ei:
        return
    mid = (si + ei) // 2
    merge_sort(a, si, mid)
    merge_sort(a, mid + 1, ei)
    merge_sorted_arrays(a, si, ei)

def selection_sort():
    for i in range(arrSize - 1):
        min_index = i
        for j in range(i + 1, arrSize):
            if arr[j] < arr[min_index]:
                min_index = j
            visualize(i, min_index)
            time.sleep(0.001)
        arr[i], arr[min_index] = arr[min_index], arr[i]

def binary_search(a, x):
    l, r = 0, arrSize - 1
    while l <= r:
        m = l + (r - l) // 2
        visualize(m, l, r)
        time.sleep(0.07)

        if a[m] == x:
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

def load_arr():
    global arr
    arr = Barr.copy()

def randomize_and_save_array():
    global Barr
    Barr = [random.randint(1, SCREEN_HEIGHT) for _ in range(arrSize)]

def execute():
    global complete
    randomize_and_save_array()
    load_arr()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                complete = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_0:
                    randomize_and_save_array()
                    load_arr()
                elif event.key == pygame.K_1:
                    load_arr()
                    selection_sort()
                    complete = True
                elif event.key == pygame.K_2:
                    load_arr()
                    merge_sort(arr, 0, arrSize - 1)
                    complete = True
                elif event.key == pygame.K_3:
                    load_arr()
                    quick_sort(arr, 0, arrSize - 1)
                    complete = True
                elif event.key == pygame.K_4:
                    val = int(input("Enter value to search: "))
                    res = binary_search(arr, val)
                    if res != -1:
                        print(f"Found at index {res}")
                    else:
                        print("Not found.")
        visualize()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    execute()
