# Ejercicios con algoritmos



## Primeros 3 ejercicios



### Ejercicio 1



*Calcular la letra del DNI Español*



**Paso 1**: Definir el problema

- A partir de un número de DNI hemos de calcular la letra.

¿Cómo se calcula la letra del DNI?

Número del DNI dividido entre 23 y el resto será el ``` resultadoResto ```

El ``` resultadoResto ``` lo compararemos con la lista de códigos de la siguiente tabla de letras ```tablaLetrasDni``` 



| resultadoResto | Letra |
| -------------- | ----- |
| 0              | T   |
| 1              | R   |
| 2              | W   |
| 3              | A   |
| 4              | G   |
| 5              | M   |
| 6              | Y   |
| 7              | F   |
| 8              | P   |
| 9              | D   |
| 10             | X   |
| 11             | B   |
| 12             | N   |
| 13             | J   |
| 14             | Z   |
| 15             | S   |
| 16             | Q   |
| 17             | V   |
| 18             | H   |
| 19             | L   |
| 20             | C   |
| 21             | K   |
| 22             | E   |



**Paso 2**: Poner la entrada, el proceso y la salida

Entrada: ```DNI``` y ```tablaLetrasDni```
Proceso:
 - Validar que el DNI tenga 8 dígitos, y que sean todos numéricos.
   - Si es errónea asigne la variable ```resultado``` "DNI inválido"
 - Dividimos DNI entre 23 y el resto lo asignamos a resultadoResto.
 - Comparar el ```resultadoResto``` con los valores de la tabla, asignemos a ```letraDNI``` el valor equivalente de la tabla.

Salida: ```resultado```

**Paso 3**: Escribir el pseudocódigo

```
 Algoritmo CalculoDNI

  DNI <- 0
  tablaLetrasDni[] <- ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

  Hacer

      Leer DNI

      Si longitud DNI > 8 o longitud DNI < 8 Entonces
          resultado <- "DNI inválido"

  Mientras longitud DNI > 8 o longitud DNI < 8

  resultadoResto <- DNI % 23

  Para i=0 Hasta longitud tablaLetrasDni -1 Hacer

      Si resultadoResto-1 = i Entonces
          resultado <- tablaLetrasDni[i]
  Fin Para
      Escribir "La letra de este DNI es " + resultado

 Fin Algoritmo
```


### Ejercicio 2

 *Calcular el salario de un empleado*

 **Paso 1**

 El salario en España se calcula a partir del salario bruto anual, que incluye todas las percepciones económicas que recibe un trabajador durante el año, incluyendo salario base, pagas extras, complementos y otros conceptos retributivos.

 A partir del salario bruto se deducen las cotizaciones a la Seguridad Social y el impuesto sobre la Renta de las Personas Físicas (IRPF), que varían en función del nivel salarial y la situación personal del trabajador.

 **Paso 2**

 Entrada: ```salarioBase```, ```pagasExtras```, ```complementos```, ```otrosConceptosRetributivos```, ```IRPF```, ```seguridadSocial```

 Proceso: 
  - Sumar ```salarioBase```, ```pagasExtras```, ```complementos```, ```otrosConceptosRetributivos``` y asignarlo a ```salarioBruto```
  - Sumar ```IRPF```, ```seguridadSocial``` y asignarlo a ```deducciones```
  - ```salarioNeto``` es igual a ```salarioBruto``` - ```deducciones```


 Salida: (```salarioBruto```, ```salarioNeto```)

 **Paso 3**

```
Algoritmo CalculoSalario

  Inicio

    Leer salarioBase
    Leer pagasExtras
    Leer complementos
    Leer otrosConceptosRetributivos
    Leer IRPF
    Leer seguridadSocial

    salarioBruto <- salarioBase + pagasExtras + complementos + otrosConceptosRetributivos
    deducciones <- IRPF + seguridadSocial
    salarioNeto <- salarioBruto - deducciones

    Escribir (salarioBruto, salarioNeto)

  FIn

Fin Algoritmo
```


### Ejercicio 3

 *Determinar la ruta para llegar a una ciudad por avión*

**Paso 1**

 Las rutas de vuelo están ya predefinidas en función de la compañia, por desgracia rutas que sean demasiado largas requerirán de transbordos por lo que se habrá de calcular cuál es la ruta más efectiva para llegar desde un punto X a un punto Y en el menor número de transbordos posibles.

