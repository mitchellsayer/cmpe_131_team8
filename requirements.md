
## Functional Requirements

1. Users can gain points on their account from making purchases
2. Users can spend those points on some sort of discounts
3. Users can subscribe or pay a one time fee for perks like free shipping
4. Users can make a wishlist of listings they might want to look at later
5. Users can search for listings
6. listings of the same item are posted on the same page (in other words no duplicate Listings)
7. filter Listings by price or other constraints
8. main page: featured items, patch notes, welcome sign
9. timed listings that expire after a given time. date of posting to see how long an item has been available
10. Viewing User History: Purchased, Sold, viewed, rated
11. User Wallet to keep track of website money and points
12. Star ratings for each item
bonus: Hidden Easter Eggs 

## Non-functional Requirements

1. User Settings: Dark mode, privacy
2. no more than 30 second load times for pages
3. multi-Language support 
4. Change how many listings can be seen at a time
5. Change how many pages can be skipped at once

## Use Cases

1. make wishlist
- **Pre-condition:** User must be logged in, 

- **Trigger:** User Clicks "add to wishlist" 

- **Primary Sequence:**
  
  1. The Customer Searches or Browses for a listing
  2. The Customer clicks into one they find interesting
  3. They click the "Add to wishlist" button
  4. The System adds the listing to a list element in the user database
  5. The wishlist can be viewed from the User page

- **Primary Postconditions:** The User has a wishlist with listings they can reference later 

- **Alternate Sequence:** 
  
  1. A User doesn't click into a listing and can't find the "add to wishlist" button

- **Alternate Sequence <optional>:**
  
  1. The User doesn't want to save the item to their wishlist and they don't click the add to wishlist button

2. Filter items 
   **Pre-Condition** User must be in the Listings section of the website

   **Trigger** User clicks one of the checkboxes to filter the Listings shown

   **Primary Sequence**
   1. The Customer navigates to the Listings page
   2. On the left they click the checkbox that says "Below 50$"
   3. Only Listings under 50$ are shown on the page.

   **Primary Postconditions** The user can browse Listings more effectively based on price

   **Alternate Sequence**
   1. The User navigates to the Listing page
   2. They don't click the check box and all the Listings are displayed as normal

3. Leave Star Ratings
	**Pre-Condition** A logged in User has purchased the item in order to post a rating

	**Trigger** Click on one of the 5 stars based on how much you would like to rate the item

	**Primary Sequence**
	1. navigate to you purchase history
	2. Select the Listing you wish to rate
	3. Click on the Star value you would like to give the item
	4. Click confirm
	5. The System calculates the average of all the ratings posted and displays that on the listing

	**Primary postcondition** There is a rating posted on the listing that represents ratings left by buyers

4. Post Timed Listings
	**Pre-Condition** A Logged in User

	**Trigger** The "post timed Listing" button is clicked

	**Primary Sequence**
	1. Navigate to the User page
	2. click "post timed listing"
	3. fill out all the details of the listing including the length of time it should be posted for
	4. click confirm
	
	**Primary Postcondition** The described Listing is posted with a timer to expire when the User specified
5. Pay Taxes
	**Pre-condition** Website Initialized

	**Trigger** click the checkout button

	**Primary Sequence**
	1. Navigate to the Listings page
	2. enter a listing and add it to cart
	3. click on the cart tab
	4. The tax required will be calculated and shown before the final payment is taken

	**Primary PostCondition** An Appropriate amount of extra payment is taken for taxes
6. apply discounts
	**Pre-Conditions** A Logged in User has enough points to apply a discount

	**Trigger** The apply discount button is pressed

	**Primary Sequence**
	1. Navigate to the Listings page and select one for purchase
	2. add it to cart and navigate to the cart tab
	3. press one of the discount options based on how many points you would like to spend
	4. the payment due should be reduced and the User can continue with the checkout process

	**Primary PostCondition** The correct amount of payment was taken off for the correct amount of points
