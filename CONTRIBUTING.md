# Contributing to Math Model

Thank you for your interest in contributing to the Math Model project! We welcome contributions from the community.

## 🤝 How to Contribute

### Reporting Bugs

Before creating a bug report, please check the issue list to avoid duplicates. When creating a bug report, include:

- **Clear description**: Explain what the bug is
- **Steps to reproduce**: Provide specific steps to reproduce the issue
- **Expected behavior**: Describe what you expected to happen
- **Actual behavior**: Describe what actually happened
- **Environment**: Include Python version, OS, and relevant library versions

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When suggesting an enhancement, please include:

- **Use case**: Describe the use case and motivation
- **Proposed solution**: Explain how you'd like the feature to work
- **Alternative solutions**: List alternative approaches if any

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Test your changes** thoroughly

4. **Commit with clear messages**
   ```bash
   git commit -m "feat: add new feature"
   ```

5. **Push to your fork** and open a Pull Request

## 📋 Code Guidelines

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise

### Code Quality

- Use type hints where appropriate
- Write clear, commented code
- Avoid unnecessary complexity
- Ensure backward compatibility when possible

### Testing

- Write tests for new functionality
- Ensure all tests pass before submitting PR
- Aim for good test coverage

```bash
pytest
```

### Code Formatting

Format your code with Black and sort imports with isort:

```bash
black .
isort .
```

Lint with flake8:

```bash
flake8 .
```

## 📝 Commit Messages

Use clear, descriptive commit messages following conventional commits:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for formatting changes
- `refactor:` for code refactoring
- `test:` for test additions/changes
- `chore:` for maintenance tasks

Example:
```
feat: add support for additional math tools

- Implement tool integration framework
- Add example tools documentation
```

## 📚 Documentation

- Keep documentation up-to-date with code changes
- Add docstrings to all public APIs
- Update README if adding new features
- Document any configuration changes

## 🔄 Review Process

- Code reviews will be conducted by maintainers
- Constructive feedback will be provided
- All conversations should remain respectful and professional
- Changes may be requested before merging

## ⚖️ Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## ❓ Questions?

Feel free to ask questions by opening an issue or starting a discussion. We're here to help!

---

**Happy contributing!** 🎉
