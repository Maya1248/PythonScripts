import matplotlib.pyplot as plt

def lerp(a,b,t):
    return a*(1-t) + b*t

def lerp2D(A,B,t):
    x1 = A[0]
    y1 = A[1]

    x2 = B[0]
    y2 = B[1]
    
    x = lerp(x1,x2,t)
    y = lerp(y1,y2,t)

    return (x,y)

def lerp2Darray(A,B,f):
    lerp_arr = []
    for i in range(f+1):
        t = i/10
        lerp_arr.append(lerp2D(A,B,t))

    return lerp_arr

def lerp2D3point_bezier(A,B,C,f):
    a = lerp2Darray(A,B,f)
    b = lerp2Darray(B,C,f)

    bezier = []
    for i in range(f+1):
        t = i/10
        bezier.append(lerp2D(a[i], b[i], t))

    return bezier

def plotify(bezier):
    x = []
    y = []
    for coord in bezier:
        x.append(coord[0])
        y.append(coord[1])

    return x,y


def generate(point_A, point_B, point_C):
    A = point_A
    B = point_B
    C = point_C
    f = 10 # immutable sharpness; awaiting update, do not change as of now

    bezier = lerp2D3point_bezier(A,B,C,f)
    x,y = plotify(bezier)

    plt.plot(x,y)
    plt.show()


if __name__ == "__main__":
    print("Point A")
    x = float(input("X: "))
    y = float(input("Y: "))
    point_A = (x,y)
    print("-"*10)

    print("Point B")
    x = float(input("X: "))
    y = float(input("Y: "))
    point_B = (x,y)
    print("-"*10)

    print("Point C")
    x = float(input("X: "))
    y = float(input("Y: "))
    point_C = (x,y)
    print("-"*10)

    generate(point_A,point_B,point_C)


    
