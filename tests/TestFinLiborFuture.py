###############################################################################
# Copyright (C) 2018, 2019, 2020 Dominic O'Kane
###############################################################################

from FinTestCases import FinTestCases, globalTestCaseMode

from financepy.products.libor.FinLiborFuture import FinLiborFuture
from financepy.finutils.FinDate import FinDate

testCases = FinTestCases(__file__, globalTestCaseMode)

###############################################################################


def test_FinLiborFuture():

    todayDate = FinDate(5, 5, 2020)

    testCases.header("VALUES")

    for i in range(1, 12):
        fut = FinLiborFuture(todayDate, i, "3M")
        testCases.print(fut)

        fra = fut.toFRA(0.020, 0.0)
        testCases.print(fra)

###############################################################################


test_FinLiborFuture()
testCases.compareTestCases()
