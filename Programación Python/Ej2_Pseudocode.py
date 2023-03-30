salarioBase = input("¿Cuál es el salario base?: ")
pagasExtras = input("¿Cuánto corresponde de pagas extras?: ")
complementos = input("¿Cuánto corresponde de complementos?: ")
otrosConceptosRetributivos = input("Indica el valor total de otros conceptos retributivos: ")
IRPF = input("Indica el IRPF: ")
segSocial = input("Indica cuánto debe pagar de Seg Social: ")

salarioBruto = salarioBase + pagasExtras + complementos + otrosConceptosRetributivos
deducciones = IRPF + segSocial
salarioNeto = salarioBruto - deducciones

print("El salario bruto es: " + salarioBruto)
print("El salario Neto es:" + salarioNeto)