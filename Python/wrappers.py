def on_error(error_msg):
    def test_fun_decorator(test_fun):
        def fun_wrapper(var):
            try:
                test_fun(var)
            except Exception as e:
                print(e)
                print(error_msg)
        return fun_wrapper
    return test_fun_decorator


@on_error("Error message")
def test(var1):
    print("test")
    print(var1)
    raise Exception("test_exception")


if __name__ == '__main__':
    test("variable")

# Result:
#
# test
# variable
# test_exception
# Error message
