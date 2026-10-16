class BadRequestException(Exception):
   def __init__(self, message: str = "Requisição invalida"):
      self.message = message
      super().__init__(self.message)