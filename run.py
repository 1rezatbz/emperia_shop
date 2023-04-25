from apis import app
import uvicorn
from src.config import check_db

if __name__ == '__main__':
    check_db()
    uvicorn.run(app, host='localhost', port=8000)
