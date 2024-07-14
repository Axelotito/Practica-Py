file = open("example.txt", "w")

file.write("Hello World\n")
file.write("This is our new text file\n")
file.write("Hola que tal\n")

file2 = open(".\Codedex\Python_intermediate\Example_file_reader.txt", "w")

lines = ["hola esto", "\nes una", "\nlinea nueva"]
file2.writelines(lines)
file2.close()

file2 = open(".\Codedex\Python_intermediate\Example_file_reader.txt", "r")
print("using read() method: ")
content = file2.read()
print(content)
file2.close()

""" 
Esto que se hace con with es para que no tengas que colocar el close()
al final del archivo, ya que con with se cierra automaticamente 
"""

with open(".\Codedex\Python_intermediate\Example_file_reader.txt", "w") as file3:
    file3.write("Esto est un texto que va a modificar el archivo")

with open(".\Codedex\Python_intermediate\Example_file_reader.txt", "r") as file3:
    content = file3.read()
    print(content)

""" Activity: make a list of songs and write them in a file """

liked_songs = [
    {"title": "Minero", "artist": "ElRubiusOMG"},
    {"title": "TheLonliest", "artist": "Maneskin"},
]


def write_songs(liked_Song, file_name):
    with open(file_name, "w") as file:
        file.write("Liked songs:\n")
        for number,songs in enumerate(liked_Song, start = 1):
            #enumerate()es usado para conseguir el idex del elemento
            #numero es el indice y songs en la lista de liked_songs
            #para el metodo enumerate() se tienen que poner dos variables antes
            #la primera para el indice y la segunda para los elementos
            file.write(f"{number}. song: {songs['title']} es de {songs['artist']}\n")


write_songs(liked_songs, "liked_songs.txt")
