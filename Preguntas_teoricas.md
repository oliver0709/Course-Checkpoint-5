# Course Checkpoint 5. Preguntas teóricas


## 1.¿Qué es un condicional en Python?

Los condicionales en Python son estructuras de control fundamentales que nos permiten tomar decisiones y ejecutar diferentes acciones según el resultado de una condición. En ese sentido, se expresan en bloques de código que nos permiten evaluar dicha condición y ejecutar un conjunto de instrucciones si esa condición es verdadera, es decir que puede ser una expresión que devuelve un valor booleano (True o False).

Hay que tener en cuenta de que de no ser por las estructuras de control, el código en cualquier lenguaje de programación sería ejecutado secuencialmente hasta terminar. Un código, no deja de ser un conjunto de instrucciones que son ejecutadas unas tras otra. Gracias a las estructuras de control, podemos cambiar el flujo de ejecución de un programa, haciendo que ciertos bloques de código se ejecuten si y solo si se dan unas condiciones particulares. Por tanto, los condicionales son fundamentales para crear programas que respondan de manera inteligente a diferentes situaciones. En el caso de Python, los más comunes son  if, else y elif (que combina else y if).

- Estructura básica de los condicionales en Python


  Los condicionales se definen utilizando las siguientes palabras clave:
  
  
  - if: Se utiliza para evaluar una condición y ejecutar un bloque de código si esa condición es verdadera.
  - elif (opcional): Se utiliza para evaluar condiciones adicionales en caso de que la primera condición no se cumpla.
  - else (opcional): Se utiliza para ejecutar un bloque de código si ninguna de las condiciones anteriores es verdadera.
  
Estos elementos serian expresados en Python de la siguiente manera:
```Python
if condición:
    # bloque de código si la condición es verdadera
elif condición2:
    # bloque de código si la condición2 es verdadera
else:
    # bloque de código si ninguna de las condiciones anteriores es verdadera
```
Es importante destacar que los bloques de código están indentados, lo que significa que tienen un nivel de sangría con respecto a la línea que contiene la estructura del condicional. La indentación es fundamental en Python, ya que define la estructura del código.

### Uso del if

Un ejemplo de uso sería si tenemos dos valores a y b que queremos dividir. Antes de entrar en el bloque de código que divide a/b, sería importante verificar que b es distinto de cero, ya que la división por cero no está definida. Es aquí donde entran los condicionales if.
```Python
a = 4
b = 2
if b != 0:
    print(a/b)
```

En este ejemplo podemos ver como se puede usar un if en Python. Con el operador != se comprueba que el número b sea distinto de cero, y si lo es, se ejecuta el código que está indentado. Por lo tanto, un if tiene dos partes:

  - La condición que se tiene que cumplir para que el bloque de código se ejecute, en nuestro caso b!=0.
  - El bloque de código que se ejecutará si se cumple la condición anterior.

Es muy importante tener en cuenta que la sentencia if debe ir terminada por ":" y el bloque de código a ejecutar debe estar indentado. En ese sentido, el bloque de código puede también contener más de una línea, es decir puede contener más de una instrucción:
```Python
if b != 0:
    c = a/b
    d = c + 1
    print(d)
```

Todo lo que vaya después del if y este indentado, será parte del bloque de código que se ejecutará si la condición se cumple. Si hay  un segundo print() “Fuera if” será ejecutado siempre, ya que está fuera del bloque if, como se muestra a continuación:
```Python
if b != 0:
    c = a/b
    print("Dentro if")
print("Fuera if")
```
Existen otros operadores como el de comparar si un número es mayor que otro. Su uso es igual que el anterior:

```Python
if b > 0:
    print(a/b)
```
Se puede también combinar varias condiciones entre el ***if*** y los ***":"***

Por ejemplo, se puede requerir que un número sea mayor que 5 y además menor que 15. Tenemos en realidad tres operadores usados conjuntamente, que serán evaluados por separado hasta devolver el resultado final, que será True si la condición se cumple o False en caso contrario:
```Python
a = 10
if a > 5 and a < 15:
    print("Mayor que 5 y menos que 15")
```
Es muy importante tener en cuenta que a diferencia de en otros lenguajes, en Python no puede haber un bloque if vacío. El siguiente código daría un _SyntaxError_:
```Python
if a > 5:
```
Por lo tanto, si tenemos un _if_ sin contenido, tal vez porque sea una tarea pendiente que estamos dejando para implementar en un futuro, es necesario hacer uso de pass para evitar el error. Realmente __pass__ no hace nada, simplemente es para tener contento al intérprete de código.

```Python
if a > 5:
    pass
```
Algo no demasiado recomendable pero que es posible, es poner todo el bloque que va dentro del if en la misma línea, justo a continuación de los __":"__ . Si el bloque de código no es muy largo, puede ser útil para ahorrarse alguna línea de código:
```Python
if a > 5: print("Es > 5")
```
Si el bloque de código tiene más de una línea, se pueden poner también en la misma línea separándolas con __";"__.
```Python
if a > 5: print("Es > 5"); print("Dentro del if")
```

### Uso de else y elif  

Es posible que no solo queramos hacer algo si una determinada condición se cumple, sino que además queramos hacer algo de lo contrario. Es aquí donde entra la cláusula **else**. La parte del __if__ se comporta de la manera que ya hemos explicado, con la diferencia que si esa condición no se cumple, se ejecutará el código presente dentro del else. Cabe puntualizar que ambos bloques de código son excluyentes, se entra o en uno o en otro, pero nunca se ejecutarán los dos. Por ejemplo:
```Python
x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")
```
Hasta ahora hemos visto cómo ejecutar un bloque de código si se cumple una instrucción, u otra si no se cumple, pero no es suficiente. En muchos casos, podemos tener varias condiciones diferentes y para cada una queremos un código distinto. Es aquí donde entra en juego el **elif**. Por ejemplo:

```Python
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
```
Con la cláusula _elif_ podemos ejecutar tantos bloques de código distintos como queramos según la condición. Traducido al lenguaje natural, sería algo así como decir: si es igual a 5 haz esto, si es igual a 6 haz lo otro, si es igual a 7 haz lo otro.

Se puede usar también de manera conjunta todo, el _if_ con el _elif_ y un _else_ al final. Es muy importante notar que if y else solamente puede haber uno, mientras que elif puede haber varios, tal y como se puede apreciar a continuación:
```Python
x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")
```
### Operador ternario

El operador ternario o _ternary operator_ es una herramienta muy potente que muchos lenguajes de programación tienen. Se trata de una cláusula _if-else_ que se define en una sola línea y puede ser usado, por ejemplo, dentro de un print().

```Python
x = 5
print("Es 5" if x == 5 else "No es 5")
#Es 5
```
Existen tres partes en un operador ternario, que son exactamente iguales a los que había en un if else. Tenemos la condición a evaluar, el código que se ejecuta si se cumple, y el código que se ejecuta si no se cumple. En este caso, tenemos los tres en la misma línea.

```Python
# [código si se cumple] if [condición] else [código si no se cumple]
```

