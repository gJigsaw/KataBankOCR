"test the results module"

import pytest

from parse.generators.results_from_accounts import results_from_accounts

import check_generator
import fixtures

test_iterability = check_generator.raises_on_non_iterable(generator=results_from_accounts)

test_element_type = \
    check_generator.raises_on_bad_element_type(generator=results_from_accounts,
                                               value_or_type=fixtures.Accounts.get_random())
test_element_length = \
    check_generator.raises_on_bad_element_length(generator=results_from_accounts,
                                                 valid_element=fixtures.Accounts.get_random())
test_element_composition = \
    check_generator.raises_on_bad_element_composition(generator=results_from_accounts,
                                                      valid_element=fixtures.Accounts.get_random(),
                                                      adulterants=['\t', '-', 'I', 'l', '/', '\r'])

def test_parses_known_accounts_to_results():
    "confirm known account recognized correctly"
    expected = fixtures.Results.of_example_accounts()
    found = list(results_from_accounts(fixtures.Accounts.of_example_accounts()))
    assert expected == found

@pytest.mark.parametrize('expected_result, account', (
        zip(fixtures.Results.of_flawed_accounts(), fixtures.Accounts.of_flawed_accounts())
        ))
def test_parses_account_with_errors_to_expected_result(expected_result, account):
    "confirm superpositions with flawed figures yield expected accounts"
    found_results = list(results_from_accounts([account]))
    assert [expected_result] == found_results
