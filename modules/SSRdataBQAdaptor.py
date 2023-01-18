from modules.Environment import Envi
from modules.BigQueryAdaptor import BigQueryAdaptor
from modules.BigQueryConnection import BigQueryConnection
from modules.BigQueryParams import BigQueryParams


class SSRdataBQAdaptor(BigQueryAdaptor):
    def __init__(self, project: str):
        if project == 'GH':
            cred_path = Envi.GH_BQ_CRED
        elif project == 'SSR':
            cred_path = Envi.SSR_BQ_CRED
        else:
            cred_path = Envi.GH_BQ_CRED

        super(SSRdataBQAdaptor, self).__init__(
            BigQueryConnection(BigQueryParams(cert_path=cred_path)))

    def insert_row_from_dataframe(self, dataset, table, insert_data):
        self.insert_data = insert_data
        self.dataset_name = dataset
        self.table_name = table
        self.mode = self.INSERT_ROW_MODE
        self.exec()

    def insert_bbos_data(self, dataset, table, insert_data):
        self.insert_data = insert_data
        self.dataset_name = dataset
        self.table_name = table
        self.mode = self.INSERT_MODE
        self.exec()

    def insert_general_information_user_phone(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserPhone.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_applicant(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Applicant.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_day))
        # self.exec()
        return self.statement

    def query_bbos_cash(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Cash.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_cash_entry(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'CashEntry.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_deposit(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Deposit.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_dispatch_order(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'DispatchOrder.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_user_user_id(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserUserID.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement
    #

    def query_general_information_currency(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Currency.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile
        # self.exec()
        return self.statement

    def query_general_information_bank(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Bank.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile
        # self.exec()
        return self.statement

    def query_general_information_domain(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Domain.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile
        # self.exec()
        return self.statement
    #
    # def delete_general_information_domain(self):
    #     self.mode = self.QUERY_MODE
    #     self.statement = f"delete from `gcp-20220516-001.general_information.Domain` where true;"
    #     self.exec()
    #     return True

    def query_general_information_domain_config(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'DomainConfig.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL_DAY}', str(interval_day))
        # self.exec()
        return self.statement

    # def delete_general_information_domain_config(self):
    #     self.mode = self.QUERY_MODE
    #     self.statement = f"delete from `gcp-20220516-001.general_information.Domain_Config` where true;"
    #     self.exec()
    #     return True

    def query_general_information_game_vendor(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GameVendor.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL_DAY}', str(interval_day))
        # self.exec()
        return self.statement

    def query_general_information_geoip_region(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GeoipRegion.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL_DAY}', str(interval_day))
        # self.exec()
        return self.statement

    def query_general_information_geoip_country(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GeoipCountry.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL_DAY}', str(interval_day))
        # self.exec()
        return self.statement

    def query_general_information_opcode(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Opcode.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL_DAY}', str(interval_day))
        # self.exec()
        return self.statement

    def query_general_information_oauth2(self , interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Oauth2.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile
        # self.exec()
        return self.statement

    # def delete_oauth2(self, interval_day: int):
    #     self.mode = self.QUERY_MODE
    #     self.statement = f"delete from `gcp-20220516-001.general_information.Oauth2` where true;"
    #     self.exec()
    #     return True

    def insert_general_information_promotion_type(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'PromotionType.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL_DAY}', str(interval_day))
        # self.exec()
        return self.statement

    def insert_general_information_rebate_dispatch(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoRebateDispatch.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(120))  # general_info 分鐘
        # self.exec()
        return self.statement

    def insert_general_information_rebate_entry_list(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoRebateEntryList.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_rebate_entry_list_detail(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoRebateEntryListDetail.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_config(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserConfig.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_contact(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserContact.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_created(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserCreated.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_detail(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserDetail.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_email(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserEmail.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_level(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserLevel.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_phone(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserPhone.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_general_information_user_stat(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'GenInfoUserStat.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_execution_log(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'ExecutionLog.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def insert_bbos_game_code(self,interval_min: int ):
        fd = open(Envi.BBOS_SQL_PATH + 'GameCode.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL_DAY}', str(interval_min))
        # self.exec()
        return self.statement

    def delete_bbos_game_code(self, dataset: str):
        self.mode = self.QUERY_MODE
        self.statement = f"delete from `gcp-20220516-001.{dataset}.Game_Code` where true;"
        self.exec()
        return True

    def query_bbos_invoice(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Invoice.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_invoice_detail(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'InvoiceDetail.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_jackpots(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Jackpots.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_level(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Level.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_login(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Login.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_promotion(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Promotion.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_promotion_uxm(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'PromotionUXM.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_day))
        # self.exec()
        return self.statement

    def query_bbos_rebate_dispatch(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'RebateDispatch.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_rebate_entry_list(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'RebateEntryList.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_rebate_entry_list_detail(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'RebateEntryListDetail.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_rebate_event(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'RebateEvent.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'User.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_address(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserAddress.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_bank(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserBank.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_blacklist(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserBlacklist.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_config(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserConfig.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_contact(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserContact.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_created(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserCreated.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_detail(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserDetail.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_email(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserEmail.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_level(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserLevel.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_phone(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserPhone.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_stat(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserStat.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_user_vip_level(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'UserVipLevel.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_vip_level(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'VipLevel.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_wager(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Wager.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_wager_by_first_at(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Wager.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_wager_by_settle_at(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Wager.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_wager_by_user_id(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Wager.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_withdraw(self, interval_min: int):
        fd = open(Envi.BBOS_SQL_PATH + 'Withdraw.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_min))
        # self.exec()
        return self.statement

    def query_bbos_withdraw_flag_log(self, interval_day: int):
        fd = open(Envi.BBOS_SQL_PATH + 'WithdrawFlagLog.sql', 'r')
        sqlFile = fd.read()
        self.mode = self.QUERY_MODE
        self.statement = sqlFile.replace('{INTERVAL}', str(interval_day))
        # self.exec()
        return self.statement
