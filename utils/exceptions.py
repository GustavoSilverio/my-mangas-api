from fastapi import HTTPException

def raiseResponseException(status_code: int, message: str, error_type: str):
    raise HTTPException(
            status_code=status_code,
            detail={
                "message": message,
                "type": error_type
            }
        )