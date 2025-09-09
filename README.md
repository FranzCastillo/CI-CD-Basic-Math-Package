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
  - git add .
  - git commit -m "Message"
  - git push origin main
- Create a pull request to `main` branch
    - git checkout -b feature-branch
    - git add .
    - git commit -m "Message"
    - git push origin feature-branch
