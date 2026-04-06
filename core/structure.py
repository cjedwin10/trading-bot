def detect_swings(df, left=3, right=3):
    highs, lows = [], []

    for i in range(left, len(df) - right):
        if all(df['high'][i] > df['high'][i-j] for j in range(1, left+1)) and \
           all(df['high'][i] > df['high'][i+j] for j in range(1, right+1)):
            highs.append((i, df['high'][i]))

        if all(df['low'][i] < df['low'][i-j] for j in range(1, left+1)) and \
           all(df['low'][i] < df['low'][i+j] for j in range(1, right+1)):
            lows.append((i, df['low'][i]))

    return highs, lows


def get_trend(highs, lows):
    if len(highs) < 2 or len(lows) < 2:
        return "range"

    if highs[-1][1] > highs[-2][1] and lows[-1][1] > lows[-2][1]:
        return "bullish"

    if highs[-1][1] < highs[-2][1] and lows[-1][1] < lows[-2][1]:
        return "bearish"

    return "range"