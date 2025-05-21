import re

def roman_to_int(s: str) -> int:
    # Função para verificar se o numeral romano é válido
    def is_valid_roman(s: str) -> bool:
        # Expressão regular para verificar se o numeral romano é válido
        pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return re.match(pattern, s) is not None
    
    if not is_valid_roman(s):
        raise ValueError("Numeral romano inválido")
    
    # Mapeamento dos numerais romanos para os valores correspondentes
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    # Inicializa a variável de resultado
    result = 0
    # Variável para armazenar o valor do numeral romano anterior
    prev_value = 0
    
    # Percorre cada caractere do numeral romano, da direita para a esquerda
    for char in reversed(s):
        # Obtém o valor do numeral romano atual
        value = roman_values[char]
        
        # Se o valor atual for menor que o valor anterior, subtrai o valor atual
        if value < prev_value:
            result -= value
        else:
            # Caso contrário, adiciona o valor atual
            result += value
        
        # Atualiza o valor do numeral romano anterior
        prev_value = value
    
    return result