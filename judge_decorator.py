def html_tag(func):

    def wrapper(tag):
        r=func()
        print('<{0}>{1}</{0}>'.format(tag,r))
        func()
    return wrapper

a,b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())
