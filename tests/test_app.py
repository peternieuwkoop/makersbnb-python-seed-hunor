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

"""
We can see all listings
"""
def test_all_listings(page, test_web_address, db_connection):
    db_connection.seed("seeds/listings_table.sql")
    page.goto(f"http://{test_web_address}/listings")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Name: Country Cottage\nDescription: Quaint little cottage with a view\nPrice (GBP): 75",
        "Name: Beach House\nDescription: Well situated beachfront property\nPrice (GBP): 100",
        "Name: Potato House\nDescription: House that looks like a potato\nPrice (GBP): 250"
        ])
    
"""
We can see an individual listing by its id
"""
def test_get_individual_listing(page, test_web_address, db_connection):
    db_connection.seed("seeds/listings_table.sql")
    page.goto(f"http://{test_web_address}/listings/1")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Description: Quaint little cottage with a view\nPrice (GBP): 75"
        ])
    
"""
We can see all listings belonging to a specified user_id
"""
def test_access_users_listings(page, test_web_address, db_connection):
    db_connection.seed("seeds/listings_table.sql")
    page.goto(f"http://{test_web_address}/listings/user/1")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text([
        "Name: Country Cottage\nDescription: Quaint little cottage with a view\nPrice (GBP): 75",
        "Name: Beach House\nDescription: Well situated beachfront property\nPrice (GBP): 100"
    ])
