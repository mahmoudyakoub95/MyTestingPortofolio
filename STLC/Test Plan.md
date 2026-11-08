# Test Plan for GroceryMate – New Features

## 1. Product Analysis

**Objective**

The objective is to test the three new features of the GroceryMate webshop and ensure that they work as expected without affecting existing functionality.

**User Group**

The main users are registered customers, customers who have purchased products, and customers who want to buy alcoholic products.

**Hardware and Software Specifications**

Testing will be performed on desktop computers, laptops, tablets, and smartphones.

Operating systems: Windows, macOS, Android, and iOS.

Browsers: Chrome, Firefox, Safari, and Edge.

**Product Functionality**

The webshop offers product search, sorting, categories, favorites, shopping cart, and checkout.

The new features are:
- **Product Ratings:** Registered customers who have purchased a product can rate it from 1 to 5 stars and optionally add written feedback.
- **Age Verification:** Users must confirm that they are at least 18 years old before accessing alcoholic products.
- **Shipping Costs:** Orders of €20 or more qualify for free shipping. Orders below €20 have a €5 shipping fee.

## 2. Test Strategy

**Scope of Testing**

The testing will cover the three new features: Product Ratings, Age Verification, and Shipping Costs. Existing webshop functionality will also be tested to ensure that the new features do not cause problems.

**Types of Testing**

- Functional Testing
- Regression Testing
- Compatibility Testing
- Usability Testing

**Risks and Issues**

- Unclear requirements may lead to incorrect test cases.
- Incorrect age verification could allow underage users to access alcoholic products.
- Incorrect shipping calculations could result in wrong order totals.
- Changes may affect existing webshop functionality.

**Test Logistics**

The testing will be performed by QA Engineers. The Test Manager will coordinate the testing activities and report the results.

## 3. Test Objectives

The main objectives are to ensure that:

- Product ratings and written feedback work according to the requirements.
- Age verification prevents underage users from accessing alcoholic products.
- Shipping costs are calculated correctly.
- Existing webshop functionality continues to work after the changes.

**Expected Outcomes**

All three new features work according to the defined requirements, and no critical issues remain before release.

## 4. Test Criteria

**Suspension Criteria**

Testing will be paused if the test environment is unavailable or a critical defect prevents further testing.

**Exit Criteria**

Testing can be completed when all planned test cases have been executed, critical defects have been resolved, and the new features meet the defined requirements.

## 5. Resource Planning

**Human Resources**

- Test Manager
- QA Engineers
- Developers (for fixing reported defects)

**Hardware and Software**

- Desktop computers, laptops, tablets, and smartphones
- Supported web browsers
- Test environment and test accounts

## 6. Test Environment

Testing will be performed in the test environment before the features are released to production.

The environment should include the latest version of the GroceryMate webshop, test accounts, and the necessary test data.

## 7. Schedule and Effort Estimation

| Activity | Estimated Effort |
|---|---:|
| Test Planning | 4 hours |
| Test Case Design | 8 hours |
| Test Execution | 12 hours |
| Regression Testing | 4 hours |
| Test Reporting | 2 hours |
| **Total** | **30 hours** |

The schedule will be finalized based on the development and release dates.

## 8. Test Deliverables

- Test Plan
- Test Cases
- Test Data
- Defect Reports
- Test Execution Report
- Final Test Summary
