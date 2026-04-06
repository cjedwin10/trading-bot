def detect_displacement(df):
    body = abs(df['close'].iloc[-1] - df['open'].iloc[-1])
    avg = abs(df['close'] - df['open']).mean()
    return body > avg * 1.5


def detect_fvg(df):
    zones = []
    for i in range(2, len(df)):
        if df['low'].iloc[i] > df['high'].iloc[i-2]:
            zones.append(("bullish", df['high'].iloc[i-2], df['low'].iloc[i]))
        if df['high'].iloc[i] < df['low'].iloc[i-2]:
            zones.append(("bearish", df['low'].iloc[i-2], df['high'].iloc[i]))
    return zones