class Operaciones:
    def sumar(self, numero1, numero2):  
        return numero1 + numero2

    def restar(self, numero1, numero2):  
        return numero1 - numero2

    def multiplicar(self, numero1, numero2):  
        return numero1 * numero2

    def dividir(self, numero1, numero2):  
        if numero2 == 0:
            return "Error: No se puede dividir por cero"
        return numero1 / numero2