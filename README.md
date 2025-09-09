# Math Utils

Simple math utilities package for demonstration of **CI/CD with GitHub Actions**.

![CI](https://github.com/FranzCastillo/CI-CD-Basic-Math-Package/actions/workflows/ci.yml/badge.svg)

## Functions
- `square(n)`
- `factorial(n)`
- `is_prime(n)`
- `gcd(a, b)`
- `lcm(a, b)`

## Install
```bash
pip install .
```

## Trigger CI/CD
- Push code to `main` branch
- Create a pull request to `main` branch
```bash
git checkout -b feature/test-pipeline
git add .
git commit -m "Test"
git push origin feature/test-pipeline
```
