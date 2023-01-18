import traceback
import logging
from modules import Environment as envi
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler, setup_logging
from modules.SSRdataBQAdaptor import SSRdataBQAdaptor
import datetime


class SSRBBOSSQ:
    def __init__(self):
        self.sq = SSRdataBQAdaptor('SSR')
        self.insert_minutes = 120
        self.insert_day = 3
        self.domain_worker = {
            'Applicant': self.sq.query_bbos_applicant,
            'Cash': self.sq.query_bbos_cash,
            'Cash_Entry': self.sq.query_bbos_cash_entry,
            'Currency': self.sq.insert_general_information_currency,  # 待確認
            'Deposit': self.sq.query_bbos_deposit,
            'Dispatch_Order': self.sq.query_bbos_dispatch_order,
            'Execution_Log': self.sq.query_bbos_execution_log,
            'Invoice': self.sq.query_bbos_invoice,
            'Invoice_Detail': self.sq.query_bbos_invoice_detail,
            'Jackpots': self.sq.query_bbos_jackpots,
            'Level': self.sq.query_bbos_level,
            'Login': self.sq.query_bbos_login,
            'Promotion': self.sq.query_bbos_promotion,
            'Promotion_UXM': self.sq.query_bbos_promotion_uxm,
            'Rebate_Dispatch': self.sq.query_bbos_rebate_dispatch,
            'Rebate_Entry_List': self.sq.query_bbos_rebate_entry_list,
            'Rebate_Entry_List_Detail': self.sq.query_bbos_rebate_entry_list_detail,
            'Rebate_Event': self.sq.query_bbos_rebate_event,
            'User': self.sq.query_bbos_user,
            'User_Address': self.sq.query_bbos_user_address,
            'User_Bank': self.sq.query_bbos_user_bank,
            'User_Blacklist': self.sq.query_bbos_user_blacklist,
            'User_Config': self.sq.query_bbos_user_config,
            'User_Contact': self.sq.query_bbos_user_contact,
            'User_Created': self.sq.query_bbos_user_created,
            'User_Detail': self.sq.query_bbos_user_detail,
            'User_Email': self.sq.query_bbos_user_email,
            'User_Level': self.sq.query_bbos_user_level,
            'User_Phone': self.sq.query_bbos_user_phone,
            'User_Stat': self.sq.query_bbos_user_stat,
            'User_Vip_Level': self.sq.query_bbos_user_vip_level,
            'Vip_Level': self.sq.query_bbos_vip_level,
            'Wager': self.sq.query_bbos_wager,
            'Wager_By_First_At': self.sq.query_bbos_wager_by_first_at,
            'Wager_By_Settle_At': self.sq.query_bbos_wager_by_settle_at,
            'Wager_By_User_id': self.sq.query_bbos_wager_by_user_id,
            'Withdraw': self.sq.query_bbos_withdraw,
            'Bank': self.sq.query_general_information_bank,
            'Currency': self.sq.query_general_information_currency,
            'Domain': self.sq.query_general_information_domain,
            'Domain_Config': self.sq.query_general_information_domain_config,
            'Game_Code': self.sq.insert_bbos_game_code,
            'Game_Vendor': self.sq.query_general_information_game_vendor,
            'Geoip_Country': self.sq.query_general_information_geoip_country,
            'Geoip_Region': self.sq.query_general_information_geoip_region,
            'Oauth2': self.sq.query_general_information_oauth2,
            'Opcode': self.sq.query_general_information_opcode,
            'Gen_Rebate_Dispatch': self.sq.insert_general_information_rebate_dispatch,
        }

    def do_work(self, worker_bot):
        worker_bot()

    def do_all_work(self):
        for w in self.worker.keys():
            if 'deposit' in w:
                print(self.worker.values())

    def run_worker(self, m):
        if not envi.isDevEnv:
            client = google.cloud.logging.Client()
            handler = CloudLoggingHandler(client, name="SSR_BBOS_SQ.log")
            logging.getLogger().setLevel(logging.INFO)
            setup_logging(handler)
            logging.info(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': ====== SSR_BBOS_SQ EXECUTE ======')
        worker_bot = self.worker[m]
        try:
            self.do_work(worker_bot)

            BQ_check_result = self.sq.result
            print(BQ_check_result)
            logging.info(BQ_check_result)

        except Exception as e:
            traceback.print_exc()
            # logger.exception(traceback.format_exc())
            logging.exception(traceback.format_exc())
            print(self.sq.result)
            logging.info(self.sq.result)

# if __name__ == '__main__':
#     test = SSRBBOSSQ()
