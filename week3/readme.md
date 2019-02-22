### Questions: 

**Functions/decorators/scopes**
1. What is the scopes? For what LEGB stands for?
2. What is `nonlocal` and `global`?
3. Provide some examples of decorators.
4. (*) For which purpose can we use `@functools.wraps(func)`, `@functools.singledispatch`
5. What does this mean: `*args, **kwargs`? And why would we use it?


**Generators (and recall of iterators)**
1. What is the relation between generator and iterator? 
2. How `yield` statement works? 
3. Why generators used in python? What are their advantages? 


**Recall (data types, structures, iterators)**
1. What objects can we pass as a dict key?
2. What template should iterator implement?
3. Does Python have build-in method for creation of iterator?
4. How are arguments are passed to the functions - by reference of by value?
5. What are negative indexes and why are they used?
6. What is the difference between `__repr__` and `__str__`? 

### Useful links: 

**Functions/decorators/scopes**
1. Functions, scopes, functional programming (ipython notebook): https://github.com/Tobichimaru/Python/blob/master/Functions%2C%20Scopes%2C%20Functional%20Programming.ipynb
2. Decorators, functools (ipython notebook): https://github.com/Tobichimaru/Python/blob/master/Decorators.ipynb
3. Decorators (theory): https://www.programiz.com/python-programming/decorator

**Generators (and recall of iterators)**
1. Generators and iterators (theory): https://www.programiz.com/python-programming/generator
2. Iterators (theory): https://www.programiz.com/python-programming/iterator

### Tasks:
1. Re-write iterators of a binary tree from the 2nd week assigment to use generators. 
2. Write decorator which will measure the execution time of a function.
3. Write a fucntion to which you can pass any number of arguments. 
   This function should return the sum of the arguments if all arguments can be casted to the integer type. Implement a decorator that will validate arguments. 
