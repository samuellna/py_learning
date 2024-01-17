def three_numbers_sum(x, y = None, z = None): # OBS: If some function arg. have a default value, all next arg. gotta have it too!
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


three_numbers_sum(1, 2)
three_numbers_sum(3, 5)
three_numbers_sum(100, 200)
three_numbers_sum(7, 9, 0)
three_numbers_sum(y=9, z=0, x=7)