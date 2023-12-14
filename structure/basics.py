print("hello")

some_var = "foo"

print(f"This is an interpolated string with the value [{some_var}]")

person = {'name': "bob",
          'age': 42,
          'address': {
              'house': "Foobar",
              'town': "Nowhere"
          }}

print(f"The persons age is: {person['age']}")
print(f"persons house is: {person['address']['house']}")


def say_hello(p_person):
    print(f"Hello from '{p_person}'")


say_hello("alice")

say_hello(p_person="charlie")
