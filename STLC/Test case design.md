# Test Case Design – GroceryMate

## 1. Product Rating System

**Test Design Techniques:** Boundary Value Analysis (BVA), Decision Table Testing, Use Case Testing, Error Guessing.

**Test Case 1 – Submit a 1-star rating**

**Test Design Technique:** Boundary Value Analysis (BVA)

**Input:** A registered user who has purchased the product selects 1 star and submits the rating.

**Expected Outcome:** The system accepts the rating and saves it successfully.

**Automation:** Yes. This is a repeatable functional test and can be automated to verify that the minimum rating value is accepted.

**Test Case 2 – Submit a 5-star rating**

**Test Design Technique:** Boundary Value Analysis (BVA)

**Input:** A registered user who has purchased the product selects 5 stars and submits the rating.

**Expected Outcome:** The system accepts the rating and saves it successfully.

**Automation:** Yes. This verifies the upper boundary of the rating range and is suitable for automation.

**Test Case 3 – Submit a rating without written feedback**

**Test Design Technique:** Decision Table Testing

**Input:** A registered user who has purchased the product selects 4 stars and submits the rating without entering written feedback.

**Expected Outcome:** The system accepts and saves the star rating without requiring written feedback.

**Automation:** Yes. This is a repeatable test that verifies written feedback is optional.

**Test Case 4 – Submit a rating without purchasing the product**

**Test Design Technique:** Decision Table Testing

**Input:** A registered user who has not purchased the product attempts to submit a 5-star rating.

**Expected Outcome:** The system rejects the submission because only users who have purchased the product are allowed to submit a rating or review.

**Automation:** Yes. This is suitable for automation because the purchase status and submission result can be checked systematically.

**Test Case 5 – Edit an existing review**

**Test Design Technique:** Use Case Testing

**Input:** A registered user who has purchased the product opens an existing review, changes the star rating and written feedback, and saves the changes.

**Expected Outcome:** The system updates the existing review successfully.

**Automation:** Yes. This verifies an important user workflow and can be repeated with different rating and feedback values.

**Test Case 6 – Delete an existing review**

**Test Design Technique:** Use Case Testing

**Input:** A registered user who has purchased the product selects the option to delete their existing review.

**Expected Outcome:** The system deletes the entire review, including the star rating and written feedback.

**Automation:** Yes. This is a repeatable user workflow and can be automated to verify that the review is removed.

**Test Case 7 – Remove written feedback but keep the star rating**

**Test Design Technique:** Use Case Testing

**Input:** A registered user edits an existing review and removes only the written feedback while keeping the star rating unchanged.

**Expected Outcome:** The system removes the written feedback but keeps the star rating.

**Automation:** Yes. This verifies that the system correctly handles editing only part of a review.

**Test Case 8 – Submit written feedback without selecting a star rating**

**Test Design Technique:** Error Guessing

**Input:** A registered user who has purchased the product enters written feedback but does not select any stars, then attempts to submit the review.

**Expected Outcome:** The system should not accept a review without a star rating, since the rating system requires a value from 1 to 5 stars.

**Automation:** Yes. This negative test can be automated to check that an incomplete rating submission is handled correctly.

**Note:** The requirement does not explicitly state whether a star rating is mandatory when written feedback is submitted. This expected behavior should be confirmed.

## 2. Age Verification

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), State Transition Testing, Error Guessing.

**Test Case 1 – Verify age of exactly 18 years**

**Test Design Technique:** Boundary Value Analysis (BVA)

**Input:** A user opens the alcoholic products category and enters a date of birth that makes them exactly 18 years old.

**Expected Outcome:** The system accepts the date of birth and allows the user to access the alcoholic products category.

**Automation:** Yes. This is a boundary test and can be automated to verify the minimum permitted age.

**Test Case 2 – Verify age of one day under 18**

**Test Design Technique:** Boundary Value Analysis (BVA)