Es muy útil y permite ahorrarse algunas líneas de código, además de aumentar la eficiencia de nuestro trabajo. Por ejemplo, en el siguiente código intentamos dividir a entre b. Si b es diferente a cero, se realiza la división y se almacena en c, de lo contrario se almacena -1. Ese -1 podría ser una forma de indicar que ha habido un error con la división:
```Python
a = 10
b = 5
c = a/b if b!=0 else -1
print(c)
#Da como resultado 2
```

### Prácticas Recomendadas:

- Claridad y simplicidad: Se debe utilizar condiciones claras y simples.
- Evitar condicionales anidados profundos: Si se encuentra anidando demasiados _if_, hay que considerar reestructurar el código o usar funciones.
- Precisión en las condiciones: Hay que asegurarse de que las condiciones no dejen fuera casos válidos o incluyan casos inválidos.

## 2.¿Cuáles son los diferentes tipos de bucles en Python y por qué son útiles?


En Python, los bucles permiten repetir una secuencia de instrucciones, lo que es esencial para tareas que requieren repetición, como procesar elementos de una lista, ejecutar operaciones hasta que se cumpla una condición, entre otros. En general, son útiles para automatizar tareas repetitivas y procesar grandes cantidades de datos.

- Los dos tipos principales de bucles son:

  - Bucle for: Se utiliza cuando conocemos de antemano cuántas veces queremos que se repita una acción. Por ejemplo, iterar sobre una lista o rango.
  - Bucle while: Se utiliza cuando no sabemos cuántas veces se debe repetir una acción y depende de una condición. Por ejemplo, mientras un contador sea menor o igual a cierto valor.
  
Ejemplo de bucle for:
```Python
for i in range(1, 6):
    print(i)
```

Ejemplo de bucle while:
```Python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

### Uso del bucle for

Como se mencionó anteriormente, la principal diferencia con el bucle while es que el número de iteraciones de un for esta definido de antemano, mientras que en un while no, lo cual se denota en la condición. Mientras que en el while la condición es evaluada en cada iteración para decidir si volver a ejecutar o no el código, en el for no existe tal condición, sino un iterable que define las veces que se ejecutará el código. En el siguiente ejemplo vemos un bucle for que se ejecuta 5 veces, y donde la i incrementa su valor “automáticamente” en 1 en cada iteración.

```Python
for i in range(0, 5):
    print(i) 
# Salida:
# 0
# 1
# 2
# 3
# 4
```

Ademas,  si se busca un número que va creciendo de 0 a n, hacerlo con _for_ nos ahorra alguna línea de código, porque no tenemos que escribir código para incrementar el número.

En Python, se puede iterar prácticamente todo, como por ejemplo una cadena. En el siguiente ejemplo vemos como la i va tomando los valores de cada letra:
```Python
for i in "Python":
    print(i)
# Salida:
# P
# y
# t
# h
# o
# n
```

### Iterables e iteradores

Para una mayor comprensión de los bucles for, es muy importante entender los conceptos de iterables e iteradores. Empecemos con un par de definiciones:

>Los **iterables** son aquellos objetos que, como su nombre indica, pueden ser iterados, lo que dicho de otra forma es, que puedan ser indexados. Si se piensa en un array (o una lista en Python), podemos indexarlo con lista[1] por ejemplo, por lo que sería un iterable.


>Los **iteradores** son objetos que hacen referencia a un elemento, y que tienen un método _next_ que permite hacer referencia al siguiente.


Ambos son conceptos un tanto abstractos y que pueden ser complicados de entender. Algunos ejemplos de iterables en Python son las listas, tuplas, cadenas o diccionarios. Sabiendo esto, lo primero que tenemos que tener claro es que en un for, lo que va después del in deberá ser siempre un iterable:

```Python
#for <variable> in <iterable>:
#    <Código>
```
Tiene bastante sentido, porque si queremos iterar una variable, ésta debe ser iterable. Para comprobar esto, se puede hacer a través de la función _isinstance()_. Si nos fijamos en el resultado, True significa que es iterable y False que no lo es:

```Python
from collections import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #False
```
Por lo tanto, las listas y las cadenas son iterables, pero un número, que es un entero, no lo es. Es por eso por lo que no podemos hacer lo siguiente, ya que daría un error. De hecho, el error sería _TypeError: int' object is not iterable_:

```Python
numero = 10
for i in numero:
    print(i)
```
Una vez entendidos los iterables, veamos los iteradores. Para entender los iteradores, es importante conocer la función _iter()_ en Python. Dicha función puede ser llamada sobre un objeto que sea iterable, y nos devolverá un iterador como se ve en el siguiente ejemplo:

```Python
lista = [5, 6, 3, 2]
it = iter(lista)
print(it)       #<list_iterator object at 0x106243828>
print(type(it)) #<class 'list_iterator'>
```
Vemos que al imprimir it es un iterador, de la clase _list_iterator_. Esta variable iteradora hace referencia a la lista original y nos permite acceder a sus elementos con la función _next()_. Cada vez que llamamos a next() sobre it, nos devuelve el siguiente elemento de la lista original. Por lo tanto, si queremos acceder al elemento 4, tendremos que llamar 4 veces a next(). Aqui, el iterador empieza apuntando fuera de la lista, y no hace referencia al primer elemento hasta que no se llama a next() por primera vez, tal y como se aprecia a continuacion:

```Python
lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
#     [5, 6, 3, 2]
#      ^
#      |
#     it
print(next(it))
#     [5, 6, 3, 2]
#         ^
#         |
#        it
print(next(it))
#     [5, 6, 3, 2]
#            ^
#            |
#           it
```
Tambien existen otros iteradores para diferentes clases:
- str_iterator para cadenas
- tuple_iterator para tuplas.
- set_iterator para sets.
- dict_keyiterator para diccionarios.
  
Dado que el iterador hace referencia a nuestra lista, si llamamos más veces a _next()_ que la longitud de la lista, nos devolverá un error _StopIteration_. Lamentablemente no existe ninguna opción de volver al elemento anterior.
```Python
lista = [5, 6]
it = iter(lista)
print(next(it))
print(next(it))
#print(next(it)) # Error! StopIteration
```
Es perfectamente posible tener diferentes iteradores para la misma lista, y serán totalmente independientes. Tan solo dependerán de la lista, como es evidente, pero no entre ellos:
```Python
lista = [5, 6, 7]
it1 = iter(lista)
it2 = iter(lista)
print(next(it1)) #5
print(next(it1)) #6
print(next(it1)) #7
print(next(it2)) #5
```

### For anidados

Es posible anidar los for, es decir, meter uno dentro de otro. Esto puede ser muy útil si queremos iterar algún objeto que en cada elemento tiene a su vez otra clase iterable. Podemos tener por ejemplo, una lista de listas, una especie de matriz:
```Python
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
```
Si iteramos usando sólo un for, estaremos realmente accediendo a la segunda lista, pero no a los elementos individuales:

```Python
for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]
```
Si queremos acceder a cada elemento individualmente, podemos anidar dos for. Uno de ellos se encargará de iterar las columnas y el otro las filas:
```Python
for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3
```

### Uso del bucle While

El uso del while nos permite ejecutar una sección de código repetidas veces, de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla. Cuando se deje de cumplir, se saldrá del bucle y se continuará la ejecución normal. Por ejemplo:

```Python
x = 5
while x > 0:
    x -=1
    print(x)

