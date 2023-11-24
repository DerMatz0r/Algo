import random


class Node:
    def __init__(self, point):
        self.point = point

class MNode:
    def __init__(self, median, left=None, right=None):
        self.median = median
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None

    if (len(points) == 1):
        return Node(
            point=points[0]
        )

    if(depth%2==0):
        x_werte = [tupel[0] for tupel in points]
        median=find_median(x_werte)
        kleiner_als_median = [tupel for tupel in points if tupel[0] < median]
        groesser_als_median = [tupel for tupel in points if tupel[0] >= median]

        return MNode(
            median=median,
            left=build_kd_tree(kleiner_als_median,depth+1),
            right=build_kd_tree(groesser_als_median,depth+1)
        )
    if (depth % 2 == 1):
        y_werte = [tupel[1] for tupel in points]
        median = find_median(y_werte)
        kleiner_als_median = [tupel for tupel in points if tupel[1] < median]
        groesser_als_median = [tupel for tupel in points if tupel[1] >= median]

        return MNode(
                median=median,
                left=build_kd_tree(kleiner_als_median, depth + 1),
                right=build_kd_tree(groesser_als_median, depth + 1)
        )

def searchKDTree(root,range):
    if isinstance(root,Node):
        if root.point[0] in range:
            if root.point[1] in range:
                return root



def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)

    if k == pivot_index:
        return arr[pivot_index]
    elif k < pivot_index:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k)

def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
        # Wenn die Anzahl der Elemente gerade ist, finden wir den Index des rechten Medians
        median_index = n // 2
    else:
        # Wenn die Anzahl der Elemente ungerade ist, finden wir den Index des Medians
        median_index = (n - 1) // 2

    return randomized_select(arr, 0, len(arr) - 1, median_index)

#def drawTree(kdTree):
#    graph=nx.Graph()
#    l=kdTree.left
#    print("na")

def get_tree_string(root_node: MNode):
    if root_node is None:
        return "Empty"
    if isinstance(root_node,MNode):
        return "MNode(" + str(root_node.median) + ", " + str(get_tree_string(root_node.left)) + ", " + str(get_tree_string(root_node.right)) + ")"
    if isinstance(root_node,Node):
        return "Node(" +str(root_node.point)


# Beispiel
points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
kd_tree = build_kd_tree(points)
print(get_tree_string(kd_tree))
#drawTree(kd_tree)
print("moin")

