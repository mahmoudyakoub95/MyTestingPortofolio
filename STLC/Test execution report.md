# Test Execution Report – GroceryMate

## 1. Test Execution Information

- **Application:** GroceryMate
- **Tester:** Mahmoud Yaakoub
- **Execution date:** 10-11-2026
- **Browser and version:** ChromeVersion 155.0.8059.82 (Offizieller Build) (64-Bit)
- **Operating system:** Windows 11 pro

## 2. Execution Summary

| Status | Total |
|---|---:|
| Passed | 19 |
| Failed | 6 |
| Blocked | 0 |
| Not Run | 0 |
| **Total test cases** | **25** |

## 3. Test Execution Results

### Feature 1 – Product Rating System

| Test Case ID | Test Case | Expected Result | Status | Actual Result / Comments | Bug Reference |
|---|---|---|---|---|---|
| TC-01 | Submit a 1-star rating | The system accepts and saves a 1-star rating. | Passed |  |  |
| TC-02 | Submit a 5-star rating | The system accepts and saves a 5-star rating. | Passed |  |  |
| TC-03 | Submit a rating with written feedback | The system saves the star rating together with the written feedback. | Passed |  |  |
| TC-04 | Submit a rating without written feedback | The system saves the star rating without requiring a written comment. | Passed |  |  |
| TC-05 | Submit a rating without purchasing the product | The system does not allow a user who has not purchased the product to submit a rating. | Passed |  |  |
| TC-06 | Edit an existing review | The user can edit their existing review. | Passed |  |  |
| TC-07 | Delete an existing review | The user can delete their entire review. | Passed |  |  |
| TC-08 | Remove written feedback but keep the rating | The user can remove the written comment while keeping the star rating. | Passed |  |  |
| TC-09 | Submit a very long comment | The system handles the comment according to its allowed length and does not crash. | Passed |  |  |
| TC-10 | Edit or delete a review after logging in again | The user's existing review remains available and can be edited or deleted after logging in again. | Passed |  |  |
| TC-11 | Submit a comment longer than 500 characters after editing an existing review | The comment must not exceed the expected maximum of 500 characters. | **Failed** | A comment of approximately 4,000 characters was accepted. No 500-character limit was enforced. | https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/1 |
| TC-12 | Delete a review, then submit a new rating and comment for the same product | After deleting the previous review, the user can submit a new rating with written feedback. | **Failed** | After deleting the review, the system allowed only a rating; adding a written comment was not possible. |  |

### Feature 2 – Age Verification

| Test Case ID | Test Case | Expected Result | Status | Actual Result / Comments | Bug Reference |
|---|---|---|---|---|---|
| TC-13 | Verify a user who is exactly 18 years old | The user is allowed to access the alcoholic products category. | Passed |  |  |
| TC-14 | Verify a user who is one day under 18 | The user is denied access and sees the specified underage message. | Passed |  |  |
| TC-15 | Verify a user who is 25 years old | The user is allowed to access the alcoholic products category. | Passed |  |  |
| TC-16 | Verify that underage users cannot access or view alcoholic products | Alcoholic products are not accessible or visible to users under 18. | Passed |  |  |
| TC-17 | Check whether the age verification window appears when entering the alcoholic products category | The age verification window appears when the user tries to enter the alcoholic products category. | **Failed** | The age verification window appeared when entering the general shopping page, rather than when entering the alcoholic products category. | https://github.com/mahmoudyakoub95/MyTestingPortofolio/issues/3 |
| TC-18 | Enter a future date of birth | The system rejects the invalid date and displays an appropriate error message. | **Failed** | The displayed error message was incorrect. |  |
| TC-19 | Enter an invalid date (31/02/2000) | The system rejects the invalid date and displays an appropriate error message. | **Failed** | The displayed error message was incorrect. |  |

### Feature 3 – Shipping Cost Change

| Test Case ID | Test Case | Expected Result | Status | Actual Result / Comments | Bug Reference |
|---|---|---|---|---|---|
| TC-20 | Place an order with a total of exactly €20 | Shipping is free. | Passed |  |  |
| TC-21 | Place an order with a total of €19.99 | A shipping fee of €5 is applied. | Passed |  |  |
| TC-22 | Place an order with a total of €25 | Shipping is free. | Passed |  |  |
| TC-23 | Place an order with a total of €15 | A €5 shipping fee is applied, and the message states that the user needs to spend €5 more to qualify for free shipping. | Passed |  |  |
| TC-24 | Remove product(s) so the order total changes from above €20 to below €20 | The system recalculates shipping and applies the €5 shipping fee. | **Failed** |  |  |
| TC-25 | Add product(s) so the order total changes from below €20 to €20 or more | The system recalculates shipping and removes the €5 fee. | Passed |  |  |

## 4. Bug References

Add the corresponding GitHub Issue number or link for each failed test case.

| Test Case ID | Bug Description | GitHub Issue Reference |
|---|---|---|
| TC-11 | No 500-character limit when editing a review comment. |  |
| TC-12 | After deleting a review, the user cannot submit a new written comment with a new rating. |  |
| TC-17 | Age verification window appears on the general shopping page instead of when entering the alcoholic products category. |  |
| TC-18 | Incorrect error message for a future date of birth. |  |
| TC-19 | Incorrect error message for an invalid date of birth. |  |
| TC-24 | Shipping fee is not correctly recalculated after the order total drops below €20. |  |


