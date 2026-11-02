class ConflictException(Exception):
   def __init__(self, message: str = "Conflito na requisição"):
      self.message = message
      super().__init__(self.message)