import random

class Tree:
    def __init__(self, points):
        self.root = build_kd_tree(points)

    def print(self):
        print(get_tree_string(self.root))

    def searchKDTreePoint(self,point):
        searchKDTreePoint(self.root,point)

class Node:
    def __init__(self, point):
        self.point = point

class Leaf:
    def __init__(self, median, left=None, right=None):
        self.median = median
        self.left = left
        self.right = right


class Range:
    def __init__(self, intervals):
        if len(intervals) != 2:
            raise ValueError("Die Anzahl der Intervalle muss zwei sein.")

        self.intervals = intervals

    def is_fully_contained(self, median):
        for i in range(2):
            if not (self.intervals[i][0] < median < self.intervals[i][1]):
                return False
        return True

    def is_intersect(self, median):
        for i in range(2):
            if not (self.intervals[i][0] <= median <= self.intervals[i][1]):
                return False
        return True


# Beispiel der Verwendung
try:
    my_range = Range([[2, 5], [3, 7]])

    # Testen der is_fully_contained-Methode
    print(my_range.is_fully_contained([3, 4]))  # True
    print(my_range.is_fully_contained([6, 4]))  # False

    # Testen der is_intersect-Methode
    print(my_range.is_intersect([4, 5]))  # True
    print(my_range.is_intersect([1, 8]))  # False

except ValueError as e:
    print(f"Fehler beim Erstellen der Range: {e}")


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

        return Leaf(
            median=median,
            left=build_kd_tree(kleiner_als_median,depth+1),
            right=build_kd_tree(groesser_als_median,depth+1)
        )
    if (depth % 2 == 1):
        y_werte = [tupel[1] for tupel in points]
        median = find_median(y_werte)
        kleiner_als_median = [tupel for tupel in points if tupel[1] < median]
        groesser_als_median = [tupel for tupel in points if tupel[1] >= median]

        return Leaf(
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

def get_tree_string(root_node: Leaf):
    if root_node is None:
        return "Empty"
    if isinstance(root_node, Leaf):
        return "MNode(" + str(root_node.median) + ", " + str(get_tree_string(root_node.left)) + ", " + str(get_tree_string(root_node.right)) + ")"
    if isinstance(root_node,Node):
        return "Node(" +str(root_node.point)

def searchKDTreePoint(root,point,depth=0):
    if isinstance(root, Leaf):
        if (depth % 2 == 0):
            if(point[0]<root.median):
                searchKDTreePoint(root.left,point,depth+1)
            else:
                searchKDTreePoint(root.right,point,depth+1)
        else:
            if (point[1] < root.median):
                searchKDTreePoint(root.left, point, depth + 1)
            else:
                searchKDTreePoint(root.right, point, depth + 1)
    else:
        if(point[0]==root.point[0] and point[1]==root.point[1]):
            return True
        else:
            return False
def rangeSearch(root,range:Range):
    if isinstance(root, Leaf):
        return root
    else:
        if range.is_fully_contained(root.left.median)==True:
            return root.left
        else:
            if range.is_intersect(root.left.median)==True:
                rangeSearch(root.left,range)
        if(range.is_fully_contained(root.right.median)==True):
            return root.right
        else:
            if(range.is_intersect(root.right.median)):
                return rangeSearch(root.right,range)


# Beispiel
points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
kd_tree = Tree(points)
print(get_tree_string(kd_tree))
#drawTree(kd_tree)
print("moin")

