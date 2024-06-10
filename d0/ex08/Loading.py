def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_length = 80
    for i, item in enumerate(lst):
        yield item
        frac = (i+1) / total
        arrow = int(frac * bar_length - 1) * '=' + '>'
        padding = int(bar_length - len(arrow)) * ' '
        en = '\n' if i+1 == total else '\r'
        print(f"{int(frac*100)}%|[{arrow}{padding}]| {i+1}/{total}", end=en)
