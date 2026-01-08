import math

def det_2x2(m)->float:
    """Determinant of a 2x2 matrix."""
    a,b,c,d = *m[0], *m[1]
    return a*d - b*c

def distance(p1:tuple,p2:tuple)->float:
    """Euclidean distance between two points."""
    x1, y1, x2, y2 = *p1, *p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def zcross(A,B,C):
    """Z component of the cross product of the vectors formed by AB and BC.
    
    Args:
        A,B,C (tuple): Points A,B,C as (x,y) tuples.

    Returns:
        float: z component of the corss product.
    """
    ax, ay, bx, by, cx, cy = *A, *B, *C
    # computing vectors AB and BC by B-A and C-B
    ab,bc = (bx-ax, by-ay) , (cx-bx, cy-by)
    return det_2x2([ab,bc])

def perimeter(points: list) -> float:
    """Calculate the perimeter of the polygon.
    
    Args:
        points (list[tuple]): 
            List of tuple of representing the polygon 
            in the anti-clockwise order.

    Returns:
        float: the perimeter of the polygon.
    """
    
    return sum(distance(p1,p2) for p1,p2 in zip(points, points[1:]+points[:1]))

def bounding_box(points: list) -> tuple:
    """Calculate the bounding box of the polygon.
    
    Args:
        points (list[tuple]): 
            List of tuple of representing the polygon 
            in the anti-clockwise order.

    Returns:
        bottom_left (tuple), top_right (tuple): 
            coordinates of the bottom left and top right 
            vertices of the bounding box.
    """
    
    
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return (min(xs), min(ys)), (max(xs), max(ys))
    

def area(points: list):
    """Calculate the area of the polygon using the shoelace formula.
    
    Args:
        points (list[tuple]): 
            List of tuple of representing the polygon 
            in the anti-clockwise order.

    Returns:
        (int|float): the area of the polygon.
    """
    
    
    return sum(det_2x2([p1,p2]) for p1,p2 in zip(points, points[1:]+points[:1])) / 2
    

def is_convex(points: list) -> bool:
    """Check if the polygon is convex using cross products.
    
    Args:
        points (list[tuple]): 
            List of tuple of representing the polygon 
            in the anti-clockwise order.

    Returns:
        (bool): True if the polygon is convex else concave.
    """
    
    
    n = len(points)
    points += points[:2]
    return all(zcross(points[i],points[i+1],points[i+2])>=0 for i in range(n))
    
# #Another Method:
# import math

# def det_2x2(m)->float:
#     """Determinant of a 2x2 matrix."""
#     a,b,c,d = *m[0], *m[1]
#     return a*d - b*c

# def distance(p1:tuple,p2:tuple)->float:
#     """Euclidean distance between two points."""
#     x1, y1, x2, y2 = *p1, *p2
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# def zcross(A,B,C):
#     """Z component of the cross product of the vectors formed by AB and BC.
    
#     Args:
#         A,B,C (tuple): Points A,B,C as (x,y) tuples.

#     Returns:
#         float: z component of the corss product.
#     """
#     ax, ay, bx, by, cx, cy = *A, *B, *C
#     # computing vectors AB and BC by B-A and C-B
#     ab,bc = (bx-ax, by-ay) , (cx-bx, cy-by)
#     return det_2x2([ab,bc])

# def perimeter(points: list) -> float:
#     """Calculate the perimeter of the polygon.
    
#     Args:
#         points (list[tuple]): 
#             List of tuple of representing the polygon 
#             in the anti-clockwise order.

#     Returns:
#         float: the perimeter of the polygon.
#     """
#     pre = points[0]
#     sum=0
    
#     for i in points:
#         sum += distance(pre,i)
#         pre=i
#     return sum+distance(points[0],points[-1])
    

# def bounding_box(points: list) -> tuple:
#     """Calculate the bounding box of the polygon.
    
#     Args:
#         points (list[tuple]): 
#             List of tuple of representing the polygon 
#             in the anti-clockwise order.

#     Returns:
#         bottom_left (tuple), top_right (tuple): 
#             coordinates of the bottom left and top right 
#             vertices of the bounding box.
#     """
#     minx=100
#     miny=100
#     maxx=0 
#     maxy=0
    
