import time
import MetaTrader5 as mt5

from core.data import get_data
from strategy.strategy import generate_signal
from execution.trader import execute_trade
from config.settings import SYMBOL, SLEEP_TIME

def run():
    if not mt5.initialize():
        print("MT5 failed")
        return

    while True:
        df = get_data(SYMBOL, mt5.TIMEFRAME_M5)

        signal = generate_signal(df)

        if signal:
            print("Executing:", signal)
            execute_trade(signal, SYMBOL)

        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    run()