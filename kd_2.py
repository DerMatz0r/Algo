import random

#todo bereichsuche mit eigenen datentyp region
#noch klasse tree erstellen die Node und Mnode hat
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
        erg=getMedian(x_werte)
        median=erg[0]
        kleiner_als_median = erg[1]
        groesser_als_median = erg[2]

        return MNode(
            median=median,
            left=build_kd_tree(kleiner_als_median,depth+1),
            right=build_kd_tree(groesser_als_median,depth+1)
        )
    if (depth % 2 == 1):
        y_werte = [tupel[1] for tupel in points]
        erg = getMedian(y_werte)
        median = erg[0]
        kleiner_als_median = erg[1]
        groesser_als_median = erg[2]

        return MNode(
                median=median,
                left=build_kd_tree(kleiner_als_median, depth + 1),
                right=build_kd_tree(groesser_als_median, depth + 1)
        )

def searchKDTreePoint(root,point,depth=0):
    if isinstance(root,MNode):
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


def getMedian(array):
    array=sorted(array)
    n = len(array)
    m = n // 2

    median_value = array[m]
    return median_value

def get_tree_string(root_node: MNode):
    if root_node is None:
        return "Empty"
    if isinstance(root_node,MNode):
        return "MNode(" + str(root_node.median) + ", " + str(get_tree_string(root_node.left)) + ", " + str(get_tree_string(root_node.right)) + ")"
    if isinstance(root_node,Node):
        return "Node(" +str(root_node.point)


# Beispiel
points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
a=[6,9,2,7,1,10,34,50]
getMedian(a)
kd_tree = build_kd_tree(points)
print(get_tree_string(kd_tree))

print("moin")

