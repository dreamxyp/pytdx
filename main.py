if __name__ == '__main__':
    import pprint
    from pytdx.exhq import TdxExHq_API
    api = TdxExHq_API()
    with api.connect('139.9.51.18', 7709):
        x = api.to_df(api.get_history_instrument_bars_range(74, "BABA", 20170613,20170620))
        pprint.pprint(x.tail())