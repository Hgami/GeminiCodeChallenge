from src.api_methods.post import post_api_call


class CheckBalance:
    @staticmethod
    def check_balance():
        return post_api_call('/v1/balances', None, 'check_balance_api')
