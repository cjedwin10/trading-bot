from core.structure import detect_swings, get_trend


def analyze_timeframe(df):
    """
    Analyze a single timeframe:
    - Detect swings
    - Determine trend
    """
    highs, lows = detect_swings(df)
    trend = get_trend(highs, lows)

    return {
        "trend": trend,
        "highs": highs,
        "lows": lows
    }


def mtf_analysis(htf_df, ltf_df):
    """
    Multi-timeframe alignment:
    HTF = bias
    LTF = execution
    """

    htf = analyze_timeframe(htf_df)
    ltf = analyze_timeframe(ltf_df)

    return {
        "htf_trend": htf["trend"],
        "ltf_trend": ltf["trend"],
        "htf_highs": htf["highs"],
        "htf_lows": htf["lows"],
        "ltf_highs": ltf["highs"],
        "ltf_lows": ltf["lows"]
    }


def is_aligned(mtf_data):
    """
    Check if HTF and LTF agree
    """
    return mtf_data["htf_trend"] == mtf_data["ltf_trend"]


def get_bias(mtf_data):
    """
    Returns final trading bias
    """

    if mtf_data["htf_trend"] == "bullish":
        return "buy"

    elif mtf_data["htf_trend"] == "bearish":
        return "sell"

    return None


def entry_allowed(mtf_data):
    """
    Strong filter:
    Only trade when both HTF and LTF align
    """

    if mtf_data["htf_trend"] == "bullish" and mtf_data["ltf_trend"] == "bullish":
        return "buy"

    if mtf_data["htf_trend"] == "bearish" and mtf_data["ltf_trend"] == "bearish":
        return "sell"

    return None