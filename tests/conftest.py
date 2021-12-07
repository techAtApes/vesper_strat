import pytest
from brownie import config
from brownie import Contract

@pytest.fixture
def gov(accounts):
    yield accounts.at("0xFEB4acf3df3cDEA7399794D0869ef76A6EfAff52", force=True)

@pytest.fixture
def sushi_router():
    yield Contract("0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F")

@pytest.fixture
def uni_router():
    yield Contract("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")

# @pytest.fixture
# def pool_rewards_wbtc():
#     # yield Contract("0xd59996055b5E0d154f2851A030E207E0dF0343B0") # USDC
#     yield Contract("0x479A8666Ad530af3054209Db74F3C74eCd295f8D") # WBTC
#     # yield Contract("0x93567318aaBd27E21c52F766d2844Fc6De9Dc738") # WETH

# @pytest.fixture
# def pool_rewards_usdc():
#     yield Contract("0xd59996055b5E0d154f2851A030E207E0dF0343B0") # USDC
#     # yield Contract("0x479A8666Ad530af3054209Db74F3C74eCd295f8D") # WBTC
#     # yield Contract("0x93567318aaBd27E21c52F766d2844Fc6De9Dc738") # WETH

@pytest.fixture
def pool_rewards_weth():
    # yield Contract("0xd59996055b5E0d154f2851A030E207E0dF0343B0") # USDC
    # yield Contract("0x479A8666Ad530af3054209Db74F3C74eCd295f8D") # WBTC
    yield Contract("0x93567318aaBd27E21c52F766d2844Fc6De9Dc738") # WETH

# @pytest.fixture
# def want_pool_usdc():
#     # yield Contract("0x4B2e76EbBc9f2923d83F5FBDe695D8733db1a17B") # WBTC
#     yield Contract("0x0C49066C0808Ee8c673553B7cbd99BCC9ABf113d") # USDC
#     # yield Contract("0x103cc17C2B1586e5Cd9BaD308690bCd0BBe54D5e") # WETH

# @pytest.fixture
# def want_pool_wbtc():
#     yield Contract("0x4B2e76EbBc9f2923d83F5FBDe695D8733db1a17B") # WBTC
#     # yield Contract("0x0C49066C0808Ee8c673553B7cbd99BCC9ABf113d") # USDC
#     # yield Contract("0x103cc17C2B1586e5Cd9BaD308690bCd0BBe54D5e") # WETH

@pytest.fixture
def want_pool_weth():
    # yield Contract("0x4B2e76EbBc9f2923d83F5FBDe695D8733db1a17B") # WBTC
    # yield Contract("0x0C49066C0808Ee8c673553B7cbd99BCC9ABf113d") # USDC
    yield Contract("0xd1C117319B3595fbc39b471AB1fd485629eb05F2") # WETH 0xd1C117319B3595fbc39b471AB1fd485629eb05F2

# @pytest.fixture
# def usdc():
#     token_address = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"  # USDC
#     yield Contract(token_address)

# @pytest.fixture
# def wbtc():
#     token_address = "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"  # WBTC 
#     yield Contract(token_address)

    

@pytest.fixture
def user(accounts):
    yield accounts[6]

@pytest.fixture
def user2(accounts):
    yield accounts[7]


@pytest.fixture
def rewards(accounts):
    yield accounts[1]


@pytest.fixture
def guardian(accounts):
    yield accounts[2]


@pytest.fixture
def management(accounts):
    yield accounts[3]


@pytest.fixture
def strategist(accounts):
    yield accounts[4]


@pytest.fixture
def keeper(accounts):
    yield accounts[5]


# @pytest.fixture
# def amount_wbtc(accounts, user, user2, wbtc):
#     amount = 10 * 10 ** wbtc.decimals()
#     # In order to get some funds for the token you are about to use,
#     # it impersonate an exchange address to use it's funds.
#     wbtc_whale = accounts.at("0xF977814e90dA44bFA03b6295A0616a897441aceC", force=True)
#     wbtc.transfer(user, amount, {"from": wbtc_whale})
#     yield amount

# @pytest.fixture
# def amount_usdc(accounts, usdc, user, user2):
#     amount = 10_000 * 10 ** usdc.decimals()
#     # In order to get some funds for the token you are about to use,
#     # it impersonate an exchange address to use it's funds.
#     usdc_whale = accounts.at("0xF977814e90dA44bFA03b6295A0616a897441aceC", force=True)
#     usdc.transfer(user, amount, {"from": usdc_whale})
#     yield amount

@pytest.fixture
def amount_weth(accounts, weth, user, user2):
    amount = 10_000 * 10 ** weth.decimals()
    # In order to get some funds for the token you are about to use,
    # it impersonate an exchange address to use it's funds.
    weth_whale = accounts.at("0xF977814e90dA44bFA03b6295A0616a897441aceC", force=True)
    weth.transfer(user, amount, {"from": weth_whale})
    yield amount

