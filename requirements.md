## Functional Requirements

1. User Login/Authentication (MS)
2. User Logout (MS)
3. Create User Account (MS)
4. Delete User Account (MM)
5. Search For Items (ZG)
6. Purchase Confirmation Email (MA)
7. Select Item Quantity (MM)
8. New Item Listing Form (ZG)
9. Additional Sales Tax (MS)
10. View Purchase History (MS)
11. Apply Price Filter (ZG)
12. Payment Card Validation (MM)
13. User Account Page (ZG)
14. Purchase Item Listing (MS)
15. Item Listing Page (MS)

## Non-functional Requirements

1. Denial of Payment Card (MM)
2. Mobile Compatible Webpages (MS)
3. Proper Storage/Transmission (MS)
4. Jinja Template Application (MS/ZG/MA/MM)
5. Home Page Item Carousel (MA)
6. User Profile w/ Item Purchases (MS)


## Use Cases

### 1. Search Item
- **Pre-condition:** User must be logged in 

- **Trigger:** User clicks on "Search" tab

- **Primary Sequence:**
  1. User enters key word to narrow down search
  2. System checks items stored in database to see if there's a match
  3. System displays matching items  

- **Primary Postconditions:** User sees item they're looking for

- **Alternate Sequence:** System displays message "Item not found"

### 2. Select Quantity
- **Pre-condition:** User must be logged in and must be on "Listings" page

- **Trigger:** User increases/decreases arrow button featured for each item

- **Primary Sequence:**
  1. User selects item that interests them on "Listings" page
  2. Item quantity is incremeneted/decremented depending on user's preference

- **Primary Postconditions:** User is charged for item they have selected OR User doesn't select any items for purchase and isn't charged

- **Alternate Sequence:** Default quantity for each item is "1"


### 3. Check Purchase History
- **Pre-condition:** User must be logged in and have clicked "Purchase Now" option on "Checkout" page

- **Trigger:** User clicks on the "Purchase History" tab 

- **Primary Sequence:**
  1. 
  2. System shows all listings purchased by user


- **Primary Postconditions:** User sees items purchased in the past
              
                              
- **Alternate Sequence:** System prompts user that purchase history can't be found


### 4. Add Tax
- **Pre-condition:** User must be logged in and have selected an item for purchase

- **Trigger:** User clicks "Purchase" option for their item

- **Primary Sequence:**

  1. "Checkout" page shows user's selected item
  2. System takes item's price and adds on a 10% sales tax for "Total"

- **Primary Postconditions:**  User is charged for the item in their checkout 
                               User is sent a confirmation email containing purchase detail


### 5. Filter Items 
- **Pre-Condition** User must be logged in and on "Listings" page of website

- **Trigger** User selects filter dropdown at top of "Listings" page

- **Primary Sequence**
   1. On the left, in the filter dropdown, Users select "high to low" or "low to high".
   2. Filter is applied when the user clicks apply filters.

- **Primary Postconditions** The user can browse Listings more effectively based on price.


### 6. Post New Listing
- **Pre-condition:** User must be logged in and on "New Listing" page of website

- **Trigger:** User clicks "New Listing" button in menu bar

- **Primary Sequence:**
  1. User enters a listing Title, Description, Brand, Price, Stock, and Image
  2. When "Post Listing" button is clicked, the item's information is stored into database
  3. The "Listings" page is updated with new listing

- **Primary Postconditions:** New item listing will be visible to all users
- **Alternate Sequence:** User simply clicks on a different website tab to void any listing they attempted to post