**Paso 2**

 Entrada: ```origen``` y ```destino```
 Proceso: 
  - Localizamos el sitio de origen y el sitio de destino
  - Obtenemos todos los viajes que poseen
  - Mostramos los viajes involucrados
 Salida: ```ruta```

**Paso 3**

 ```
 Algoritmo RutasVuelo

  Inicio
 
    madrid1[] <- ["Madrid", "Bruselas"]
    madrid2[] <- ["Madrid", "WashintonDC"]
    bruselas1[] <- ["Bruselas", "Seúl"]
    bruselas2[] <- ["Bruselas", "WashintonDC"]
    seul1[] <- ["Seúl", "Tokyo"]
    seul2[] <- ["Seúl", "Canadá"]
    tokyo1[] <- ["Tokyo", "WashintonDC"]
    whashintonDC1[] <- ["WhashintonDC", "Canadá"]

    rutas[][] <- [madrid1, madrid2, bruselas1, bruselas2, seul1, seul2, tokyo1, washintonDC1]

    listaOrigenes <- {}
    listaDestinos <- {}

    Leer origen
    Leer destino

    Para i = 0 hasta rutas.Longitud-1 con paso i+1 Hacer

      Si rutas[i][0] Es Igual A origen O destino Y rutas[i][1] Es Igual A origen O destino Entonces
        Mostrar("Vuelo directo desde origen hasta destino")
      Sino
        Mostrar "No existen vuelos directos, calculando transbordo..."

        Para i = 0 hasta rutas.Longitud-1 con paso i+1 Hacer
          Para j = 0 hasta 1 con paso j+1 Hacer
            Si rutas[i][j] Es Igual A origen Entonces
              listaOrígenes.Añadir(rutas[i])
            Sino
              Si rutas[i][j] Es Igual A destino Entonces
                listaDestinos.Añadir(rutas[i])
              Fin Si
            Fin Si
          Fin Para
        Fin Para

        Para Cada ruta En listaOrigenes Hacer
          Si ruta[0] Es Igual A origen Entonces
            Para Cada ruta2 En listaDestinos Hacer
              Si ruta[1] Es Igual A ruta2[0] O ruta2[1] Entonces
                Mostrar "Tu vuelo desde origen debe pasar por ruta[1] para llegar hasta destino"
              Fin Si
            Fin Para
          Fin Si
        Fin Para
      Fin Si
    Fin Para

  Fin
 ```


### Ejercicio 4

 *Calcula el área y perímetro de un círculo dado su radio*

**Paso 1**

 El perímetro de un círculo se obtiene multiplicando pi por el diámetro del círculo mientras que el área se calcula multiplicando pi por el radio al cuadrado.

**Paso 2**

 Entrada: ``Area``, ``Perimetro``, ``Pi``, ``Radio``

 Proceso:
 - Multiplicar ``Radio`` por sí mismo, por ``Pi y asignar`` a  ``Area``
 - Multiplicar ``Radio`` por ``π``, por 2 y asignar a ``Perímetro``

 Salida:
 Escribir ``Area`` y ``Perímetro``

**Paso 3**

 ```
 Algoritmo AreaPerimetro
	# Entrada
	Radio<-Leer()
	Pi<-3,14159264
	# Proceso
	Area<-RadioxRadioXπ
	Perímetro<-Radioxπx2
	# Salida
	Escribir (Area, Perímetro)
 Fin Algoritmo
 ```


### Ejercicio 5

 *Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor*

**Paso 1**

 La comparación se realizará de forma sistemática guardando los números en una colección y ordenádolos usando bucles hasta que el mayor quede al final de la colección y el menor al principio.

**Paso 2**

 Entrada: ``Listanum``
 Proceso:
 - Hacer un bucle de resta de número de la lista
 - según los resultados asignar los números a ``mayornum`` y ``menornum``
 Salida:
Escribir  ``mayornum`` y ``menornum``

**Paso 3**

 ```
 Algoritmo comparadordetamaños
	# Entrada
	Listanum<-Leer()
	mayornum<-listanum[0]
	menornum<-Listanum[0]
	
	# Proceso
	Para i=0 hasta Listanum.lungitud-1 con paso 1 hacer
		si Listanum[i]>mayornum
			mayornum<-Listanum[i]
		sino si Listanum[i]<menormun
			menornum<-Listanum[i]		
		Finsi
	# Salida
 Fin Algoritmo
 ```


### Ejercicio 6

 *Crea un algoritmo que convierta grados Celsius a Fahrenheit*

