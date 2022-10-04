from json import loads
from requests import get
from cbpro import AuthenticatedClient
from gspread import service_account
import time
from time import sleep
import yaml
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

gc = service_account()

defaultViewKey = config['defaultViewKey']
defaultViewPass = config['defaultViewPass']
defaultViewSecret = config['defaultViewSecret']
default_client = AuthenticatedClient(defaultViewKey, defaultViewSecret, defaultViewPass)

bitcoinViewKey = config['bitcoinViewKey']
bitcoinViewPass = config['bitcoinViewPass']
bitcoinViewSecret = config['bitcoinViewSecret']
bitcoin_client = AuthenticatedClient(bitcoinViewKey, bitcoinViewSecret, bitcoinViewPass)

etheriumViewKey = config['etheriumViewKey']
etheriumViewPass = config['etheriumViewPass']
etheriumViewSecret = config['etheriumViewSecret']
etherium_client = AuthenticatedClient(etheriumViewKey, etheriumViewSecret, etheriumViewPass)

fillParameters = {
    "before": None,
    "after": None,
    "limit": 1
    }

tickerurl = "https://api.exchange.coinbase.com/products/"
tickerHeaders = {"Accept": "application/json"}

print("Hit CTRL+C to stop")

while True:
    print(time.strftime("%H:%M:%S", time.localtime()))

    sh = gc.open("Holdings")
    defaultWorksheet = sh.worksheet("Coinbase Default")
    btcWorksheet = sh.worksheet("Coinbase BTC")
    ethWorksheet = sh.worksheet("Coinbase ETH")

#00 Get fills from Coinbase api
#documentation at https://cbpro2.readthedocs.io/en/latest/authenticated_client.html

    print("Getting fills from Coinbase api")

    ethbtcListFills = list(default_client.get_fills(product_id="ETH-BTC", kwargs=fillParameters))
    ethbtcDictFills = ethbtcListFills[0]
    # print(ethbtcDictFills)
    sleep(1)

    solbtcListFills = list(bitcoin_client.get_fills(product_id="SOL-BTC", kwargs=fillParameters))
    solbtcDictFills = solbtcListFills[0]
    # print(solbtcDictFills)
    atombtcListFills = list(bitcoin_client.get_fills(product_id="ATOM-BTC", kwargs=fillParameters))
    atombtcDictFills = atombtcListFills[0]
    # print(solbtcDictFills)
    algobtcListFills = list(bitcoin_client.get_fills(product_id="ALGO-BTC", kwargs=fillParameters))
    algobtcDictFills = algobtcListFills[0]
    # print(algobtcDictFills)
    dotbtcListFills = list(bitcoin_client.get_fills(product_id="DOT-BTC", kwargs=fillParameters))
    dotbtcDictFills = dotbtcListFills[0]
    # print(dotbtcDictFills)
    xtzbtcListFills = list(bitcoin_client.get_fills(product_id="XTZ-BTC", kwargs=fillParameters))
    xtzbtcDictFills = xtzbtcListFills[0]
    # print(xtzbtcDictFills)
    sleep(1)

    adaethListFills = list(etherium_client.get_fills(product_id="ADA-ETH", kwargs=fillParameters))
    adaethDictFills = adaethListFills[0]
    # print(adaethDictFills)
    linkethListFills = list(etherium_client.get_fills(product_id="LINK-ETH", kwargs=fillParameters))
    linkethDictFills = linkethListFills[0]
    # print(linkethDictFills)
    batethListFills = list(etherium_client.get_fills(product_id="BAT-ETH", kwargs=fillParameters))
    batethDictFills = batethListFills[0]
    # print(batethDictFills)
    manaethListFills = list(etherium_client.get_fills(product_id="MANA-ETH", kwargs=fillParameters))
    manaethDictFills = manaethListFills[0]
    # print(manaethDictFills)
    sushiethListFills = list(etherium_client.get_fills(product_id="SUSHI-ETH", kwargs=fillParameters))
    sushiethDictFills = sushiethListFills[0]
    # print(sushiethDictFills)
    sleep(1)


