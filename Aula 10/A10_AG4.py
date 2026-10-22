def funcao_X(y):
    if(len(y) <= 1):
        return y
    
    return y[-1] + funcao_X(y[:-1])

print(funcao_X("Python"))