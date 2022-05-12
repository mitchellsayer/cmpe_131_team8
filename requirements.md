## Functional Requirements

1. User login and authentication
2. User logout
3. Create new account
4. Delete account
5. Search function for posted items
6. Automatic confirmation email sent upon purchase completion
7. Ability to select quantity of item being purchased
8. New Item listing functionality (form submission)
9. Sales Tax automatically added during item checkout
10. View purchase history
11. Configurable Price filter for listings 
12. Implementation of Luhn Algorithm for credit card number validation.

## Non-functional Requirements

1. Credit Card will not be charged upon purchase, the action will be spoofed
2. Site-wide Dark Mode option
3. Proper storage and transmission of password data using hashes
4. Code base will be made maintainable by effective use of Jinja templating and modular site components.

## Use Cases

### 1. Search Item
- **Pre-condition:** Shopper must be authenticated 

- **Trigger:** Shopper clicks on the "Search" tab on top of website page 

- **Trigger:** User goto checkout
               
- **Primary Sequence:**
  1. Customer enters in a key word ("toys", "food", "clothes") to narrow down search
  2. System searches through all of the items from website to see if they match narrowed down search
  3. System ignores all items that don't meet requirements
  4. System orders all items alphabetically into a list
  5. System prompts user with items from their specified category 

- **Primary Postconditions:** Customer sees the item they are looking for within the website OR Customer receives the message "No Items Found" if website doesn't sell the item

- **Alternate Sequence:** System prompts user that the item can't be found OR System asks user to enter in a valid item to search bar


### 2. Select Quantity
- **Pre-condition:** Shopper must be signed into website database and must have selected an item from the search menu

- **Trigger:** Shopper clicks on the "Quantity" button featured for each item

- **Primary Sequence:**
  1. Customer enters in a key word ("toys", "food", "clothes") to narrow down search
  2. System searches through all of the items from website to see if they match narrowed down search
  3. System ignores all items that don't meet requirements
  4. System orders all items alphabetically into a list
  5. System prompts user with items from their specified category
  6. Customer selects how many of each item they want ("1" is default amount)

- **Primary Postconditions:** Customer is charged for all of the items they have selected OR Customer doesn't select any items for purchase and isn't charged

- **Alternate Sequence:** System automatically selects "1" for each item selected by shopper


### 3. Check Purchase History
- **Pre-condition:** Shopper must be signed into website database, must have selected an item from the search menu, and must have gone through checkout/physically purchased item(s)

- **Trigger:** Shopper clicks on the "Purchase History" tab 

- **Primary Sequence:**
  1. System prompts customer with their past purchase history, including time stamp of when purchase occurred
  2. Customer filters out past purchases by entering a specific date (ie 4/14)


- **Primary Postconditions:** Customer sees the items purchased in the past
                                OR
                              Customer receives the message "No History Found" if website doesn't have history of a purchase occurring



- **Alternate Sequence:** System prompts user that their history can't be found


### 4. Add Tax
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


- **Alternate Sequence:** System prompts user that they need to add items to cart to be charged OR System asks user to enter a valid number of items into cart (greater than 0)


### 5. Filter items 
- **Pre-Condition** User must be in the Listings section of the website

- **Trigger** User selects filter dropdown at top of listing page

- **Primary Sequence**
   1. On the left, in the filter dropdown, Users select "high to low" or "low to high".
   2. Filter is applied when the user clicks apply filters.

- **Primary Postconditions** The user can browse Listings more effectively based on price.


### 6. Post Listing
- **Pre-condition:** User must be logged in and authenticated.

- **Trigger:** User clicks "New Listing" button in the menu bar

- **Primary Sequence:**
  1. User enters listing title
  2. User enters listing description
  3. User enters listing price
  4. When "Post Listing" button is clicked, a db entry for the post is inserted.
  5. Client browsers viewing listing data are updated with new listing

- **Primary Postconditions:** The newly created listing will be available to view by all logged in users, and in the post history page for the current user. Other users can (fake) purchase the listed item.

- **Alternate Sequence:** User selects "Cancel" button and the currently inputted form data is dropped.
