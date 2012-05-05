# Utilities

def memoize(func):
    """Simple memoizing decorator."""
    cache = {}

    def apply(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return apply

