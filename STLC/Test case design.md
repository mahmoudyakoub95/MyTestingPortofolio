# Test Case Design – GroceryMate

## 1. Product Rating System

### Test Design Techniques
- Boundary Value Analysis (BVA)
- Equivalence Partitioning (EP)
- Decision Table Testing
- Use Case Testing
- Error Guessing

### TC-01 – Submit a 1-star rating
- **Test Design Technique:** Boundary Value Analysis (BVA)
- **Test Case:** Verify that a user can submit the minimum rating of 1 star.
- **Input:** Select 1 star and submit the rating.
- **Expected Outcome:** The system accepts and saves the 1-star rating.
- **Automation:** Yes – validates the minimum rating value.

### TC-02 – Submit a 5-star rating
- **Test Design Technique:** Boundary Value Analysis (BVA)
- **Test Case:** Verify that a user can submit the maximum rating of 5 stars.
- **Input:** Select 5 stars and submit the rating.
- **Expected Outcome:** The system accepts and saves the 5-star rating.
- **Automation:** Yes – validates the maximum rating value.

### TC-03 – Submit a rating with written feedback
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that a user can submit a star rating together with a written comment.
- **Input:** Select 4 stars, enter "Good product", and submit.
- **Expected Outcome:** The system saves both the star rating and the written feedback.
- **Automation:** Yes – the submission workflow can be repeated automatically.

### TC-04 – Submit a rating without written feedback
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that a user can submit a star rating without adding a written comment.
- **Input:** Select 4 stars and submit without entering a comment.
- **Expected Outcome:** The system saves the star rating without requiring written feedback.
- **Automation:** Yes – verifies the optional comment behavior.

### TC-05 – Submit a rating without purchasing the product
- **Test Design Technique:** Decision Table Testing
- **Test Case:** Verify that a user who has not purchased a product cannot submit a rating.
- **Input:** Log in with a registered account that has not purchased the selected product and attempt to submit a rating.
- **Expected Outcome:** The system does not allow the user to submit a rating or review.
- **Automation:** Yes – verifies user permissions and purchase conditions.

### TC-06 – Edit an existing review
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that a user can edit an existing review.
- **Input:** Open an existing review, change the star rating or written comment, and save the changes.
- **Expected Outcome:** The system updates the existing review with the new information.
- **Automation:** Yes – the edit workflow is repeatable.

### TC-07 – Delete an existing review
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that a user can delete their entire review.
- **Input:** Open an existing review and select the delete option.
- **Expected Outcome:** The system deletes the review, including the star rating and written comment.
- **Automation:** Yes – the deletion workflow can be automated.

### TC-08 – Remove written feedback but keep the rating
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that a user can remove only the written comment while keeping the star rating.
- **Input:** Edit an existing review, remove the written comment, keep the star rating, and save.
- **Expected Outcome:** The system removes the written comment but keeps the star rating.
- **Automation:** Yes – verifies the review update behavior.

### TC-09 – Submit a very long comment
- **Test Design Technique:** Error Guessing
- **Test Case:** Verify how the system handles a very long written comment when submitting a new review.
- **Input:** Enter a very long comment and submit the review.
- **Expected Outcome:** The system handles the comment according to its allowed length and does not crash.
- **Automation:** Yes – different comment lengths can be tested automatically.

### TC-10 – Edit or delete a review after logging in again
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that a user's existing review remains available after logging out and logging in again.
- **Input:** Submit a review, log out, log in again with the same account, and try to edit or delete the review.
- **Expected Outcome:** The existing review is still available and can be edited or deleted.
- **Automation:** Yes – the login and review management workflow can be automated.

### TC-11 – Submit a comment longer than 500 characters after editing an existing review
- **Test Design Technique:** Error Guessing
- **Test Case:** Verify that the system enforces a maximum comment length of 500 characters when editing an existing review.
- **Input:** Open an existing review, edit the comment, enter more than 500 characters (e.g. 4,000 characters), and save.
- **Expected Outcome:** The system does not accept a comment longer than 500 characters. It should prevent additional characters or display an appropriate validation message.
- **Automation:** Yes – boundary and maximum-length validation can be tested automatically.

### TC-12 – Delete a review and submit a new review again
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that a user can submit a new rating and written comment after deleting their previous review for the same product.
- **Input:** Delete an existing review, then select a new star rating, enter a written comment, and submit.
- **Expected Outcome:** The system allows the user to submit a new rating together with written feedback.
- **Automation:** Yes – the complete delete-and-resubmit workflow can be repeated automatically.

---

## 2. Age Verification

### Test Design Techniques
- Boundary Value Analysis (BVA)
- Equivalence Partitioning (EP)
- Use Case Testing
- Error Guessing

### TC-13 – Verify a user who is exactly 18 years old
- **Test Design Technique:** Boundary Value Analysis (BVA)
- **Test Case:** Verify that a user who has reached the minimum legal age can access alcoholic products.
- **Input:** Enter a date of birth corresponding to exactly 18 years of age.
- **Expected Outcome:** The system accepts the date of birth and allows access to the alcoholic products category.
- **Automation:** Yes – the age boundary can be tested automatically.

### TC-14 – Verify a user who is one day under 18
- **Test Design Technique:** Boundary Value Analysis (BVA)
- **Test Case:** Verify that a user who is one day younger than 18 is denied access.
- **Input:** Enter a date of birth corresponding to one day under 18 years of age.
- **Expected Outcome:** The system denies access and displays the following message: "Sorry, you are underage. You will be able to buy when you are 18."
- **Automation:** Yes – the age boundary and expected message can be verified automatically.