**Paso 1**

 La transformación de grados Celsius a Fahrenheit se determina multiplicando los grados Celsius por 9, dividiendo el resultado entre 5 y sumándole 32.

**Paso 2**

 Entrada: ``GradosCelsius``, ``GradosFahrenheit``
 Proceso:
 - Multiplicar ``GradosCelsius`` por 1,8, sumarle 32 y asignarle ``GradosFahrenheit``
 Salida:
 Escribir ``GradosFahrenheit``.

**Paso 3**

 ```
 Algoritmo conversorGrados
	# Entrada
	GradosCelsius<-Leer()
	# Proceso
	GradosFahrenheit <- GradosCelsius * 1,8 + 32
	# Salida
	Escribir (GradosFahrenheit)
 Fin Algoritmo
 ```



### Ejercicio 7

 *Dado un número entero, crea un algoritmo que determine si es par o impar*

**Paso 1**

 Si el resto del número entero es 0, el número es par.

**Paso 2**

 Entrada: ``Numero``

 Proceso:
 - Dividir ``Numero`` entre 2.
 - Asignar en funcion del resultado un boolean de verdadero o falso a ``ResultadoPar``

 Salida:
 Si ``resultadoPar``=verdadero, escribir "Tu número es par"
 Si ``resultadoPar``=falso, escribir "Tu número es falso"

**Paso 3**

 ```
 Algoritmo parimpar
	# Entrada
	Numero<-Leer()
	# Proceso
	si numero mod 2 = 0 Entonces
		resultadoPar=verdadero
	sino
		resultadoPar=falso
	Fin si
	# Salida
	Si resultadoPar=verdadero
		escribir "Tu número es par"
	Sino
		escribir "Tu número es impar"
	Fin si
 Fin Algoritmo
 ```


### Ejercicio 8

 *Crea un algoritmo que determine si un año es bisiesto o no*

**Paso 1**

  1. Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
  2. Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 
  3. Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 
  4. El año es un año bisiesto (tiene 366 días).
  5. El año no es un año bisiesto (tiene 365 días).

**Paso 2**

 Entrada: ```anyo```
 
 Proceso: 
  - Comprobar mediante una condición si es divisible entre 4, 400 y 100
  - Dependiendo del resultado se determinará si es bisiesto o no
 
 Salida: ``bisiesto``

**Paso 3**

 ```
 Sub Algoritmo EsBisiesto (anyo)
	Si anyo%4=0 o anyo%400=0 y anyo%100<>0 Entonces
		Bisiesto=True
		
	SiNo
		Bisiesto=False
	Fin Si
 Fin Sub Algoritmo
		
  Sub Algoritmo AñoBisiesto
	Escribir "Introduzca un anyo"
	Leer anyo
	Si (EsBisiesto(anyo)) entonces
		Escribir anyo+" es bisiesto"
	Si No
		Escribir anyo+" no es bisiesto"
 FinAlgoritmo
 ```


### Ejercicio 9

 *Crea un algoritmo que determine si una cadena de texto es un palíndromo o no*

**Paso 1**

 Para calcular palíndromos debemos obtener el string de la palabra o frase, quitarle toda la puntuación y espacios e invertirla, si ambos valores de string son idénticos es que la palabra/frase es un palíndromo

**Paso 2**

 Entrada: ```frase```, ```copia```
 
 Proceso:
 - El primer paso es eliminar de la cadena de texto ``frase`` todos los elementos no alfanuméricos como comas, puntos e incluso los espacios
 - Asignamos a ``copia`` el valor de frase
 - Invertimos la cadena de ``copia``
 - Comparamos ambas cadenas y si son iguales diremos que ``esPalindromo`` es verdadero, de lo contrario será falso
 
 Salida: ```esPalindromo```

**Paso 3**

 ```
 Algoritmo Palindromo
   # Entrada
   cadena <- leer()
   #Proceso
   #cadena <- Convertir a minúsculas y eliminar espacios en blanco
   reversa <- depuracionCadena(cadena)
   Si cadena es igual a reversa entonces
     resultado <- "La cadena es un palíndromo"
   Sino
     resultado <- "La cadena no es un palíndromo"
   Fin Si
   # Salida
   escribir resultado
Fin Algoritmo

SubAlgoritmo depuracionCadena (cadena)
    #quita los espacios en blanco, otros caracteres y convierte todo a minusculas
    i<-0
    Mientras cadena[i] sea diferente de findecadena Haga
        caracter<-""
        Si  el ASCII de cadena[i]  mayor que 64 y ASCII de cadena[i] menor que 91 Entonces
            caracter<-cadena[i] en minusculas
        Fin Si
        Si  el ASCII de cadena[i]  mayor que 96 y ASCII de cadena[i] menor que 123 Entonces
            caracter<-cadena[i]
        End Si
        temporal <- temporal + caracter
        Si caracter es diferente "" Entonces
            i<-i+1
        Fin Si
    Fin Mientras
    L<-i
    reversa<-""
    Para N = 0 Hasta L-1 Con Paso 1 Haga
        reversa    <-reversa+ temporal[i-1]
        i<-i-1
    Fin Para
    devuelva reversa
Fin SubAlgoritmo
 ```



