
A,B,C=10,20,30
X,Y,Z,E=40,50,60,70
J,K,I,O=80,90,100,110


l = [(A, B, C), (X, Y, Z, E), (1, 2, 4), (J, K, I, O)]

# Extracting the third element from each tuple
result = [t[2] for t in l if len(t) > 2]

print(result)
