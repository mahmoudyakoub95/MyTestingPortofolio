# GroceryMate – Requirements Analysis With Open Questions

## 1. Product Rating System

### Questions

1. Who should be allowed to submit a product rating or review?
2. Can users edit or delete a review after submitting it?
3. Is written feedback mandatory, or can users submit only a star rating?

### Detailed Requirement

The system shall provide a 5-star rating system, allowing users to rate products from 1 to 5 stars. Only registered users who have purchased the product can submit a rating or review. Users can submit a star rating without written feedback or submit written feedback together with their star rating. Users can edit their existing review, delete their entire review, or remove only the written comment by editing the review while keeping the star rating.

### Open Questions

It still needs to be clarified whether users can submit a review immediately after purchasing a product or only after receiving it. It also needs to be clarified whether the purchase requirement applies to submitting star ratings as well as written comments.

## 2. Age Verification

### Questions

1. What date format should users enter for age verification?
2. Should age verification be saved per user, so that the user only needs to verify their age once, or should it be requested every time the user starts a new session?
3. What should happen if a user enters an incorrect date of birth by mistake or enters an invalid date (e.g. month 15)? Should the user be able to correct or reset the entered date?
4. What error message should be displayed if a user is under 18 years old?

### Detailed Requirement

The system shall require users to verify that they are at least 18 years old before accessing the category containing alcoholic products. When a user opens this category, the system shall display an age verification window asking the user to enter their date of birth in day/month/year format. If the user is under 18, the system shall display the following message: "Sorry, you are underage. You will be able to buy when you are 18."

### Open Questions

It still needs to be clarified whether age verification should be saved per user or requested at the beginning of every new session. It also needs to be clarified how the system should handle incorrect or invalid dates of birth, including whether users can correct or reset their entries.

## 3. Shipping Cost Change

### Questions

1. What is the order value limit above which shipping becomes free?
2. How much is the shipping cost for orders below this limit?
3. Should the system display a message informing users about the free-shipping threshold and how much more they need to spend to qualify?
4. Should the shipping cost be updated automatically whenever the order value goes above or below the threshold, or should the user refresh or reopen the page?

### Detailed Requirement

The system shall provide free shipping for orders with a total value of €20 or more. For orders below €20, a shipping fee of €5 shall be applied. The system shall display a message below the order details informing users that they can receive free shipping by reaching the required order value. The message shall also indicate how much more the user needs to spend to qualify for free shipping.

### Open Questions

Should the shipping cost be updated automatically whenever the order value goes above or below €20, or should the user refresh or reopen the page?
