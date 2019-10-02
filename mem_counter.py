import sys

def show_size(x, y):
    # print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    spam_y = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                spam_y += show_size(key, spam_y)
                spam_y += show_size(value, spam_y)
        elif not isinstance(x, str):
            for item in x:
                spam_y += show_size(item,spam_y)

    return spam_y
