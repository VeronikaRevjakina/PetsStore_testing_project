# Petstore test project

The scope of this project is to do simple testing on https://petstore.swagger.io/v2

GET and PUT/DELETE/POST methods with different complexity levels are required.



## Limitations:
- Python3
- Pytest   (https://github.com/pytest-dev/pytest)
- requests (https://github.com/psf/requests)

## How to run tests using docker 
1. Set up working directory from pets folder

2. Create docker image assuming that you are in the root folder:
```
docker build -t pets_tests .
```
3. Run container 
```
docker run --rm -v  {your_absolute_sys_path}/test_reports:/WORK_DIR/test_reports pets_tests
```
