from string import capwords

def print_bench(names, outputs):

    for name, output in zip(names, outputs):
        print(f"\n{capwords(name)} test:\n{output}")