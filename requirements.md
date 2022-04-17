## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Points rewards system to earn points and use towards total amount
2. Users personel wishlist
3. Search through users wishlist to check if something is added or not 
4. Remove button at checkout for items
5. Provide shipping free if a certain amont of total is reached
6. Provide sellers contact information 
7. feedback on item for seller
8. Connect to Google search or calender API
9. Price control for user to select from $0 - $x
10. check availability of item
11. buy item ( with randomised fake card)
12. Display User profile

## Non-functional Requirements

1. Welcome page
2. background image that relates to the website
3. consistent theme
4. consistent color scheme with buttons

## Use Cases

1. Search wishlist 
- **Pre-condition:** User needs to be logged in
                     User goto wishlist
                     User search for item in search tab

- **Trigger:** User types item in search box
               
- **Primary Sequence:**
  1. If item exsist in wishlist, show item to user
  2. Else display item not found

- **Primary Postconditions:** User finds item and decides whether or not to buy item

2. buy item
- **Pre-condition:** User needs to be logged in

- **Trigger:** User goto checkout
               
- **Primary Sequence:**
  1. user types information (firstname, lastname, address, credit/debit card etc)
  2. user continues with checkout

- **Primary Postconditions:** payment is processed and user is provided with confirmation, date/time of arrival

3. Remove item
- **Pre-condition:** User needs to be logged in
                     User needs to be at checkout

- **Trigger:** User clicks remove 
               
- **Primary Sequence:**
  1. Specific item is removed from users list

- **Primary Postconditions:** User checkout list gets updated with the specific item removed

4. Check History
  **Pre-condition:** User needs to be logged in

  **Trigger:** User clicks on  "History" tab/link
  
  **Primary Sequence:** System shows all past items brought

  **Primary Postconditions:** User sees the items purchased in the past OR receives the message "No History Found"

5. Send Feedback
   **Pre-condition:** User needs to be logged in
                      User must have item in purchase history
   
   **Trigger:** Click send Feedback
   
   **Primary Sequence:** Email is sent to seller
   
   **Primary Postconditions:** Massage shown to user that feedback sent
