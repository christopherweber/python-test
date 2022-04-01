import requests 
print("hello there")

msg = "Hacking mainframe..."
print(msg)

resource_url = "https://api.firehydrant.io/v1/services"
intergration_url = "https://api.firehydrant.io/v1/ticketing/projects/3003a67c-3937-4e23-9895-e6c3e03e536e/configuration_options"
# notes_url = "https://api.firehydrant.io/v1/incidents/9deac448-f5ed-4b6e-9456-d2d6b67d44c7/notes"

headers = {"Authorization": "Bearer fhb-fa1ce19a1bc4463905ae800b6c96920c", "Content-Type": "application/json"}

service_payload = {

                "name": "Testing NEW SERVICE HONEYCOMB v2",

                "labels": {
                "name": "sli_slo_client -- [Platform Engineering]",
                "source_id": "1O",
                "business_unit": "Platform Engineering",
                "taxonomy": "juno"
                },

                "service_tier": 5,

                "functionalities": None,

                "owner": None,

                "teams": [
                    {
                        "id": "85f9a639-301f-46c7-bf85-6914de2bbfe9"
                    }
                ],
                "owner": {
                "id": "85f9a639-301f-46c7-bf85-6914de2bbfe9"
                 },
                 "external_resources": [
                {
                "connection_type": "pager_duty",
                "remote_id": "P0CK8TL"
                }
                ],

                "alert_on_add": True,
                "remove_remaining_external_resources": True,
                "remove_remaining_functionalities": True,
                 "remove_remaining_teams": True

            }

payload = {
  "name": "sli_slo_client -- [Platform Engineering]",
  "description": "The client application",
  "labels": {
    "name": "sli_slo_client -- [Platform Engineering]",
    "source_id": "1O",
    "business_unit": "Platform Engineering",
    "taxonomy": "juno"
  },
  "service_tier": 5,
  "teams": [
    {
      "id": "85f9a639-301f-46c7-bf85-6914de2bbfe9"
    }
  ],
  "owner": {
    "id": "85f9a639-301f-46c7-bf85-6914de2bbfe9"
  },
  "functionalities": [
    {
      "id": "123"
    }
  ],
  "external_resources": [
    {
      "connection_type": "pager_duty",
      "remote_id": "PWJ11NE"
    },
    {
      "connection_type": "pager_duty",
      "remote_id": "123"
    }
  ]
}

service_metrics = {
  
}
# events_payload = {"incidentId":"9deac448-f5ed-4b6e-9456-d2d6b67d44c7","visibility":"private_to_org","status_pages":[],"body":"test 4"}
# (mttm * incidents) / time window

def get_metrics():
  change_event_url = "https://api.firehydrant.io/v1/changes/events"
  service_url= "https://api.firehydrant.io/v1/metrics/services/00f1d192-5248-48f2-920a-93edcda63200"
  query_incidents="https://api.firehydrant.io/v1/incidents?severities=UNSET,SEV1&environments=5bfb39cf-e31e-489e-b720-aa186c4535fd&start_date=2022-03-01&end_date=2022-03-29"
  resp = requests.get(query_incidents, headers=headers)
  data = resp.json()
  print(data)

get_metrics()


def create_star_event(incidentId, visibility, body):
    notes_url = f"https://api.firehydrant.io/v1/incidents/{incidentId}/notes"
    events_url = f"https://api.firehydrant.io/v1/incidents/{incidentId}/events"
    events_payload = {'incidentId': incidentId, 'visibility': visibility, 'body': body}
    resp = requests.post(notes_url, json=events_payload, headers=headers)
    resp = requests.get(events_url, headers=headers)
    data = resp.json()
    event_id = data["data"][0]["id"]
    star_events_url = f"https://api.firehydrant.io/v1/incidents/{incidentId}/events/{event_id}/votes"
    resp = requests.patch(star_events_url, json={"direction": "up"}, headers=headers)
    
create_star_event('9deac448-f5ed-4b6e-9456-d2d6b67d44c7', 'private_to_org', 'this should work part 2')

# def get_event(incidentId):
  # events_url = f"https://api.firehydrant.io/v1/incidents/{incidentId}/events"
#   resp = requests.get(events_url, headers=headers)
#   resp.status_code
#   data = resp.json()
#   event_id = data["data"][0]["id"]
#   print(data["data"][0]["id"])
#   print(events_url)
  
# get_event("9deac448-f5ed-4b6e-9456-d2d6b67d44c7")
  


