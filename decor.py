def decorator_maker(*args):

    print "Decorator maker. Called once when decorator creates with arg"

    def my_decorator(func):

        print "Decorator called when decorating function"

        def wrapped():
            for i in range(0, *args):
                print func()
            return func

        print "Decorated function return."

        return wrapped

    print "Decorator return"
    return my_decorator

@decorator_maker(5)
def function_to_decorate():
    print "Simple function text"

function_to_decorate()