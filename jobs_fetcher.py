import requests

def fetch_jobs():
    url = 'https://www.arbeitnow.com/api/job-board-api'
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    jobs = data.get("data", [])

    job_list = []
    for job in jobs:
        job_info = {
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "description": job.get("description"),
            "url": job.get("url"),
            "tags": job.get("tags", []),
            "remote": job.get("remote", False),
            "job_types": job.get("job_types", [])
        }
        job_list.append(job_info)

    return job_list


def fetch_jobs_filtered(location=None, remote=None, tag=None):
    url = 'https://www.arbeitnow.com/api/job-board-api'
    response = requests.get(url)
    response.raise_for_status()
    jobs = response.json().get("data", [])

    filtered = []
    for job in jobs:
        if location and location.lower() not in job.get("location", "").lower():
            continue
        if remote is not None and job.get("remote") != remote:
            continue
        if tag and tag.lower() not in [t.lower() for t in job.get("tags", [])]:
            continue
        filtered.append(job)
    return filtered


if __name__ == "__main__":
    jobs = fetch_jobs()
    for j in jobs:
        print(f"Title: {j['title']}")
        print(f"Company: {j['company']}")
        print(f"Location: {j['location']}")
        print(f"Remote: {'Yes' if j['remote'] else 'No'}")
        print(f"Tags: {', '.join(j['tags'])}")
        print(f"URL: {j['url']}")
        print("-" * 40)
