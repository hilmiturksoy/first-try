from contextlib import contextmanager

@contextmanager
def demonstrate_cm():
    print('Anything before yield is executed at the very beginning')
    yield
    print('Anything after yield is executed at the very end')


with demonstrate_cm():
    for n in range(10):
      print(n, end="\n")