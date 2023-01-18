import os
from configparser import ConfigParser


class Envi:
    cfg = ConfigParser(allow_no_value=True)
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    PATH = ROOT_PATH.replace('/modules', '/')
    cfg.read(PATH + 'config.ini')
    LOG_DIR = PATH + 'log/'
    GH_BQ_CRED = PATH + 'cred/gcp-ghr-bq.json'
    SSR_BQ_CRED = PATH + 'cred/gh-bigquery.json'
    BQ_INSTANCE_NAME = 'gcp-20190903-01'
    # if not os.path.exists(LOG_DIR):
    #     os.mkdir(LOG_DIR)
    TIME_SLEEP = 10
    MONITOR_LIST = ['VX88', 'EY', 'KR', 'ESBP', 'YB01', 'SG']
    TABLE_LIST = ['Bank', 'Cash', 'Cash_Entry', 'Currency', 'Deposit', 'Domain', 'Domain_Config', 'Execution_Log', 'Game_Code',
              'Game_Vendor', 'Geoip_Country', 'Geoip_Region', 'Invoice', 'Invoice_Detail', 'Jackpots', 'Level', 'Login',
              'Oauth2', 'Opcode', 'Promotion', 'Rebate_Dispatch', 'Rebate_Entry_List', 'Rebate_Entry_List_Detail',
              'Rebate_Event', 'User', 'User_Address', 'User_Bank', 'User_Blacklist', 'User_Config', 'User_Contact',
              'User_Created', 'User_Detail', 'User_Email', 'User_Level', 'User_Phone', 'User_Stat', 'User_Vip_Level',
              'User_user_id', 'Vip_Level', 'Wager', 'Withdraw']
    WITHOUT_DOMAIN_TABLES =['Cash', 'Invoice_Detail', 'Rebate_Dispatch', 'Rebate_Entry_List', 'Rebate_Entry_List_Detail','User_Contact', 'User_Config',
                       'User_Created', 'User_Detail', 'User_Email', 'User_Level', 'User_Phone', 'User_Stat']

    GENERAL_INFORMATION_TABLES =['Bank', 'Currency', 'Currency_Code_bbos', 'Domain', 'Domain_Config',  'Game_Code', 'Game_Vendor',
                             'Geoip_Country', 'Geoip_Region',  'Oauth2', 'Opcode', 'Promotion_Type', 'Gen_Rebate_Dispatch']

# DEBUG_MODE = bool(cfg.get('Environment', 'DEBUG'))


    VTC_GH_PROJECT_ID = 'gcp-20190903-01'
    VTC_SSR_PROJECT_ID = 'gcp-20220516-001'


######################################################
# PUB SUB TOPIC
######################################################
    TOPIC_NAME = 'projects/gcp-20190903-01/topics/test_dataflow'

######################################################
# DOMAIN_DIC
######################################################
# DOMAIN_ID_LIST = [38, 41, 67, 70, 82, 94, 102, 6, 71, 96]
    DOMAIN_ID_LIST = [70, 82]

    DOMAIN_TABLE_DICT = {
    # '38': 'esbp',
    # '41': 'ey',
    # '67': 'yb01',
    '70': 'test_dataflow_vx88',
    '82': 'test_dataflow_kr',
    # '94': '5151',
    # '102': 'halo',
    # '6': 'esball',
    # '71': 'vx88_demo',
    # '96': 'ma',
}

    DOMAIN_DICT2 = {
    'test_dataflow_vx88': '70',
    'test_dataflow_kr': '82'
    }


    DOMAIN_DICT = {
    # '38': 'esbp',
    # '41': 'ey',
    # '67': 'yb01',
    '70': 'vx88',
    '82': 'kr',
    # '94': '5151',
    # '102': 'halo',
    # '6': 'esball',
    # '71': 'vx88_demo',
    # '96': 'ma',
    }


    BBOS_SQL_PATH = PATH + 'schedule_sql/BBOS_RawData/'


if __name__ == '__main__':
    test = Envi()
    print(test.SSR_BQ_CRED)