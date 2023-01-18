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
            VTC_GH = output.TABLE_NAME.replace('gcp-20220516-001', 'gcp-20190903-01')
            domain_pipeline = first_rows | f'Filter GH {table_name}: {tables}' >> beam.Filter(lambda find_domain: find_domain['domain_id'] == self.code) \
                                         | f'Remove GH {table_name}: {tables}' >> beam.Filter(lambda del_domain: del_domain.pop('domain_id')) \
                                         | f"Write GH {VTC_GH}  {tables}" >> beam.io.WriteToBigQuery(VTC_GH, schema=output.SCHEMA)

        else:
            VTC_GH = output.TABLE_NAME.replace('gcp-20220516-001', 'gcp-20190903-01')
            domain_pipeline = first_rows | f'Filter GH {table_name}: {tables}' >> beam.Filter(lambda find_domain: find_domain['domain_id'] == self.code) \
                                         | f"Write GH id: {VTC_GH}  {tables}" >> beam.io.WriteToBigQuery(VTC_GH, schema=output.SCHEMA)

    def build_ssr_geninfo_pipeline(self, first_rows, output):
        VTC_SSR = output.TABLE_NAME
        print(VTC_SSR)
        print(output.TABLE_NAME)
        g_pipeline = first_rows | f"Write to ssr_GenInfo {output.TABLE_NAME} " >> beam.io.WriteToBigQuery(VTC_SSR, schema=output.SCHEMA)

    def build_gh_geninfo_pipeline(self, first_rows, output):
        VTC_GH = output.TABLE_NAME.replace('gcp-20220516-001', 'gcp-20190903-01')
        print(VTC_GH)
        print(output.TABLE_NAME)
        g_pipeline = first_rows | f"Write to gh_GenInfo {output.TABLE_NAME} " >> beam.io.WriteToBigQuery(VTC_GH, schema=output.SCHEMA)
