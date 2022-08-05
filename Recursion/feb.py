from xml.sax.handler import feature_validation
sum=0
def fvo(a):
    if a<2:
        return a
    return fvo(a-1)+fvo(a-2)

print(fvo(4))

