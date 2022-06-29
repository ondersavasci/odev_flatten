l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lnew = []

def flatten(x):
    for i in x:
        if isinstance(i, list):
            flatten(i)
        else: 
            lnew.append(i)

flatten(l)
print(lnew)
