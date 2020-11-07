def sim(Q,D):
    return dotProduct(Q,D)/(vectorLength(Q)*vectorLength(D))

def vectorLength(Z):
    return sum(i**2 for i in Z)**(1/2)

def dotProduct(Q,D):
    return sum(Qi*Di for Qi, Di in zip(Q, D))

print(sim([0,0,2],[2,3,5]))