import cbpro
import constants

#Public Client ******************************************************************************************************

_client = cbpro.PublicClient()

# Authenticated Client

auth_client = cbpro.AuthenticatedClient(constants.SANDBOX_KEY, constants.SANDBOX_B64SECRET, constants.SANDBOX_PASSPHRASE,
                                  api_url="https://api-public.sandbox.pro.coinbase.com")


asset = auth_client.get_accounts()

#Public Client Methods ******************************************************************************************************

# print(asset)

order_book = _client.get_product_order_book('BTC-USD')

# print(order_book)

product_ticker = _client.get_product_ticker(product_id='BTC-USD')

# print(product_ticker)

product_trades = _client.get_product_trades(product_id='BTC-USD')

# generator??? ******************************************************************************************************
# print(product_trades)

product_historic_rates = _client.get_product_historic_rates(product_id='BTC-USD')

# print(product_historic_rates)

product_24hr_stats = _client.get_product_24hr_stats('ETH-USD')

# why NotFound when ETH-USD? ******************************************************************************************************
# print(product_24hr_stats)

currencies = _client.get_currencies()

# print(currencies)

time = _client.get_time()

# print(time)


tick = _client.get_product_ticker(product_id='BTC-USD')

# print(tick['bid'])


#Authenticated Client Methods ******************************************************************************************************

# auth_client.buy(price='43000', #USD
#                size='5', #BTC
#                order_type='limit',
#                product_id='BTC-USD')


auth_client.sell(price='40000', #USD
                size='20', #BTC
                order_type='limit',
                product_id='BTC-USD')


# def get_fills(self, product_id=None, order_id=None, **kwargs):

# fills_gen = auth_client.get_fills()
# Get all fills (will possibly make multiple HTTP requests)
# all_fills = list(fills_gen)




# _client.buy(price='40000', #USD
#                size='5', #BTC
#                order_type='limit',
#                product_id='BTC-USD')

    # _client = cbpro.PublicClient()
 
    # tick = _client.get_product_ticker(product_id='BTC-USD')
 
    # print(tick['bid'])
    # # _client = cbpro.AuthenticatedClient(constants.SANDBOX_KEY, 
    # #         constants.SANDBOX_PASSPHRASE, 
    # #         constants.SANDBOX_B64SECRET,
    # #     api_url="https://docs.pro.coinbase.com/#sandbox")

    # # tick = _client.get_product_ticker(product_id='BTC-USD')

    # # print(tick['bid'])





    # # def trade(self, action, limitPrice, quantity):
    # #     pass

    # # def viewAccounts(self, currentPair):
    # #     pass

    # # def viewOrder(self, order_id):
    # #     pass