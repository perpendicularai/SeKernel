# 📝 SeKernel
A semantic-kernel for Streamlit python projects

## ⚙️ How to
- clone the repo
- from within the project directory run `pip install -e .`
- Import into your projects:
- - ```
    # Load kernel
    import kernel

    data = kernel.readData() # This may then be used in your LlamaCpp prompt

    # Use kernel to store conversations
    storedData = kernel.saveData()
    ```
