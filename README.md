# pytest-ci-demo

This repository is for practicing **pytest** and **GitHub Actions CI**.  
Here’s the step-by-step learning curriculum for myself.

## 📖 References
- [Official Pytest Documentation](https://docs.pytest.org/en/stable/how-to/index.html)

---

## 1️⃣ Pytest Basics
- [x] Install and run pytest  
- [x] Write simple test functions (`test_*.py`)  
- [x] Use `assert` for checks  
- [x] Understand test results (`. F E s x X`)  
- [x] Practice failing, skipping, xfail, xpass tests  

---

## 2️⃣ Pytest Features
- [ ] Use `@pytest.mark.parametrize` for multiple cases  
- [ ] Learn `fixture` for setup/teardown  
- [ ] Conditional skip (`skipif`)  
- [ ] Group tests with markers (`slow`, `db`, etc.)  
- [ ] Share fixtures via `conftest.py`  

---

## 3️⃣ Test Organization
- [ ] Use `src/` + `tests/` project structure  
- [ ] Follow naming rules for files and functions  
- [ ] Distinguish unit vs integration tests  
- [ ] Configure pytest with `pytest.ini`  

---

## 4️⃣ Reports & Analysis
- [ ] Run with options: `-v`, `-q`, `-k`  
- [ ] Measure coverage with `pytest-cov`  
- [ ] Re-run failed tests only (`--lf`)  
- [ ] Export JUnit XML reports  

---

## 5️⃣ GitHub Actions CI
- [x] Create `.github/workflows/tests.yml`  
- [x] Run pytest automatically on push/PR  
- [x] See pass/fail in GitHub Actions  
- [ ] Test with multiple Python versions (matrix)  
- [ ] Add coverage reporting in CI  

---