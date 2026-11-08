# Test Plan for GroceryMate – New Features

## 1. Analyze the Product

### Objective

The objective of this release is to introduce three new features to the existing GroceryMate webshop: a product rating system, age verification for alcoholic products, and a shipping cost calculation based on the order value.

The purpose of testing is to ensure that these features work according to the defined requirements and that existing webshop functionality continues to work correctly after their implementation.

### User Base

The product is used by customers who visit the GroceryMate webshop to browse and purchase grocery products.

The relevant user groups for the new features are:

- **Registered customers:** Users who have an account and can purchase products and submit product ratings.
- **Customers who have purchased products:** Registered users who are eligible to rate and review products they have purchased.
- **Customers accessing alcoholic products:** Users who need to verify that they are at least 18 years old before accessing the alcoholic products category.
- **All webshop customers:** Users who need to see the correct shipping costs depending on their order value.

### Hardware and Software Specifications

**Hardware Requirements:**
- Devices: PCs, laptops, smartphones, and tablets.
- Specifications: Standard configurations for Android and iOS devices; desktops with at least 4 GB RAM and a 2 GHz processor.

**Software Requirements:**
- Operating Systems: Windows, macOS, Android, and iOS.
- Browsers: Chrome, Firefox, Safari, and Edge.
- Dependencies: Backend services, user account services, product and order data, and payment interfaces.

### Product Functionality

The existing GroceryMate webshop allows users to:

- Register and log in.
- Search for products.
- Sort products and browse product categories.
- Add products to favorites.
- Add products to the shopping cart.
- Enter billing and shipping information during checkout.
- Select a payment method.
- View the total order price.

The following new features will be introduced:

- **Product Rating System:** Users who are registered and have purchased a product can rate it using a 5-star system and optionally leave written feedback. Users can edit or delete their reviews.
- **Age Verification:** Users must verify that they are at least 18 years old before accessing the alcoholic products category. Users under 18 are not allowed to view the products.
- **Shipping Cost Change:** Orders with a total value of €20 or more qualify for free shipping. Orders below €20 have a shipping cost of €5. A message below the order details informs users about the free-shipping threshold and how much more they need to spend to qualify.

---

## 2. Design the Test Strategy

### Scope of Testing

**In Scope:**

- Product Rating System:
  - Verify that only registered users who have purchased a product can submit a rating or review.
  - Verify that users can submit ratings from 1 to 5 stars.
  - Verify that written feedback is optional.
  - Verify that users can edit their reviews.
  - Verify that users can delete their entire review or remove only the written comment.

- Age Verification:
  - Verify that the age verification window appears when users open the alcoholic products category.
  - Verify that users enter their date of birth in day/month/year format.
  - Verify that users aged 18 or older can access the category.
  - Verify that users under 18 cannot access or view alcoholic products.
  - Verify that the correct underage message is displayed.

- Shipping Cost Change:
  - Verify that orders with a total value of €20 or more have free shipping.
  - Verify that orders below €20 have a shipping cost of €5.
  - Verify that the free-shipping information is displayed below the order details.
  - Verify that the message indicates how much more the customer needs to spend to qualify for free shipping.

- Regression testing of existing functionality that could be affected by the new features, especially product details, user accounts, shopping cart, and checkout.

**Out of Scope:**

- Testing existing features that are not affected by the new functionality.
- Testing the internal implementation of third-party payment providers.
- Testing backend database operations that do not affect the functionality or behavior of the webshop.
- Testing features that are not part of this release.

### Type of Testing

- **Functional Testing:** Verify that all three new features work according to the detailed requirements.
- **Regression Testing:** Ensure that existing webshop functionality continues to work after the new features are implemented.
- **Boundary Value Analysis:** Test important boundaries, such as the age limit of 18 and the shipping threshold of €20.
- **Equivalence Partitioning:** Test relevant groups of input values, such as users under 18 and users aged 18 or older, as well as orders below and at or above €20.
- **Usability Testing:** Verify that messages, instructions, and user interactions are understandable.
- **Compatibility Testing:** Check that the new features work across the supported browsers, operating systems, and devices.
- **Security Testing:** Check that users cannot bypass age restrictions or submit reviews without meeting the defined eligibility requirements.
- **Performance Testing:** Check that the new features do not negatively affect the webshop's response time under expected usage conditions.
- **User Acceptance Testing (UAT):** Confirm that the new features meet the expectations of the intended users and business stakeholders.

### Risks and Issues

- **Unclear or incomplete requirements**
  - Mitigation: Clarify remaining details with stakeholders before final test execution.

- **Incorrect age verification**
  - Mitigation: Test valid and invalid dates of birth and verify access restrictions for users under 18.

- **Incorrect shipping cost calculation**
  - Mitigation: Test order values below, exactly at, and above the €20 threshold.

- **Insufficient test data**
  - Mitigation: Prepare test accounts, purchased-product data, different product ratings, and shopping carts with different order values.

- **Regression issues**
  - Mitigation: Include relevant existing webshop functionality in the regression test scope.

- **Resource unavailability**
  - Mitigation: Plan testing activities in advance and identify backup resources.

### Test Logistics (Test Responsibilities)

- **Test Manager:** Responsible for test planning, coordination, and reporting.
- **QA Engineer (Functional Testing):** Responsible for designing and executing functional test cases for all three features.
- **QA Engineer (Regression Testing):** Responsible for checking existing webshop functionality that could be affected by the new features.
- **QA Engineer (Performance and Security Testing):** Responsible for performance and security checks.
- **End Users / Business Stakeholders:** Responsible for participating in user acceptance testing.

