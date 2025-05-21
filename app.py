from flask import Flask, jsonify
from roman_converter import roman_to_int

app = Flask(__name__)

@app.route('/romantointeger/<string:roman_numeral>', methods=['GET'])
def convert_roman_to_integer(roman_numeral):
    try:
        result = roman_to_int(roman_numeral)
        return jsonify({"integer": result}), 200
    except ValueError as e:
        return jsonify({"error": "Invalid Roman numeral", "details": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
