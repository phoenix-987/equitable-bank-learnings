import fire

def hello(name='Jake'):
    return f'Hi bro {name}. How you doin?'

if __name__ == '__main__':
    fire.Fire(hello)