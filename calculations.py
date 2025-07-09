from typing import TypeAlias, Literal

Dollars : TypeAlias = int
Years : TypeAlias = int
VALID_PAYMENT_SCHEDULES = ["monthly", "quarterly", "annually", "at maturity"]
InterestPaymentSchedule : TypeAlias = Literal[tuple(VALID_PAYMENT_SCHEDULES)]

def term_deposit_interest(deposit_amount : Dollars,
             yearly_interest_percent : float,
             investment_term : Years,
             payment_schedule : InterestPaymentSchedule
            ) -> Dollars:
    
    """
    >>> term_deposit_interest(10000, 1.10, 3, "at maturity")
    10330
    >>> term_deposit_interest(10000, 1.10, 3, "monthly")
    10335
    >>> term_deposit_interest(10000, 1.10, 3, "quarterly")
    10335
    >>> term_deposit_interest(10000, 1.10, 3, "annually")
    10334
    >>> term_deposit_interest(920000, 1.20, 5, "at maturity")
    975200
    >>> term_deposit_interest(920000, 1.20, 5, "monthly")
    976860
    >>> term_deposit_interest(920000, 1.20, 5, "quarterly")
    976802
    >>> term_deposit_interest(920000, 1.20, 5, "annually")
    976541
    """

    yearly_interest_rate = yearly_interest_percent / 100

    match payment_schedule:
        case "monthly":
            return round(deposit_amount * (1 + yearly_interest_rate/4)**(investment_term*4))
        case "quarterly":
            return round(deposit_amount * (1 + yearly_interest_rate/4)**(investment_term*4))
        case "annually":
            return round(deposit_amount * (1 + yearly_interest_rate)**investment_term)
        case "at maturity":
            return round(deposit_amount * (1 + yearly_interest_rate*investment_term))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)