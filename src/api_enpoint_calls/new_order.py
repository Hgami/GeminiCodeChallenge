from src.api_methods.post import post_api_call


class NewOrder:
    @staticmethod
    def new_order(api_call_name, symbol, amount, price, side, type_order, options=["immediate-or-cancel"]):
        payload = {
            'symbol': symbol,
            'amount': amount,
            'price': price,
            'side': side,
            'options': options,
            'type': type_order
        }
        return post_api_call('/v1/order/new', payload, api_call_name)
