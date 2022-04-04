from src.api_enpoint_calls.check_balance import CheckBalance
from src.api_enpoint_calls.new_order import NewOrder
from src.api_enpoint_calls.get_past_trades import GetPastTrades
from src.api_enpoint_calls.get_active_orders import ActiveOrders
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

symbol = 'btcusd'

"""
   This file contains all the test functions related for new order api calls  
   The one which are commented, can also be used after uncommenting them.
   
   Below two api calls are meant to be failed as part of negative testing
    test_stop_limit_buy_order()
    test_rate_limit_buy_orders()

   Below 3 api calls should be succesded as part of positive testing 
    test_new_buy_order()
    test_new_sell_order()
    test_stop_limit_sell_order()
   
"""


def test_new_buy_order():
    new_buy_order = NewOrder().new_order('test_new_buy_order', symbol, "1", "40000", "buy", "exchange limit",
                                         ["maker-or-cancel"])
    print('New Buy order id is : {}'.format(new_buy_order['order_id']))
    validate_response_fields_for_order(new_buy_order)
    get_all_active_order_details(new_buy_order['order_id'])


def test_new_sell_order():
    new_sell_order = NewOrder().new_order('test_new_sell_order', symbol, "1", "50000", "sell", "exchange limit",
                                          ["maker-or-cancel"])
    print('New Sell order id is : {}'.format(new_sell_order['order_id']))
    validate_response_fields_for_order(new_sell_order)
    get_all_active_order_details(new_sell_order['order_id'])


def test_stop_limit_buy_order():
    NewOrder().new_order('test_stop_limit_buy_order', symbol, "1", "40000", "buy", "exchange stop limit",
                         ["maker-or-cancel"])


def test_stop_limit_sell_order():
    new_stop_limit_sell_order = NewOrder().new_order('test_stop_limit_sell_order', symbol, "1", "25000", "sell",
                                                     "exchange stop limit", ["maker-or-cancel"])
    print('New Stop Sell order id is : {}'.format(new_stop_limit_sell_order['order_id']))
    validate_response_fields_for_order(new_stop_limit_sell_order)
    get_all_active_order_details(new_stop_limit_sell_order['order_id'])


def test_rate_limit_buy_orders():
    NewOrder().new_order('test_multiple_buy_order', symbol, "1", "40000", "buy", "exchange limit", ["maker-or-cancel"])


def validate_response_fields_for_order(order_response):
    assert type(order_response) is dict
    assert "order_id" in order_response
    assert "id" in order_response
    assert "symbol" in order_response
    assert "exchange" in order_response
    assert "avg_execution_price" in order_response
    assert "side" in order_response
    assert "type" in order_response
    assert "timestamp" in order_response
    assert "timestampms" in order_response
    assert "is_live" in order_response
    assert "is_cancelled" in order_response
    assert "is_hidden" in order_response
    assert "was_forced" in order_response
    assert "executed_amount" in order_response
    assert "options" in order_response
    assert "price" in order_response
    assert "original_amount" in order_response
    assert order_response['symbol'] == symbol, 'Invalid symbol : {}'.format(order_response['symbol'])
    assert order_response['original_amount'] == '1', 'Invalid Amount  : {}'.format(order_response['original_amount'])
    assert order_response['is_live'] == True, 'Order should be currently active  : {}'.format(order_response['is_live'])


def validate_new_order_id_in_active_trades(active_order_details, expected_order_id):
    for i in active_order_details:
        if i.get('order_id') == expected_order_id:
            logging.info('New Order id  {} found in active trade status'.format(expected_order_id))
        else:
            SystemExit('New Order id  {} did-not found in active trade status'.format(expected_order_id))


def get_all_active_order_details(expected_order_id):
    active_order_details = ActiveOrders().active_orders()
    validate_new_order_id_in_active_trades(active_order_details, expected_order_id)


def get_all_past_trades_for_btc():
    past_trades = GetPastTrades().get_past_trades(symbol)
    logging.info(past_trades)


def check_balance_in_btc():
    btc_balance = CheckBalance().check_balance()
    logging.info(btc_balance)


test_new_buy_order()
test_new_sell_order()
test_stop_limit_sell_order()
test_stop_limit_buy_order()
test_rate_limit_buy_orders()

# get_all_past_trades_for_btc()
# check_balance_in_btc()