### TC-15 – Verify a user who is 25 years old
- **Test Design Technique:** Equivalence Partitioning (EP)
- **Test Case:** Verify that an adult user older than 18 can access alcoholic products.
- **Input:** Enter a date of birth corresponding to 25 years of age.
- **Expected Outcome:** The system accepts the date of birth and allows access to the alcoholic products category.
- **Automation:** Yes – validates the adult age group.

### TC-16 – Verify that underage users cannot access or view alcoholic products
- **Test Design Technique:** Equivalence Partitioning (EP)
- **Test Case:** Verify that users under 18 cannot access or view alcoholic products.
- **Input:** Enter a date of birth corresponding to an age below 18 and attempt to access the alcoholic products category.
- **Expected Outcome:** The system denies access to the category and prevents the user from viewing alcoholic products. The specified underage message is displayed.
- **Automation:** Yes – access restrictions can be checked automatically.

### TC-17 – Check whether the age verification window appears when entering the alcoholic products category
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that the age verification window appears when a user tries to enter the alcoholic products category.
- **Input:** Open the GroceryMate website and navigate to the alcoholic products category.
- **Expected Outcome:** The system displays the age verification window when the user tries to access the alcoholic products category.
- **Automation:** Yes – the navigation flow and verification window can be checked automatically.

### TC-18 – Enter a future date of birth
- **Test Design Technique:** Error Guessing
- **Test Case:** Verify that the system handles a date of birth in the future.
- **Input:** Enter a future date as the date of birth.
- **Expected Outcome:** The system rejects the invalid date and displays an appropriate error message.
- **Automation:** Yes – invalid date inputs can be tested automatically.

### TC-19 – Enter an invalid date of birth
- **Test Design Technique:** Error Guessing
- **Test Case:** Verify that the system rejects an invalid calendar date.
- **Input:** Enter 31/02/2000 as the date of birth.
- **Expected Outcome:** The system rejects the invalid date and displays an appropriate error message.
- **Automation:** Yes – invalid calendar dates can be tested automatically.

---

## 3. Shipping Cost Change

### Test Design Techniques
- Boundary Value Analysis (BVA)
- Equivalence Partitioning (EP)
- Decision Table Testing
- Use Case Testing

### TC-20 – Place an order with a total of €20
- **Test Design Technique:** Boundary Value Analysis (BVA)
- **Test Case:** Verify that an order with a total value of exactly €20 qualifies for free shipping.
- **Input:** Add products to the cart with a total value of exactly €20.
- **Expected Outcome:** The system applies free shipping and does not add a shipping fee.
- **Automation:** Yes – the shipping threshold can be validated automatically.

### TC-21 – Place an order with a total of €19.99
- **Test Design Technique:** Boundary Value Analysis (BVA)
- **Test Case:** Verify that an order just below the €20 threshold is charged for shipping.
- **Input:** Add products to the cart with a total value of €19.99.
- **Expected Outcome:** The system applies a shipping fee of €5.
- **Automation:** Yes – boundary value calculations can be tested automatically.

### TC-22 – Place an order with a total of €25
- **Test Design Technique:** Equivalence Partitioning (EP)
- **Test Case:** Verify that an order above the €20 threshold qualifies for free shipping.
- **Input:** Add products to the cart with a total value of €25.
- **Expected Outcome:** The system applies free shipping and does not add a shipping fee.
- **Automation:** Yes – this is a repeatable shipping calculation scenario.

### TC-23 – Place an order with a total of €15
- **Test Design Technique:** Decision Table Testing
- **Test Case:** Verify the shipping fee and free-shipping notification for an order below €20.
- **Input:** Add products to the cart with a total value of €15.
- **Expected Outcome:** The system applies a shipping fee of €5 and displays a message informing the user that they need to spend €5 more to qualify for free shipping.
- **Automation:** Yes – both the shipping fee and displayed message can be checked automatically.

### TC-24 – Remove products so the order total changes from above €20 to below €20
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that the shipping fee is recalculated when the user removes products and the order total falls below €20.
- **Input:** Add products to the cart so the total is above €20, then remove one or more products until the total is below €20.
- **Expected Outcome:** The system recalculates the shipping cost and applies a shipping fee of €5.
- **Automation:** Yes – cart changes and shipping recalculation can be tested automatically.

### TC-25 – Add products so the order total changes from below €20 to €20 or more
- **Test Design Technique:** Use Case Testing
- **Test Case:** Verify that the shipping fee is removed when the user adds products and the order total reaches or exceeds €20.
- **Input:** Add products to the cart so the total is below €20, then add one or more products until the total reaches or exceeds €20.
- **Expected Outcome:** The system recalculates the shipping cost, removes the €5 shipping fee, and applies free shipping.
- **Automation:** Yes – cart changes and shipping recalculation can be tested automatically.

---

## Notes
1. TC-11 uses the 500-character maximum as an additional expected requirement. This limit was not included in the original detailed requirement.
2. TC-12, TC-24 and TC-25 were added based on scenarios discovered or requested during test execution.
3. TC-17 was updated to check specifically when the age verification window appears.
4. Automation recommendations are suggestions. The test cases can initially be executed manually.
