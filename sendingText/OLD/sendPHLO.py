import plivo

auth_id = ''
auth_token = ''
phlo_id = ''
payload = {"from" : "+15186350270","to" : "+"}
phlo_client = plivo.phlo.RestClient(auth_id=auth_id, auth_token=auth_token)
phlo = phlo_client.phlo.get(phlo_id)
response = phlo.run(**payload)
#response = phlo.run()
print(str(response))