#     for i in points:
#         if i[0]>maxx:
#             maxx=i[0]
#         if i[0]<minx:
#             minx=i[0]
        
#         if i[1]>maxy:
#             maxy=i[1]
#         if i[1]<miny:
#             miny=i[1]
       
#     return ((minx,miny),(maxx,maxy))
            
        
        
    

# def area(points: list):
#     """Calculate the area of the polygon using the shoelace formula.
    
#     Args:
#         points (list[tuple]): 
#             List of tuple of representing the polygon 
#             in the anti-clockwise order.

#     Returns:
#         (int|float): the area of the polygon.
#     """
#     l=points+[points[0]]
#     sum=0 
#     pre=points[0]
    
#     for i in l:
#         m=[pre,i]
#         sum += det_2x2(m)
#         pre=i 
#     return .5*sum
    

# def is_convex(points: list) -> bool:
#     """Check if the polygon is convex using cross products.
    
#     Args:
#         points (list[tuple]): 
#             List of tuple of representing the polygon 
#             in the anti-clockwise order.

#     Returns:
#         (bool): True if the polygon is convex else concave.
#     """
#     l=points+[points[0]]+[points[1]]
#     pre1=points[0]
#     pre2=points[1]
#     c=0
#     for i in l[2::]:
#         if zcross(pre1,pre2,i)<0:
#             c=1
#             break
#         else:
#             pre1=pre2
#             pre2=i
#     if c==1:
#         return False
#     else:
#         return True
    
#     Polygon Analysis
# Given a list of points representing the vertices of a polygon in anti-clockwise direction, implement various functions to analyze the properties of the polygon.

# perimeter: The total length of the polygon, calculated by summing the distances between consecutive vertices.\Given the vertices p1,p2,...,pn the perimeter is given by dist(p1,p2) + dist(p2,p3) + ... + dist(pn, p1)
# bounding_box: The smallest rectangle that can contain the polygon, represented by the coordinates of its bottom-left and top-right corners. Given the vertices as (x1,y1), (x2,y2), ... ,(xn,yn), the bottom-left coordinate is given by (min(x1,x2...,xn), min(y1,y2,...,yn)) and the top-right coordinate is given by (max(x1,x2,...,xn), max(y1,y2,...,yn)).
# area: The area of the polygon using the Shoelace formula, based on the coordinates of the vertices.
# Area of a polygon = Half the sum of determinants of coordinates of adjacent vertices (in anti-clockwise order)
# = 1/2*(det([p1,p2]) + det([p2,p3]) + ... + det([pn,p1])).
# is_convex: A check to determine if the polygon is convex. A polygon is convex if the z component of the cross product is greater than or equal to zero for all the vector pairs formed by consecutive edges (in anti-clockwise direction), i.e, zcross(p[i],p[i+1],p[i+2]) > 0 for all adjacent edges ((p[i],p[i+1]),(p[i+1],p[i+2]))
# The helper fucntions det_2x2, distance and zcross give in the template can be utilized.

# Links for visualization: Polygon Visualization, Z Cross Visualization

# Example

# points = [(2,1),(5,1),(7,3),(4,6),(1,4)]

# perimeter = distance((2,1),(5,1))
#             + ... 
#             + distance((4,6),(1,4)) 
#             + distance((1,4),(2,1))
#           = 3 + 2.83 + 4.24 + 3.61 + 3.16 
#           = 16.84

# minimum values in x and y coordinates are 1 and 1 respectively
# maximum values in x and y coordinates are 7 and 6 respectively

# Thus, bounding_box = ((1,1),(7,6))

# area  = 1/2* (det([(2,1),(5,1)])+...+det([(1,4),(2,1)]))
#       = 1/2 *(-3 + 8 + 30 + 10 + -7)
#       = 38/2 = 19

# zcross values are:
#     zcross((2,1),(5,1),(7,3)) = 6 
#     zcross((5,1),(7,3),(4,6)) = 12
#     zcross((7,3),(4,6),(1,4)) = 15
#     zcross((4,6),(1,4),(2,1)) = 11
#     zcross((1,4),(2,1),(5,1)) = 9

# All values are positive thus convex.

