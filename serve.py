import os
from time import sleep

import uvicorn

if __name__ == "__main__":
    print("Run migrations...")
    sleep(5)
    os.system("alembic upgrade head")
    print("Run app...")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
