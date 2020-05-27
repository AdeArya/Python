def example(test,*args, **kwargs):
    
    # is a normal string
    print(test, '>>>',type(test))
    print('')

    # args is a tuple
    if args:
        print(args, '>>>',type(args))
        print('')
    
    # kwargs is a dictionary
    if kwargs:
        print(kwargs, '>>>',type(kwargs))
        print('')

example('ade',1,2,3,'ade',name = 'ade', age = 18)