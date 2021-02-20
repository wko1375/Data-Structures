#question 3a
def print_triangle(n):
    if n == 1:
        print("*" * n)
    if n <= 0:
        print()
    else:
        print_triangle(n-1)
        print("*" * n)

def print_triangle_right(n):
    if n == 1:
        print("*")
    if n <= 0:
        print()
    else:
        print("*" * n)
        print_triangle_right(n-1)


#question 3b
def print_opposite_triangles(n):
    if n <= 0:
        print()
    elif n == 1:
        print("*")
        print("*")
    else:
        print("*" * n)
        print_opposite_triangles(n-1)
        print("*" * n)

#question 3c
def print_ruler(n):
    if n == 0:
        
