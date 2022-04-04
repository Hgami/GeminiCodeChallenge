import base64
import hashlib
import hmac
import json
import time
import requests
import logging

from src.config.config import public_key, private_key, base_url
from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def test_response_status(r):
    try:
        status_code = r.status_code
        expected_status_code = 200
        assert status_code == expected_status_code, 'Invalid Status code : {}'.format(status_code)
    except AssertionError as msg:
        if status_code == 400 or status_code == 429:
            get_failed_reason = (json.loads(r.text).get('reason'))
            logging.info("Response back from request : {} ".format(r.text))
            logging.info(msg)
            raise SystemExit('Cannot make call because of : {}'.format(get_failed_reason))
        else:
            raise SystemExit(msg)


def post_api_call(endpoint, payload, api_call_name):
    if payload is None:
        payload = {}
    request_url = base_url + endpoint

    payload['request'] = endpoint
    payload['nonce'] = int(time.time() * 22000)

    if api_call_name == 'test_stop_limit_buy_order' or api_call_name == 'test_stop_limit_sell_order':
        payload['stop_price'] = '45000'
        payload.pop('options')

    b64_payload = base64.b64encode(json.dumps(payload).encode('utf-8'))
    signature = hmac.new(private_key.encode('utf-8'), b64_payload,
                         hashlib.sha384).hexdigest()

    headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': public_key,
        'X-GEMINI-PAYLOAD': b64_payload,
        'X-GEMINI-SIGNATURE': signature,
        'Cache-Control': "no-cache"
    }

    try:
        if api_call_name == 'test_multiple_buy_order':
            post_url_to_send = [(request_url, headers)] * 20
            with ThreadPoolExecutor(max_workers=20) as pool:
                response_list = list(pool.map(post_multiple_url, post_url_to_send))
            for response in response_list:
                test_response_status(response)
        else:
            r = requests.post(request_url, headers=headers)
            test_response_status(r)
            response_dict = json.loads(r.text)
    except NotADirectoryError:
        raise SystemExit('Could not load json to python dic {}', format(response_dict))

    if api_call_name == 'check_balance_api':
        for i in response_dict:
            if i.get('currency') == 'BTC':
                btc_amount_available = (i.get('available'))
                return btc_amount_available

    return response_dict


def post_multiple_url(args):
    return requests.post(args[0], headers=args[1])
