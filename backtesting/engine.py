import pandas as pd

class Backtester:

    def __init__(self, data, strategy, initial_balance=10000):
        self