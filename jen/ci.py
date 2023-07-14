import jenkins
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['CICD']
collection = db['jenkins']

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='fefef1800ede4b3881602df92bea2bee')

# Get information about a specific job
job_name = 'File'  # Replace with the actual job name
try:
    info = server.get_job_info(job_name)

    # Get the last completed build
    last_completed_build = info['lastCompletedBuild']
    if last_completed_build is not None:
        completed_build_number = last_completed_build['number']
        completed_build_duration = last_completed_build.get('duration', 'Not available')
        completed_build_status = last_completed_build.get('result', 'Result not available')

        # Build the data document
        data = {
            'Job Name': job_name,
            'Last Completed Build': completed_build_number,
            'Duration': completed_build_duration,
            'Successful Builds': 0,
            'Failed Builds': 0
        }

        # Check if the build was successful or failed
        if completed_build_status == 'SUCCESS':
            data['Successful Builds'] += 1
        else:
            data['Failed Builds'] += 1

        # Store the data as a single document in MongoDB
        collection.insert_one(data)
        print("Job details stored in the database successfully.")

    else:
        print("No completed builds found for the job.")

except jenkins.NotFoundException:
    print(f"Job '{job_name}' does not exist on the Jenkins server.")