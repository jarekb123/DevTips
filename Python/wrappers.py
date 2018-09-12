def on_error(error_msg):
    def test_fun_decorator(test_fun):
        def fun_wrapper():
            try:
                test_fun()
            except Exception as e:
                print(e)
                print(error_msg)
        return fun_wrapper
    return test_fun_decorator


@on_error("Error message")
def test():
    print("test")
    raise Exception("test_exception")


if __name__ == '__main__':
    test()

# Result:
#
# test
# test_exception
# Error message
