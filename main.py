from fastapi import FastAPI, Path, Query
from api import users, sections, courses

app = FastAPI(
            title="FastAPI with Polat",
                description="Test api project",
                version="0.0.1",
                # terms_of_service="http://example.com/terms/",
                contact={
                    "name": "Ali",
                    # "url": "http://x-force.example.com/contact/",
                    "email": "op@gmail.com",
                },
                license_info={
                    "name": "SEU",
                },
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)


