

def test_function(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


if __name__ == "__main__":
    test_function(1, 2, 3, 4, 5, kwarg1=6, kwarg2=7)


'''
Output:
    arg1: 1
    arg2: 2
    args: (3, 4, 5)
    kwargs: {'kwarg1': 6, 'kwarg2': 7}


The *args syntax is used to specify a variable-length list of arguments to a function. In this example, the args parameter is a tuple 
    containing all of the additional positional arguments passed to the function (in this case, (3, 4, 5)).

The **kwargs syntax is used to specify a variable-length list of keyword arguments to a function. In this example, the kwargs parameter is a 
    dictionary containing all of the additional keyword arguments passed to the function (in this case, {'kwarg1': 6, 'kwarg2': 7}).

The *args and **kwargs syntax can be useful when you want to write a function that can accept a variable number of arguments or keyword arguments. 
They can also be useful when you want to pass a list or dictionary of arguments to a function using the * and ** operators.

'''