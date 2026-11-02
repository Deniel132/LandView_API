class UnauthorizedException(Exception):
   def __init__(self, message: str = "Não autorizado"):
      self.message = message
      super().__init__(self.message)