Feature: Test the functionality of products category
  # Scenariu 1: Verificare cel mai mare pret din lista "Laptop laptopuri"

  @products_page
  # Scenariu 1
  Scenario: Check the highest price from the "Laptop laptops" list
    Given I am on the "Laptops, tablets & software" page
    When I click on "Laptop laptops"
    And I click to the sort products and choose to see descending list
    Then I choose the most expensive product from the displayed list

