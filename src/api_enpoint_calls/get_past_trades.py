from src.api_methods.post import post_api_call


class GetPastTrades:
    @staticmethod
    def get_past_trades(symbol):
        payload = {
            'symbol': symbol
        }
        return post_api_call('/v1/mytrades', payload, 'get_past_trades')
