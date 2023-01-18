gcloud functions deploy ssr_test_bq_schedule --source=. \
--memory 8GB --timeout=540s --quiet --service-account your_accout@yourproject_name.iam.gserviceaccount.com \
 --entry-point main  --runtime python37  --trigger-http --region=us-central1 \
--allow-unauthenticated