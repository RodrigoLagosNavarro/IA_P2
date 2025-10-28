# ============================================================
# Enfoque 1: Problemas de satisfraccion de restricciones
# Autor: Rodrigo Lagos Navarro - Grupo 6E 2P
# ============================================================

# Este código implementa un CSP usando backtracking. Se busca asignar valores
# a las variables de manera que se cumplan todas las restricciones definidas.

class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables    # Lista de variables del problema
        self.domains = domains        # Diccionario con los posibles valores de cada variable
        self.constraints = constraints # Función que verifica restricciones entre dos variables
        self.solution = {}            # Diccionario donde se almacenará la solución parcial/completa

    def is_valid(self, var, value):
        # Comprueba si asignar 'value' a 'var' cumple las restricciones con las demás variables ya asignadas
        for other in self.solution:
            if not self.constraints(var, value, other, self.solution[other]):
                return False
        return True

    def backtrack(self):
        # Si ya se asignaron todas las variables, retorno la solución
        if len(self.solution) == len(self.variables):
            return self.solution

        var = self.select_unassigned_variable()  # Selecciono una variable sin asignar
        for value in self.domains[var]:
            if self.is_valid(var, value):
                self.solution[var] = value  # Asigno temporalmente
                result = self.backtrack()   # Intento continuar con la siguiente variable
                if result:
                    return result
                del self.solution[var]      # Retroceso si no se encontró solución

        return None  # Si no hay valores válidos, retorno None

    def select_unassigned_variable(self):
        # Retorna la primera variable sin asignar
        for var in self.variables:
            if var not in self.solution:
                return var
        return None

# Definición de variables y dominios
variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# Restricción: valores de las variables deben ser distintos
def constraints(var1, val1, var2, val2):
    return val1 != val2  

# Creo el objeto CSP y ejecuto backtracking
csp = CSP(variables, domains, constraints)
solution = csp.backtrack()

# Imprimo la solución encontrada o aviso si no existe
if solution:
    print("Solución encontrada:", solution)
else:
    print("No se encontró solución.")
