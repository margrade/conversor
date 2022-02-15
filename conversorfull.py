valor_dolar=212
option= input("Presione 1 si desea convertir de dólares a pesos; Presione 2 si desea convertir de pesos a dólares: ")

if option=="1":
    dolares= input("¿Cuántos dólares desea convertir?: ")
    dolares=float(dolares)
    pesos=(dolares*valor_dolar)
    pesos=str(round(pesos,2))
    print("La cantidad de pesos argentinos disponible es de $ "+pesos +" pesos")

if option=="2":
    pesos= input("¿Cuántos pesos desea convertir?: ")
    pesos=float(pesos)
    dolares=(pesos/valor_dolar)
    dolares=str(round(dolares,2))
    print("La cantidad de dólares disponible es de $ "+dolares +" dólares")
