
### Questions:

1. What is GIL? Why it is implemented in python? 
2. What is the difference between thread and process? 
3. How garbage collection works? 

### Materials: 

1. (ipython) https://github.com/Tobichimaru/Python/blob/master/GIL%2C%20GC.ipynb
2. Garbage collection:
	* https://asvetlov.blogspot.com/2013/05/gc.html
	* https://habr.com/ru/post/417215/
3. GIL: 
    * https://habr.com/ru/post/84629/
    * https://habr.com/ru/post/417215/
4. Threading vs multiprocessing: 
	* https://medium.com/practo-engineering/threading-vs-multiprocessing-in-python-7b57f224eadb

### Tasks

1. Suppose you have two methods that generate odd and even numbers. Your task is to output
a range of numbers from 1 to 100 sequentially using these two methods.
2. Solve the task about [dining philosophers problem](https://ru.wikipedia.org/wiki/Задача_об_обедающих_философах). 
The essence of the problem is to develop a model of behavior (parallel algorithm), in which none of the philosophers will starve, that is, will always alternate food intake and reflection (the philosopher must begin with thinking).
Take a look into the interface given in this week module. Feel free to implement a new class that implement a `Fork` or `Philosopher` class.
