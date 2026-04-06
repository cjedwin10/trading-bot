import MetaTrader5 as mt5

def execute_trade(signal, symbol="XAUUSD"):
    tick = mt5.symbol_info_tick(symbol)

    if signal["type"] == "buy":
        price = tick.ask
        order_type = mt5.ORDER_TYPE_BUY
    else:
        price = tick.bid
        order_type = mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.05,
        "type": order_type,
        "price": price,
        "deviation": 20,
        "magic": 123456,
        "comment": "SMC Bot",
    }

    mt5.order_send(request)