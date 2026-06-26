from fastapi import APIRouter

Router = APIRouter(prefix="/job", tags=["job"])


@router.get("/")
def read_root():
    return {"job":"job root"}

@router.get("/{job_id}")
def read_job():
    return {"job": "job root"}

@router.get("/{job_id}")
def read_job(job_id: int):
    return {"job_id": job_id}