**Input:** A user opens the alcoholic products category and enters a date of birth that makes them one day younger than 18.

**Expected Outcome:** The system denies access to the alcoholic products category and displays the following message: "Sorry, you are underage. You will be able to buy when you are 18."

**Automation:** Yes. This is a critical age restriction test and should be automated to prevent incorrect access.

**Test Case 3 – Verify age of an adult user**

**Test Design Technique:** Equivalence Partitioning (EP)

**Input:** A user opens the alcoholic products category and enters a date of birth that makes them 25 years old.

**Expected Outcome:** The system accepts the date of birth and allows the user to access the alcoholic products category.

**Automation:** Yes. This verifies the valid adult age group and can be repeated with different dates of birth.

**Test Case 4 – Verify access after an underage result**

**Test Design Technique:** State Transition Testing

**Input:** A user opens the alcoholic products category. The system displays the age verification window. The user enters a date of birth indicating that they are under 18.

**Expected Outcome:** The system moves to the denied-access state. Alcoholic products are not displayed, and the system shows the specified underage message.

**Automation:** Yes. This test verifies the transition from the age verification prompt to the denied-access state.

**Test Case 5 – Enter a date of birth in the future**

**Test Design Technique:** Error Guessing

**Input:** A user opens the alcoholic products category and enters a date of birth that is later than the current date.

**Expected Outcome:** The system should reject the future date of birth and should not grant access based on an invalid date.

**Automation:** Yes. This negative test can be automated to check how the system handles an invalid date value.

**Note:** Future-date validation is not explicitly described in the detailed requirements. The expected behavior and any error message should be confirmed.

**Test Case 6 – Enter an invalid date**

**Test Design Technique:** Error Guessing

**Input:** A user opens the alcoholic products category and enters an invalid date, for example, 31/02/2000.

**Expected Outcome:** The system should reject the invalid date and should not grant access to the alcoholic products category.

**Automation:** Yes. This test can be automated to verify that invalid date values are not accepted.

**Note:** The detailed requirements specify the date format as DD/MM/YYYY but do not define how invalid dates should be handled or which error message should be displayed. This behavior should be confirmed.

## 3. Shipping Cost Change

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Decision Table Testing, Error Guessing.

**Test Case 1 – Order value is exactly €20**

**Test Design Technique:** Boundary Value Analysis (BVA)

**Input:** A user adds products to the cart with a total order value of exactly €20.

**Expected Outcome:** The system applies free shipping, and no shipping fee is added to the order total.

**Automation:** Yes. This is a critical boundary test and should be automated to verify the free-shipping threshold.

**Test Case 2 – Order value is €19.99**

**Test Design Technique:** Boundary Value Analysis (BVA)

**Input:** A user adds products to the cart with a total order value of €19.99.

**Expected Outcome:** The system applies a shipping fee of €5.

**Automation:** Yes. This test verifies the value immediately below the free-shipping threshold and is suitable for automation.

**Test Case 3 – Order value is above €20**

**Test Design Technique:** Equivalence Partitioning (EP)

**Input:** A user adds products to the cart with a total order value of €25.

**Expected Outcome:** The system applies free shipping, and no shipping fee is added to the order total.

**Automation:** Yes. This verifies the valid order-value group above the threshold and can be automated with different values.

**Test Case 4 – Display the remaining amount needed for free shipping**

**Test Design Technique:** Decision Table Testing

**Input:** A user adds products to the cart with a total order value of €15.

**Expected Outcome:** The system applies a shipping fee of €5 and displays a message below the order details informing the user that they need to spend €5 more to qualify for free shipping.

**Automation:** Yes. The calculation and displayed message can be checked automatically using different order values.



**Note:** The detailed requirements specify a €5 shipping fee for orders below €20 but do not explicitly describe how the fee is handled across different checkout steps. This test checks a reasonable potential error and should be aligned with the checkout implementation.
