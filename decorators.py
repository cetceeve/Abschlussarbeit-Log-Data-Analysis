# decorators to simplify data traversal
# exec on all data
def exec_all(log_data):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if (wrapper.flat_list == None):
                print('converting')
                all_arr = log_data.values()
                wrapper.flat_list = [item for sublist in all_arr for item in sublist]
            return func(wrapper.flat_list, *args, **kwargs)
        wrapper.flat_list = None
        return wrapper
    return decorator

# exec function for every user
def exec_per_user(log_data, user_arr):
    def decorator(func):
        def wrapper(*args, **kwargs):
             return [func(log_data[user], *args, **kwargs) for user in user_arr]
        return wrapper
    return decorator
