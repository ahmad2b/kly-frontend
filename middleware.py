import time
from fastapi import Request
from logger import logger


async def log_middleware(request: Request, call_next):
    start = time.time()

    response = await call_next(request)
    process_time = time.time() - start

    log_dict = {
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "process_time": f"{process_time:.4f} ms",
    }
    logger.info(log_dict, extra=log_dict)
    return response
