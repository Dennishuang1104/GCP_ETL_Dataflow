import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from modules import SSRBBosStruct
from modules.Environment import Envi
from modules.SSRBBOS import SSRBBOSSQ
import os.path
import sys
import concurrent.futures
from modules.Domain_Pipeline import DomainPipeline
window_interval_sec = 60

def run():
    print(sys.path)
    """Build and run the pipeline."""
    os.environ.setdefault('GOOGLE_APPLICATION_CREDENTIALS', 'modules/cred/gh-bigquery.json')
    options = PipelineOptions(
        project='gcp-20220516-001',
        temp_location="gs://ssr_bbos_dataflow/test",
        staging_location="gs://ssr_bbos_dataflow/test",
        region='us-central1',
        job_name="dennis-dataflow-test"
    )
    test = SSRBBOSSQ()
    with beam.Pipeline(options=options) as pipeline:
        for table in test.domain_worker.keys():
            # tables = test.domain_worker[table]
            q = test.domain_worker[table]
            # task_thread.threads.append(task_thread.executor.submit(table_name))
            if table in Envi.GENERAL_INFORMATION_TABLES:
                g_query = q(test.insert_minutes)
                # print(g_query)
                geninfo_rows = pipeline | f'Query_TABLE {table}' >> beam.io.ReadFromBigQuery(query=g_query, use_standard_sql=True)
                g_output = getattr(SSRBBosStruct, table)()
                g_output.get_table_name('test_general_information')
                gh_geninfo_pipeline = DomainPipeline()
                gh_geninfo_pipeline.build_ssr_geninfo_pipeline(geninfo_rows, g_output)
                # gh_geninfo_pipeline.build_gh_geninfo_pipeline(geninfo_rows, g_output)
            else:
                query = q(test.insert_minutes)
                domain_rows = pipeline | f'Query_TABLE {table}' >> beam.io.ReadFromBigQuery(query=query, use_standard_sql=True)
                for domain_id in Envi.DOMAIN_ID_LIST:
                    ssr_domain_pipeline = DomainPipeline()
                    # 讀取Raw_data
                    output = getattr(SSRBBosStruct, table)()
                    table_name = Envi.DOMAIN_TABLE_DICT.get(str(domain_id))
                    output.get_table_name(table_name)
                    ssr_domain_pipeline.build_vtcssr_pipeline(domain_rows, output, table_name, table, domain_id)


if __name__ == "__main__":
    run()