@pytest.fixture
def strategy(weth_strategy):
    yield weth_strategy

@pytest.fixture
def vault(weth_vault):
    yield weth_vault

@pytest.fixture
def token(weth):
    yield weth

@pytest.fixture
def amount(amount_weth):
    yield amount_weth

@pytest.fixture
def weth():
    token_address = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    yield Contract(token_address)


@pytest.fixture
def weth_amout(gov, weth, accounts):
    weth_amout = 10 ** weth.decimals()
    a = accounts[7]
    a.transfer(gov, "10 ether")
    gov.transfer(weth, weth_amout)
    yield weth_amout

@pytest.fixture
def vsp(accounts, user):
    amount = 1e20
    token_address = "0x1b40183EFB4Dd766f11bDa7A7c3AD8982e998421"
    vspContract = Contract(token_address)
    reserve = accounts.at("0x9520b477Aa81180E6DdC006Fc09Fb6d3eb4e807A", force=True)
    vspContract.transfer(user, amount, {"from": reserve})
    yield vspContract


# @pytest.fixture
# def usdc_vault(pm, usdc, gov, rewards, guardian):
#     Vault = pm(config["dependencies"][0]).Vault
#     vault = guardian.deploy(Vault)
#     vault.initialize(usdc, gov, rewards, "", "", guardian)
#     vault.setDepositLimit(2 ** 256 - 1, {"from": gov})
#     vault.setManagement(gov, {"from": gov})
#     yield vault

# @pytest.fixture
# def wbtc_vault(pm, gov, wbtc, rewards, guardian):
#     Vault = pm(config["dependencies"][0]).Vault
#     vault = guardian.deploy(Vault)
#     vault.initialize(wbtc, gov, rewards, "", "", guardian)
#     vault.setDepositLimit(2 ** 256 - 1, {"from": gov})
#     vault.setManagement(gov, {"from": gov})
#     yield vault


@pytest.fixture
def weth_vault(pm, gov, weth, rewards, guardian):
    Vault = pm(config["dependencies"][0]).Vault
    vault = guardian.deploy(Vault)
    vault.initialize(weth, gov, rewards, "", "", guardian)
    vault.setDepositLimit(2 ** 256 - 1, {"from": gov})
    vault.setManagement(gov, {"from": gov})
    yield vault

@pytest.fixture
def want_pool():
    yield Contract('0x4B2e76EbBc9f2923d83F5FBDe695D8733db1a17B')

@pytest.fixture
def pool_rewards():
    yield Contract("0x479A8666Ad530af3054209Db74F3C74eCd295f8D")

# @pytest.fixture
# def wbtc_strategy(strategist, keeper, wbtc_vault, StrategyVesper, gov, want_pool, pool_rewards, vsp, uni_router, sushi_router):
#     #strategy = strategist.deploy(StrategyVesper, vault)
#     strategy = strategist.deploy(
#         StrategyVesper, 
#         wbtc_vault,
#         want_pool,
#         pool_rewards,
#         1e16,
#         0,
#         5_000, # 50% percent keep,
#         "Vesper WBTC"
#     )
    
#     debt_ratio = 10_000               # 100%
#     minDebtPerHarvest = 0             # Lower limit on debt add
#     maxDebtPerHarvest = 2 ** 256 - 1  # Upper limit on debt add
#     performance_fee = 1000            # Strategist perf fee: 10%

#     wbtc_vault.addStrategy(
#         strategy, 
#         debt_ratio, 
#         minDebtPerHarvest, 
#         maxDebtPerHarvest, 
#         performance_fee,
#         {"from": gov}
#     )
#     yield strategy

@pytest.fixture
def weth_strategy(strategist, keeper, weth_vault, StrategyVesper, gov, want_pool, pool_rewards, vsp, uni_router, sushi_router):
    #strategy = strategist.deploy(StrategyVesper, vault)
    strategy = strategist.deploy(
        StrategyVesper, 
        weth_vault,
        want_pool,
        pool_rewards,
        1e16,
        0,
        5_000, # 50% percent keep,
        "Vesper WETH"
    )
    
    debt_ratio = 10_000               # 100%
    minDebtPerHarvest = 0             # Lower limit on debt add
    maxDebtPerHarvest = 2 ** 256 - 1  # Upper limit on debt add
    performance_fee = 1000            # Strategist perf fee: 10%

    weth_vault.addStrategy(
        strategy, 
        debt_ratio, 
        minDebtPerHarvest, 
        maxDebtPerHarvest, 
        performance_fee,
        {"from": gov}
    )
    yield strategy
