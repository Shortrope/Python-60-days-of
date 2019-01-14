# Pytest

## Virtual Environment

    python3 -m venv venv/
    source venv/bin/activate
    pip3 install pytest
    deactivate

Backup and restore environment

    pip3 freeze > requirements.txt
    pip3 install -r requirements.txt

Root Proj Dir
    src/
    test/
    venv/
    .gitignore
    requirements.txt

.gitignore

    .venv
    venv/
    ENV/

## Run the tests

    python3 -m pytest
    or
    pytest -v
        -v      verbose
        -s      do not show console output (shows print statements on console)
        -q      quiet mode. helpful if running many tests 100s or 1000s
       --ignore    ignore specified path when discovering tests
       --maxfail   Stop ofter the specified number of failures
        run specific tests: see vid 2.6
        

## Test discovery
- functions: 'test' at the begining of the function name
- Classes w testes in them: 'Test' at the beginning of the name and NO 'init' methond
- test module filenames start or end w 'test_' or '_test'

## Setup and Teardown functions
_*See Test Fixtures: better option_  
setup/teardown functions will execute code before and after
- test modules
    - def setup_module():
    - def teardown_module():
- Test functions
    - def setup_function():
    - def teardown_function():
- Test classes
    - def setup_class():
    - def teardown_class():
- Test methods in test classes
    - def setup_method():
    - def teardown_method():

## Test Fixtures
Better alternative to setup/teardown
- The `@pytest.fixture` decorator is applied to functions
- Each unit test can specify which fixtures they want executed
- 'autouse' parameter if set to True, automatically executes the fixture for all tests

Two methods to tell a function to use the fixture:

    @pytest.fixture()
    def mathfix():
        return Math()

    def test_Add(mathfix):
        assert math.add(1,1) == 2

    @pytest.mark.usefixtures("mathfix")
    def test_Sub():
        assert math.add(1,1) == 2

Can also tell all tests to use the fixture - autouse

    @pytest.fixture(autouse=True)
    def mathfix():
        return Math()

### Teardown w `yield`
- Code after the `yield` keyword is executed after the fixture goes out of scope
- `yield` is a replacement for `return`. Any return values are specified in the yield statement

example:

    @pytest.fixture()
    def setup1():
        print("Setup")
        yield
        print("Teardown")

### Teardown w `request.addfinalizer()`
This method allows multiple functions to be run

    @pytest.fixture()
    def setup1():
        print("Setup")

        def teardown_1():
            print("Teardown 1")

        def teardown_2():
            print("Teardown 2")
    
    def test1(setup1):
        ...

### Fixture Scope
- Function: Run fixture once for each test
- Class:    Run fixture once for each class of tests
- Module:   Run fixture once when the module goes in scope
- Session:  Run fixture when pytest starts

example:

    @yptest.fixture(scope='session')
    @yptest.fixture(scope='module')
    @yptest.fixture(scope='class')
    @yptest.fixture(scope='function')

### Fixtures can return data
The following example will run the test 3 times, once for each value in 'params'

    @pytest.fixture(params=[1,2,3])
    def setup(request):
        tetVal = request.param
        print("Setup retVal = {}".format(reVal))
        return retVal

    def test1(setup):
        print("setup = {}".format(setup))
        assert True

## Assertions

assert 1 == 1
assert [1,2,3] == [1,2,3]

### Floating Point Valuse
Use the pytest `approx` function

    from pytest import approx
    assert (0.1 + 0.2) == approx(0.3)

## Verifing Exceptions

def test_1():
    with raises(ValueError)
        raise ValueError

## Pytest command line args
