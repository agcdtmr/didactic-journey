import requests


def request_api():
    response = requests.get('https://www.themuse.com/api/public/jobs?category=Computer%20and%20IT&category=Customer%20Service&category=Data%20and%20Analytics&category=Data%20Science&category=Design%20and%20UX&category=IT&category=Science%20and%20Engineering&category=Software%20Engineer&category=Software%20Engineering&category=UX&level=Entry%20Level&level=Internship&page=0').json()

    for job in response['results']:
        data = [{
            "employer_name": entry['company']['name'],
            "job_title": entry['name'],
            "link": entry['refs']['landing_page'],
            "publication_date": entry['publication_date'],
            # To do: retrieve all locations
            "location": entry['locations'][0]['name'],
            # To do: retrieve all categories
            "category": entry['categories'][0]['name'],
            "job_ID": entry['id'],
            "company_id": entry['company']['id'],
            "job_description": entry['contents'],

        }
            for entry in response['results']]

        return data


# print(request_api())