# Salida: 4,3,2,1,0
```
En el ejemplo anterior tenemos un caso sencillo de while. Tenemos una condición x>0 y un bloque de código a ejecutar mientras dure esa condición x-=1 y print(x). Por lo tanto, mientras que x sea mayor que 0, se ejecutará el código. Una vez se llega al final, se vuelve a empezar y si la condición se cumple, se ejecuta otra vez. En este caso se entra al bloque de código 5 veces, hasta que en la sexta, x vale cero y por lo tanto la condición ya no se cumple. En ese sentido, el while tiene dos partes:

  - La condición que se tiene que cumplir para que se ejecute el código.
  - El bloque de código que se ejecutará mientras la condición se cumpla.

Hay que tener cuidado con este tipo de bucle, ya que un mal uso del while puede dar lugar a bucles infinitos y problemas. Cierto es que en algún caso tal vez nos interese tener un bucle infinito, pero salvo que estemos seguros de lo que estamos haciendo, hay que tener cuidado. Imaginemos que tenemos un bucle cuya condición siempre se cumple. Por ejemplo, si ponemos True en la condición del while, siempre que se evalúe esa expresión, el resultado será True y se ejecutará el bloque de código. Una vez llegado al final del bloque, se volverá a evaluar la condición, se cumplirá, y vuelta a empezar.

```Python
# No ejecutar esto:
while True:
    print("Bucle infinito")
```

Es posible tener un while en una sola línea, algo muy útil si el bloque que queremos ejecutar es corto. En el caso de tener más de una sentencia, las debemos separar con ";". Por ejemplo:
```Python
x = 5
while x > 0: x-=1; print(x)
```

También podemos usar otro tipo de operación dentro del while, como la que se muestra a continuación. En este caso tenemos una lista que mientras no esté vacía, vamos eliminando su primer elemento:
```Python
x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)
#['Dos', 'Tres']
#['Tres']
#[]
```

### Else y while

Algo no muy corriente en otros lenguajes de programación, pero si en Python, es el uso de la cláusula else al final del while. Por ejemplo, la sección de código que se encuentra dentro del else, se ejecutará cuando el bucle termine, pero solo si lo hace “por razones naturales”. Es decir, el bucle termina porque la condición se deja de cumplir, y no porque se ha hecho uso del _break_:
```Python
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")
```

A este respecto, si un bucle termina por el break, el print() no se ejecutará. Por lo tanto, se podría decir que si no hay realmente ninguna sentencia break dentro del bucle, tal vez no tenga mucho sentido el uso del else, ya que un bloque de código fuera del bucle cumplirá con la misma funcionalidad.
```Python
x = 5
while True:
    x -= 1
    print(x) #4, 3, 2, 1, 0
    if x == 0:
        break
else:
    # El print no se ejecuta
    print("Fin del bucle")
```
### Bucles anidados

Ya hemos visto que los bucles while tienen una condición a evaluar y un bloque de código a ejecutar. Hemos visto ejemplos donde el bloque de código son operaciones sencillas como la resta, pero podemos complicar un poco más las cosas y meter otro bucle while dentro del primero. Es algo que resulta especialmente útil si, por ejemplo, queremos generar permutaciones de números, es decir, si queremos generar todas las combinaciones posibles. Imaginemos que queremos generar todas las combinaciones de dos números hasta 2. Es decir, 0-0, 0-1, 0-2,… hasta 2-2:
```Python
# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0
```
El primer bucle genera números del 0 al 2, lo que corresponde a la variable i. Por otro lado, el segundo bucle genera también números del 0 al 2, almacenados en la variable j. Al tener un bucle dentro de otro, lo que pasa es que por cada i se generan 3 j. Es muy importante no olvidar que al finalizar el bucle de la j, debemos resetear j=0 para que en la siguiente iteración la condición de entrada se cumpla.

Podemos complicar las cosas aún más y tener tres bucles anidados, generando combinaciones de 3 elementos con números 0, 1, 2. En este caso, tendremos desde 0,0,0 hasta 2,2,2:
```Python
i, j, k = 0, 0, 0
while i < 3:
    while j < 3:
        while k < 3:
            print(i,j,k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0
```
Finalmente, un clásico ejemplo de uso de while es la sucesión de Fibonacci en Python. En matemáticas, esto se trata de una sucesión infinita de números naturales, donde el siguiente es calculado sumando los dos anteriores:
```Python
a, b = 0, 1
while b < 25:
    print(b)
    a, b = b, a + b
#1, 1, 2, 3, 5, 8, 13, 21
```
### Prácticas Recomendadas:

- Evitar Bucles Infinitos: Hay que asegurase de que el bucle while tenga una condición de terminación clara.
- Uso de _break_ y _continue_: Se deberia utilizar break para salir de un bucle y continue para saltar al siguiente ciclo de iteración.
- Eficacia: Es preferible usar for para iterar sobre objetos iterables y while cuando la condición de terminación depende de una lógica más compleja.


## 3. ¿Qué es una lista por comprensión en Python?

Una de las principales ventajas de Python es que una misma funcionalidad puede ser escrita de maneras muy diferentes, ya que su sintaxis es muy rica en lo que se conoce como expresiones idiomáticas o _idiomatic expressions_. Las __list comprehension__ o comprensión de listas son una de ellas.

En Python, éstas son una forma concisa y eficiente de crear listas aplicando una expresión a cada elemento de otro iterable, como una lista, tupla o rango. Esta característica permite simplificar la creación de listas en una sola línea de código. Por ejemplo, podemos crear una lista con los cuadrados de los primeros 5 números de la siguiente forma:

```Python
cuadrados = [i**2 for i in range(5)]
#[0, 1, 4, 9, 16]
```
De no existir, podríamos hacer lo mismo de la siguiente forma, pero necesitamos alguna que otra línea más de código:
```Python
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
#[0, 1, 4, 9, 16]
```
El resultado es el mismo, pero resulta menos claro. Antes de continuar, veamos la sintaxis general de las comprensiones de listas:

```Python
nueva_lista = [expresión for elemento in iterable]
```
- nueva_lista: La lista resultante que se desea crear.
- expresión: La operación que se aplicará a cada elemento del iterable.
- elemento: El elemento actual del iterable.
- iterable: Cualquier objeto en Python que pueda recorrerse y acceder a elementos individuales, como listas, tuplas o cadenas.


En ese sentido, basicamente tenemos el _for elemento in iterable_, que itera un determinado iterable y “almacena” cada uno de los elementos en _elemento_, como vimos anteriormente en el caso del bucle for. Por otro lado, tenemos la _expresión_, que es lo que será añadido a la lista en cada iteración.

Como se vio en el ejemplo de cuadrados, la expresión puede ser una operación _i**2_, pero también puede ser un valor constante. El siguiente ejemplo genera una lista de cinco unos:
```Python
unos = [1 for i in range(5)]
#[1, 1, 1, 1, 1]
```
La expresión también puede ser una llamada a una función. Se podría escribir el ejemplo de cuadrados de la siguiente manera:
```Python
def eleva_al_2(i):
    return i**2

cuadrados = [eleva_al_2(i) for i in range(5)]
#[0, 1, 4, 9, 16]
```
Como se puede observar, las posibilidades son bastante amplias. Cualquier elemento que sea iterable puede ser usado con las list comprehensions. Anteriormente hemos iterado range(), pero podemos hacer lo mismo para una lista. En el siguiente ejemplo vemos cómo dividir todos los números de una lista entre 10:
```Python
lista = [10, 20, 30, 40 , 50]
nueva_lista = [i/10 for i in lista]
#[1.0, 2.0, 3.0, 4.0, 5.0]
```

### Añadiendo condicionales

Hasta ahora, vimos que es posible modificar todos los elementos de un iterable (como una lista) de diferentes maneras, sobre todo en casos donde se busca elevar cada elemento al cuadrado o dividiendo cada elemento por diez. Pero, ¿y si quisiéramos realizar la operación sobre el elemento sólo si una determinada condición se cumple? Si este fuera el caso, sería posible añadiendo un condicional if. La expresión genérica sería la siguiente:
```Python
lista = [expresión for elemento in iterable if condición]
```
Por lo tanto, la expresión sólo se aplicará al elemento si se cumple la condición. Veamos un ejemplo con una frase, de la que queremos saber el número de erres que tiene:
```Python
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']
```
Lo que hace el código anterior es iterar cada letra de la frase, y si es una r, se añade a la lista. De esta manera, el resultado es una lista con tantas letras r como la frase original tiene, y adicionalmente podemos calcular las veces que se repite con _len()_:
```Python
print(len(erres))
#4
```

### Sets comprehension

Las _set comprehensions_ son muy similares a las listas que hemos visto con anterioridad. La única diferencia es que debemos hacer uso de {}. Como resulta evidente, dado que los set no permiten duplicados, si intentamos añadir un elemento que ya existe en el set, simplemente no se añadirá. Bajo esta premisa, si lo aplicamos al ejemplo anterior, daria el siguiente resultado:
```Python
frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r"}
#{'r'}
```

### Dictionary comprehension

Y por último, también tenemos las comprensiones de diccionarios. Son muy similares a las anteriores, con la única diferencia que debemos especificar la _key_ o clave. Veamos un ejemplo:
```Python
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
#{'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}
```
Como se puede apreciar, usando _":"_ asignamos un valor a una clave. Hemos usado también _zip()_, que nos permite iterar dos listas paralelamente. Por lo tanto, en este ejemplo estamos convirtiendo dos listas a un diccionario.

Después de haber visto y analizado las comprensiones en sus diversas vertientes, se puede evidenciar que son herramientas muy útiles para hacer que nuestro código resulte más compacto y fácil de leer. Siempre que tengamos una colección iterable que queramos modificar, son una buena opción si es que queremos evitar tener que escribir bucles for.

Las comprensiones están también muy relacionadas con el concepto de programación funcional y otras funciones que Python nos ofrece como _filter_ o _map_. En ese sentido, map() y filter() son dos funciones incorporadas en Python que tambien se utilizan para procesar iterables (como listas, tuplas o rangos) de manera eficiente. A continuación, detallamos cómo funcionan y cuál es su diferencia:


- La función map() itera a través de todos los elementos de un iterable y aplica una función que le pasamos como argumento a cada uno de ellos.

Sintaxis: 
```Python
map(función, iterable(s))
```
Por ejemplo:
```Python
def empieza_con_A(s):
    return s[0] == "A"

frutas = ["Manzana", "Banana", "Pera", "Albaricoque", "Naranja"]
resultado = list(map(empieza_con_A, frutas))
# Salida: [True, False, False, True, False]
```

- La función filter() también itera a través de los elementos de un iterable, pero solo mantiene aquellos elementos que cumplen una condición especificada en una función. La función pasada a filter() debe devolver valores booleanos (verdadero o falso).
  
Sintaxis:
```Python
filter(función, iterable)
```
Por ejemplo:
```Python
def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(es_par, numeros))
# Salida: [2, 4, 6, 8]
````
#### Diferencias:

