from src.api_methods.post import post_api_call


class ActiveOrders:
    @staticmethod
    def active_orders():
        return post_api_call('/v1/orders', None, 'get_active_orders')
