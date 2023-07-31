from fastapi import FastAPI

app = FastAPI()

change = {}
@app.post("/salesperformance")
async def create_update(quarters:str, category:str, subcategory:str, change_made:str, report_made:str, output:str):
    change = {
        "quarters": quarters,
        "category": category,
        "subcategory": subcategory,
        "change_made": change_made,
        "report_made": report_made,
        "output": output
    }
    return change