### Ejercicio 10

 *Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente*

**Paso 1**

 Para ordenar alfabéticamente primero tendremos que obtener el orden alfabético de cada nombre comparándolos con el alfabeto. Una vez hecho esto, se organizarán los nomrbres en función de su posición otorgada.

**Paso 2**

 Entrada: ``listaPalabras``, ``palabra``
 
 Proceso: 
  - Pedir palabras hasta satisfacer al usuario
  - Agregar las palabras a una colección
  - Ordenar la colección
 
 Salida: ``listaPalabras``

**Paso 3**

 ```
 Algoritmo

  listaPalabras <- {}

  Hacer

    Mostrar "Introduce palabras para agregar a la lista"

    Leer palabra

    Si palabra Distinto de 0 Entonces
      listaPalabras <- añadir(palabra)      
    Fin Si
  Mientras palabra Distinto de 0

  Mostrar Ordenar(listaPalabras)

 Fin
 ```


### Ejercicio 11

 *Crea un algoritmo que calcule el factorial de un número entero*

**Paso 1**

 El factorial de un entero positivo n, el "factorial de n" o "n factorial" se define en principio como el producto de todos los números enteros positivos desde 1 (es decir, los números naturales) hasta n. Por ejemplo:

**Paso 2**

 Entrada: ``num``

 Proceso: 
  - Pedimos un número para realizarle el factorial
  - Multiplicamos ese número por el que va antes hasta llegar a 0
  - Una vez se llegue a 0 se dejará de multiplicar

 Salida: ``resultado``

**Paso 3**

 ```
 Algoritmo NúmeroFactorial

  Inicio

    resultado <- 0

    Hacer

      Leer num

      Si num No Es Entero Entonces
        Mostrar "El número introducido debe ser un entero."
      Fin Si
    Mientras num No Es Entero

    Factorial(num, resultado)

    Mostrar resultado

  Fin
 ```

Sub Algoritmo Factorial(n, resultado)

  resultado = resultado + Factorial(n-1)

Fin Sub Algoritmo

### Ejercicio 12

 *Dado un número entero, crea un algoritmo que determine si es primo o no*

**Paso 1**

 Si el número sólo es divisible entre 1 y él mismo es primo

**Paso 2**

 Entrada: ``num``

 Proceso: 
  - Pedimos un número natural
  - Lo intentamos dividir entre todos los números anteriores hasta 1
  - Si sólo es divisible entre 1 y él mismo hacer ``esPrimo`` verdadero

 Salida: ``esPrimo``

**Paso 3**

 ```
 Algoritmo

  Inicio
 
    resultado <- 0
    EsPrimo <- Verdadero

    Hacer

      Leer num

      Si num No Es Entero O num <= 0 Entonces
        Mostrar "El número introducido debe ser un entero superior a 0."
      Fin Si
    Mientras num No Es Entero O num <= 0

    Para i = num-1 Hasta 2 Con Paso -1 Hacer

      Si num mod i = 0 Entonces
        EsPrimo = Falso
      Fin Si
    Fin Para

    Si EsPrimo = Verdadero Entonces
      Mostrar num + " es un número primo"
    Sino
      Mostrar num + " no es un número primo"
    Fin Si

  Fin
 ```


### Ejercicio 13

 *Crea un algoritmo que calcule el área y volumen de un cubo dado su lado*

**Paso 1**

 Explicación del ejercicio y solución

**Paso 2**

 Entrada: ``lado``

 Proceso:
  - El lado se pedirá en metros para mayor facilidad
  - Se calcula el área del cubo elevando a 2 la medida del lado
  - El volumen se calculará elevando a 2 la medida del lado

 Salida: ``area``, ``volumen``

