" test the results module "

import pytest
import random

import settings
from parser.results import results_from_accounts
from parser.validators import Validate

from common_tools import flatten
from common_tools import invalid_lengths, fit_to_length, replace_element

class TestResultsFromAccounts:
    " exercise the results_from_accounts function "

    class TestInput:
        " confirm invalid input raises appropriate error "

        def test_with_non_iterable(self, non_iterable):
            " confirm error raised on non-iterable input "
            results = results_from_accounts(non_iterable)
            pytest.raises(TypeError, list, results)

        def test_with_non_string(self, non_string):
            " confirm error raised on iterable that yields a non_string "
            accounts = [non_string,]
            results = results_from_accounts(accounts)
            pytest.raises(TypeError, list, results)

        @pytest.fixture(params=invalid_lengths(settings.figures_per_entry))
        def invalid_account_length(self, request):
            " return an invalid length for an Account "
            return request.param

        def test_with_account_of_invalid_length(self, get_account, invalid_account_length):
            " confirm error raised for result of invalid length "
            invalid_length_account = fit_to_length(get_account(), invalid_account_length)
            results = results_from_accounts([invalid_length_account,])
            pytest.raises(ValueError, list, results)

        some_non_numerals = {'\t', '-', 'I', 'l', '/', '\\', '\r'}
        in_common = some_non_numerals.intersection(settings.valid_numerals)
        assert set() == in_common
        @pytest.mark.parametrize('non_numeral', some_non_numerals)
        def test_with_non_account(self, get_account, non_numeral):
            " confirm error raised for non_account "
            adulterated_account = replace_element(get_account(), non_numeral)
            results = results_from_accounts([adulterated_account,])
            e = pytest.raises(TypeError, list, results)
            msg = 'Account "%s" contains unexpected element "%s" at index'
            msg = msg % (adulterated_account, non_numeral)
            assert msg in e.value.message

    class TestOutput:
        " confirm valid input results in valid output "

        def test_returns_iterable(self, get_accounts):
            " confirm iterable "
            results = results_from_accounts(get_accounts())
            Validate.iterable(results)

        def test_element_types(self, get_accounts):
            " confirm iterable yields strings "
            results = results_from_accounts(get_accounts())
            Validate.elements('type', basestring, results, 'Result')

        @pytest.mark.parametrize('account, result', (
            ('000000000', '000000000',),
            ('111111111', '111111111 ERR'),
            ('222222222', '222222222 ERR'), 
            ('333333333', '333333333 ERR'),
            ('444444444', '444444444 ERR'),
            ('555555555', '555555555 ERR'),
            ('666666666', '666666666 ERR'),
            ('777777777', '777777777 ERR'),
            ('888888888', '888888888 ERR'),
            ('999999999', '999999999 ERR'),
            ('123456789', '123456789'),
            ))
        def test_parses_known_accounts_to_results(self, account, result):
            " confirm known accounts recognized correctly "
            expected = [result,]
            found = list(results_from_accounts([account,]))
            assert expected == found