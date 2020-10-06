# Top package has to be globally unique because Python does not merge same
# modules from different libraries.

def calc(a, b):
    return a * b - a - b
