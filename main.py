# if __name__ == '__main__':
#     import pprint
#     from pytdx.exhq import TdxExHq_API
#     api = TdxExHq_API()
#     with api.connect('139.9.51.18', 7709):
#         x = api.to_df(api.get_history_instrument_bars_range(74, "BABA", 20170613,20170620))
#         pprint.pprint(x.tail())


# if __name__ == '__main__':
#
#     from pytdx.util.best_ip import select_best_ip
#     from pytdx.hq import TdxHq_API
#     api = TdxHq_API()
#     with api.connect('139.9.51.18', 7709):
#         # 11 扩缩股
#         print(api.to_df(api.get_xdxr_info(1, '600381')))
#         # 12 非流通股缩股
#         print(api.to_df(api.get_xdxr_info(1, '600339')))
#         # 13 送认购权证
#         print(api.to_df(api.get_xdxr_info(1, '600008')))
#         # 14 送认沽权证
#         print(api.to_df(api.get_xdxr_info(0, '000932')))


if __name__ == '__main__':
    import pprint
    from pytdx.hq import TdxHq_API
    from pytdx.log import DEBUG, log
    from pytdx.params import TDXParams

    api = TdxHq_API()
    if api.connect('139.9.51.18', 7709):
        # log.info("获取股票行情")
        # stocks = api.get_security_quotes([(0, "000001"), (1, "600300")])
        # pprint.pprint(stocks)
        log.info("获取k线")
        data = api.get_security_bars(9, 0, '000001', 4, 3)
        pprint.pprint(data)
        # log.info("获取 深市 股票数量")
        # pprint.pprint(api.get_security_count(0))
        # log.info("获取股票列表")
        # stocks = api.get_security_list(1, 255)
        # pprint.pprint(stocks)
        # log.info("获取指数k线")
        # data = api.get_index_bars(9, 1, '000001', 1, 2)
        # pprint.pprint(data)
        # log.info("查询分时行情")
        # data = api.get_minute_time_data(TDXParams.MARKET_SH, '600300')
        # pprint.pprint(data)
        # log.info("查询历史分时行情")
        # data = api.get_history_minute_time_data(
        #     TDXParams.MARKET_SH, '600300', 20161209)
        # pprint.pprint(data)
        # log.info("查询分时成交")
        # data = api.get_transaction_data(TDXParams.MARKET_SZ, '000001', 0, 30)
        # pprint.pprint(data)
        # log.info("查询历史分时成交")
        # data = api.get_history_transaction_data(
        #     TDXParams.MARKET_SZ, '000001', 0, 10, 20170209)
        # pprint.pprint(data)
        # log.info("查询公司信息目录")
        # data = api.get_company_info_category(TDXParams.MARKET_SZ, '000001')
        # pprint.pprint(data)
        # log.info("读取公司信息-最新提示")
        # data = api.get_company_info_content(0, '000001', '000001.txt', 0, 10)
        # pprint.pprint(data)
        # log.info("读取除权除息信息")
        # data = api.get_xdxr_info(1, '600300')
        # pprint.pprint(data)
        # log.info("读取财务信息")
        # data = api.get_finance_info(0, '000001')
        # pprint.pprint(data)
        # log.info("日线级别k线获取函数")
        # data = api.get_k_data('000001', '2017-07-01', '2017-07-10')
        # pprint.pprint(data)

        api.disconnect()