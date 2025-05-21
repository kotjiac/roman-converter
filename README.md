# Conversor numeral romano para hindu-arábico

## Uso

### Instalação de Dependências
Para instalar as dependências necessárias, execute o seguinte comando:
```bash
pip install -r requirements.txt
```

### Executando a Aplicação Flask
Para iniciar o servidor Flask, execute:
```bash
python app.py
```
A API estará disponível em `http://127.0.0.1:5000`.

### Exemplos de Uso da API

Para converter um numeral romano para inteiro, use o endpoint `/romantointeger/<numeral_romano>`.

Exemplo de sucesso:
```bash
curl http://127.0.0.1:5000/romantointeger/MCMLXXXI
```
Saída esperada:
```json
{
  "integer": 1981
}
```

Exemplo de numeral inválido:
```bash
curl http://127.0.0.1:5000/romantointeger/INVALID
```
Saída esperada:
```json
{
  "details": "'I' is not a valid Roman numeral character.",
  "error": "Invalid Roman numeral"
}
```

## Testes

```bash
python -m unittest test_roman_converter.py
```