- map() aplica una función a todos los elementos y devuelve una lista con los resultados.
- filter() filtra los elementos según una condición y devuelve una lista con los elementos que cumplen esa condición.
  
En resumen, map() transforma todos los elementos, mientras que filter() selecciona solo algunos elementos del iterable. Ambas funciones son útiles en programación funcional y pueden reemplazarse con comprensiones de lista o bucles, pero proporcionan una forma más elegante y concisa de resolver ciertos problemas.


En ciertas ocasiones, no obstante, cabe destacar que las comprensiones no resultan sólo útiles porque pueden ser escritas en una sola línea de código, sino que también pueden llegar a ser más rápidas que otros métodos. Es muy importante, por lo tanto, medir su tiempo de ejecución para saber si son una buena elección.

### Prácticas Recomendadas:

- Legibilidad: No se debe sacrificar la legibilidad por la concisión; las comprensiones complejas deben dividirse en varias líneas o reescribirse como bucles for tradicionales. 
- Uso Moderado: Hay que utilizar las comprensiones de listas cuando mejoren la claridad y la eficiencia del código. En ese sentido, se debe tener cuidado con su uso y no abusar de ellas. Resulta fácil caer en la tentación de acabar escribiendo comprensiones que son tan largas que prácticamente son imposibles de leer, algo que puede no ser muy buena idea.


## 3. ¿Qué es un argumento en Python?

Un argumento es un valor que se pasa a una función en el momento de su llamada. Puede ser un valor constante, una variable o incluso el resultado de otra función. Los argumentos son esenciales para que las funciones realicen operaciones con datos dinámicos. En Python, generalmente los argumentos pueden ser posicionales (se pasan en el orden en que aparecen en la función) o por palabra clave (se especifican por su nombre).

Por ejemplo:
```python
def saludo(nombre, mensaje='Hola'):
    print(f"{mensaje}, {nombre}!")

saludo("Ana")  # Usando solo el argumento posicional
saludo("Carlos", mensaje="Buen día")  # Usando ambos argumentos 
```

En ese contexto, al igual que en otros lenguajes de programación, cuando hablamos de argumentos, tenemos que hablar también de los que implica definir nuestras propias funciones. Para ello, en el caso de Python, hacemos uso de _def_, tal y como se ve a continuacion:
```python
def nombre_funcion(argumentos):
    código
    return retorno-salida
```
Cualquier función tendrá un nombre, unos argumentos de entrada, un código a ejecutar y unos parámetros de salida. Al igual que las funciones matemáticas, en programación nos permiten realizar diferentes operaciones con la entrada y posteriormente entregar una determinada salida que dependerá del código que escribamos dentro. Por lo tanto, es totalmente análogo al clásico _y=f(x)_ de las matemáticas:
```python
def f(x):
    return 2*x
y = f(3)
print(y) # 6
```

Algo que diferencia en cierto modo las funciones en el mundo de la programación, es que no sólo realizan una operación con sus entradas, sino que también parten de los siguientes principios:

  - El principio de **reusabilidad**, que nos dice que si por ejemplo tenemos un fragmento de código usado en muchos sitios, la mejor solución sería pasarlo a una función. Esto nos evitaría tener código repetido, y que modificarlo fuera más fácil, ya que bastaría con cambiar la función una vez.
  
  - Y el principio de **modularidad**, que defiende que en vez de escribir largos trozos de código, es mejor crear módulos o funciones que agrupen ciertos fragmentos de código en funcionalidades específicas, haciendo que el código resultante sea más fácil de leer.
  
