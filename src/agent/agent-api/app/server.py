from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from sql_azure_openai import chain as sql_azure_openai_chain

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, sql_azure_openai_chain, path="/sql-azure-openai")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
