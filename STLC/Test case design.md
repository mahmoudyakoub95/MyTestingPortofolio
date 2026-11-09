# Test Case Design – GroceryMate

## 1. Product Rating System

**Test Design Techniques:** BVA, Decision Table Testing, Use Case Testing, Error Guessing.

**Test Case 1 – Submit a 1-star rating**

**Technique:** BVA

**Input:** A registered user who purchased the product selects 1 star and submits the rating.

**Expected Outcome:** The rating is accepted and saved.

**Automation:** Yes – verifies the minimum rating value.

**Test Case 2 – Submit a 5-star rating**

**Technique:** BVA

**Input:** A registered user who purchased the product selects 5 stars and submits the rating.

**Expected Outcome:** The rating is accepted and saved.

**Automation:** Yes – verifies the maximum rating value.

**Test Case 3 – Submit a rating with written feedback**

**Technique:** Use Case Testing

**Input:** A registered user who purchased the product selects 4 stars, enters written feedback, and submits the review.

**Expected Outcome:** The system accepts and saves both the star rating and written feedback.

**Automation:** Yes – verifies the normal review submission workflow.

**Test Case 4 – Submit a rating without written feedback**

**Technique:** Use Case Testing

**Input:** A registered user who purchased the product selects 4 stars without entering written feedback.

**Expected Outcome:** The system accepts the star rating without written feedback.

**Automation:** Yes – verifies that written feedback is optional.

**Test Case 5 – Submit a rating without purchasing the product**

**Technique:** Decision Table Testing

**Input:** A registered user who has not purchased the product attempts to submit a rating.

**Expected Outcome:** The system rejects the submission.

**Automation:** Yes – verifies the purchase restriction.

**Test Case 6 – Edit an existing review**

**Technique:** Use Case Testing

**Input:** A user edits the star rating and written feedback of an existing review.

**Expected Outcome:** The system updates the review successfully.

**Automation:** Yes – verifies the review-editing workflow.

**Test Case 7 – Delete an existing review**

**Technique:** Use Case Testing

**Input:** A user selects the option to delete an existing review.

**Expected Outcome:** The system deletes the entire review, including the star rating and written feedback.

**Automation:** Yes – verifies the review-deletion workflow.

**Test Case 8 – Remove written feedback but keep the star rating**

**Technique:** Use Case Testing

**Input:** A user removes the written feedback while keeping the star rating unchanged.

**Expected Outcome:** The written feedback is removed, and the star rating remains.

**Automation:** Yes – verifies partial review editing.

**Test Case 9 – Submit a very long comment with 500**

**Technique:** BVA

**Input:** A registered user who purchased the product enters a very long written comment (500 charachter)and submits the review.

**Expected Outcome:** The system handles the comment without crashing or displaying an unexpected error.

**Automation:** Yes – checks how the system handles unusually long input.

**Test Case 10 – Edit or delete a review after logging in again**

**Technique:** Use Case Testing

**Input:** A user submits a review, logs out, logs back into the same account, and attempts to edit or delete the existing review.

**Expected Outcome:** The user's existing review is still available and can be edited or deleted.

**Automation:** Yes – verifies that reviews remain associated with the user's account across sessions.

---

## 2. Age Verification

**Test Design Techniques:** BVA, EP, State Transition Testing, Error Guessing.

**Test Case 1 – Verify age of exactly 18 years**

**Technique:** BVA

**Input:** A user enters a date of birth indicating they are exactly 18 years old.

**Expected Outcome:** The system allows access to the alcoholic products category.

**Automation:** Yes – verifies the minimum permitted age.

**Test Case 2 – Verify age of one day under 18**

**Technique:** BVA

**Input:** A user enters a date of birth indicating they are one day younger than 18.

**Expected Outcome:** Access is denied, and the system displays: "Sorry, you are underage. You will be able to buy when you are 18."

**Automation:** Yes – verifies the age restriction.

**Test Case 3 – Verify age of an adult user**

**Technique:** EP

**Input:** A user enters a date of birth indicating they are 25 years old.

**Expected Outcome:** The system allows access to the alcoholic products category.

**Automation:** Yes – verifies the valid adult age group.

**Test Case 4 – Verify denied access for an underage user**

**Technique:** EP

**Input:** A user opens the alcoholic products category and enters a date of birth indicating they are under 18.

**Expected Outcome:** The system denies access, hides the alcoholic products, and displays the underage message.

**Automation:** Yes – verifies that underage users cannot access the category.

**Test Case 5 – Verify age verification window appears**

**Technique:** Use Case Testing

**Input:** A user opens the alcoholic products category.

**Expected Outcome:** The system displays the age verification window before allowing access to the category.

**Automation:** Yes – verifies that age verification is triggered when entering the category.

**Test Case 6 – Enter a future date of birth**

**Technique:** Error Guessing

**Input:** A user enters a date of birth later than the current date.

**Expected Outcome:** The system should reject the date and should not grant access.

**Automation:** Yes – checks invalid date handling.

**Note:** Future-date validation is not specified in the requirements and should be confirmed.

**Test Case 7 – Enter an invalid date**

**Technique:** Error Guessing

**Input:** A user enters an invalid date, for example, 31/02/2000.

**Expected Outcome:** The system should reject the invalid date and should not grant access.

**Automation:** Yes – checks invalid date handling.

**Note:** The requirements specify DD/MM/YYYY but do not define the handling of invalid dates.

---

## 3. Shipping Cost Change

**Test Design Techniques:** BVA, EP, Decision Table Testing, Use Case Testing, Error Guessing.

**Test Case 1 – Order value is exactly €20**

**Technique:** BVA

**Input:** A user adds products worth exactly €20 to the cart.

**Expected Outcome:** Free shipping is applied.

**Automation:** Yes – verifies the free-shipping threshold.

**Test Case 2 – Order value is €19.99**

**Technique:** BVA

**Input:** A user adds products worth €19.99 to the cart.

**Expected Outcome:** A shipping fee of €5 is applied.

**Automation:** Yes – verifies the value below the threshold.

**Test Case 3 – Order value is above €20**

**Technique:** EP

**Input:** A user adds products worth €25 to the cart.

**Expected Outcome:** Free shipping is applied.

**Automation:** Yes – verifies the valid order-value group.

**Test Case 4 – Display the remaining amount for free shipping**

**Technique:** Decision Table Testing

**Input:** A user adds products worth €15 to the cart.

**Expected Outcome:** The system displays a message below the order details informing the user that they need to spend €5 more to qualify for free shipping.

**Automation:** Yes – verifies the remaining-amount calculation and message.

**Test Case 5 – Move from free shipping to paid shipping**

**Technique:** Use Case Testing

**Input:** A user adds products worth more than €20 to the cart and then removes one or more products, reducing the order value below €20.

**Expected Outcome:** The system applies the €5 shipping fee to the order.

**Automation:** Yes – verifies that shipping costs are recalculated when the cart value decreases below the threshold.

**Test Case 6 – Move from paid shipping to free shipping**

**Technique:** Use Case Testing

**Input:** A user adds products worth less than €20 to the cart and then adds more products, increasing the order value to €20 or more.

**Expected Outcome:** The system removes the €5 shipping fee and applies free shipping.

**Automation:** Yes – verifies that shipping costs are recalculated when the cart value reaches the free-shipping threshold.
