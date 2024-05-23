#!/usr/bin/env python

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
"""Dialogflow API Python sample showing how to manage Conversation Profiles.
"""

from google.cloud import dialogflow_v2beta1 as dialogflow
#from google.cloud import dialogflow as dialogflow
import os

# [START dialogflow_create_conversation_profile]
def create_conversation_profile(
    project_id,
    display_name,
    language_code,
):
    """Creates a conversation profile with given values.

    Args:
        project_id: The ID of the project to create the conversation profile in.
        display_name: The display name of the conversation profile.
        language_code: The language code of the conversation profile.
        time_zone: The time zone of the conversation profile.

    Returns:
        The created conversation profile.
    """

    # Create a Dialogflow client.
    client = dialogflow.ConversationProfilesClient()

    # Construct the conversation profile object.
    conversation_profile = {
        "display_name": display_name,
        "language_code": language_code,
    }

    # Create the conversation profile.
    response = client.create_conversation_profile(
        parent=client.common_project_path(project_id),
        conversation_profile=conversation_profile,
    )

    print(f"Created conversation profile: {response.name}")
    return response

# [END dialogflow_create_conversation_profile]

if __name__ == "__main__":
    # [START dialogflow_create_conversation_profile]
    # Get the values from environment variables
    project_id = os.environ.get("PROJECT_ID")
    display_name = os.environ.get("CONVERSATION_PROFILE_DISPLAY_NAME")
    language_code = os.environ.get("LANGUAGE_CODE")

    create_conversation_profile(
        project_id=project_id,
        display_name=display_name,
        language_code=language_code,
    )