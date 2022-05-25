import pingid
import os

PROPERTIES_FILE = 'pingid.properties'
org_report_file = "orgReport.csv"

pingid = pingid.PingIDDriver(PROPERTIES_FILE, verbose=True)

""" User Management API: Create Job """
print("Calling Create Job...")
create_job_body = {'jobType': "USER_REPORTS"}
create_job_response = pingid.call('rest/4/createjob/do', create_job_body)
job_token = create_job_response['responseBody']['jobToken']

""" User Management API: Get Job Status"""
job_status_body = {'jobToken': job_token}
job_status_response = 'PENDING'
while job_status_response != 'DONE':
    job_status_response = pingid.call('rest/4/getjobstatus/do', job_status_body)['responseBody']['jobResult']['status']
    print(job_status_response)
    if job_status_response == 'FAILURE':
        print('Something went wrong...')
        exit()

""" User Mangement API: Get Organization Report """
print("Calling Get Org Report...")
org_report_body = {'fileType': "CSV"}
org_report_response = pingid.call('rest/4/getorgreport/do', org_report_body)

""" Writing report to CSV """
print(f"Creating {org_report_file}...")
org_report_csv = open(org_report_file, 'w', newline='')
org_report_csv.write(org_report_response)
org_report_csv.close()

print(f"Org report successfully created. Located at: {org_report_file}")