### Pasando argumentos de entrada

Bajo las premisas anteriores, empecemos por la función más sencilla de todas. Una función sin parámetros de entrada ni parámetros de salida:
```python
def di_hola():
    print("Hola")
```
Hemos declarado o definido la función. El siguiente paso, en referencia a los argumentos, es pasar como entrada un nombre, se imprimirá Hola y el nombre:
```python
def di_hola(nombre):
    print("Hola", nombre)
di_hola("Juan")
# Hola Juan
```

En esta linea, y teniendo en cuenta nuestro desarrollo, profundizaremos en las formas en las que Python permite pasar argumentos.

### Argumentos por posición

Tal y como vimos al principio, los argumentos por posición o posicionales son la forma más básica e intuitiva de pasar parámetros. Si tenemos una función resta() que acepta dos parámetros, se puede llamarla como se muestra a continuación:
```python
def resta(a, b):
    return a-b
resta(5, 3) # 2
```
Al tratarse de parámetros posicionales, se interpretará que el primer número es la _a_ y el segundo la _b_. El número de parámetros es fijo, por lo que si intentamos llamar a la función con solo uno, dará error:
```python
resta(1) # Error! TypeError
```
Tampoco es posible usar más argumentos de los tiene la función definida, ya que no sabría qué hacer con ellos. Por lo tanto, si lo intentamos, Python nos dirá que toma 2 posicionales y estamos pasando 3, lo que no es posible:
```python
#TypeError: resta() takes 2 positional arguments but 3 were given
#resta(5,4,3) # Error
```

### Argumentos por nombre

Otra forma de llamar a una función, es usando el nombre del argumento con _"="_ y su valor. El siguiente código hace lo mismo que el código anterior, con la diferencia de que los argumentos no son posicionales:
```python
resta(a=3, b=5) # -2
```

Al indicar en la llamada a la función el nombre de la variable y el valor, el orden ya no importa, y se podría llamar de la siguiente forma:
```python
resta(b=5, a=3) # -2
```

Como es de esperar, si indicamos un argumento que no ha sido definido como parámetro de entrada, tendremos un error:
```python
#resta() got an unexpected keyword argument 'c'
#resta(b=5, c=3) # Error!
```

### Argumentos por defecto

Tal vez queramos tener una función con algún parámetro opcional, que pueda ser usado o no dependiendo de diferentes circunstancias. Para ello, lo que podemos hacer es asignar un valor por defecto a la función. En el siguiente caso **c** valdría cero salvo que se indique lo contrario:
```python
def suma(a, b, c=0):
    return a+b+c
suma(5,5,3) # 13
```
Dado que el parámetro c tiene un valor por defecto, la función puede ser llamada sin ese valor:
```python
suma(4,3) # 7
```

Podemos incluso asignar un valor por defecto a todos los parámetros, por lo que se podría llamar a la función sin ningún argumento de entrada:
```python
def suma(a=3, b=5, c=0):
    return a+b+c
suma() # 8
```

Las siguientes llamadas a la función también son válidas:
```python
suma(1)     # 6
suma(4,5)   # 9
suma(5,3,2) # 10
```

O haciendo uso de lo que hemos visto antes en referencia a los nombres de los argumentos:
```python
suma(a=5, b=3) #8
```

### Argumentos de longitud variable

En el ejemplo con argumentos por defecto, hemos visto que la función puede ser llamada con diferente número de argumentos de entrada, pero esto no es realmente una función con argumentos de longitud variable, ya que existe un número máximo.
Imaginemos que queremos una función suma() como la de antes, pero en este caso necesitamos que sume todos los números de entrada que se le pasen, sin importar si son 3 o 100. Una primera forma de hacerlo sería con una lista:
```python
def suma(numeros):
    total = 0
    for n in numeros:
        total += n
    return total
suma([1,3,5,4]) # 13
```
La forma es válida y cumple nuestro requisito, pero realmente no estamos trabajando con argumentos de longitud variable, sino que tenemos un solo argumento que es una lista de números.

Por suerte, Python tiene herramientas muy potentes a este respecto, las cuales veremos a continuación: 

### Uso de *args

Gracias a los _*args_ en Python, podemos definir funciones cuyo número de argumentos es variable. Es decir, podemos definir funciones genéricas que no aceptan un número determinado de parámetros, sino que se “adaptan” al número de argumentos con los que son llamados. Cabe destacar que no se debe confundir * con los punteros en otros lenguajes de programación, no tiene nada que ver.

El args viene de _arguments_ en inglés, o argumentos. Haciendo uso de *args en la declaración de la función, podemos hacer que el número de parámetros que acepte sea variable. Por ejemplo:
```python
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

suma(1, 3, 4, 2)
#Salida 10
suma(1, 1)
#Salida 2
```

Antes de nada, el uso del nombre _args_ es totalmente arbitrario, por lo que se podría haberlo llamado como quisieramos. Es una mera convención entre los usuarios de Python y resulta frecuente darle ese nombre. Lo que sí es un requisito, es usar * junto al nombre.

En el ejemplo anterior hemos visto como *args puede ser iterado, ya que en realidad es una tupla. Por lo tanto, iterando la tupla podemos acceder a todos los argumentos de entrada y, en nuestro caso, sumarlos y devolverlos.

Cabe señalar que este es un mero ejemplo didáctico. En realidad podríamos hacer algo como lo siguiente, lo que sería mucho más sencillo:
```python
def suma(*args):
    return sum(args)

suma(5, 5, 3)
#Salida 13
```

Con esto resolvemos nuestro problema inicial, en el que necesitábamos un número variable de argumentos. Sin embargo, hay otra forma que nos proporciona además un nombre asociado al argumento, entonces es cuando el uso de **kwargs cobra vital importancia. La explicamos a continuación.

### Uso de **kwargs

Al igual que en *args, en _**kwargs_ el nombre es una mera convención entre los usuarios de Python. Se puede usar cualquier otro nombre, siempre y cuando se respete el **.

En este caso, en vez de tener una tupla tenemos un diccionario. Se puede verificar de la siguiente forma con type():
```python
def suma(**kwargs):
    print(type(kwargs))

suma(x=3)
#<class 'dict'>
```
Pero veamos un ejemplo más completo. A diferencia de *args, los **kwargs nos permiten dar un nombre a cada argumento de entrada, pudiendo acceder a ellos dentro de la función a través de un diccionario:
```python
def suma(**kwargs):
    s = 0
    for key, value in kwargs.items():
        print(key, "=", value)
        s += value
    return s

suma(a=3, b=10, c=3)
#Salida
#a = 3
#b = 10
#c = 3
#16
```
Como podemos ver, es posible iterar los argumentos de entrada con _items()_, y podemos acceder a la clave _key_ (o nombre) y el valor o _value_ de cada argumento. El uso de los **kwargs es muy útil si además de querer acceder al valor de las variables dentro de la función, se quiere darles un nombre que de una información extra.

### Mezclando *args y **kwargs

Una vez que entendemos el uso de *args y **kwargs, podemos complicar las cosas un poco más. Es posible mezclar argumentos normales con *args y **kwargs dentro de la misma función. Para ello, se debe definir la función en el siguiente orden:

  - Primero argumentos normales
  - Después los *args
  - Y por último los **kwargs
  
