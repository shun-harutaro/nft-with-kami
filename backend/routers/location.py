#フロントエンドは/frontend/src/components
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

GOOGLE_MAPS_API_KEY = "AIzaSyDbDeMxbmZ5ElzhxeeNYk2cjBBU4xftHbc" #os.getenv("AIzaSyDbDeMxbmZ5ElzhxeeNYk2cjBBU4xftHbc")

@router.get("/location")
async def get_nearby_shrines(latitude: float, longitude: float, radius: int = 5000):#Query(5000)
    """
    現在地を基に半径内の神社を取得する
    """
    try:
        url = (
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
            f"?location={latitude},{longitude}&radius={radius}&keyword=神社&key={GOOGLE_MAPS_API_KEY}&language=ja&region=jp"
        )
        response = requests.get(url)
        response_data = response.json()

        #print(f"Latitude: {latitude}, Longitude: {longitude}")

        
        # 必要な情報を整理
        shrines = [
            {
                "name": result.get("name"),
                "address": result.get("vicinity"),
                "location": result.get("geometry", {}).get("location")
            }
            for result in response_data.get("results", [])[:5]
        ]
        
        return JSONResponse(content={"shrines": shrines})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
