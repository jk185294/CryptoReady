import cbpro
import constants
import trading_systems

trading_systems.auth_client.sell(price='40000', #USD
                size='20', #BTC
                order_type='limit',
                product_id='BTC-USD')