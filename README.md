# ThinkFlow

Discovering research papers made easy! Our project understands your specific questions and finds research papers that match. Simply ask, and explore academic knowledge effortlessly.


## Acknowledgements

Our project is based on [llm-app](https://github.com/pathwaycom/llm-app). We express our appreciation to the llm-app contributors for their invaluable efforts and contributions.



## Get Started

### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.

### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/debugger-lang/ThinkFlow
```

Next, navigate to the repository:

```bash
cd ThinkFlow
```

### Step 2: Set environment variables

Create an .env file in the root directory and add the following environment variables, adjusting their values according to your specific requirements and setup.

For example:

```bash
APP_VARIANT=contextful
PATHWAY_REST_CONNECTOR_HOST=0.0.0.0
PATHWAY_REST_CONNECTOR_PORT=8080
OPENAI_API_KEY=<Your Token>
PATHWAY_CACHE_DIR=/tmp/cache
```

### Step 3: Build and deploy custom API [You can test by deploying it locally on port 8080]

You can install and run the LLM App.

- **Install poetry:**

  ```bash
  pip install poetry
  ```

- **Install llm_app and dependencies:**

  ```bash
  poetry install --with examples --extras local
  pip install poetry
  ```

  You can omit `--extras local` part if you're not going to run local example.

### Step 4: Fetch research papers into a json file
```bash
#run this 
python fetch_papers.py
```
Adjust the number of fetched papers by modifying the `num_papers` variable in the `fetch_papers.py` file.

### Step 5: **Run:** You can start the example with the command:

  ```bash
  poetry run ./run_examples.py contextful
  ```


### Step 6: Launch the User Interface

Go to the `examples/ui/ directory` and execute `streamlit run server.py`. Then, access the URL displayed in the terminal to engage with the app using a chat interface.

## Troubleshooting

Please check out our [Q&A](https://github.com/pathwaycom/llm-app/discussions/categories/q-a) to get solutions for common installation problems and other issues.

### Raise an issue

To provide feedback or report a bug, please [raise an issue](https://github.com/debugger-lang/ThinkFlow/issues).

## Contributing

Anyone who wishes to contribute to this project, whether documentation, features, bug fixes, code cleanup, testing, or code reviews, is very much encouraged to do so.

## Need help?

Feel free to reach out.
