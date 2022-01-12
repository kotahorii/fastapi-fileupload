from fastapi import File, UploadFile, status, HTTPException
import os
import shutil
import string
import random

ALLOWED_EXTENSIONS = set(["jpg", "jpeg", "png"])
UPLOAD_FOLDER = "./uploads"


def allowed_file(filename: str):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def randomname(n: int):
    randlst = [
        random.choice(string.ascii_letters + string.digits)
        for i in range(n)
    ]
    return "".join(randlst)


def upload(file: UploadFile = File(...)):
    if file and allowed_file(file.filename):
        filename = randomname(10) + "_" + file.filename
        fileobj = file.file
        upload_dir = open(os.path.join(UPLOAD_FOLDER, filename), "wb+")
        shutil.copyfileobj(fileobj, upload_dir)
        upload_dir.close()
        return {"file uploaded": filename}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="file is invalid",
    )
