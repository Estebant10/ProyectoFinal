# Estructura de Datos
# Esteban Tabares Londoño.

print("\n#####################################################")
print("##             ALGORITMO DE HUFFMAN                ##")
print("#####################################################")

Names = []
for line in open('Pruebatexto.txt', 'r').readlines():
    Names.append(line.strip())

my_string = Names
len_my_string = len(my_string)

print("Su Mensaje Es:")
print(my_string)
print("\nSus Datos Tienen Una Longitud De: ", len_my_string * 7, "Bits")

# Crea una lista de caracteres y la frecuencia de aparicion de cada uno
letters = []
only_letters = []

# Ciclo calcula la frecuencia con la que se repite un caracter
for letter in my_string:
    if letter not in letters:
        freq = my_string.count(letter)
        letters.append(freq)
        letters.append(letter)
        only_letters.append(letter)

# Genera la base de level para la frecuencia del arbol de Huffman
nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)

# Combina los nodos para crear el Arbol de Huffman y asigna un 1 o 0 dependiendo del string


def combine(nodes):
    pos = 0
    newnode = []

    if len(nodes) > 1:
        nodes.sort()
        # Agrega el 1 o 0
        nodes[pos].append("0")
        nodes[pos+1].append("1")
        combined_node1 = (nodes[pos][0]+nodes[pos+1][0])
        combined_node2 = (nodes[pos][1]+nodes[pos+1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes = []
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine(nodes)
    return huffman_tree


newnodes = combine(nodes)

# Hace que el árbol empiece descendientemente
huffman_tree.sort(reverse=True)
print("\nArbol De Huffman Con La Combinación De Nodos:")

# Visualización
checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)

count = 0
for level in huffman_tree:
    print("level", count, ":", level)
    count += 1
print()

# Construye el código binario para cada caracter
letter_binary = []
if len(only_letters) == 1:
    letter_code = [only_letters[0], "0"]
    letter_binary.append(letter_code*len(my_string))
else:
    for letter in only_letters:
        lettercode = ""
        for node in checklist:
            if len(node) > 2 and letter in node[1]:
                lettercode = lettercode + node[2]
        letter_code = [letter, lettercode]
        letter_binary.append(letter_code)

# Letras con el código binario
print("Sus Codigos En Binario Son Los Siguientes:")
for letter in letter_binary:
    print(letter[0], letter[1])

# Crea una secuencia de bits con los nuevos códigos
bitstring = ""
for character in my_string:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]

# Convierte el string a un número binario
binary = (bin(int(bitstring, base=2)))

# Resumen de compresión de datos
uncompressed_file_size = len(my_string) * 7
compressed_file_size = len(binary) - 2
print("\nSu Archivo Original Era De", uncompressed_file_size,
      "Bits. El Archivo Comprimido Es De", compressed_file_size, "Bits.")

# Datos comprimidos en una cadena de dígitos binarios
print("\nSu Mensaje En Binario Es:")
print(binary)

# Generar archivo comprimido
data = [binary]
fic = open("Pruebatexto.txt", "w")
for line in data:
    fic.write(line)
    fic.write("\n")

fic.close()


####################################

# Decodificación
# Utiliza el arreglo letter_binary para conseguir cada código
# Convierte de binario a un string

bitstring = str(binary[2:])  # El str inicia con el resto de la matriz
uncompressed_string = ""
code = ""
for digit in bitstring:
    code = code+digit
    pos = 0
    for letter in letter_binary:
        if code == letter[1]:
            uncompressed_string = uncompressed_string+letter_binary[pos][0]
            code = ""
        pos += 1

print("Su Archivo Decodificado Es:")
print(uncompressed_string)

# Generar archivo descomprimido
data = [uncompressed_string]
fic = open("Pruebatexto_descomprimido.txt", "w")
for line in data:
    fic.write(line)
    fic.write("\n")

fic.close()
