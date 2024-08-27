from fastapi import APIRouter, File, Query, UploadFile
from fastapi.responses import JSONResponse
from app.services.quotazione_service import import_excel_data

router = APIRouter()

@router.post("/import-listone")
async def import_listone(file: UploadFile = File(...), year: str = Query(...)):
    try:
        # Call the service method to read the Excel file and get IDs
        ids = import_excel_data(file.file, year)
        
        # Return only the array of IDs
        return JSONResponse(content=ids)

    except ValueError as ve:
        return JSONResponse(content={"error": str(ve)}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)