# Enter your code here. Read input from STDIN. Print output to STDOUT
def mean(x):
    #print x
    return sum(x) / len(x)

def linearRegression(x,y,xx):
    x_diff = [x[i] - mean(x) for i in range(len(x))]
    y_diff = [y[i] - mean(y) for i in range(len(y))]
    
    x_diff2 = [x_diff[i]**2 for i in range(len(x_diff))]
    y_diff2 = [y_diff[i]**2 for i in range(len(y_diff))]
    
    x_y_diff = [x_diff[i]*y_diff[i] for i in range(len(x_diff))]
    
    b_1 = sum(x_y_diff) / sum(x_diff2)
    b_0 = mean(y) - b_1*mean(x)
    #print b_1,b_0
    #print round(b_1,3)
    print b_1,b_0,xx
    print '%.1f' % (b_1*xx+b_0)
    
x = [95,85,80,70,60]
y = [85,95,70,65,70]
x = [float(x[i]) for i in range(len(x))]
y = [float(y[i]) for i in range(len(y))]
linearRegression(x,y,80)