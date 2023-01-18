
# Defines the BigQuery schema for the output table.

class Applicant:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'promotion_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'ip', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'user_agent', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Applicant'


class Bank:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'abbr', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Bank'


class Cash:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'balance', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Cash'


class Cash_Entry:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'opcode', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'balance', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'trans_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'operator', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'memo', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'internal_memo', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Cash_Entry'


class Currency:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'currency', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'exchange_rate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'effective_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        print(self.TABLE_NAME)
        self.TABLE_NAME = f'your-project-name:{table_name}.Currency'


class Deposit:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'submit_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'confirm_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'status', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'first', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'unfinished', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'invoice_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'entry_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'fee', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'opcode', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'NULLABLE'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Deposit'


class Dispatch_Order:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'promotion_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Dispatch_Order'


class Domain:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'test', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Domain'


class Domain_Config:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'ingroup_transfer', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Domain_Config'


class Execution_Log:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'table_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'major_key', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'method', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'message', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'operator', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'item_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'ip', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'country_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'city_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Execution_Log'

class Game_Code:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'vendor_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'type', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'game_code', 'type': 'STRING', 'mode': 'REQUIRED'},
                                  {'name': 'online_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'zh_tw_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'zh_cn_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'en_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ja_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ko_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'vi_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'hi_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'sort', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'hot_sort', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Game_Code'


class Game_Vendor:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'lobby_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'tc_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'sc_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'en_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ja_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'vi_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'kr_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Game_Vendor'


class Geoip_Country:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'country', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'en_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'zh_tw_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'zh_cn_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self,table_name):
        self.TABLE_NAME = f'gcp-20220516-001:{table_name}.Geoip_Country'

class Geoip_Region:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'country_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'country', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'region', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'en_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'zh_tw_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'zh_cn_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Geoip_Region'

class Invoice:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'opcode', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Invoice'


class Invoice_Detail:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'invoice_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'data', 'type': 'JSON', 'mode': 'NULLABLE'},
                                  {'name': 'dirty_data', 'type': 'JSON', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Invoice_Detail'


class Jackpots:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'STRING', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'vendor', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'kind_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'game_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'grade', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'deal', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'payoff', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'exchange_rate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'account_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Jackpots'


class Level:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'level_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'level_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'role', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Level'


class Login:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'role', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'username', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ip', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ipv6', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'host', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'client_os', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'client_browser', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'country_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'city_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'result', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'ingress', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'entrance', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'region', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'user_agent', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'login_date_ae', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Login'



class Oauth2:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'client_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Oauth2'


class Opcode:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'opcode', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Opcode'

class Promotion:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'code', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'url', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Promotion'


class Promotion_Type:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'type', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'opcode', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Promotion_Type'


class Promotion_UXM:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'promotion_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'promotion_type', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'start_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'end_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'sign', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'},
                                  {'name': 'status', 'type': 'INTEGER', 'mode': 'NULLABLE'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Promotion_UXM'


class Rebate_Dispatch:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'rebate_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'event_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'level_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip_config_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'group_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'stat', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'done', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'canceled', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'restat', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'restat_version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'stat_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'done_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'start_canceled_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'canceled_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'operator', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Rebate_Dispatch'


class Gen_Rebate_Dispatch:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'rebate_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'event_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'level_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip_config_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'group_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'stat', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'done', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'canceled', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'restat', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'restat_version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'stat_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'done_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'start_canceled_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'canceled_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'operator', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Rebate_Dispatch'


class Rebate_Entry_List:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'event_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'rebate_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'level_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'original_amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'canceled', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip_config_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'group_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'self', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'valid_bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'sport', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'live', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'slots', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'lottery', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'card', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'mahjong', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'rebate_done_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'canceled_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Rebate_Entry_List'


class Rebate_Entry_List_Detail:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'entry_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vendor_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'type', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'valid_bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'rebate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'original_amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'exception', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Rebate_Entry_List_Detail'


class Rebate_Event:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'event_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'event_name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'frequency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'self', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'end_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Rebate_Event'


class User:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'User_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'username', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'upper_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'role', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'bankrupt', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'tied', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'locked', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'last_login', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'last_ip', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'last_online', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'blacklist_modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'checked', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'failed', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User'


class User_Address:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'is_default', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'phone', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'address', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Address'

class User_Bank:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'bank_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'account', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'province', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'branch', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self,table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Bank'


class User_Blacklist:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'blacklist_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'created_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                            {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Blacklist'


class User_Config:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'ingroup_transfer', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Config'


class User_Contact:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'contact_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'value', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Contact'


class User_Created:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'ip', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'country', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'region', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'created_by', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'register_channel', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Created'


class User_Detail:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'alias', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'birthday', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'gender', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'image_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'custom_image_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'custom', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'content_rating', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Detail'


class User_Email:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'email', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'confirm', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'confirm_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Email'


class User_Level:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'level_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Level'


class User_Phone:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'phone', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'confirm', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'confirm_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Phone'


class User_Stat:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'last_deposit_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Stat'


class User_Vip_Level:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'config_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'vip_level', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.User_Vip_Level'

class User_user_id:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'username', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'upper_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'role', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'bankrupt', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'tied', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'locked', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'last_login', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'last_ip', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'last_online', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'blacklist_modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'checked', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'failed', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}


class Vip_Level:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'complex', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'enable', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'display', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Vip_Level'


class Wager:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'vendor', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'game_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'deal', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'device', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'os', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'payoff', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'valid_bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'commision', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'exchange_rate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'result', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'settle_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'account_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'first_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Wager'


class Wager_By_First_At:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'vendor', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'game_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'deal', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'device', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'os', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'payoff', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'valid_bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'commision', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'exchange_rate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'result', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'settle_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'account_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'first_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Wager_By_First_At'


class Wager_By_First_At:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'vendor', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'game_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'deal', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'device', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'os', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'payoff', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'valid_bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'commision', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'exchange_rate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'result', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'settle_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'account_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'first_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Wager_By_First_At'


class Wager_By_Settle_At:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'vendor', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'game_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'deal', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'device', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'os', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'payoff', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'valid_bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'commision', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'exchange_rate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'result', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'settle_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'account_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'first_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Wager_By_Settle_At'


class Wager_By_User_id:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'vendor', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'game_code', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'deal', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'device', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'os', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'payoff', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'valid_bet', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'commision', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'exchange_rate', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'result', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'settle_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'account_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'modified_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'first_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'version', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Wager_By_User_id'


class Withdraw:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'parent_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'offer', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'real_amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'currency', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'process', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'confirm', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'cancel', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'reject', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'locked', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'risk_auto', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'risk_confirm', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'risk_cancel', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'risk_reject', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'holding', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'operator', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'holding_operator', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'account', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'address', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'first', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'fee', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'administrative_amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'offer_deduction', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'user_virtual_bank_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'user_bank_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'confirm_at', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'client_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'flag', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'original_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Withdraw'


class Withdraw_Flag_Log:
    def __init__(self):
        self.TABLE_NAME = ''
        self.SCHEMA = {'fields': [
                                  {'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
                                  {'name': 'domain_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'promotion_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'promotion_name', 'type': 'STRING', 'mode': 'REQUIRED'},
                                  {'name': 'user_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'withdraw_limit', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'amount', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'lottery_price', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'real_amount', 'type': 'NUMERIC', 'mode': 'NULLABLE'},
                                  {'name': 'gift_card_vendor', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'gift_card_kind', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'ref_id', 'type': 'STRING', 'mode': 'NULLABLE'},
                                  {'name': 'dispatch_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'dispatch_time', 'type': 'INTEGER', 'mode': 'NULLABLE'},
                                  {'name': 'original_create_time', 'type': 'DATETIME', 'mode': 'NULLABLE'},
                                  {'name': 'created_time', 'type': 'DATETIME', 'mode': 'REQUIRED'}]}

    def get_table_name(self, table_name):
        self.TABLE_NAME = f'your-project-name:{table_name}.Withdraw_Flag_Log'
