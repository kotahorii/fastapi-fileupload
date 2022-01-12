from fastapi import (
    APIRouter,
    UploadFile,
    File,
    status,
    staticfiles,
    responses,
)
from ..functions import fileupload


router = APIRouter(prefix="/upload", tags=["file"])
router.mount(
    "/uploads",
    staticfiles.StaticFiles(directory="uploads"),
    name="uploads",
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload(file: UploadFile = File(...)):
    return fileupload.upload(file)


@router.get("/download/{name}", response_class=responses.FileResponse)
def get_file(name: str):
    path = f"uploads/{name}"
    return path