**Paso 3**

 ```
 Algoritmo Cubo
 
  Hacer

    Mostrar "Introduce la longitud del lado en metros"

    Leer lado

    Si lado No Es Numérico Entonces O lado < 0
      Mostrar "El valor introducido debe ser un número superior a 0."
    Fin Si
  Mientras lado No Es Numérico Y lado <= 0

  area <- lado * lado

  volumen <- lado * lado * lado

  Mostrar "El área del cubo es de " + area + " metros cuadrados mientras que su volumen es de " + volumen + " metros cúbicos o " + volumen*1000 + " Litros."

 Fin Algoritmo
 ```


### Ejercicio 14

 *Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista*

**Paso 1**

 Se pedirán números hasta que el usuario esté satisfecho, entonces se hará un sumatorio de los números pares y se mostrará el resultado por pantalla

**Paso 2**

 Entrada: ``num``, ``listaNum``

 Proceso:
  - Pedimos números y los agregamos a ``listaNum``
  - Sumamos todos los números pares en la variable ``resultado``

 Salida: ``resultado``

**Paso 3**

 ```
 Algoritmo SumaPares

  listaNum <- {}
  resultado <- 0

  Hacer

    Mostrar "Introduce un número superior a 0, cuando quieras dejar de introducir números escribe 0"

    Leer num

    Si num < 0 Entonces
      Mostrar "El valor introducido debe ser un número superior a 0."
    Sino
      listaNum <- añadir(num)
    Fin Si
  Mientras num Distinto de 0

  Para i=0 Hasta longitud listaNum-1 Con Paso 1

    Si listaNum[i] mod 2 = 0 Entonces
      resultado = resultado + listaNum[i]
    Fin Si
  Fin Para
  
  Mostrar resultado

 Fin Algoritmo
 ```


### Ejercicio 15

 *Crea un algoritmo que determine si un número es positivo, negativo o cero*

**Paso 1**

 Si el número es superior a 0 el valor será positivo, si es menor que 0 será negativo o de lo contrario es que el número otorgado es 0

**Paso 2**

 Entrada: ``num``
 
 Proceso:
 - Pedimos un número
 - Si el número es superior a 0 el valor será positivo
 - Si el número es menor que 0 será negativo
 - Si no es ni positivo ni negativo es que el número introducido es 0

 Salida: ``mensaje``

**Paso 3**

 ```
 Algoritmo PositivoNegativo

  mensaje <- ""

  Mostrar "Introduce un número"

  Hacer

    Leer num

    Si num No Es Numérico Entonces
      Mostrar "El valor introducido debe ser un número."
    Fin Si
  Mientras num No Es Numérico
  
  Si num < 0 Entonces
    Mensaje <- "El número introducido es negativo"
  Sino Si num > 0 Entonces
    Mensaje <- "El número introducido es positivo
  Sino
    Mensaje <- "El número introducido es 0"
  Fin Si

  Mostrar mensaje

 Fin Algoritmo
 ```


### Ejercicio 16

 *Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista*

**Paso 1**

 Primero se pedirá una lista donde se almacenarán números enteros, luego se sumarán todos los números de dicha lista y, finalmente, se dividirá el resultado entre la cantidad de números que contiene la lista.

**Paso 2**

 Entrada: ``num``, ``listaNum``

 Proceso:
  - Pedimos números y los agregamos a ``listaNum``
  - Sumamos todos los números de ``listaNum``
  - Dividimos el resultado por la longitud de ``listaNum``

 Salida: ``resultado``

**Paso 3**

 ```
 Algoritmo MediaAritmética

  listaNum <- {}
  resultado <- 0

  Hacer

    Mostrar "Introduce un número, cuando quieras dejar de introducir números escribe 0"

    Leer num

      listaNum <- añadir(num)
  Mientras num Distinto de 0
  
  Para i = 0 Hasta longitud listaNum -1 Con Paso 1

    resultado = resultado + listaNum[i]
  Fin Para

  resultado = resultado / longitud listaNum

  Mostrar resultado

 Fin
 ```


### Ejercicio 17

 *Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto*

**Paso 1**

 Es un juego donde el usuario debe introducir números y la consola le dice si el número que ha introducido es mayor o menor que el correcto hasta que acierte.

**Paso 2**

 Entrada: ``intento``

 Proceso:
  - Crearemos un número aleatorio del 1 al 100 en ``objetivo``
  - Le pediremos un número al jugador
  - Le diremos si el número objetivo es superior o inferior al número otorgado por el jugador
  - Si el jugador acierta se acaba la partida

 Salida: Mostrar "Enhorabuena has ganado"

