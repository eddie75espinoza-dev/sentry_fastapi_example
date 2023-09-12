from fastapi import FastAPI
import logging
import tracker_sentry

logging.basicConfig(
    filename="test_fastapi.log",
    filemode="w",
)

app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/sentry-debug")
async def root():
    logger.error("Raise error")
    x = 1 / 0


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8050)
