def sim(Q,D):
    print("Panjang Q: ",vectorLength(Q))
    print("Panjang D: ",vectorLength(D))
    print("Dot product: ",dotProduct(Q,D))
    return dotProduct(Q,D)/(vectorLength(Q)*vectorLength(D))

def vectorLength(Z):
    return sum(Z[keys]**2 for keys in Z)**(1/2)

def dotProduct(Q,D):
    return sum(Q[keys]*D[keys] for keys in Q)