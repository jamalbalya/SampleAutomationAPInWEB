# SampleAutomationAPInWEB

This example performs a simple test on the /api/search/lawyer endpoint of the Perqara API, which returns a list of lawyers based on search criteria. The test verifies that the endpoint returns a 200 status code (indicating success), and that the response contains the expected keys (total and items). It also verifies that the items key is a list with at least one element, and that each item in the list has the expected keys (id, name, slug, location, rating, practiceAreas, languages, price, and profileImage). You can modify the test to suit your specific needs, such as testing other search criteria or adding additional assertions.