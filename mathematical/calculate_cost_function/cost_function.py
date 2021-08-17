def calculate_cost_func(h_x:callable, x, y, theta:tuple):
    """
    pass x, y values and h_x function, to calculate the cost function, provided (theta0, theta1).
    """
    sum_m = 0
    m = min(len(x), len(y))
    for x_i, y_i in zip(x, y):
        sum_m += (h_x(x_i) - y_i)**2
    
    cost_function_value = sum_m / (2*m)
    print(f"Cost function values at {theta}: {cost_function_value}")

    return cost_function_value

if __name__ == '__main__':
    x_values, y_values = [6,5,10,3], [7,4,9,4]
    th0, th1 = 2,1
    calculate_cost_func(lambda x: th0+th1*x, x_values, y_values, (th0, th1))


