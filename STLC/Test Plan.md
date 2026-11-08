# Test Plan for GroceryMate – New Features

## 1. Analyze Product

**Objective**

The objective of this test plan is to define the testing activities for the three new features of the GroceryMate webshop. Testing will ensure that the new features work according to the requirements and do not negatively affect existing functionality.

**User Group**

The target users are registered customers who use the webshop to search for and purchase products. This includes customers who want to rate purchased products and customers who want to access or purchase alcoholic products.

**Hardware and Software Specifications**

Testing will be performed on desktop computers, laptops, tablets, and smartphones.

- Operating systems: Windows, macOS, Android, and iOS.
- Browsers: Google Chrome, Mozilla Firefox, Safari, and Microsoft Edge.
- Devices should have sufficient resources to run the webshop smoothly.

**Product Functionality**

GroceryMate is an online grocery webshop that allows users to register, log in, search and sort products, browse categories, manage favorites, add products to a shopping cart, and complete purchases.

The new features to be tested are:

- **Product Ratings:** Registered users who have purchased a product can submit a rating from 1 to 5 stars and optionally provide written feedback. Users can also edit or delete their reviews.
- **Age Verification:** Users must verify that they are at least 18 years old before accessing the category containing alcoholic products.
- **Shipping Cost Change:** Orders with a total value of €20 or more qualify for free shipping. Orders below €20 have a shipping fee of €5.

## 2. Design Test Strategy

**Scope of Testing**

The testing scope includes the three new features: Product Ratings, Age Verification, and Shipping Costs. It also includes regression testing of the existing webshop functionality to ensure that the changes do not affect product browsing, the shopping cart, or checkout.

**Types of Testing**

- **Functional Testing:** To check whether the new features work according to the requirements.
- **Regression Testing:** To ensure that existing webshop functionality still works after the changes.
- **Compatibility Testing:** To check the webshop on different browsers and devices.
- **Usability Testing:** To check whether the new features are easy to understand and use.
- **Acceptance Testing:** To ensure that the features meet the business requirements.

**Risks and Issues**

- Unclear requirements may lead to incorrect test cases or misunderstandings.
- Incorrect age verification may allow underage users to access alcoholic products.
- Incorrect shipping calculations may result in wrong order totals.
- Changes to existing functionality may affect the shopping cart or checkout process.

These risks will be addressed through requirement reviews, appropriate test cases, and regression testing.

**Test Logistics**

The Test Manager is responsible for coordinating the testing activities and reporting the results. QA Engineers are responsible for preparing test cases, executing tests, and reporting defects. Developers are responsible for investigating and fixing reported defects.

## 3. Define Test Objectives

The main objectives are to ensure that:

- Users can submit, edit, and delete product ratings and reviews according to the requirements.
- Age verification correctly restricts access to alcoholic products for users under 18.
- Shipping costs are calculated correctly based on the order value.
- Existing webshop functionality continues to work correctly.

**Expected Outcomes**

All three new features should work according to the defined requirements. Existing functionality should remain unaffected, and no critical defects should remain before release.

## 4. Define Test Criteria

**Suspension Criteria**

Testing may be suspended if the test environment is unavailable, the webshop cannot be accessed, or critical defects prevent further testing.

**Exit Criteria**

Testing can be considered complete when all planned test cases have been executed, critical defects have been resolved, and the new features meet the defined requirements. The test results should be documented and reviewed before release.

## 5. Resource Planning

**Human Resources**

- Test Manager: Coordinates testing activities and monitors progress.
- QA Engineers: Prepare and execute test cases and report defects.
- Developers: Investigate and fix reported defects.
- Business Stakeholders: Review the results and confirm that the requirements are fulfilled.

**Hardware and Software Resources**

Desktop computers, laptops, smartphones, tablets, supported browsers, test accounts, and access to the GroceryMate test environment will be required.

## 6. Plan Test Environment

Testing will be performed in a dedicated test environment before the new features are released to production.

The environment should contain the latest version of the GroceryMate webshop, the required test accounts, and suitable test data.

Different browsers and devices will be used to check compatibility. Test data should include products, user accounts, and shopping carts with different order values.

## 7. Schedule and Estimation

The following table provides an initial estimation of the testing activities:

| Testing Activity | Estimated Effort |
|---|---:|
| Test Planning | 6 hours |
| Test Case Design | 10 hours |
| Test Environment and Test Data Preparation | 4 hours |
| Functional Testing | 12 hours |
| Regression Testing | 6 hours |
| Compatibility and Usability Testing | 6 hours |
| Defect Retesting | 4 hours |
| Test Reporting | 2 hours |
| **Total** | **50 hours** |

The actual schedule will depend on the development completion date and availability of the test environment.

## 8. Determine Test Deliverables

The following deliverables will be provided during the testing process:

- **Test Plan:** Describes the testing approach, scope, resources, and schedule.
- **Test Cases:** Contains the test scenarios and expected results for the new features.
- **Test Data:** Includes the accounts, products, and order values required for testing.
- **Defect Reports:** Documents the defects found during testing.
- **Test Execution Report:** Shows the executed test cases and their results.
- **Test Summary Report:** Provides an overview of the testing results and the overall readiness of the new features.