---

## 3. Define Test Objectives

### Objectives

- **Functionality:** Ensure that the product rating system, age verification, and shipping cost calculation work according to the detailed requirements.
- **Product Rating System:** Ensure that only eligible users can submit reviews and that ratings and written feedback can be created, edited, and deleted as specified.
- **Age Verification:** Ensure that users under 18 cannot access alcoholic products and that users who meet the age requirement can access the category.
- **Shipping Cost Calculation:** Ensure that orders below €20 have a €5 shipping fee and orders of €20 or more qualify for free shipping.
- **GUI:** Verify that the new messages, rating controls, and age verification window are displayed correctly and consistently.
- **Usability:** Ensure that users can understand and use the new features easily.
- **Compatibility:** Ensure that the new features work across the supported browsers, operating systems, and devices.
- **Regression:** Ensure that existing webshop functionality is not negatively affected by the new features.
- **Security:** Ensure that age restrictions and review eligibility rules cannot be bypassed through normal user interactions.

### Expected Outcomes

- All three new features work according to the defined requirements.
- Only registered users who have purchased a product can submit a rating or review.
- Users can submit a rating without written feedback and can edit or delete their reviews.
- Users under 18 cannot access or view alcoholic products.
- Users who are at least 18 years old can access the alcoholic products category.
- The correct underage message is displayed when a user is under 18.
- Orders below €20 have a shipping fee of €5.
- Orders of €20 or more qualify for free shipping.
- The free-shipping information is displayed clearly below the order details.
- Existing webshop functionality continues to work correctly.
- No critical usability, compatibility, or security issues remain unresolved.

---

## 4. Define Test Criteria

### Suspension Criteria

Testing will be suspended if:

- Critical defects prevent the execution of further test cases.
- The test environment is unavailable or unstable.
- Required test data or test accounts are unavailable.
- The application is not accessible or major functionality is blocked.

### Exit Criteria

Testing can be considered complete when:

- All planned test cases have been executed.
- At least 95% of the planned test cases have been executed.
- At least 90% of the executed test cases have passed.
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects remain open.
- All three new features meet their defined functional requirements.
- Relevant regression tests have been completed successfully.
- User acceptance testing has been completed and approved.

---

## 5. Resource Planning

- **Human Resources:** Test Manager, QA Engineers, Development Team, and End Users for UAT.
- **Hardware:** PCs, laptops, smartphones, and tablets.
- **Software:** Chrome, Firefox, Safari, and Edge; Windows, macOS, Android, and iOS.
- **Test Data:**
  - Registered and unregistered user accounts.
  - User accounts with and without purchased products.
  - Products with and without existing reviews.
  - Valid dates of birth for users aged 18 or older and users under 18.
  - Shopping carts with order values below, exactly at, and above €20.
- **Infrastructure:** Development and test environments, test management tools, defect tracking tools, and test automation tools.

---

## 6. Plan Test Environment

### Test Devices

- Desktop computers and laptops.
- Smartphones and tablets.
- Real devices with supported operating systems and browsers, where available.

### Test Environments

- **Development (DEV):** Used by developers for initial implementation and unit testing.
- **Testing (TEST):** Used by QA Engineers for functional, integration, system, and regression testing.
- **Acceptance (ACC):** Used for user acceptance testing before release.
- **Production (PROD):** The live GroceryMate webshop after release.

Testing should primarily take place in the TEST environment. The ACC environment will be used to confirm that the features are ready for release.

---

## 7. Schedule and Estimation

The following schedule is an initial estimation. Exact dates and responsibilities can be defined once the development and release dates are confirmed.

| Activity | Environment | Responsible Person | Estimated Effort |
|---|---|---|---:|
| Test Planning | All | Test Manager / QA Team | 8 hours |
| Test Case Design | All | QA Team | 12 hours |
| Unit Testing | DEV | Development Team | 8 hours |
| Integration Testing | TEST | QA Team | 8 hours |
| Functional Testing | TEST | QA Team | 16 hours |
| Regression Testing | TEST | QA Team | 8 hours |
| Compatibility Testing | TEST | QA Team | 6 hours |
| Performance and Security Testing | TEST | QA Team | 8 hours |
| User Acceptance Testing (UAT) | ACC | End Users / Business Stakeholders | 4 hours |
| Test Reporting and Release Recommendation | ACC | Test Manager / QA Team | 4 hours |

---

## 8. Determine Test Deliverables

The following documents and tools will be created and maintained during the testing process:

- **Test Plan Document:** Describes the testing scope, strategy, objectives, resources, environment, schedule, and criteria.
- **Test Cases:** Detailed test cases for the product rating system, age verification, and shipping cost change.
- **Test Scripts:** Automated scripts for selected repeatable test cases.
- **Test Data:** Prepared user accounts, product data, dates of birth, and order values.
- **Defect Reports:** Documentation of identified defects, including steps to reproduce, expected results, and actual results.
- **Test Execution Reports:** Results of executed test cases, including passed, failed, and blocked tests.
- **Regression Test Results:** Evidence that existing webshop functionality continues to work correctly.
- **UAT Sign-off Document:** Confirmation from the relevant stakeholders that the new features meet the acceptance requirements.
