# [Integrating machine learning APIs](https://developers.google.com/codelabs/cloud-ml-apis?hl=en&continue=https%3A%2F%2Fcodelabs.developers.google.com%2F%3Fcat%3Dmachinelearning#0)

## Overview

* **Cloud Vision** to understand the content of an image
* **Cloud Speech-to-Text** to transcribe audio to text
* **Cloud Translation** to translate an arbitrary string to any supported language
* **Cloud Natural Language** to extract information from text
* Construct a pipeline that compares an audio recording with an image and determines their relevance to each other
  * Speech recording -> Cloud Speech-to-Text -> Cloud Translation -> Cloud Natural Language -> Compare
  * Image -> Cloud Vision -> Compare

## Setup and Requirements

* Cloud Console
  * **PROJECT_ID**
  * enable billing

### Enable the APIs

* APIs & services -> Enable APIs and Services -> API Library
* setting up authentication

### Cloud Shell

* Google Cloud Shell is a command line environment running in the Cloud.

### Service Account

* You will need a service account to authenticate.
  * ```gcloud iam service-accounts create [NAME]```
* Now you'll need to generate a key to use that service account. Replace [FILE_NAME] with desired name of key, [NAME] with the service account name from above and [PROJECT_ID] with the ID of your project. The following command will create and download the key as [FILE_NAME].json: 
  * ```gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com```
* To use the service account, you'll have to set the variable GOOGLE_APPLICATION_CREDENTIALS to the path of the key. To do this, run the following command after replacing [PATH_TO_FILE] and [FILE_NAME]:
  * ```export GOOGLE_APPLICATION_CREDENTIALS=[PATH_TO_FILE]/[FILE_NAME].json```

## Cloud Vision

* Python client
  * [code samples](https://cloud.google.com/vision/docs/samples)
    * curl

## Cloud Translation

## Cloud Natural Language

## [Integrating ML APIs](https://github.com/googlecodelabs/integrating-ml-apis/blob/master/solution.py)