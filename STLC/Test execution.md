# Test Execution Documentation

**Application:** GroceryMate  
**Base URL:** https://grocerymate.masterschool.com/

This document contains six representative test execution scenarios: two for each feature. The scenarios follow the step-by-step structure of the provided GitHub example.

---

## Feature 1: Product Rating

### Scenario 1: Submit a rating with written feedback (Valid scenario)

**Related test case:** TC-03  
**Scenario type:** Valid  
**Execution result:** Passed

**User story:** As a registered user who has purchased a product, I want to submit a star rating together with written feedback so that I can share my experience with other users.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|---:|---|---|:---:|---|---|
| 1 | Open the GroceryMate webshop. | The webshop homepage is displayed. | OK | https://grocerymate.masterschool.com/ | — |
| 2 | Log in with a registered user account that has purchased the product. | The user is logged in successfully. | OK | [Login page URL] | — |
| 3 | Navigate to the product that the user has purchased. | The selected product page is displayed. | OK | [Product page URL] | — |
| 4 | Select a star rating between 1 and 5. | The selected star rating is accepted. | OK | [Product page URL] | — |
| 5 | Enter written feedback in the review field. | The written feedback is accepted. | OK | [Product page URL] | — |
| 6 | Submit the review. | The review is submitted successfully and both the star rating and written feedback are displayed for the product. | OK | [Product page URL] | — |

### Scenario 2: Delete a review and submit a new review (Invalid scenario)

**Related test case:** TC-12  
**Scenario type:** Invalid  
**Execution result:** Failed

**User story:** As a registered user who has purchased a product, I want to delete my existing review and submit a new review containing a star rating and written feedback.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|---:|---|---|:---:|---|---|
| 1 | Open the GroceryMate webshop and log in with the registered user account. | The webshop is displayed and the user is logged in successfully. | OK | https://grocerymate.masterschool.com/ | — |
| 2 | Navigate to a product for which the user has already submitted a review. | The product page and the user's existing review are displayed. | OK | [Product page URL] | — |
| 3 | Delete the existing review. | The existing review is deleted successfully. | OK | [Product page URL] | — |
| 4 | Select a new star rating for the same product. | The new star rating is accepted. | OK | [Product page URL] | — |
| 5 | Enter written feedback for the new review and submit it. | The system accepts and submits the new rating together with the written feedback. | NOK | [Product page URL] | [https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/2] |
| 6 | Check the newly submitted review on the product page. | The new star rating and written feedback are both displayed. | NOK | [Product page URL] | [https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/2] |

**Observed result:** After deleting the previous review, the system allowed the user to submit a new rating, but it did not allow the user to add written feedback.

---

## Feature 2: Age Verification

### Scenario 3: Verify a user who is 25 years old (Valid scenario)

**Related test case:** TC-15  
**Scenario type:** Valid  
**Execution result:** Passed

**User story:** As a user who is at least 18 years old, I want to verify my age so that I can access the category containing alcoholic products.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|---:|---|---|:---:|---|---|
| 1 | Open the GroceryMate webshop. | The webshop homepage is displayed. | OK | https://grocerymate.masterschool.com/ | — |
| 2 | Navigate to the category containing alcoholic products and open the age verification window. | The age verification window is displayed and asks the user to enter their date of birth in day/month/year format. | OK | [Alcohol category URL] | — |
| 3 | Enter a date of birth showing that the user is 25 years old. | The entered date of birth is accepted as belonging to a user who is at least 18 years old. | OK | [Age verification URL] | — |
| 4 | Submit the date of birth. | The age verification is successful and the user is allowed to access alcoholic products. | OK | [Alcohol category URL] | — |

### Scenario 4: Check when the age verification window appears (Invalid scenario)

**Related test case:** TC-17  
**Scenario type:** Invalid  
**Execution result:** Failed

**User story:** As a webshop user, I should be asked to verify my age when I open the category containing alcoholic products, rather than when I access the general shopping page.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|---:|---|---|:---:|---|---|
| 1 | Open the GroceryMate webshop. | The webshop homepage is displayed without an age verification window. | NOK | https://grocerymate.masterschool.com/ | [https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/3] |
| 2 | Navigate to the category containing alcoholic products. | The age verification window appears when the user opens the alcoholic products category. | NOK | [Alcohol category URL] | [https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/3] |
| 3 | Check the point at which the age verification window is displayed. | The age verification window is displayed specifically when entering the alcoholic products category, not on the general shopping page. | NOK | [Page URL] | [https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/3] |

**Observed result:** The age verification window appeared on the general shopping page instead of appearing when entering the alcoholic products category.

---

## Feature 3: Shipping

### Scenario 5: Place an order with a total of €25 (Valid scenario)

**Related test case:** TC-22  
**Scenario type:** Valid  
**Execution result:** Passed

**User story:** As a customer, when my order total is €20 or more, I want to receive free shipping.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|---:|---|---|:---:|---|---|
| 1 | Open the GroceryMate webshop. | The webshop homepage is displayed. | OK | https://grocerymate.masterschool.com/ | — |
| 2 | Add products to the shopping cart until the order subtotal is €25. | The selected products are added to the cart and the order subtotal is €25. | OK | [Product page URL] | — |
| 3 | Open the shopping cart or order summary. | The order details and subtotal are displayed. | OK | [Cart page URL] | — |
| 4 | Check the shipping fee. | No shipping fee is applied because the order total is at least €20. | OK | [Cart page URL] | — |

### Scenario 6: Remove products so the order total falls below €20 (Invalid scenario)

**Related test case:** TC-24  
**Scenario type:** Invalid  
**Execution result:** Failed

**User story:** As a customer, when I remove products and my order total falls below €20, I expect the shipping fee and free-shipping information to be recalculated automatically.

| Step# | Action | Expected outcome | OK/NOK | URL | Link to issue |
|---:|---|---|:---:|---|---|
| 1 | Open the GroceryMate webshop and add products to the shopping cart until the order total is at least €20. | The selected products are added to the cart and the order qualifies for free shipping. | OK | https://grocerymate.masterschool.com/ | — |
| 2 | Open the shopping cart or order summary. | The order details and free-shipping status are displayed. | OK | [Cart page URL] | — |
| 3 | Remove one or more products so that the order total falls below €20. | The products are removed and the order subtotal is updated to an amount below €20. | OK | [Cart page URL] | — |
| 4 | Check the shipping fee and the free-shipping information after the order total changes. | The system recalculates the order: a €5 shipping fee is applied, and the message indicates how much more the customer needs to spend to qualify for free shipping. | NOK | [Cart page URL] | [https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/6] |

**Observed result:** This test case failed. The specific actual behavior observed after removing the products has not been provided, so it should be added here before submitting the report.

---


