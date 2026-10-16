from infrastructure.erro.exceptions.not_found_exception import NotFoundException


from fastapi import  FastAPI, Request
from infrastructure.erro.error_response import ErrorResponse

class GlobalHandler:
   def __init__(self, api: FastAPI):
      api.add_exception_handler(Exception, self.internal_error_handler)
      api.add_exception_handler(NotFoundException, self.not_found_handler)


   @staticmethod
   async def internal_error_handler(request: Request, e: Exception):
      return ErrorResponse(
         status_code=500,
         error = type(e).__name__,
         message = "Erro interno",
         type =  e.args,
         path =  request.url.path,
      ).to_response()

   @staticmethod
   async def not_found_handler(request: Request, e: Exception):
      if not isinstance(e, NotFoundException):
         raise e

      return ErrorResponse(
         status_code=404,
         error = type(e).__name__,
         message =e.message,
         path = request.url.path,
         type = None
      ).to_response()

   @staticmethod
   async def bad_request_handler(request: Request, e: Exception):
      if not isinstance(e, NotFoundException):
         raise e

      return ErrorResponse(
         status_code=400,
         error=type(e).__name__,
         message=e.message,
         path=request.url.path,
         type = None
      ).to_response()

