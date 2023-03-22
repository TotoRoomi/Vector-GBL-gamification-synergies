'''
matrix[][] -> graf x axel och y axel 
       0 -> a   -a -> a 
                 y
                 |
                 |
       ---------- ---------- x
                 |
                 |
'''


def index_finder(graph_point,axis_scale):
    '''
    param graph_point: a point on the visual graph going from -axis_scale to axis_scale on both
    the x axis and the y axis.
    The function converts that graph points position into the index of a matrix starting from
    0 to axis_scale*2
    e.g. : if axis_scale = 10 then origo would correspond to Matrix[10][10]. 
    '''
    index = graph_point+axis_scale
    return index

def main():
    print("What is your axis scale: ")
    axis_scale = int(input())
    x_min = axis_scale*(-1)
    x_max = axis_scale
    y_min = axis_scale*(-1)
    y_max = axis_scale
    print("your x min, max and y min max are",x_min," ",x_max," ", y_min, " ", y_max)
    while(True):
        print("Enter a graph point: ")
        num = int(input())
        print(index_finder(num,axis_scale))

if __name__ == "__main__":
    main()
