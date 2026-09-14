import random

from fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP("pocai")


class WeatherReading(BaseModel):
    temperature: float
    humidity: float


@mcp.tool
def getTemperature(city: str) -> WeatherReading:
    """Return a simulated temperature and humidity reading for a city."""
    return WeatherReading(
        temperature=round(random.uniform(-10.0, 40.0), 1),
        humidity=round(random.uniform(0.0, 100.0), 1),
    )


if __name__ == "__main__":
    mcp.run(transport="http", port=8080, path="/mcp-weather")
