def find_element(name, index, args, kwargs):
    if name in kwargs:
        return kwargs[name]
    return args[index]


def validate_username(foo):
    def inner(*args, **kwargs):
        username = find_element('username', 0, args, kwargs)
        if username.lower() not in ("admin", "root", "user") and 5<=len(username)<=20:
            for i in username:
                if not i.isalnum():
                    break
            else:
                return foo(*args, **kwargs)
        print("username in Note valid")
        return
    return inner

def validate_email(foo):
    def inner(*args, **kwargs):
        email = find_element('email', 1, args, kwargs)
        if email and email.find(' ')==-1:
            x = email.split('@')
            if len(x)==2 and not x[0].isdigit():
                x=x[1].split('.')
                if len(x)==2:
                    return foo(*args, **kwargs)
        print("email is Not valid")
        return
    return inner

def validate_phone(foo):
    def inner(*args, **kwargs):
        phone = find_element('phone', 2, args, kwargs)
        if ( len(phone)== 12 and phone[0:4]=='+374') or (len(phone)==9 and phone[0]=='0'):
                return foo(*args,**kwargs)
        print("phone number is Not Valid")
        return
    return inner

def validate_pass(foo):
    def inner(*args, **kwargs):
        password = find_element('password', 3, args, kwargs)
        if len(password)>=8:
            upper = False
            lower = False
            digit = False
            i=0
            while i<len(password) and not upper or not digit or not lower:
                if password[i].isupper():
                    upper=True
                elif password[i].islower():
                    lower=True
                elif password[i].isdigit():
                    digit=True
                i+=1
            if upper and lower and digit:
                return foo(*args, **kwargs)
        print("password is Not Valid")
        return 
    return inner

def validate_re_pass(foo):
    def inner(*args, **kwargs):
        password = find_element('password', 3, args, kwargs)
        re_pass = find_element('re_pass', 4, args, kwargs)
        if password==re_pass:
            return foo(*args, **kwargs)
        print("wrong repeat Not Valid")
        return
    return inner


        
@validate_username
@validate_email
@validate_phone
@validate_pass
@validate_re_pass
def foo(username, email, phone, password, re_pass):
    print("You've got it!!!")


foo( email = 'a1@gmail.com', username =  'Angela', phone = '096456789',password = 'AAAaaa111', re_pass = 'AAAaaa111' )
foo('Angela', 'a1@gmail.com', '096123456', 'AAAaaa111', 'AAAaaa111')
