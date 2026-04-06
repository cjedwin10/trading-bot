import MetaTrader5 as mt5

def calculate_lot(symbol, risk_percent, sl_distance_points):
    account_info = mt5.account_info()
    balance = account_info.balance

    symbol_info = mt5.symbol_info(symbol)

    tick_value = symbol_info.trade_tick_value
    tick_size = symbol_info.trade_tick_size

    risk_amount = balance * risk_percent

    lot = risk_amount / (sl_distance_points * tick_value / tick_size)

    return round(lot, 2)


def calculate_sl_tp(df, direction, rr=2):
    last_candle = df.iloc[-1]

    if direction == "buy":
        sl = last_candle['low'] - 10
        tp = last_candle['close'] + (last_candle['close'] - sl) * rr

    else:
        sl = last_candle['high'] + 10
        tp = last_candle['close'] - (sl - last_candle['close']) * rr

    return sl, tp


def risk_check(max_trades_per_day, current_trades):
    if current_trades >= max_trades_per_day:
        return False
    return True