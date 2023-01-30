locals {
  data_lake_bucket = "dtc_data_lake"
  
}

locals {
  auth_file ="C:/Users/Dell/Documents/DataTalks.Club/Gcloud/tofag-20/dtc-de-project-376110-68c52722e95c.json"
}



//export GOOGLE_AUTHENTICATION_CREDENTIALS="C:/Users/Dell/Documents/DataTalks.Club/Gcloud/tofag-20/dtc-de-project-376110-68c52722e95c.json"

variable "project" {
  description = "Your GCP Project ID"
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default = "europe-west6"
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "trips_data_all"
}


