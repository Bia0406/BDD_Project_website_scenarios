Feature: Test the functionality of products category
  # Scenariu 1: Verificare cel mai mare pret din lista "Laptop laptopuri"
  # Scenariu 2: Verificare cel mai mic pret din lista "Telefoane Mobile"
  # Scenariu 3:

  @products_page
  # Scenariu 1
  Scenario: Check the highest price from the "Laptop laptops" list
    Given I am on the "Laptops, tablets & software" page
    When I click on "Laptop laptops"
    And I click to the sort products and choose to see descending list
    Then I choose the most expensive product from the displayed list

  @products_page
  # Scenariu 2
  Scenario: Check the cheapest price from the "Mobile Phones" list
    Given I am on the "Mobile Phones & Gadgets" page
    When I click on "Mobile Phones"
    And I click to the sort products and choose to see the lowest price from list
    Then I choose the cheapest product from the displayed list

