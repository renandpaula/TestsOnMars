# Story2

Acceptance criteria from User Story #2
	- Promotional codes are in the format XX9-XXX-999.
	- Characters are all random.
	- The first digit indicates the discount percentage (2 = 20%, 3 = 30% etc).
	- The next two digits are random.
	- The final digit is a check digit; it is equal to the sum of all other digits modulo 10, eg:
		AF3-FJK-41?: 3 + 4 + 1 = 8, so the complete promotional code is AF3-FJK-418
		JJ5-OPQ-32?: 5 + 3 + 2 = 10, so the complete promotional code is JJ5-OPQ-320
	- When a valid code is entered, the search result should have a “Promotional code [code] used: [discount]% discount!” message.
	- Otherwise, show “Sorry, code [invalid promo code] is not valid”.

All tests were written based on these criteria.

=== This is a context step that runs before every scenario ===

* Goto MarsAirs homepage

===

## TC01: Verify Valid Promotional Codes
Tags: UserStory2, Code

Estratégia: Valor Limite + Condicional de verificação de dezena

| Discount | Code        |
|----------|-------------|
| 10       | XX1-XXX-001 |  
| 50       | XX5-XXX-410 |  
| 90       | XX9-XXX-009 |

* Click in "Departing" and select "July"
* Click in "Returning" and select "December (two years from now)"
* Type promotion code <Code>
* Click "Search"
* Verify if discount of <Discount> from <Code> is applied

## TC02: Verify Invalid Promotional Codes
Tags: UserStory2, Code


| Code        |
|-------------|
| XX0-XXX-000 |  
| XX2-XXX-206 |
| XX9-XXX-999 |
| XX4-XXX-XX4 |
| X4X-XXX-XX4 |
| 4XX-XXX-XX4 |
| XX4-XXX-4XX |
| XX4-XXX-X4X |
| XX4-X1X-XX5 |

* Click in "Departing" and select "July"
* Click in "Returning" and select "December (two years from now)"
* Type promotion code <Code>
* Click "Search"
* Verify if discount from <Code> is not valid

