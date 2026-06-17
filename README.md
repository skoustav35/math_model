# Math Model 🧮

Train the best math LLM to use math tools and achieve the most accurate math answers within a 7B parameter budget.

## 🎯 Project Overview

This project focuses on developing and training a 7B parameter language model specialized in mathematical problem-solving. The model is designed to leverage mathematical tools to provide accurate solutions across various mathematical domains.

### Key Features

- **Optimized for Math**: Specialized training for mathematical reasoning and tool usage
- **Efficient Size**: Compact 7B parameter architecture for practical deployment
- **Tool Integration**: Built-in support for mathematical tools and utilities
- **High Accuracy**: Trained specifically to maximize correctness on mathematical tasks

## 📋 Requirements

- Python 3.8+
- PyTorch
- Transformers library
- Additional dependencies listed in `requirements.txt`

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/skoustav35/math_model.git
cd math_model

# Install dependencies
pip install -r requirements.txt
```

### Training

```bash
python train.py
```

### Generation

```bash
python generate.py
```

## 📁 Project Structure

```
math_model/
├── train.py          # Training script for the math model
├── generate.py       # Generation script for inference
├── requirements.txt  # Project dependencies
├── .gitignore        # Git ignore patterns
└── README.md         # This file
```

## 🔧 Configuration

Key parameters can be adjusted in the training and generation scripts:
- Model size and architecture
- Training hyperparameters
- Tool integration settings
- Mathematical domain focus

## 📊 Performance

The model is optimized for:
- Mathematical reasoning accuracy
- Tool-assisted problem solving
- Efficient inference (7B parameters)
- Multi-domain mathematical tasks

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 📚 Resources

- [Transformers Documentation](https://huggingface.co/transformers/)
- [PyTorch Documentation](https://pytorch.org/docs/)

## 🐛 Issues & Support

For bug reports and feature requests, please use the [GitHub Issues](https://github.com/skoustav35/math_model/issues) page.

## 👤 Author

- **skoustav35** - Initial work

---

**Star this project if you find it useful!** ⭐
