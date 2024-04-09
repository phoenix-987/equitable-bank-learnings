import fire

def hello(name='Jake'):
    return f'Good Afternoon {name}, How are you?'

if __name__ == '__main__':
    fire.Fire(hello)