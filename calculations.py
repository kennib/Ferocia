from typing import TypeAlias, Literal

Dollars : TypeAlias = int
Years : TypeAlias = int
InterestPaymentSchedule : TypeAlias = Literal["monthly", "quarterly", "annually", "at maturity"]

def term_deposit_interest(deposit_amount : Dollars,
             yearly_interest_percent : float,
             investment_term : Years,
             payment_schedule : InterestPaymentSchedule
            ) -> Dollars:
    
    """
    >>> term_deposit_interest(10000, 1.10, 3, "at maturity")
    10330
    >>> term_deposit_interest(10354, 1.10, 3, "monthly")
    10335
    >>> term_deposit_interest(10354, 1.10, 3, "quarterly")
    10335
    >>> term_deposit_interest(10354, 1.10, 3, "annually")
    10334
    """

    yearly_interest_rate = yearly_interest_percent / 100

    match payment_schedule:
        case "monthly":
            return
        case "quarterly":
            return
        case "annually":
            return
        case "at maturity":
            return int(deposit_amount * (1 + yearly_interest_rate*investment_term))

if __name__ == '__main__':
    import doctest
    doctest.testmod()