Veamos un ejemplo:
```python
def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

funcion(10, 20, 1, 2, 3, 4, x="Hola", y="Que", z="Tal")
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal
```
Y por último, como complemento adicional, es crucial saber lo que se conoce como _tuple unpacking_. A este respecto, haciendo uso de *, podemos extraer los valores de una lista o tupla, y que sean pasados como argumentos a la función:
```python
def funcion(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    for arg in args:
        print("args =", arg)
    for key, value in kwargs.items():
        print(key, "=", value)

args = [1, 2, 3, 4]
kwargs = {'x':"Hola", 'y':"Que", 'z':"Tal"}

funcion(10, 20, *args, **kwargs)
#Salida
#a = 10
#b = 20
#args = 1
#args = 2
#args = 3
#args = 4
#x = Hola
#y = Que
#z = Tal
```

### Prácticas Recomendadas:

- Uso de Palabras Clave: Cuando una función acepta varios argumentos, llamar a la función con argumentos de palabras clave mejora la legibilidad.
 
- Documentar y Ser Explícito: Al usar kwargs, hay que asegurarse de que estén bien documentados y explícitos. Si se proporciona nombres descriptivos para los argumentos de palabra clave, esto facilitará la comprensión del código por parte de otros desarrolladores.
  
- Combinar con Args: Siempre que sea posible, hay que combinar kwargs con argumentos posicionales (args). Esto ayuda a mantener una estructura clara y coherente en nuestras funciones.


## 5. ¿Qué es una función Lambda en Python?


Las funciones lambda en Python son pequeñas funciones anónimas definidas con la palabra clave __lambda__. Son sintácticamente restringidas a una sola expresión, es decir que típicamente se definen en una línea y cuyo código a ejecutar suele ser pequeño. Se utiliza para crear expresiones simples y temporales. A diferencia de las funciones regulares definidas con la palabra clave _def_, las funciones lambda no tienen un nombre y se crean en el lugar donde se necesitan.

Sintaxis:
```python
lambda args: expresión
```
- args representa los argumentos que la función lambda puede recibir (separados por comas).
- La expresión es el cuerpo de la función, y solo puede contener una sola expresión.

