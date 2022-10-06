st = 'йцу1'
n_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
try:
    print(list(filter(lambda tuple: tuple[0] == st, zip(n_list, range(len(n_list)))))[1][1])
except IndexError:
    print(-1)