# Story1

Acceptance criteria from User Story #1
	- There should be ‘departure’ and ‘return’ fields on a search form.
	- Flights leave every six months, in July and December, both ways.
	- Trips for the next two years should be searchable.
	- If there are seats, display “Seats available! Call 0800 MARSAIR to book!”
	- If there are no seats, display “Sorry, there are no more seats available.”

=== This is a context step that runs before every scenario ===

* Goto MarsAirs homepage

===	

## TC01: Valid search whithout a code
Tags: UserStory1

* Click in "Departing" and select "July"
* Click in "Returning" and select "December (two years from now)"
* Click "Search"
* Verify if message "Seats available!" is displayed
* Verify if message "Call 0800 MARSAIR to book!" is displayed

## TC02: Valid search with a code
Tags: UserStory1, Code

* Click in "Departing" and select "July"
* Click in "Returning" and select "December (two years from now)"
* Type promotion code "JJ5-OPQ-319"
* Click "Search"
* Verify if message "Seats available!" is displayed
* Verify if discount of "50" from "JJ5-OPQ-319" is applied
* Verify if message "Call 0800 MARSAIR to book!" is displayed


## TC03: No seat scenario
Tags: UserStory1

* Click in "Departing" and select "July"
* Click in "Returning" and select "December (next year)"
* Click "Search"
* Verify if message "Sorry, there are no more seats available." is displayed


