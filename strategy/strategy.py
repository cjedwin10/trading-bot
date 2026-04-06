from core.structure import detect_swings, get_trend
from core.smc import detect_displacement

def generate_signal(df):
    highs, lows = detect_swings(df)
    trend = get_trend(highs, lows)

    displacement = detect_displacement(df)

    if trend == "bullish" and displacement:
        return {"type": "buy"}

    if trend == "bearish" and displacement:
        return {"type": "sell"}

    return None