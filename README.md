# GeminiCodeChallenge
This is a code challenge assignment for Gemini focuses on  'New Order API calls'

####Assumption
    All the api calls are for BTCUSD
    Amount : 1 
    All the Order Request will have response isLive = True ( That means it should be part of order-active status
    Just run test_function.py file to execute the code.
    Not adding requirnments.txt file as python3 is needed. 

####Test Cases
    In this assignment I have created 5 different test functions & they are as follows  

    All the test validates the following 

    1. Proper Signature header while sending request 
    2. Validate Response Status
    3. Validate Response fields 
    4. Validate that "New Order" is actually part of Currently Active Order List 
    5. Stop limit buy order will fail 

   Below two api calls are meant to be failed as part of **Negative Testing**

      1. test_stop_limit_buy_order()
      2. test_rate_limit_buy_orders()`

   Below 3 api calls should be succeeded as part of **Positive Testing** 

      1. test_new_buy_order()
      2. test_new_sell_order()
      3. test_stop_limit_sell_order()
      
---
1. `Test_new_buy_order():` for sending buy orders 
---
2. `Test_new_sell_order():` for sending sell orders
---
3. `Test_stop_limit_buy_order(): `  for sending stop limit buy order
   1. `(This will fail as stop price is higher than origical price)`
---
4. `Test_stop_limit_sell_order():` for sending stop limit sell order
---
5. `Test_rate_limit_buy_orders():` for testing 20 request simultaneously buy orders 
   1. `(This will fail with status code 429)`
---

####Project Stucture 

```The project stucture is very straight-forward, simple and kept it clean as much as possible.

1. api_endpoint_calls : As name says - this dictory will consist all the .py files with endcalls 
    example - check_balances, get_active_orders, new_orders, get_past_trades

2. api_methods : This will consist of api methods that we normally have - 
   1. get , post , delete, put , etc methods

3. config folder - has all the important information that is needed for the project

4. tests -> test_functionality : Consist of various functions which are used for testing purpose  

