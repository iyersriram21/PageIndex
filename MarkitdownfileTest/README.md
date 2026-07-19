# MarkItDown PDF Testing Notebook

This workspace contains a Jupyter notebook for testing MarkItDown with a PDF and comparing the output against a LangChain/OpenAI-based workflow.

## Files

- `Test_markitdown.ipynb` - Notebook used to run the PDF-to-Markdown conversion and ask a question about the document.
- `README.md` - Setup and usage instructions.

## Prerequisites

Make sure you have:

- Python 3.10+ installed
- A virtual environment created in the project folder
- An OpenAI API key available in your environment or `.env` file

## Setup

From the project folder:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install markitdown langchain langchain-openai langchain-community pypdf python-dotenv ipykernel
```

If you are using a `.env` file, make sure it contains:

```text
OPENAI_API_KEY=your_api_key_here
```

## Register the Notebook Kernel

To use the virtual environment in Jupyter/VS Code:

```powershell
.\venv\Scripts\python.exe -m ipykernel install --user --name=markitdown-venv --display-name="Python (markitdown-venv)"
```

Then select that kernel in the notebook toolbar.

## Run the Notebook

1. Open `Test_markitdown.ipynb`
2. Select the `Python (markitdown-venv)` kernel
3. Run the notebook cells

## Notes

The notebook uses:

- `MarkItDown` to convert a PDF into Markdown text
- `ChatOpenAI` from LangChain to ask questions about the extracted content
- `python-dotenv` to load environment variables from a `.env` file

If the PDF file name changes, update `PDF_PATH` in the notebook.
