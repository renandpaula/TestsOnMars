# Story4

Acceptance criteria from User Story #4
	- “Unfortunately, this schedule is not possible. Please try again.” displayed when return date is less than 1 year from the departure.

=== This is a context step that runs before every scenario ===

* Goto MarsAirs homepage

===	

## TC01: Invalid search scenario
Tags: UserStory4

| Departure | Return   |
|-----------|----------|
| July      | December |
| December  | July     |
| December  | December |
| July      | July     |

* Click in "Departing" and select <Departure>
* Click in "Returning" and select <Return>
* Click "Search"
* Verify if message "Unfortunately, this schedule is not possible. Please try again." is displayed


