# Fungsi ini memiliki 2 parameter yaitu dictionary Q dan D yang
# merepresentasikan vektor query dan vektor dokumen dan menghasilkan
# similaritas dari rumus cos-sin similarity
def sim(Q, D):
    return dotProduct(Q, D)/(vectorLength(Q)*vectorLength(D))
# fungsi ini digunakan untuk mengembalikan panjang vektor


def vectorLength(Z):
    return sum(Z[keys]**2 for keys in Z)**(1/2)
# fungsi ini digunakan untuk menghitung dot product dari Q dan D berdasarkan keys


def dotProduct(Q, D):
    return sum(Q[keys]*D[keys] for keys in Q)
