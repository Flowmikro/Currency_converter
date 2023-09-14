from flask import Flask, request, jsonify

from services import convert_currency

app = Flask(__name__)


@app.route('/api/rates', methods=['GET'])
def get_rates():
    """Получаем с конвертированную валюту """
    to_currency = request.args.get('to')  # to=RUB
    from_currency = request.args.get('from')  # from=USD
    amount_currency = request.args.get('value')  # value=1
    result = convert_currency(to_currency, from_currency, amount_currency)  # вызываем функцию для
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