**Paso 3**

 ```
 Algoritmo AdivinaNúmeros

  objetivo <- Random(1-100) #La función Random asigna un número entero aleatorio entre un rango de números otorgado

  Hacer

    Mostrar "Introduce un número entero del 1 al 100"

    Leer intento

    Si intento < 1 O intento > 100 O intento No Es Entero Entonces
      Mostrar "El valor introducido debe ser un número entero superior a 0."
    Sino Si intento < objetivo Entonces
      Mostrar "El número introducido es menor al correcto"
    Sino Si intento > objetivo
      Mostrar "El número introducido es mayor al correcto"
    Fin Si
  Mientras intento Distinto De objetivo

  Mostrar "Enhorabuena has ganado"

 Fin
 ```


### Ejercicio 18

 *Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto*

**Paso 1**

 Un anagrama es la formación de palabras mediante la manipulación de las letras de otras palabras.

**Paso 2**

 Entrada: ``cadena1``, ``cadena2``

 Proceso:
  - Pediremos ambas cadenas
  - Compararemos los caracteres de ambas cadenas y, si son exactamente los mismos, significará que es un anagrama

 Salida: Mostrar por pantalla si es anagrama o no

**Paso 3**

 ```
 Algoritmo Anagramas

  Inicio
 
    Leer cadena1
    Leer cadena2
    temp <- cadena2
    contador <- 0

    Para i = 0 Hasta longitud cadena1 Con Paso 1 Hacer
      Para j = 0 Hasta longitud cadena2 Con Paso 1 Hacer
        Si cadena1[i] = cadena2[j] Entonces
          Borrar(temp[j - contador])
          contador = contador + 1
        Fin Si
      Fin Para
    Fin Para

    Si temp = "" Entonces
      Mostrar cadena1 + " y "+ cadena2 + " son anagramas"
    Sino
      Mostrar cadena1 + " y "+ cadena2 + " no son anagramas"
    Fin Si

  Fin
 ```


### Ejercicio 19

 *Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista*

**Paso 1**

 Hay que borrar los números duplicados de la lista

**Paso 2**

 Entrada: ``num``, ``listaNum``

 Proceso:
  - Pedimos números hasta la satisfacción del usuario
  - Comparamos los números dentro de la lista
  - Los números duplicados serán borrados de una lista que ha ido recogiendo los duplicados llamada ``temp``

 Salida: ``listaNum``

**Paso 3**

 ```
 Algoritmo Duplicados
 
  listaNum <- {}
  
  Hacer

    Mostrar "Introduce un número, cuando quieras dejar de introducir números escribe 0"

    Leer num

      listaNum <- añadir(num)
  Mientras num Distinto de 0

  temp <- {}

  Para i = 0 Hasta longitud listaNum Con Paso 1 Hacer
    Para j = 0 Hasta longitud listaNum Con Paso 1 Hacer
      Si listaNum[i] = listaNum[j] Y temp No Contiene listaNum[j] Entonces
        temp <- añadir(listaNum[j])
      Fin Si
    Fin Para
  Fin Para

  Para i = 0 Hasta longitud temp Con Paso 1 Hacer
    Para j = 0 Hasta longitud listaNum Con Paso 1 hacer
      Si listaNum[j] Es Igual A temp[i] Entonces
        Borrar listaNum[j]
      Fin Si
    Fin Para
  Fin Para

  Mostrar "La lista sin duplicados es esta " + listaNum

 Fin
 ```


### Ejercicio 20

 *Crea un algoritmo que determine si un número es capicúa o no*

**Paso 1**

 Un número capicúa es aquel que se lee igual tanto del derecho como del revés

**Paso 2**

 Entrada: ``num``

 Proceso:
  - Pedimos un número
  - Si al invertir el número el resultado es el mismo entonces el número otorgado será capicua

 Salida: Mostrar por pantalla si el número es capicúa o no

**Paso 3**

 ```
 Algoritmo Capicua
 
  num <- 0

  Hacer
  
    Leer num

    Si num No Es Entero Entonces
      Mostrar "El valor introducido debe ser un número entero."
    Fin Si
  Mientras num No Es Entero

  copia <- num
  Invertir(copia)

  Si copia Es Igual A num Entonces
    Mostrar "El número es capicúa"
  Sino
    Mostrar "El número no es capicúa"
  Fin Si

 Fin
 ```
