import numpy as np 

print("Crie um array com 10 elementos usando a função arange")
arr = np.arange(10)
print (arr)

print("Transforme esse array de 1D (1x10) para 2D (2x5) usando a função reshape")
reshaped = arr.reshape(2,5)
print (reshaped)

print("Crie duas matrizes bidimensionais com valores aleatórios")
mat = np.random.randint(10, size=(2, 3))
print (mat)

print("calcule a transposta de cada matriz")
mat_t = mat.transpose()
print (mat_t)

print("multiplique as duas matrizes")
multi_mat = mat.dot(mat_t)
print (multi_mat)

#Salve as matrizes de entrada e a de saída em arquivos. Qual o tamanho dos arquivos gerados?
np.save('mat',mat)
np.save('mat_t',mat_t)
np.save('multi_mat',multi_mat)


#Crie duas bidimensionais matrizes com valores aleatórios e gere uma única matriz combinando linha a linha

print("Crie um vetor nulo de tamanho 10")
nullArray = np.full((10), np.NaN)
print(nullArray)

print("Como encontrar o tamanho da memória de qualquer matriz")
print (multi_mat.nbytes)

print("Crie um vetor nulo de tamanho 10, mas o quinto valor, que é 1")
nullArray[4]=1
print (nullArray)

print("Crie um vetor com valores que variam de 10 a 49")
array_10_49 = np.random.randint(low=10, high=50, size=(20))
print (array_10_49)

print("Inverter um vetor (o primeiro elemento se torna o último)")
array_10_49_inv = array_10_49[::-1]
print (array_10_49_inv)

print("Crie uma matriz 3x3 com valores que variam de 0 a 8one")
matrix_3_3 = np.random.randint(9, size=(3, 3))
print (matrix_3_3)

print("Crie uma matriz de identidade 3x3")
identity = np.identity(3)
print (identity)

print("Crie uma matriz 3x3x3 com valores aleatórios")
img = np.random.randint(255, size=(3, 3, 3))
print (img)

print("Crie uma matriz 10x10 com valores aleatórios e encontre os valores mínimo e máximo")
mat_random = np.random.randint(300, size=(10, 10))
mat_as_array = mat_random.ravel()
print (mat_as_array.max())
print (mat_as_array.min())

print("Crie um vetor aleatório de tamanho 30 e encontre o valor médio")
array = np.random.random(30)
print (array.mean())

print("Crie uma matriz 2D com 1 na borda e 0 dentro")
mat_border = np.ones((5,5))
mat_border[1:-1,1:-1]=0
print (mat_border)

print("Crie uma matriz 5x5 com valores 1,2,3,4 logo abaixo da diagonal")
diag = np.array([1,2,3,4,5])
diag = np.diag(diag)
print (diag)

print("Crie uma matriz estruturada representando uma posição (x, y) e uma cor (r, g, b)")
imagem = np.random.randint(low=1, high=256, size=(720, 480, 3))
print (imagem)

print("Subtrair a média de cada linha de uma matriz")
mat = np.random.randint(10, size=(2, 3))


medias = mat.mean(axis=1)
medias = medias.reshape(-1,1)
print (mat)
print (mat - medias*np.ones((2,3)))
#print (mat - mat.mean(axis=1))


print ("Como encontrar o valor mais frequente em uma matriz?")
mat_random = np.random.randint(300, size=(10, 10))
reshaped = mat_random.ravel()

counts = np.bincount(reshaped)
max_value =  np.argmax(counts)
print (max_value)

print ("Crie uma matriz a partir de um arquivo")
matriz_loaded = np.load('mat.npy')
print (matriz_loaded)

print ("crie uma matriz com valores aletaórios e salve para um arquivo")
mat_random = np.random.randint(300, size=(10, 10))
np.save('mat_random',mat_random)