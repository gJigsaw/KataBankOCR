"Test Parse module"

import pytest
import subprocess
from functools import partial

from test_input import Basic, Advanced

@pytest.fixture(params=((Basic.story_three_results, Basic.path),
                        (Advanced.story_three_results, Advanced.path),))
def expectations_and_source(request):
    "return expected results and input path from which to find them"
    expected, path = request.param
    expected = '\n'.join(expected) + '\n'
    return expected, path

def test_stdin_and_stdout(expectations_and_source):
    "confirm Results parsed correctly from StdIn to StdOut"
    expected_results, input_path = expectations_and_source
    with open(input_path) as input_file:
        found_results = subprocess.check_output(['parse/parse', '-'], stdin=input_file)
    assert expected_results == found_results

def test_in_path_and_stdout(tmpdir, expectations_and_source):
    "confirm Results parsed correctly from path to StdOut"
    expected_results, input_path = expectations_and_source
    found_results = subprocess.check_output(['parse/parse', input_path])
    assert expected_results == found_results

def test_in_path_and_out_path(tmpdir, expectations_and_source):
    "confirm Results parsed correctly from in_path to out_path"
    expected_results, input_path = expectations_and_source
    output_path = str(tmpdir.join('tmp_out_file'))
    subprocess.call(['parse/parse', input_path, output_path])
    with open(output_path) as parsed_results:
        found_results = parsed_results.read()
    assert expected_results == found_results

def test_stdin_and_out_path(tmpdir, expectations_and_source):
    "confirm Results parsed correctly from StdIn to out_path"
    expected_results, input_path = expectations_and_source
    output_path = str(tmpdir.join('tmp_out_file'))
    with open(input_path) as input_file:
        subprocess.call(['parse/parse', '-', output_path], stdin=input_file)
    with open(output_path) as parsed_results:
        found_results = parsed_results.read()
    assert expected_results == found_results
