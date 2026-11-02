from infrastructure.erro.exceptions.bad_request_exception import BadRequestException
from infrastructure.erro.exceptions.conflict_exception import ConflictException
from infrastructure.erro.exceptions.not_found_exception import NotFoundException
from infrastructure.erro.exceptions.unauthorized_exception import UnauthorizedException

from fastapi import  FastAPI, Request
from infrastructure.erro.error_response import ErrorResponse

class GlobalHandler:
   def __init__(self, api: FastAPI):
      api.add_exception_handler(Exception, self.internal_error_handler)
      api.add_exception_handler(ConflictException, self.conflict_handler)
      api.add_exception_handler(NotFoundException, self.not_found_handler)
      api.add_exception_handler(BadRequestException, self.bad_request_handler)


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
   async def conflict_handler(request: Request, e: Exception):
      if not isinstance(e, ConflictException):
         raise e

      return ErrorResponse(
         status_code=409,
         error=type(e).__name__,
         message=e.message,
         path=request.url.path,
         type=None
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
   async def unauthorized_handler(request: Request, e: Exception):
      if not isinstance(e, UnauthorizedException):
         raise e

      return ErrorResponse(
         status_code=401,
         error=type(e).__name__,
         message=e.message,
         path=request.url.path,
         type=None
      ).to_response()

   @staticmethod
   async def bad_request_handler(request: Request, e: Exception):
      if not isinstance(e, BadRequestException):
         raise e

      return ErrorResponse(
         status_code=400,
         error=type(e).__name__,
         message=e.message,
         path=request.url.path,
         type = None
      ).to_response()


