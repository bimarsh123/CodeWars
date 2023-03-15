def reverseStrimg(text):
    a=text.split(' ')
    p=[]
    for i in a:
        p.append(i[::-1])
    return (' '.join(p))
