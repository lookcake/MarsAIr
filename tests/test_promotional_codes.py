import pytest
import json
import os
from pathlib import Path

# Define readable values instead of raw indexes
JULY = "July"
DECEMBER = "December"
JULY_NEXT_YEAR = "July (next year)"
DECEMBER_NEXT_YEAR = "December (next year)"
JULY_TWO_YEARS = "July (two years from now)"
DECEMBER_TWO_YEARS = "December (two years from now)"
NUMBER_ELEMENT_IN_DROPDOWN = 7
DEFAULT_VALUE = "Select..."


# Load promo codes from JSON file
filepath = os.path.join(os.path.dirname(__file__), "testdata", "promo_codes.json")
with open(filepath, "r") as file:
    promo_codes = json.load(file)
    valid_codes = promo_codes['valid_codes']
    invalid_codes = promo_codes['invalid_codes']
    empty_code = promo_codes['empty_code']


def test_promotional_code_field_display(search_page):
    assert search_page.is_promotional_code_visible()

@pytest.mark.ac2_ac3
@pytest.mark.parametrize("data_input",valid_codes )
def test_valid_code_applies_discount(search_page, data_input):
    code = data_input["code"]
    expected_discount = data_input["expected_discount"]
    search_page.select_departure_by_text(DECEMBER)
    search_page.select_return_by_text(JULY_NEXT_YEAR)
    search_page.enter_promo_code(code)
    search_page.click_search()
    message = search_page.get_result_text()
    assert f"Promotional code {code.upper()} used: {expected_discount}% discount!" in message

@pytest.mark.ac4
@pytest.mark.parametrize("data_input",invalid_codes )
def test_invalid_code_displays_error(search_page, data_input):
    code = data_input["code"]
    search_page.select_departure_by_text(JULY)
    search_page.select_return_by_text(DECEMBER_NEXT_YEAR)
    search_page.enter_promo_code(code)
    search_page.click_search()
    message = search_page.get_result_text()
    assert f"Sorry, code {code.upper()} is not valid" in message

@pytest.mark.ac6
@pytest.mark.parametrize("data_input",empty_code )
def test_empty_code_proceeds_normally(search_page, data_input):
    search_page.select_departure_by_text(JULY)
    search_page.select_return_by_text(DECEMBER)
    search_page.enter_promo_code(data_input["code"])
    search_page.click_search()
    message = search_page.get_result_text()
    assert "discount" not in message and "not valid" not in message
