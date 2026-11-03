from typing import Optional
from pydantic import BaseModel

from dto.dashboard.StockDashboardDTO import StockDashboardDTO


class DashboardResponseDTO(BaseModel):
    lowest_stock: Optional[StockDashboardDTO] = None
    highest_stock: Optional[StockDashboardDTO] = None