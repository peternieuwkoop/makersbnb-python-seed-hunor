from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")


def test_get_home(page, test_web_address):
    page.goto(f"http://{test_web_address}/home")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Find Your Perfect Stay")


def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    h3_tag = page.locator("h3")
    expect(h3_tag).to_have_text("Login to Your Account")


def test_get_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    h3_tag = page.locator("h3")
    expect(h3_tag).to_have_text("Create an Account")

def test_get_all_listings(page, test_web_address, db_connection):
    db_connection.seed("seeds/listings_table.sql")
    page.goto(f"http://{test_web_address}/listings")
    h4_tag = page.locator("h4")
    expect(h4_tag).to_have_text([
        "Country Cottage",
        "Beach House",
        "Potato House"
    ])
    

def test_get_listing_by_id(page, test_web_address, db_connection):
    db_connection.seed("seeds/listings_table.sql")
    page.goto(f"http://{test_web_address}/find/1")
    h1_tag = page.locator("h1") 
    expect(h1_tag).to_have_text("Country Cottage")

def test_get_new_listing(page, test_web_address):
    page.goto(f"http://{test_web_address}/new-listing")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Create New Listing")


# """
# We can see all listings
# """
# def test_all_listings(page, test_web_address, db_connection):
#     db_connection.seed("seeds/listings_table.sql")
#     page.goto(f"http://{test_web_address}/listings")
#     p_tag = page.locator("p")
#     expect(p_tag).to_have_text([
#         "Name: Country Cottage\nDescription: Quaint little cottage with a view\n75",
#         "Name: Beach House\nDescription: Well situated beachfront property\n100",
#         "Name: Potato House\nDescription: House that looks like a potato\n250"
#         ])