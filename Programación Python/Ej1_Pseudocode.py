tablaLetrasDNI = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

dni = 0

while len(dni) != 8 or not isintance(dni, int):

    dni = input()
    if len(dni) == 8 and isinstance(dni, int):
        print()