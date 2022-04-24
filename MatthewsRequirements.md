#THESE ARE MY SUGGESTED IDEAS FOR TEAM 8's PROJECT

## Functional Requirements

1. Inclusion of a "Search" Option for item (using barcode or key phrases)
2. Each item having a "Quantity" tab next to it in case user wants more than one product
3. Shipping and Handling estimation fees depending on user's location 
4. Narrowed search results option depending on user's interests (toys, clothes, food, etc.)
5. "New" icon appearing on screen when a new item has been listed
6. Inclusion of coupons which allow for reduced prices (10%, 15%, etc.)
7. Feedback option to receive reviews from customers
8. Extra information page which shows how long a seller has been a member on the website
9. Rate an item based on customer's opinion (include short blurb about what they liked/didn't like related to product)
10. A "Budget" tab which only shows items valued at $50 and under
11. Depending on the day, a sale appears for specific items (Half-priced Wednesdays, Free Fridays)
12. Option to see a zoomed-in view of the item by hovering over it with user's mouse

## Non-functional Requirements

1. A flashing "Welcome!" sign that entices guests on the "Home" Page
2. Allowing a "Dark Mode" version of website with black backgrounds 
3. Calendar which shows typical date configuration (ie 4/14/2022) 
4. Avatar Image for each unique shopper

## Use Cases

1. Search Item
- **Pre-condition:** Shopper must be signed into website database

- **Trigger:** Shopper clicks on the "Search" tab on top of website page 

- **Primary Sequence:**
  
  1. Customer enters in a key word ("toys", "food", "clothes") to narrow down search
  2. System searches through all of the items from website to see if they match narrowed down search
  3. System ignores all items that don't meet requirements
  4. System orders all items alphabetically into a list
  5. System prompts user with items from their specified category 

- **Primary Postconditions:** Customer sees the item they are looking for within the website 
				OR
			      Customer receives the message "No Items Found" if website doesn't sell the item
 

- **Alternate Sequence:** System prompts user that the item can't be found
			    OR
			  System asks user to enter in a valid item to search bar
 
  
  
2. Select Quantity
- **Pre-condition:** Shopper must be signed into website database and must have selected an item from the search menu

- **Trigger:** Shopper clicks on the "Quantity" button featured for each item

- **Primary Sequence:**
  
  1. Customer enters in a key word ("toys", "food", "clothes") to narrow down search
  2. System searches through all of the items from website to see if they match narrowed down search
  3. System ignores all items that don't meet requirements
  4. System orders all items alphabetically into a list
  5. System prompts user with items from their specified category
  6. Customer selects how many of each item they want ("1" is default amount)

- **Primary Postconditions:** Customer is charged for all of the items they have selected
                                OR
                              Customer doesn't select any items for purchase and isn't charged
 

- **Alternate Sequence:** System automatically selects "1" for each item selected by shopper
                            


   
3. Check Purchase History
- **Pre-condition:** Shopper must be signed into website database, must have selected an item from the search menu, and must have gone through checkout/physically purchased item(s)

- **Trigger:** Shopper clicks on the "History" tab 

- **Primary Sequence:**
  
  1. System prompts customer with their past purchase history, including time stamp of when purchase occurred
  2. Customer filters out past purchases by entering a specific date (ie 4/14)


- **Primary Postconditions:** Customer sees the items purchased in the past
                                OR
                              Customer receives the message "No History Found" if website doesn't have history of a purchase occurring

 

- **Alternate Sequence:** System prompts user that their history can't be found
                         



4. Add Tax
- **Pre-condition:** Shopper must be signed into website database and must have selected item(s) for purchase

- **Trigger:** Shopper clicks "Checkout" option for all of their items

- **Primary Sequence:**
  
  1. Customer chooses which items interest them
  2. System prompts the user to select how many of each item they want
  3. Customer heads to checkout portion of website
  4. System charges user for items along with a 10% sales tax

- **Primary Postconditions:** Customer is charged for all of the items in cart
                                OR
                              Customer is NOT charged because there are no items in cart
 

- **Alternate Sequence:** System prompts user that they need to add items to cart to be charged
                            OR
                          System asks user to enter a valid number of items into cart (greater than 0)




5. Rate Seller
- **Pre-condition:** Shopper must be signed into website database and purchased an item from vender

- **Trigger:** Shopper clicks on the "Write a Review" tab next to seller's profile

- **Primary Sequence:**
  
  1. Customer reflects on their online shopping experience/quality of item purchased
  2. Each customer rates seller on a scale of 1 to 5 (1 being "awful" and 5 being "superb")
  3. Based on customer survey, seller's score goes either up or down (out of 100%)
  4. System informs seller when the experience form has been filled out 

- **Primary Postconditions:** Seller sees the new reviews added to their profile
                                OR
                              Customer doesn't write a rewiew, so no message appears
 

- **Alternate Sequence:** No reviews are written, thus the seller has no feedback on their profile
                           



6. Apply Coupon
- **Pre-condition:** Shopper must be signed into website database, have purchased items from the website, and is ready to checkout

- **Trigger:** Shopper clicks on the "Apply Coupon" button in "Checkout" window

- **Primary Sequence:**
  
  1. Customer chooses which items interest them
  2. System prompts the user to select how many of each item they want
  3. Customer heads to checkout portion of website
  4. Coupon is applied before customer finalizes their payment 

- **Primary Postconditions:** Customer sees that their total receipt has decreased due to the coupon
                                OR
                              Customer never applies coupon, thus keeping their total receipt the same
 

- **Alternate Sequence:** System prompts user that an item needs to be within their cart in order to apply a coupon


