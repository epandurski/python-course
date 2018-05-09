from mypackage import fibonacci

# Now `fib1` and `fib2` are accessible through `fibonacci`.
print(fibonacci.fib1)
print(fibonacci.fib2)



from mypackage.fibonacci import fib1
from mypackage.fibonacci import fib2 as fib_two

# Now can access `fib1` directly, `fib2` is accessible here as `fib_two`.
fib1(10)
fib_two(10)
assert fibonacci.fib1 is fib1
assert fibonacci.fib2 is fib_two



from mypackage import tools

# Now can access `tools` directly, as well.
tools.get_integer()