En lo concerniente a las funciones regulares, se relaciona las funciones lambdas de la siguiente manera, según la [documentación oficial de Python](https://docs.python.org/3/faq/design.html#why-can-t-lambda-expressions-contain-statements): 

>“Python lambdas are only a shorthand notation if you’re too lazy to define a function.”

Lo que significa algo así como “las funciones lambda son simplemente una versión acortada, que puedes usar si te da pereza escribir una función”. Asi mismo, se indica que las expresiones lambda de Python no pueden contener declaraciones porque el marco sintáctico de Python no puede manejar declaraciones anidadas dentro de expresiones. 

Las funciones ya son objetos de primera clase en Python, y pueden ser declaradas en un ámbito local. Por tanto, la única ventaja de usar una lambda en lugar de una función definida localmente es que no se necesita inventar un nombre para la función, por lo que es sólo una variable local a la que se asigna el objeto función (que es exactamente el mismo tipo de objeto que produce una expresión lambda).

A modo de ejemplo, ahora veremos lo que sería una función que suma dos números:
```python
def suma(a, b):
    return a+b
```
Esto se podría expresar en forma de una función lambda de la siguiente manera:
```python
lambda a, b : a + b
```
Como dijimos, una función lambda no tiene un nombre, y por lo tanto salvo que sea asignada a una variable, es totalmente inútil. Para ello, debemos hacerlo así:
```python
suma = lambda a, b: a + b
```

Una vez tenemos la función, es posible llamarla como si de una función normal se tratase:
```python
suma(2, 4)
```
Si es una función que solo queremos usar una vez, tal vez no tenga sentido almacenarla en una variable. En ese sentido, es posible declarar la función y llamarla en la misma línea:
```python
(lambda a, b: a + b)(2, 4)
```

Por otro lado, una función lambda puede ser la entrada a una función normal:
```python
def mi_funcion(lambda_func):
    return lambda_func(2,4)

mi_funcion(lambda a, b: a + b)
#6
```

En sentido opuesto y a modo didáctico, una función normal también puede ser la entrada de una función lambda de esta manera:
```python
def mi_otra_funcion(a, b):
    return a + b

(lambda a, b: mi_otra_funcion(a, b))(2, 4)
```

A pesar de que las funciones lambda tienen muchas limitaciones frente a las funciones normales, comparten gran cantidad de funcionalidades. Es posible tener argumentos con valor asignado por defecto:
```python
(lambda a, b, c=3: a + b + c)(1, 2) # 6
```

También se pueden pasar los parámetros indicando su nombre:
```python
(lambda a, b, c: a + b + c)(a=1, b=2, c=3) # 6
```

Al igual que en las funciones normales, se puede tener un número variable de argumentos haciendo uso de *, lo conocido como tuple unpacking:
```python
(lambda *args: sum(args))(1, 2, 3) # 6
```

Y si tenemos los parámetros de entrada almacenados en forma de _key_ y _value_ como si fuera un diccionario, también es posible llamar a la función:
```python
(lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3) # 6
```

Por otro lado, tambien se utilizan comúnmente como argumentos en funciones de orden superior como _map_ o _filter_. Por ejemplo, para duplicar un número:

```Python
# Función lambda para duplicar un número
duplicar = lambda x: x * 2

# Ejemplo de uso con map
mi_lista = [1, 2, 3, 4, 5, 6]
lista_duplicada = list(map(duplicar, mi_lista))  
print(lista_duplicada)  # [2, 4, 6, 8, 10, 12]
```

A continuación, otro ejemplo para verificar si un número es positivo:

```Python
# Función lambda para verificar si un número es positivo
es_positivo = lambda x: x > 0

# Ejemplo de uso con filter
numeros = [-2, 5, -10, 8, 0, 3]
numeros_positivos = list(filter(es_positivo, numeros))
print(numeros_positivos)  # [5, 8, 3]
```

En definitiva, el uso de funciones lambda ayuda a reducir el código y en ciertos casos evita nombrar funciones que solo se utilizan una vez, aportando a su vez una mayor concisión. 

### Prácticas Recomendadas:

- Limitación al Uso Simple: Hay que utilizar las funciones lambda para pequeñas funcionalidades que no requieren complejidad.
- No Sobrecargar: Se debe evitar usar lambdas complejas o de difícil comprensión y, en la medida de lo posible, documentar su propósito para facilitar la comprensión del código.

##  6. ¿Qué es un paquete pip?


PIP (acrónimo de "Pip Installs Packages" o "Preferred Installer Program") es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software en Python. 

Básicamente se trata de una herramienta de línea de comandos que realiza dichas acciones desde el Python Package Index (PyPI) y otros repositorios. En ese sentido, permite a los desarrolladores y usuarios de Python instalar, actualizar y administrar fácilmente bibliotecas y módulos de terceros en sus entornos Python.

En Python, tanto programas grandes como scripts se suelen desarrollar apoyándose en librerías y/o frameworks de terceros a los cuales llamamos dependencias. A su vez estas dependencias pueden tener otras dependencias llamadas dependencias transitivas. Esto sucede, por ejemplo, con Pandas, la cual es una librería muy popular pensada para manipular y analizar datos, cuyo desarrollo está basado en NumPy, otra librería muy conocida para realizar cálculos matriciales. Por tanto, al utilizar Pandas también utilizamos, aunque de forma indirecta, NumPy.

Gestionar todas las dependencias de un programa grande de forma manual puede llegar a ser un proceso tedioso. Por un lado requiere dedicarle tiempo y por otro se trata de un proceso en el cual es fácil realizar fallos. La solución a estos inconvenientes son los llamados sistemas de gestión de paquetes.

Antes de continuar, puntualizar que en Python cuando decimos “paquetes” solemos referirnos a librerías y frameworks de terceros. Algunos ejemplos muy conocidos son, por ejemplo, Django para el desarrollo web, o Requests para realizar peticiones HTTP.

Como mencionamos, Python tiene su propio sistema de gestión de paquetes llamado Pip, el cual viene preinstalado con cualquier versión moderna de Python. Para saber si lo tenemos instalado es tan sencillo como ejecutar el siguiente comando en nuestro terminal:

Linux y macOS
```python
$ python --version
Python 3.N.N
$ python -m pip --version
pip X.Y.Z from ... (python 3.N.N)
```
Windows
```python
C:> py --version
Python 3.N.N
C:> py -m pip --version
pip X.Y.Z from ... (python 3.N.N)
```
En caso que así sea, nos informará sobre la versión de pip que tenemos instalada. Adicionalmente, también podemos ver un listado de todos los argumentos admitidos por pip mediante el siguiente comando:
```python
$ pip --help
```
### Instalar y actualizar pip

Pip está incluido por defecto en versiones modernas de Python. En concreto se introdujo a partir de Python 2.7.9 en adelante (en Python 2) y a partir de Python 3.4 en adelante (en Python 3). Si la versión de Python es anterior a las mencionadas, existen dos alternativas para poder instalarlo. La primera, aunque sea un poco obvia hay que mencionarla, es actualizar a una versión de Python más moderna. Si por el motivo que sea esto no fuera posible, alternativamente se puede añadir pip a la instalación de Python.

En Windows o macOS, para añadir pip a la instalación de Python, primero se tiene que descargar el [script de instalación de pip](https://bootstrap.pypa.io/get-pip.py). Luego, ejecutarlo como cualquier otro script.

Linux y macOS
```python
$ python get-pip.py
```
Windows
```python
C:\>py get-pip.py
```
En distribuciones de Linux (Debian/Ubuntu) el proceso varía un poco ya que hay que usar su sistema de gestión de paquetes.
```bash
$ sudo apt update
$ sudo apt install python3-pip
```

El proceso de actualización de pip varía en función del sistema operativo. En Windows y macOS se utiliza directamente el comando pip, mientras que en Linux la actualización se realiza con el sistema de gestión de paquetes. A continuación, detallamos como actualizar pip para cada uno de esto tres sistemas operativos.

Windows
```cmd
C:\>python -m pip install --upgrade pip
```
macOS
```bash
$ python -m pip install --upgrade pip
```
Linux
```bash
$ sudo apt install --only-upgrade python3-pip
```

### Repositorios de paquetes de Python

El repositorio oficial (y más grande) de paquetes de Python es el Python Package Index (PyPI). Cualquier programador puede registrarse gratuitamente en PyPI y subir ahí sus propios paquetes. Una vez que un paquete aparece en PyPI, cualquier persona puede instalarlo localmente mediante pip. Pero como no hay ningún proceso de revisión ni de aseguramiento de la calidad, es recomendable invertir algo de tiempo en revisar el software que estamos adquiriendo.

En PyPI podemos realizar búsquedas de paquetes por nombre y/o filtrar resultados en función de ciertos criterios como el estado de desarrollo, la licencia, etc. Además, cada paquete tiene su propia página en la web de PyPI. Ahí podemos obtener mucha información sobre un paquete en cuestión: la versión, la licencia, el comando para instalarlo, el nombre del autor, las versiones de Python con las que se ha testeado el paquete, y mucho más. Para que tener una idea de ello, se puede consultar la [página de Requests en PyPI](https://pypi.org/project/requests/).

### Instalar dependencias con pip

Para instalar con pip cualquier paquete disponible en PyPI, simplemente se debe utilizar el siguiente comando:

Windows
```python
C:\>pip install package_name
```
macOS
```python
$ pip install package_name
```
Linux 
```python
$ python3 -m pip install package_name
```
Donde package_name es el nombre del paquete deseado. La herramienta pip no sólo instalará el paquete que le indicamos y su dependencias, sino que además los almacenará en una caché local de cara a futuras instalaciones.

Otro comando útil, complementario al de instalar, es el que nos muestra un listado de los paquetes instalados que es el siguiente:
```python
$ pip list 
```
Al igual que con todo en Python, pip tiene su documentación disponible. Algunos paquetes pueden tener requisitos específicos. En los casos en los que se encuentran requisitos específicos, pip también los maneja. La sintaxis para instalar un paquete y sus requisitos específicos es la siguiente:
```Python
pip install package_name[package_reqs]
```

Por ejemplo, para instalar la biblioteca pandas y sus requisitos necesarios, escribiría lo siguiente:
```Python
pip install pandas[all]
```
Una consideración a tener en cuenta es que pip instala por defecto los paquetes en el entorno global de Python. Sin embargo, es recomendable instalar nuestras dependencias en entornos virtuales de Python, ya que de este modo mantenemos las dependencias separadas por proyectos y evitamos posibles conflictos entre versiones de una misma dependencia.

### Instalación de versiones anteriores

Por defecto pip instala la última versión disponible de un paquete. Sin embargo, también es posible instalar versiones específicas. Para ello tenemos que especificar la versión deseada como se muestra a continuación, donde instalamos la versión 2.23.0 de la librería Requests:

Windows
```Python
py -m pip install requests==2.23.0
```
Linux/macOS
```Python
$ pip install requests==2.23.0
```
### Obtener información de un paquete instalado

Una vez hemos instalado un paquete en nuestro entorno de Python, podemos obtener información adicional sobre el mismo en nuestro terminal. Para ello tenemos que ejecutar el siguiente comando:

Windows
```Python
py -m pip show package_name
```
Linux/macOS
```Python
$ pip show package_name
```
### Identificar y actualizar dependencias obsoletas

Con el tiempo, las librerías que tenemos instaladas en nuestro entorno van recibiendo actualizaciones y se quedan obsoletas. Para ver un listado de las librerías que disponen de una nueva versión, se puede ejecutar el siguiente comando tanto en Windows como en Linux/macOS:
```Python
pip list --outdated
```

Para actualizar una librería en particular a su última versión hay que ejecutar el siguiente comando:

Windows
```Python
C:\>pip install --upgrade nombre_paquete
```
macOS
```Python
$ python -m pip install --upgrade nombre_paquete
```
Linux
```Python
$ pip install --upgrade nombre_paquete
```
Si se quiere actualizar todos los paquetes instalados localmente, siendo usuario avanzado de Unix, se puede utilizar lo siguiente:
```Python
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```
### Desinstalar dependencias

En algunas ocasiones instalamos una librería simplemente para probarla. Si queremos desinstalarla de nuestro entorno, es tan sencillo como ejecutar el siguiente comando:
```Python
pip uninstall nombre_paquete
```
Hemos de tener en cuenta que este comando no desinstala las posibles dependencias transitivas. Por eso son tan útiles los entornos virtuales, ya que nos permiten eliminar todas las dependencias de golpe eliminando la carpeta del entorno virtual.

### Gestión de dependencias

En lo concerniente a gestion de dependencias, es importante tener en cuenta que pip no siempre es perfecto. Puede haber ocasiones en las que dos paquetes de software diferentes necesiten versiones diferentes de la misma dependencia, lo que puede causar conflictos. En esos casos, la mejor opción es utilizar un entorno virtual de Python y especificar las versiones de los paquetes que necesitamos para cada proyecto. De esta manera, podemos mantener nuestros proyectos separados y aislados de otros paquetes y dependencias que no necesitamos.

Ahora bien, si nos encontramos trabajando en un proyecto, con pip se puede listar las dependencias del mismo usando este comando:
```python
pip freeze
```
Esto nos mostrará una lista de todos los paquetes instalados, junto con sus versiones. Incluso se puede usar este comando para un trabajo coordinado, sabiendo las dependencias y versiones necesarias para desarrollos conjuntos. En ese contexto, al desarrollar un proyecto en Python, es muy común hacer uso de paquetes y librerías externas para aprovechar las funcionalidades que estos nos ofrecen. Sin embargo, esto puede generar un problema de gestión de dependencias, especialmente cuando se trabaja en equipo o se cambia el ambiente de trabajo.

Es por eso que una práctica muy común, al utilizar pip, es crear un archivo _requirements.txt_ que contenga todas las dependencias necesarias y sus versiones correspondientes. De esta manera, al instalar todas las dependencias desde este archivo, se asegura que todos los desarrolladores en el equipo están trabajando con las mismas versiones de las librerías.

Para crear un archivo requirements.txt, basta con utilizar el siguiente comando en la terminal de comandos de Python:
```python
pip freeze > requirements.txt
```
Este comando genera un archivo llamado requirements.txt en el directorio actual, el cual contiene todas las dependencias instaladas en el entorno virtual actual y sus versiones correspondientes. Es importante mencionar que este archivo debe ser incluido en el control de versiones del proyecto, de manera que todos los desarrolladores puedan acceder a él.

Una vez que se tiene el archivo requirements.txt, es posible instalar todas las dependencias del proyecto utilizando el siguiente comando:
```python
pip install -r requirements.txt
```
Este comando nos permite instalar todas las dependencias listadas en el archivo requirements.txt de una sola vez, asegurando de esta forma que todos los desarrolladores están utilizando las mismas versiones de las librerías.

En el contenido de un archivo requirements.txt, cada línea representa una dependencia. Cada línea generalmente tiene el formato: nombre_del_paquete==versión. Por ejemplo:
```python
requests==2.23.0
numpy==1.21.4
```
En resumen, el uso de pip y la creación de un archivo requirements.txt nos permite gestionar de manera eficiente las dependencias de nuestro proyecto en Python, asegurando que todos los desarrolladores están trabajando con las mismas versiones de las librerías. Es una práctica muy útil para cualquier proyecto de software en Python y es recomendable incluirla en el flujo de trabajo del equipo de desarrollo, de esa forma se garantiza que nuestros proyectos sean flexibles y escalables.

### Creación de entornos virtuales y el manejo de paquetes privados

Como mencionamos, a través de pip es posible instalar paquetes y librerías de terceros de manera sencilla y eficiente. Así mismo, pip puede ser de gran utilidad dentro de entornos virtuales y el manejo de paquetes privados.

Una de las principales ventajas de trabajar con entornos virtuales es que nos permite crear entornos de desarrollo independientes para cada proyecto. En ese contexto, el principal propósito de activar un entorno virtual es aislar el entorno de desarrollo del sistema base. De esa manera, no habrá conflictos entre las versiones de las distintas librerías que usemos en diferentes proyectos. 

- Para crear un entorno virtual con Pip, utilizamos los siguientes comandos:

En Windows, y asumiendo que Python está incluido dentro de las variables del sistema:
```cmd
C:\>python -m venv c:\ruta\al\entorno\virtual
```
En macOS y Linux:
```bash
$ python -m venv ruta/al/entorno/virtual
```
Es recomendable que la carpeta para el entorno virtual sea una subcarpeta del proyecto Python al que está asociado.

- Para activar un entorno virtual:

En Windows:
```cmd
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```
En macOS y Linux:
```bash
$ source ruta/al/entorno/virtual/bin/activate
```
Sea cual sea nuestro sistema operativo, sabremos que el entorno virtual se ha activado porque su nombre aparece entre paréntesis delante del prompt.

- Para desactivar un entorno virtual:
  
Este comando es idéntico para Windows, macOS y Linux:
```bash
$ deactivate
```
- Para eliminar un entorno virtual:
  
En Windows:
```cmd
C:\>rmdir c:\ruta\al\entorno\virtual /s
```
En macOS y Linux:
```bash
$ rm -rf ruta/al/entorno/virtual
```
Eliminar un entorno virtual es tan sencillo como eliminar la carpeta que lo contiene. Por ello, esta operación también se puede realizar desde el correspondiente administrador de archivos. A este respecto, se debe tener cuidado al eliminar un entorno virtual, ya que esto puede afectar proyectos en curso que dependen de él

Otro aspecto importante de pip, es la posibilidad de manejar paquetes privados. Por ejemplo, si queremos utilizar una librería desarrollada en nuestra empresa que no está disponible públicamente, debemos crear un paquete privado e instalarlo en nuestros proyectos. Para ello, debemos seguir los siguientes pasos:

- Crear un archivo setup.py en la raíz de nuestro proyecto, en el que definamos la información básica del paquete. Aquí, podemos especificar el nombre del paquete, la versión, los autores y otras características.
  
- Compilar el paquete utilizando el siguiente comando:
```python
# En la raíz de nuestro proyecto
python setup.py sdist
```
Este comando generará un archivo .tar.gz en la carpeta “dist” de nuestro proyecto.

- Instalar el paquete privado en el ambiente virtual de nuestro proyecto:
```python
# En el directorio que contiene el archivo .tar.gz generado
pip install mi_paquete.tar.gz
```
De esta manera, nuestro paquete privado se instalará en el ambiente virtual de nuestro proyecto, listo para ser utilizado.

Pip es una herramienta muy poderosa que nos facilita enormemente la tarea de administrar las dependencias de nuestros proyectos. En definitiva, pip es una de las herramientas básicas que todo desarrollador de Python debería conocer para optimizar su trabajo.

 ### Prácticas Recomendadas:

- No se debe añadir manualmente ningún fichero dentro de una carpeta que almacena un entorno virtual. Esta carpeta sólo debe contener los ficheros que se crean por defecto al crear el entorno virtual y los paquetes adicionales que hayamos instalado con el comando pip.

- La carpeta del entorno virtual no debe incluirse a nuestra herramienta de control de versiones. En lugar de ello, es recomendable añadir un fichero requirements.txt con el listado de los paquetes necesarios para ejecutar el proyecto.

