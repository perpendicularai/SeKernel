# 📝 SeKernel :octocat:
A semantic-kernel for Streamlit python projects to give your applications 🧠 memory

## ⚙️ How to
- clone the repo
- from within the project directory run `python setup install`
- Import into your projects:
  - ```
    # Load kernel
    import kernel.kernel as kk

    data = kk.readData() # Ensure that the extracted kernel.json file is in the same directory that you're using the module in. This may then be used in your LlamaCpp prompt as context

    # Use kernel to store conversations
    storedData = kk.saveData()
    ```
