# Test

## Install Pytest
```
pip install pytest
```

## Pytest Commands (Using Docker Compose)
- Normal run
```
docker-compose exec api python -m pytest "src/tests"
```

- Disable warnings
```
docker-compose exec api python -m pytest "src/tests" -p no:warnings
```

- Run only the last failed tests
```
docker-compose exec api python -m pytest "src/tests" --lf
```

- Run only the tests with names that match the string expression
```
docker-compose exec api python -m pytest "src/tests" -k "config and not test_development_config"
```

- Stop the test session after the first failure
```
docker-compose exec api python -m pytest "src/tests" -x
```

- Enter PDB after first failure then end the test session
```
docker-compose exec api python -m pytest "src/tests" -x --pdb
```

- Stop the test run after two failures
```
docker-compose exec api python -m pytest "src/tests" --maxfail=2
```

- Show local variables in tracebacks
```
docker-compose exec api python -m pytest "src/tests" -l
```

- List the 2 slowest tests
```
docker-compose exec api python -m pytest "src/tests" --durations=2
```
