# GroceryMate — Requirements Analysis

## 1. Product Ratings and Comments

### Question 1: Can users rate products they have purchased through their order history?

**Observation:** I searched the website but could not find an order history or a list of previous orders.

**Answer:** I could not find an order history on the website. Therefore, I could not determine whether users are expected to rate products through their previous orders. This needs clarification.

### Question 2: Can a user submit more than one comment for the same product?

**Observation:** I could submit only one comment for a product, even after ordering the same product twice. I could edit or delete my existing comment.

**Answer:** The website allows users to submit one comment per product and to edit or delete the existing comment. I could not submit a second comment after ordering the product again. Whether multiple comments should be allowed needs clarification.

### Question 3: Can a user submit a new comment after deleting an existing rating and comment?

**Observation:** After deleting my rating and comment, I could submit a rating again, but I could not add a comment.

**Answer:** After deleting the existing rating and comment, the website allowed me to submit a new rating but did not allow me to add a comment. The expected behavior needs clarification.

## 2. Age Verification

### Question 1: What should happen if the user enters an invalid date of birth?

**Observation:** When I entered an invalid date of birth, the website displayed a message indicating that I was underage and did not allow me to access the alcohol category.

**Answer:** During my test, the website treated the invalid date as an indication that I was underage. The expected behavior for invalid dates needs clarification.

### Question 2: Can the user edit or correct their age after entering it?

**Observation:** I could not find an option to edit or correct my age after entering it.

**Answer:** I could not identify an option to edit the entered age. Whether users should be able to correct their age, and how this should work, needs clarification.

### Question 3: Is age verification required every time the user opens the alcohol category?

**Observation:** After closing and reopening the website, I was asked to verify my age again, even though I had already entered my age before registration.

**Answer:** During my test, age verification was requested again after reopening the website. Whether verification should persist for a session, a registered user, or a longer period needs clarification.

### Question 4: When should the age-verification window appear?

**Observation:** The age-verification window appeared when I clicked the **Shop** button.

**Answer:** During my test, age verification was requested when entering the shop. It is unclear whether this is the intended behavior or whether verification should be requested specifically when accessing the alcohol category. This needs clarification.

## 3. Shipping Costs

### Question 1: Should the shopping cart be emptied automatically after an order is completed?

**Observation:** After completing an order, the cart still contained the items from the previous order. The shipping costs displayed in the cart did not reflect the expected costs for the current cart value.

**Answer:** The cart still contained the previous order's items after checkout. Whether the cart should be emptied automatically after an order is completed needs clarification. This behavior may also affect shipping cost calculations and other checkout functions.

### Question 2: Should shipping costs be recalculated automatically when items are removed from the cart?

**Observation:** After removing items and reducing the cart value below $20, the shipping costs remained at $0 until I reloaded the page. After reloading, the shipping costs were updated to $5.

**Answer:** The shipping costs are not updated automatically when the cart value changes. They are updated only after reloading the page. Whether shipping costs should be recalculated immediately without reloading needs clarification.

### Question 3: Are shipping costs fixed at $5 for orders below $20?

**Observation:** I tested two different order values, both below $20, and the shipping costs were $5 in both cases.

**Answer:** In both tests, shipping costs were $5 for orders below $20. I could not determine whether this is the intended rule for all orders below the free-shipping threshold. This needs clarification.

## 4. Summary

During my exploration of the GroceryMate website, I tested the product rating and comment functionality, age verification, and shipping cost calculations.

- **Product ratings and comments:** I identified limitations related to order history, submitting multiple comments, and adding a comment after deleting an existing rating and comment.
- **Age verification:** I observed how the website handles invalid dates, whether verification is requested again after reopening the website, and when the verification window appears. I could not find an option to edit the entered age.
- **Shipping costs:** I observed that the cart retained items after checkout, shipping costs did not update when the cart value fell below $20 in my test, and orders below $20 incurred $5 shipping costs in two tests.

These findings document the website's observed behavior. Where the intended behavior could not be established from the website, clarification is required to determine the expected requirements and identify potential defects.
