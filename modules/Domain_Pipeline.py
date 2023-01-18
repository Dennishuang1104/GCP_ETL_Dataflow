from modules.Environment import Envi
import apache_beam as beam
# 兩支程式
# 加上hall/ all / table


class DomainPipeline:
    def __init__(self):
        self.table_name = ''
        self.project = ''
        self.code = int()

    def build_vtcssr_pipeline(self, first_rows, output, table_name, tables, domain_id):
        self.code = domain_id
        if tables in Envi.WITHOUT_DOMAIN_TABLES:
            VTC_SSR = output.TABLE_NAME
            print(VTC_SSR)
            domain_pipeline = first_rows | f'Filter SSR {table_name}: {tables}' >> beam.Filter(lambda find_domain: find_domain['domain_id'] == self.code) \
                                         | f'Remove SSR{table_name}: {tables}' >> beam.Filter(lambda del_domain: del_domain.pop('domain_id')) \
                                         | f"Write SSR  {VTC_SSR}  {tables}" >> beam.io.WriteToBigQuery(VTC_SSR, schema=output.SCHEMA)

        else:
            VTC_SSR = output.TABLE_NAME
            domain_pipeline = first_rows | f'Filter SSR {table_name}: {tables}' >> beam.Filter(lambda find_domain: find_domain['domain_id'] == self.code) \
                                         | f"Write SSR  {VTC_SSR}  {tables}" >> beam.io.WriteToBigQuery(VTC_SSR, schema=output.SCHEMA)

    def build_vtcgh_pipeline(self, first_rows, output, table_name, tables, domain_id):
        self.code = domain_id
        if tables in Envi.WITHOUT_DOMAIN_TABLES:
            VTC_GH = output.TABLE_NAME.replace('your-project-name', 'your-project-name')
            domain_pipeline = first_rows | f'Filter GH {table_name}: {tables}' >> beam.Filter(lambda find_domain: find_domain['domain_id'] == self.code) \
                                         | f'Remove GH {table_name}: {tables}' >> beam.Filter(lambda del_domain: del_domain.pop('domain_id')) \
                                         | f"Write GH {VTC_GH}  {tables}" >> beam.io.WriteToBigQuery(VTC_GH, schema=output.SCHEMA)

        else:
            VTC_GH = output.TABLE_NAME.replace('your-project-name', 'your-project-name')
            domain_pipeline = first_rows | f'Filter GH {table_name}: {tables}' >> beam.Filter(lambda find_domain: find_domain['domain_id'] == self.code) \
                                         | f"Write GH id: {VTC_GH}  {tables}" >> beam.io.WriteToBigQuery(VTC_GH, schema=output.SCHEMA)

    def build_ssr_geninfo_pipeline(self, first_rows, output):
        VTC_SSR = output.TABLE_NAME
        print(VTC_SSR)
        print(output.SCHEMA)
        g_query_game_code = 'SELECT * FROM `your-project-name.dataset.Game_Code` ;'
        game_code_schema = {'fields': [{'name': 'id', 'type': 'INTEGER', 'mode': 'REQUIRED'},
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
        g_pipeline = first_rows | f"Write to ssr_GenInfo {output.TABLE_NAME} " >> beam.io.WriteToBigQuery(VTC_SSR, schema=output.SCHEMA) \
                                | f"Query_TABLE {output.TABLE_NAME} Game_Code" >> beam.io.ReadFromBigQuery(query=g_query_game_code,use_standard_sql=True) \


    def build_gh_geninfo_pipeline(self, first_rows, output):
        VTC_GH = output.TABLE_NAME.replace('your-project-name', 'your-project-name')
        print(VTC_GH)
        print(output.TABLE_NAME)
        g_pipeline = first_rows | f"Write to gh_GenInfo {output.TABLE_NAME} " >> beam.io.WriteToBigQuery(VTC_GH, schema=output.SCHEMA)
