my_fav_fruit = {'mango', 'melon', 'uvas'}
he_fav_fruit = {'mango', 'fresa', 'manzana'}

''' union '''
union_favoritos = my_fav_fruit.union(he_fav_fruit)
union_favoritos = my_fav_fruit | he_fav_fruit #Esto tambien es una union
''' intersection '''
interseccion = my_fav_fruit.intersection(he_fav_fruit)
interseccion = my_fav_fruit & he_fav_fruit
''' difference '''
#diferencia = he_fav_fruit.difference(my_fav_fruit)
diferencia = he_fav_fruit - my_fav_fruit

''' intersection es para devolver los elementos comunes '''
''' union es para combinar dos sets '''
''' difference es para devolver elementos que no se encuentren en el otro set '''

print(union_favoritos)
print(interseccion)
print(diferencia)