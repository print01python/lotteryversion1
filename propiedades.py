# propiedades_numeros.py


def obtener_propiedades_numeros(numeros):
    propiedades = []
    for lista_numeros in numeros:
        for numero in lista_numeros:
            propiedades_numero = {
                "numero": numero,
                "es_entero": es_entero(numero),
                "es_natural": es_natural(numero),
                "es_racional": es_racional(numero),
                "es_irracional": es_irracional(numero),
                "es_real": es_real(numero),
                "es_compuesto": es_compuesto(numero),
                "es_positivo": es_positivo(numero),
                "es_negativo": es_negativo(numero),
                "es_decimal_finito": es_decimal_finito(numero),
                "es_cardinal": es_cardinal(numero),
                "es_ordinal": es_ordinal(numero),
                "es_par": es_par(numero),
                "es_impar": es_impar(numero),
                "es_primo": es_primo(numero),
            }
            propiedades.append(propiedades_numero)
    return propiedades


def es_par(numero):
    return numero % 2 == 0


def es_impar(numero):
    return numero % 2 != 0


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def es_entero(numero):
    return isinstance(numero, int)


def es_natural(numero):
    return numero > 0 and isinstance(numero, int)


def es_racional(numero):
    try:
        # Intenta convertir el número a un número racional
        racional = float(numero)
        return True
    except ValueError:
        return False


def es_irracional(numero):
    return not es_racional(numero)


def es_real(numero):
    return es_racional(numero) or es_irracional(numero)


def es_compuesto(numero):
    # Verifica si el número es compuesto
    if numero > 1:
        for i in range(2, int(numero**0.5) + 1):
            if (numero % i) == 0:
                return True
        return False
    return False


def es_positivo(numero):
    return numero > 0


def es_negativo(numero):
    return numero < 0


def es_decimal_finito(numero):
    # Verifica si el número es un decimal finito
    return "." in str(numero)


def es_cardinal(numero):
    # Verifica si el número es un cardinal (número natural utilizado para contar)
    return es_natural(numero)


def es_ordinal(numero):
    # Verifica si el número es un ordinal (número natural utilizado para ordenar)
    return es_natural(numero)
