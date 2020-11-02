# Reflection by Add Your Name Here

## Using fenced code blocks, please display the output from running your program with different files

TODO: Please furnish three fenced code blocks showing the output of your program

## Please use the previous program output to explain which Python function is the fastest

TODO: Use your results to explain which Python function is the fastest and why

## What is the purpose of the command `poetry run csvfaker --rows 5 email job`?

TODO: Explain the input, output, and behavior of the aforementioned command

## Explain in detail the purpose of the following two Python functions

```
def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    return len(list_start) - len(list_final)


def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    reduction = calculate_reduction(list_start, list_final)
    percent_reduction = (reduction / len(list_start)) * 100
    return percent_reduction
```

TODO: Explain how these Python functions help you run experiments. What do they do?

## Explain in detail the purpose of the following Python function

```
def timing(function):
    """Define a profiling function for execution time."""
    @wraps(function)
    def wrap(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print("The function %r took: %2.4f sec" % (function.__name__, te - ts))
        return result

    return wrap
```

TODO: Explain how this Python function supports the execution time experiments.

## What was the most confusing concept in this assignment? What did you do to ultimately understand it?

TODO: Please provide a response to this question.

## After this and a previous assignment, what do you think is the purpose of running experiments?

TODO: Please provide a response to this question.

## Explain how a technical concept in this assignment is connected to a topic in a different assignment

TODO: Please provide a response to this question.

## At your own option, do you have any other insights to share about this assignment?

If you would like to do so, please provide insights about this assignment.
