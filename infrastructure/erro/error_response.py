from typing import Any

from pydantic import BaseModel
from starlette.responses import JSONResponse


class ErrorResponse(BaseModel):
   status_code: int
   message: str
   path: str
   error: str
   type: tuple[Any,  ...] | None

   def to_response(self) -> JSONResponse:
      return JSONResponse(
         status_code=self.status_code,
         content={
            "error": self.error,
            "message": self.message,
            "path": self.path,
            "type": [str(item) for item in self.type] if self.type else None,
         },
      )