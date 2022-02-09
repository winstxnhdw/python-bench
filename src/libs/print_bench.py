def print_bench(names, outputs):

    for name, output in zip(names, outputs):
        print(f"\n{name.capitalize()} test:\n{output}")