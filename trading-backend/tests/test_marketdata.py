import time
import pytest
from unittest.mock import patch, Mock
from itertools import cycle
from MarketData import MarketData
from Model import Model
from Position import Position
        
def last_price_values():
    last_prices = [3000, 2900, 2800, 2700, 2600, 2500, 2400, 2300, 2200, 2100, 2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 700, 700, 600, 500, 400, 300, 200, 100] # Replace with your desired sequence of values
    return cycle(last_prices)

@pytest.fixture
def mock_requests_get():
    
    last_prices = last_price_values()  # Create an iterator
        
    with patch('requests.get') as mock_get:
        def side_effect(*args, **kwargs):
            mock_response = Mock()
            mock_response.json.return_value = {'lastPrice': next(last_prices)}
            mock_response.status_code = 200
            return mock_response

        mock_get.side_effect = side_effect
        yield mock_get

def test_poll_with_sequential_lastPrices(mock_requests_get):
    market_data = MarketData()

    # First call
    market_data.poll()
    assert market_data.last_price == 300  # First value

    # Second call
    market_data.poll()
    assert market_data.last_price == 200  # Second value

    # Third call
    market_data.poll()
    assert market_data.last_price == 100  # Second value

def test_evaluate_with_sequential_lastPrices(mock_requests_get):
    market_data: MarketData = MarketData()
    model: Model = Model(market_data)
    
    position = Position(model)
        
    while True:

        market_data.poll()
        result = model.evaluate()

        print('result!!1', result, model.new_price)
    
        time.sleep(1)