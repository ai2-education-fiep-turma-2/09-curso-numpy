import numpy as np
array = np.arange(0,10,1)
print("\n\n 1.")
print(array)

array_2d = np.reshape(array,(2,5))
print("\n\n 2.")
print(array_2d)

random_matrix_1 = np.random.randint(0,100,(2,5))
random_matrix_2 = np.random.randint(0,100,(2,5))
print("\n\n 3.")
print(random_matrix_1, random_matrix_2)

trans_1 = np.transpose(random_matrix_1)
trans_2 = np.transpose(random_matrix_2)
print("\n\n 4.")
print(trans_1, trans_2)

mult = np.multiply(trans_1, trans_2)
print("\n\n 5.")
print(mult)

#416 bytes
with open('test.npy', 'wb') as f:
    np.save(f, trans_1)
    np.save(f, trans_2)
    
#208 bytes
with open('test_transpose.npy', 'wb') as f:
    np.save(f, mult)
    
conc_random = np.concatenate((random_matrix_1, random_matrix_2))
print("\n\n 7.")
print(conc_random)

null_array = np.empty((1,10))
null_array[:] = np.NaN
print("\n\n 8.")
print(null_array)


print("\n\n 9.")
print(str(null_array.size * null_array.itemsize)+ "bytes")

null_array[0][4] = 1
print("\n\n 10.")
print(null_array)

random_matrix_10_49 = np.random.randint(10,49,(1,10))
print("\n\n 11.")
print(random_matrix_10_49)

inverted_rdn_10_49 = np.flip(random_matrix_10_49)
print("\n\n 12.")
print(inverted_rdn_10_49)

rdn_08_33 = np.random.randint(0,8,(3,3))
print("\n\n 13.")
print(rdn_08_33)
      
identity_33 = np.identity(3)
print("\n\n 14.")
print(identity_33)

rdn_333 = np.random.randint(0,100,(3,3,3))
print("\n\n 15.")
print(rdn_333)

rdn_1010 = np.random.randint(0,100,(10,10))
print("\n\n 16.")
print(rdn_1010)
print("Máximo: "+ str(np.max(rdn_1010)))
print("\n Mínimo: " + str(np.min(rdn_1010)))

rdn_30 = np.random.randint(0,100,(1,30))
print("\n\n 17.")
print(rdn_30)
print("Médiano: "+ str(np.mean(rdn_30)))

array_zero_inside = np.random.randint(1,2,(10,10))
array_zero_inside[1:-1,1:-1] = 0
print("\n\n 18.")
print(array_zero_inside)

print("\n\n 19.")
array_diag = np.mgrid[1:6:1]
print(np.tril(array_diag,-1))

rdn_image = np.random.randint(0,100,(3,10,10))
print("\n\n 20.")
print(rdn_image)

print("\n\n 21.")
print(str(np.subtract(np.tril(array_diag,-1), array_diag.mean())))


array_freq = np.array([10,10,10,28,28,28,28,28,3,4,2,1])
cont = np.bincount(array_freq)
print("\n\n 22.")
print(array_freq)
print("Mais frequente: "+str(np.argmax(cont)))

loaded_matrix = np.loadtxt('matrix.txt', usecols=range(7))
print("\n\n 23.")
print(loaded_matrix)


print("\n\n 24.")
with open('output.txt','wb') as f:
    np.savetxt(f, loaded_matrix, fmt='%.f')
print("Concluído")