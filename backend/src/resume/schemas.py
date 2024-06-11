from datetime import date

from pydantic import BaseModel

from backend.src.resume.models import Gender, ResumeStatus


class ResumeCreate(BaseModel):
    first_name: str
    last_name: str
    job_title: str
    age: int
    gender: Gender
    city: str
    expected_salary: int
    resume_status: ResumeStatus
    skills: str
    about: str
    experience: str
    education: str
    ready_to_relocate: bool
    ready_for_business_trips: bool


class ResumeRead(BaseModel):
    first_name: str
    last_name: str
    job_title: str
    age: int
    gender: Gender
    city: str
    expected_salary: int
    resume_status: ResumeStatus
    skills: str
    about: str
    experience: str
    education: str
    ready_to_relocate: bool
    ready_for_business_trips: bool


class ResumeUpdate(BaseModel):
    first_name: str | None
    last_name: str | None
    job_title: str | None
    age: int | None
    gender: Gender | None
    city: str | None
    expected_salary: int | None
    resume_status: ResumeStatus | None
    skills: str | None
    about: str | None
    experience: str | None
    education: str | None
    ready_to_relocate: bool | None
    ready_for_business_trips: bool | None
