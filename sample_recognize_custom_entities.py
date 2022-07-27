"""
FILE: sample_recognize_custom_entities.py
DESCRIPTION:
    This sample demonstrates how to recognize custom entities in documents.
    Recognizing custom entities is available as an action type through the begin_analyze_actions API.
    For information on regional support of custom features and how to train a model to
    recognize custom entities, see https://aka.ms/azsdk/textanalytics/customentityrecognition
USAGE:
    python sample_recognize_custom_entities.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_LANGUAGE_ENDPOINT - the endpoint to your Language resource.
    2) AZURE_LANGUAGE_KEY - your Language subscription key
    3) CUSTOM_ENTITIES_PROJECT_NAME - your Language Studio project name
    4) CUSTOM_ENTITIES_DEPLOYMENT_NAME - your Language Studio deployment name
"""


import os
from dotenv import load_dotenv
load_dotenv()


def sample_recognize_custom_entities():
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        RecognizeCustomEntitiesAction,
    )

    endpoint = os.environ["AZURE_LANGUAGE_ENDPOINT"]
    # endpoint = 'https://voice-classification.cognitiveservices.azure.com/'
    key = os.environ["AZURE_LANGUAGE_KEY"]
    # key = '46da76a4cbc04e07919c9ac09a95304e'
    project_name = os.environ["CUSTOM_ENTITIES_PROJECT_NAME"]
    # project_name = 'named_entity_hackathon'
    deployment_name = os.environ["CUSTOM_ENTITIES_DEPLOYMENT_NAME"]
    # deployment_name = 'deploy-1'
    path_to_sample_document = os.path.abspath(
        os.path.join(
            os.path.abspath(__file__),
            "..",
            "./text/text_recognized.txt",
        )
    )

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    with open(path_to_sample_document) as fd:
        document = [fd.read()]

    poller = text_analytics_client.begin_analyze_actions(
        document,
        actions=[
            RecognizeCustomEntitiesAction(
                project_name=project_name, deployment_name=deployment_name
            ),
        ],
    )

    document_results = poller.result()
    print("##################hola###################")

    for result in document_results:
        custom_entities_result = result[0]  # first document, first result
        # print("##################hola###################")
        print("custom_entities_result: ",custom_entities_result)
        print("custom_entities_result entities: ",custom_entities_result.entities)
        if not custom_entities_result.is_error:
            for entity in custom_entities_result.entities:
                # print(
                #     "Entity '{}' has categoryYY '{}' with confidence score of '{}'".format(
                #         entity.text, entity.category, entity.confidence_score
                #     )
   
                # )
                print('entity: ', entity )
                entities = []
                entities.append(entity.text)
                print("entities: ",entities)
                response_categorization = {}
                response_categorization["entities"] = []
                response_categorization["entities"].append({"text":entity.text})
                response_categorization["entities"].append({"category":entity.category})
            print(response_categorization)
            return response_categorization
        else:
            print(
                "...Is an error with code '{}' and message '{}'".format(
                    custom_entities_result.code, custom_entities_result.message
                )
            )
    # return custom_entities_result


if __name__ == "__main__":
    sample_recognize_custom_entities()