#00 Update google doc with most recent Coinbase fill
#documentation at https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account

    print("Updating Google Sheets with most recent Coinbase fills")

    if ethbtcDictFills['side'] == "sell":
        defaultWorksheet.update('C12:D12', [[ethbtcDictFills['size'], ethbtcDictFills['price']]],
                                value_input_option="user_entered")
        print("Updated ethbtc sell")
    elif ethbtcDictFills['side'] == "buy":
        defaultWorksheet.update('C18:D18', [[ethbtcDictFills['size'], ethbtcDictFills['price']]],
                                value_input_option="user_entered")
        print("Updated ethbtc buy")
    sleep(1)

    if solbtcDictFills['side'] == "sell":
        btcWorksheet.update('C12:D12', [[solbtcDictFills['size'], solbtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated solbtc sell")
    elif solbtcDictFills['side'] == "buy":
        btcWorksheet.update('C21:D21', [[solbtcDictFills['size'], solbtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated solbtc buy")
    if atombtcDictFills['side'] == "sell":
        btcWorksheet.update('C13:D13', [[atombtcDictFills['size'], atombtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated atombtc sell")
    elif atombtcDictFills['side'] == "buy":
        btcWorksheet.update('C22:D22', [[atombtcDictFills['size'], atombtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated atombtc buy")
    if algobtcDictFills['side'] == "sell":
        btcWorksheet.update('C14:D14', [[algobtcDictFills['size'], algobtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated algobtc sell")
    elif algobtcDictFills['side'] == "buy":
        btcWorksheet.update('C23:D23', [[algobtcDictFills['size'], algobtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated algobtc buy")
    if dotbtcDictFills['side'] == "sell":
        btcWorksheet.update('C15:D15', [[dotbtcDictFills['size'], dotbtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated dotbtc sell")
    elif dotbtcDictFills['side'] == "buy":
        btcWorksheet.update('C24:D24', [[dotbtcDictFills['size'], dotbtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated dotbtc buy")
    if xtzbtcDictFills['side'] == "sell":
        btcWorksheet.update('C16:D16', [[xtzbtcDictFills['size'], xtzbtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated xtzbtc sell")
    elif xtzbtcDictFills['side'] == "buy":
        btcWorksheet.update('C25:D25', [[xtzbtcDictFills['size'], xtzbtcDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated xtzbtc buy")
    sleep(1)

    if adaethDictFills['side'] == "sell":
        ethWorksheet.update('C12:D12', [[adaethDictFills['size'], adaethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated adaeth sell")
    elif adaethDictFills['side'] == "buy":
        ethWorksheet.update('C21:D21', [[adaethDictFills['size'], adaethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated adaeth buy")
    if linkethDictFills['side'] == "sell":
        ethWorksheet.update('C13:D13', [[linkethDictFills['size'], linkethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated linketh sell")
    elif linkethDictFills['side'] == "buy":
        ethWorksheet.update('C22:D22', [[linkethDictFills['size'], linkethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated linketh buy")
    if batethDictFills['side'] == "sell":
        ethWorksheet.update('C14:D14', [[batethDictFills['size'], batethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated bateth sell")
    elif batethDictFills['side'] == "buy":
        ethWorksheet.update('C23:D23', [[batethDictFills['size'], batethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated bateth buy")
    if manaethDictFills['side'] == "sell":
        ethWorksheet.update('C15:D15', [[manaethDictFills['size'], manaethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated manaeth sell")
    elif manaethDictFills['side'] == "buy":
        ethWorksheet.update('C24:D24', [[manaethDictFills['size'], manaethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated manaeth buy")
    if sushiethDictFills['side'] == "sell":
        ethWorksheet.update('C16:D16', [[sushiethDictFills['size'], sushiethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated sushieth sell")
    elif sushiethDictFills['side'] == "buy":
        ethWorksheet.update('C25:D25', [[sushiethDictFills['size'], sushiethDictFills['price']]],
                            value_input_option="user_entered")
        print("Updated sushieth buy")
    sleep(1)


#00 Get current Coinbase balances
#documentation at https://cbpro2.readthedocs.io/en/latest/authenticated_client.html

    print("Getting current Coinbase balances")

    defaultEthAccount = default_client.get_account('6d163553-4c16-4046-a6af-2f851e15401d')
    # print(defaultEthAccount['currency'], defaultEthAccount['balance'])
    defaultBtcAccount = default_client.get_account('f02dd961-4e2f-4caf-a6d2-cd6c73759d16')
    # print(defaultBtcAccount['currency'], defaultBtcAccount['balance'])
    sleep(1)

    btcBtcAccount = bitcoin_client.get_account('3c1b1608-9b9c-4ffc-ad0b-cbb425f555d3')
    # print(btcBtcAccount['currency'], btcBtcAccount['balance'])
    btcSolAccount = bitcoin_client.get_account('11359153-378d-4bcb-bbe4-5c85d1b0a4c1')
    # print(btcSolAccount['currency'], btcSolAccount['balance'])
    btcAtomAccount = bitcoin_client.get_account('b0c39a7b-960b-40cf-b4bf-a0c2f9ca126a')
    # print(btcAtomAccount['currency'], btcAtomAccount['balance'])
    btcAlgoAccount = bitcoin_client.get_account('8d577163-a27a-4b9e-a9aa-4d5399c7815a')
    # print(btcAlgoAccount['currency'], btcAlgoAccount['balance'])
    btcDotAccount = bitcoin_client.get_account('bee5a089-580f-4b68-80b5-69f26977882e')
    # print(btcDotAccount['currency'], btcDotAccount['balance'])
    btcXtzAccount = bitcoin_client.get_account('726b5b2f-f1f8-4d99-8e1e-b574f7d0889c')
    # print(btcXtzAccount['currency'], btcXtzAccount['balance'])
    sleep(1)

    ethEthAccount = etherium_client.get_account('affd0094-eea0-4489-a23e-0e16bc0233da')
    # print(ethEthAccount['currency'], ethEthAccount['balance'])
    ethAdaAccount = etherium_client.get_account('7f238269-8130-407a-b0bb-479e0bb93d36')
    # print(ethAdaAccount['currency'], ethAdaAccount['balance'])
    ethLinkAccount = etherium_client.get_account('1221b20d-23a5-4915-97d5-ea97a24cb449')
    # print(ethLinkAccount['currency'], ethLinkAccount['balance'])
    ethBatAccount = etherium_client.get_account('bff7465d-aff0-4c95-badb-40fb3e35faed')
    # print(ethBatAccount['currency'], ethBatAccount['balance'])
    ethManaAccount = etherium_client.get_account('7e16cc37-7c48-4eb7-8d0c-f2213a866a26')
    # print(ethManaAccount['currency'], ethManaAccount['balance'])
    ethSushiAccount = etherium_client.get_account('7e16cc37-7c48-4eb7-8d0c-f2213a866a26')
    # print(ethSushiAccount['currency'], ethSushiAccount['balance'])
    sleep(1)

    # x = 0
    # currencyName = ''
    # listAccounts = list(bitcoin_client.get_accounts())
    # dictAccounts = [{}]
    # while currencyName != "SOL":
    #     x = x+1
    #     dictAccounts = listAccounts[x]
    #     currencyName = dictAccounts['currency']
    # print(dictAccounts['currency'], dictAccounts['id'])

#00 Check current Coinbase ticker price
#sample code taken from https://docs.cloud.coinbase.com/exchange/reference/exchangerestapi_getproduct

    print("Checking current Coinbase ticker prices")

    ethbtcTicker = loads(get(tickerurl + "ETH-BTC/ticker", headers=tickerHeaders).text)
    # print(ethbtcTicker)
    btcusdTicker = loads(get(tickerurl + "BTC-USD/ticker", headers=tickerHeaders).text)
    # print(btcusdTicker)
    ethusdTicker = loads(get(tickerurl + "ETH-USD/ticker", headers=tickerHeaders).text)
    # print(ethusdTicker)
    sleep(1)

    solbtcTicker = loads(get(tickerurl + "SOL-BTC/ticker", headers=tickerHeaders).text)
    # print(solbtcTicker)
    atombtcTicker = loads(get(tickerurl + "ATOM-BTC/ticker", headers=tickerHeaders).text)
    # print(atombtcTicker)
    algobtcTicker = loads(get(tickerurl + "ALGO-BTC/ticker", headers=tickerHeaders).text)
    # print(ethbtcTicker)
    dotbtcTicker = loads(get(tickerurl + "DOT-BTC/ticker", headers=tickerHeaders).text)
    # print(dotbtcTicker)
    xtzbtcTicker = loads(get(tickerurl + "XTZ-BTC/ticker", headers=tickerHeaders).text)
    # print(xtzbtcTicker)
    sleep(1)

    adaethTicker = loads(get(tickerurl + "ADA-ETH/ticker", headers=tickerHeaders).text)
    # print(adaethTicker)
    linkethTicker = loads(get(tickerurl + "LINK-ETH/ticker", headers=tickerHeaders).text)
    # print(linkethTicker)
    batethTicker = loads(get(tickerurl + "BAT-ETH/ticker", headers=tickerHeaders).text)
    # print(batethTicker)
    manaethTicker = loads(get(tickerurl + "MANA-ETH/ticker", headers=tickerHeaders).text)
    # print(manaethTicker)
    sushiethTicker = loads(get(tickerurl + "SUSHI-ETH/ticker", headers=tickerHeaders).text)
    # print(sushiethTicker)
    sleep(1)


#00 Update google doc with current ticker price and balance
#documentation at https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account

    print("Updating Google Sheets with current ticker prices and Coinbase balances")

    defaultWorksheet.update('C24:D24', [[defaultEthAccount['balance'], ethusdTicker['price']]],
                            value_input_option="user_entered")
    defaultWorksheet.update('C25:D25', [[defaultBtcAccount['balance'], btcusdTicker['price']]],
                            value_input_option="user_entered")
    defaultWorksheet.update('M4', ethbtcTicker['price'],
                            value_input_option="user_entered")
    sleep(1)

    btcWorksheet.update('C30:D30', [[btcBtcAccount['balance'], btcusdTicker['price']]],
                        value_input_option="user_entered")
    btcWorksheet.update('C31:D31', [[btcSolAccount['balance'], solbtcTicker['price']]],
                        value_input_option="user_entered")
    btcWorksheet.update('C32:D32', [[btcAtomAccount['balance'], atombtcTicker['price']]],
                        value_input_option="user_entered")
    btcWorksheet.update('C33:D33', [[btcAlgoAccount['balance'], algobtcTicker['price']]],
                        value_input_option="user_entered")
    btcWorksheet.update('C34:D34', [[btcDotAccount['balance'], dotbtcTicker['price']]],
                        value_input_option="user_entered")
    btcWorksheet.update('C35:D35', [[btcXtzAccount['balance'], xtzbtcTicker['price']]],
                        value_input_option="user_entered")
    sleep(1)

    ethWorksheet.update('C30:D30', [[ethEthAccount['balance'], ethusdTicker['price']]],
                        value_input_option="user_entered")
    ethWorksheet.update('C31:D31', [[ethAdaAccount['balance'], adaethTicker['price']]],
                        value_input_option="user_entered")
    ethWorksheet.update('C32:D32', [[ethLinkAccount['balance'], linkethTicker['price']]],
                        value_input_option="user_entered")
    ethWorksheet.update('C33:D33', [[ethBatAccount['balance'], batethTicker['price']]],
                        value_input_option="user_entered")
    ethWorksheet.update('C34:D34', [[ethManaAccount['balance'], manaethTicker['price']]],
                        value_input_option="user_entered")
    ethWorksheet.update('C35:D35', [[ethSushiAccount['balance'], sushiethTicker['price']]],
                        value_input_option="user_entered")
    sleep(1)

    sleep_time = 900
    x = 4
    while x > 0:
        print("Done. Waiting till next cycle in", (sleep_time*x)/60, "minutes")
        x -= 1
        sleep(sleep_time)
