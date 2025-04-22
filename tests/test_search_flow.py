import pytest

# Define readable values
JULY = "July"
DECEMBER = "December"
JULY_NEXT_YEAR = "July (next year)"
DECEMBER_NEXT_YEAR = "December (next year)"
JULY_TWO_YEARS = "July (two years from now)"
DECEMBER_TWO_YEARS = "December (two years from now)"
NUMBER_ELEMENT_IN_DROPDOWN = 7
DEFAULT_VALUE = "Select..."

@pytest.mark.smoke
def test_dropdowns_are_visible(search_page):
    assert search_page.is_departure_dropdown_visible()
    assert search_page.is_return_dropdown_visible()

@pytest.mark.sanity
def test_dropdowns_have_seven_options(search_page):
    assert len(search_page.get_departure_options()) == NUMBER_ELEMENT_IN_DROPDOWN
    assert len(search_page.get_return_options()) == NUMBER_ELEMENT_IN_DROPDOWN

@pytest.mark.regression
def test_validation_for_unselected_fields(search_page):
    search_page.select_departure_by_text(DEFAULT_VALUE)
    search_page.select_return_by_text(DEFAULT_VALUE)
    search_page.click_search()
    message = search_page.get_result_text()
    assert "Please select both" in message or "must select" in message

def test_return_must_be_after_departure(search_page):
    search_page.select_departure_by_text(JULY_NEXT_YEAR)
    search_page.select_return_by_text(DECEMBER)
    search_page.click_search()
    message = search_page.get_result_text()
    assert "Return month must be after" in message

def test_seats_available_message(search_page):
    search_page.select_departure_by_text(DECEMBER)
    search_page.select_return_by_text(JULY_NEXT_YEAR)
    search_page.click_search()
    message = search_page.get_result_text()
    assert "Seats available!" in message

def test_seats_unavailable_message(search_page):
    search_page.select_departure_by_text(JULY_TWO_YEARS)
    search_page.select_return_by_text(DECEMBER_TWO_YEARS)
    search_page.click_search()
    message = search_page.get_result_text()
    assert "Sorry, there are no more seats" in message
