
### Questions:

Closures:
1. What is the result of this code?
```
def create_multipliers():
    return [lambda x : i * x for i in range(5)]


for multiplier in create_multipliers():
    print(multiplier(2))    
```
2. What do you know about closures? 

Context managers
1. What is context managers? What they are used for? 

Exceptions: 
1. When `finally` block is executed? 
2. Why it is bad practice to use bare `except` clause? 
```
except:  # bare except
    ...
```

### Materials: 

Topics: 
* Context managers
* Contextlib
* Closures
* Functors
* Recall of LEGB scopes
* Exceptions


Overview:
1. (ipython): https://github.com/Tobichimaru/Python/blob/master/Сontext%20managers%2C%20Closures%2C%20Functors%2C%20Imports.ipynb

Closures: 
1. Closures : http://ballingt.com/python-closures/
2. Another article on closures: https://www.geeksforgeeks.org/python-closures/

Context managers:
1. With statements: https://docs.python.org/3/reference/compound_stmts.html#with
2. Context manager type definition: https://docs.python.org/3/library/stdtypes.html#typecontextmanager
3. Context managers and contextlib: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

Additional more advanced materials 
1. contextlib: https://docs.python.org/3/library/contextlib.html


Exceptions:
1. (theory): https://docs.python.org/3/library/exceptions.html
2. (ipython): https://github.com/Tobichimaru/Python/blob/master/Exceptions.ipynb



### Tasks
1. Define a decorator `person_listener` that will format and sort in a way defined below passed list of tuples of people data. 

Tuple with a person data is defined as (FullName, Age, Sex['M' or 'F']). For example, 
`("John Smith", 20, "M")`, `("Jane Brown", 16, "F")`. 

Print people names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

The data should be read from files `input.txt`. The output should be written into `output.txt`. Use context manageres to work with I/O files. 

```
def person_lister(f):
    def inner(people):
        # complete the function
    return inner


@person_lister
def name_format(person):
    # complete the function


if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print('\n'.join(name_format(people)))
```

Sample input
```
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
```

Sample output
```
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
```

2. Define a functor `strip_characters` that will accept the string of chars. This functor should remove these chars from the string passed to the functor. 

Example of usage:
```
strip_punctuations = strip_characters(',;:.?!')
s = 'Please, strip punctuations from this string!'
print(strip_punctuations(s))
# ourput: "Please strip punctuations from this string"
```

3. Define a context manager `InfoLogger`, which will open a file `logs-info.txt`, write logs in it (e.g. called `logger.log('Some log')`), and closes the files and resources when exiting a context. 

4. Define a context manager that will measure exection time of enclosed code. Make use of [timeit](https://docs.python.org/3/library/timeit.html) lib.  
