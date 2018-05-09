import mymodule

# Now `get_integer`, `ask_for_devils_number`, and `DEVILS_NUMBER` are
# accessible through `mymodule`.
print(mymodule.get_integer)
print(mymodule.ask_for_devils_number)
print(mymodule.DEVILS_NUMBER)



from mymodule import get_integer, ask_for_devils_number
from mymodule import DEVILS_NUMBER as NICE_NUMBER

# Now we can access `get_integer` and `ask_for_devils_number`
# directly, `DEVILS_NUMBER` is accessible as `NICE_NUMBER`.
get_integer()
ask_for_devils_number()
assert mymodule.get_integer is get_integer
assert mymodule.ask_for_devils_number is ask_for_devils_number
assert mymodule.DEVILS_NUMBER is NICE_NUMBER
