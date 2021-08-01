import cbpro
import constants
 
_client = cbpro.PublicClient()
 
tick = _client.get_product_ticker(product_id='BTC-USD')
 
print(tick['bid'])

auth_client = cbpro.AuthenticatedClient(constants.SANDBOX_KEY, constants.SANDBOX_B64SECRET, constants.SANDBOX_PASSPHRASE,
                                  api_url="https://api-public.sandbox.pro.coinbase.com")

auth_client.buy(price='40000', #USD
               size='5', #BTC
               order_type='limit',
               product_id='BTC-USD')
    # import cbpro
    # # import constants

    # auth_client = cbpro.PublicClient()
 
    # tick = auth_client.get_product_ticker(product_id='BTC-USD')
 
    # print(tick['bid'])
    # # auth_client = cbpro.AuthenticatedClient(constants.SANDBOX_KEY, 
    # #         constants.SANDBOX_PASSPHRASE, 
    # #         constants.SANDBOX_B64SECRET,
    # #     api_url="https://docs.pro.coinbase.com/#sandbox")

    # # tick = auth_client.get_product_ticker(product_id='BTC-USD')

    # # print(tick['bid'])





    # # def trade(self, action, limitPrice, quantity):
    # #     pass

    # # def viewAccounts(self, currentPair):
    # #     pass

    # # def viewOrder(self, order_id):
    # #     pass