from fastapi import FastAPI, Query
from jobs_fetcher import fetch_jobs_filtered  # jobs_fetcher.py içindeki fonksiyon

app = FastAPI()

@app.get("/jobs")
def get_jobs(location: str = None, remote: bool = None, tag: str = None):
    jobs = fetch_jobs_filtered(location, remote, tag)
    return jobs
