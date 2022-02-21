# Athena API &copy; 2021, Invictus808

## Overview

Athena API (application programming interface) is designed for [invictus808.com](https://invictus808.com/) and other projects under [Invictus808](contact@invictus808.com).


## Team

### Authors
- Blaise Aranador ([Invictus808](https://invictus808.com/))


### Maintainers
- Blaise Aranador ([contact@invictus808.com](contact@invictus808.com))


---

## Documentation

### Environment
- [DigitalOcean](https://www.digitalocean.com/)
- [Ubuntu 20.04 LTS](https://ubuntu.com/)


### Requirements
- [Python 3.9](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

#### Install Python 3.9
```
sudo apt install python3.9 -y
```

#### Install pip3
```
sudo apt install python3-pip -y
```

#### [Remove old versions and install Docker](https://docs.docker.com/engine/install/ubuntu/)
```
sudo apt remove docker docker-engine docker.io containerd runc -y

sudo apt update -y

sudo apt install ca-certificates curl gnupg lsb-release -y

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update -y

sudo apt install docker-ce docker-ce-cli containerd.io -y
```

#### [Install Docker Compose](https://docs.docker.com/compose/install/)
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```


### Development

#### Install Python 3.9 Virtual Environment
```
sudo apt install python3.9-venv -y
```

#### Using Python 3.9 Virtual Environment
- Create virtual environment
```
python3 -m venv <virtual_environment_name>
```

- Activate virtual environment
```
source <virtual_environment_name>/bin/activate
```

- Deactivate virtual environment
```
deactivate
```


### Testing

#### Install Pytest
```
pip install pytest
```

#### Pytest Commands
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
