# Lab: Stack and Queue

## Overview

In this lab you will be completing two stack applications, and completing the implementation of a circular, array-backed queue.


## Stack applications

The first two exercises ask you to use the stack data structure developed in class to develop two distinct stack-driven applications.

The completed stack implementation can be found in `stack.py`. It is merely included for reference --- *you should not modify this implementation* to complete these exercises.

### 1. Paired delimiter matching

In class we wrote a function that uses a stack to determine whether opening and closing parentheses in a given string are correctly matched.

For this exercise you will extend the implementation to accept a dictionary mapping opening to closing delimiters (with the caveat that all delimiters are one-character strings). 

E.g., the following calls should return `True`:

    check_delimiters('((() ()))', {'(':')'})

    check_delimiters('[ <> () [() ()] ]', {'(':')', '<':'>', '[':']'})

    check_delimiters('("bob", "ma", "ry", ("tom"))', {'(': ')', '"': '"'})

E.g., the following calls should return `False`

    check_delimiters('([a b)]', {'(':')', '[':']'})

    check_delimiters('("hi "( ") there")', {'(':')', '"':'"'})

Note that there may be delimiters used in the string that are not in the dictionary. These should be ignored. 

It is also possible that a pair of opening and closing delimiters use the same character (e.g., `'"'` and `'"'`), in which case *they cannot be nested*. I.e., if you encounter a delimiter of this type and it is already on the stack, you should pop it off the stack rather than push another one on.

E.g., while the following call should return `False` (because the brackets, which nest, are not correctly matched):

    check_delimiters('( [ [ ) ( ] ] )', {'(':')', '[':']'})

the following call should return `False` (because the double quotes do not nest):

    check_delimiters('( " " ) ( " " )', {'(':')', '"':'"'})

 Your implementation will go into the `check_delimiters` function in `stack_apps.py`.


### 2. Infix &rarr; Postfix conversion

Another function we examined in class was one that used a stack to evaluate a postfix arithmetic expression. Because most of us are more accustomed to infix-form arithmetic expressions (e.g., `'2 * (3 + 4)'`), however, the function seems to be of limited use. The good news: we can use a stack to convert an infix expression to postfix form!

To do so, we will use the following algorithm:

1. Start with an empty list $L$ and an empty stack $S$. At the end of the algorithm, $L$ will contain the correctly ordered tokens of the postfix expression.

2. For each white-space separated token $T$ in the infix expression, carry out the first of the following rules that applies:

    - If $T$ is a number, simply append it to $L$.

    - If $S$ is empty or the top of $S$ is a left parenthesis, push $T$ onto $S$.

    - If $T$ is a left parenthesis, push it onto $S$.

    - If $T$ is a right parenthesis, keep popping values from $S$ and appending them to $L$ until a left parenthesis is popped from $S$. Note that the parentheses themselves are not appended to $L$.

    - If $T$ has higher precedence than the top of $S$ (or if the top of $S$ is a left parenthesis), push it onto $S$. 

    - If $T$ has equal precedence with the top of $S$, pop $S$ and append the popped value to $L$, then push $T$ onto $S$.

    - If $T$ has lower precedence than the top of $S$, pop $S$ and append the popped value to $L$. Then repeat these last three tests against the new top of $S$.

3. After arriving at the end of the expression, pop and append all operators on $S$ to $L$.

For your implementation, you will only need to handle the operators `+`, `-`, `*`, and `/`, where the first two have lower precedence than the second two. Assume that all expressions are well-formed (i.e., valid).

Another writeup containing a detailed explanation of the steps above (though it prints the tokens immediately rather than adding them to a list) can be found at http://csis.pace.edu/~wolf/CS122/infix-postfix.htm

Your implementation will go into the `infix_to_postfix` function in `stack_apps.py`.

## Circular, array-backed queue

In class we started to build a queue that makes use of a fixed-size array to store its elements, and whose `head` and `tail` indices "wrap around" when they reach the end of the array (using modular arithmetic).

For this exercise you will complete this implementation so that it properly detects when it is full (in which case it should raise a `RuntimeError` when `enqueue` is called), and so that it can be resized when necessary (using the `resize` method). You will also implement an `__iter__` method that allows the queue to be iterated over from front (head) to back (tail).

The starter code can be found in class `Queue`, found in the file `circ_queue.py`. You should not modify the `__init__` method, and your implementation should ensure that when dequeuing an item, its slot in the array is reset to `None`, and that when the queue is emptied its `head` and `tail` attributes are reset to `-1`.

Assume that `resize` will only be called with a value greater than the current length of the underlying array. Note that the underlying data container is a `numpy` array --- when you resize the queue, you should create a new `numpy` array of the appropriate size and copy the existing elements over to it.
