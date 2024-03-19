
# AI Chat Bot Interface: Front End with Enhanced Functionality

Welcome to the GitHub repository of our innovative Front End AI Chat Bot Interface. This project is designed to create a seamless and interactive user experience, incorporating chat, document upload, and web search functionalities. By default, it utilizes LMStudio as the backend, ensuring powerful and efficient natural language processing capabilities.

## Features

- **Chat Functionality**: Engage in real-time conversations with an AI, capable of understanding and responding to a wide range of queries and commands.
- **Document Upload**: Easily upload documents for the AI to read, analyze, and provide feedback on, enhancing the interaction and utility of the chatbot.
- **Web Search**: Leverage the AI's ability to perform web searches, returning relevant information directly within the chat interface, making it a one-stop solution for information retrieval.

At its core, this interface is powered by LMStudio, a robust backend framework for managing AI and machine learning operations. LMStudio offers scalable, efficient processing for natural language tasks, making it an ideal choice for powering sophisticated AI interactions.

## Getting Started

To get started with this project, follow these steps to install LMStudio, set up a Conda environment, and install the necessary requirements.

### Prerequisites

Ensure you have Python 3.11 installed on your system to guarantee compatibility with the project's codebase and dependencies.

### Installing LMStudio

Before setting up the project, you need to install LMStudio. Visit the LMStudio official documentation for detailed installation instructions, as the process may vary depending on your operating system and setup preferences. `https://lmstudio.ai/`

### Setting Up a Conda Environment

1. If you don't have Conda installed, download and install Anaconda or Miniconda from their respective websites.
   to get to your windows command line (which you need access to for this to work)
Click the Start menu or press the Windows key, type "cmd" or "Command Prompt" in the search bar, then select the Command Prompt application from the search results.
3. Once installed, open your terminal or command prompt and create a new Conda environment by running:
   ```
   conda create --name ai-chat-bot python=3.11
   ```
4. Activate the newly created environment:
   ```
   conda activate ai-chat-bot
   ```

### Installing Required Packages

With your Conda environment ready and activated, proceed to install the required Python packages.

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-github-repository/ai-chat-bot-interface.git
   ```
2. Navigate to the repository's root directory:
   ```
   cd Wolf-s-Bot-of-Knowledge
   ```
3. Install the requirements by running:
   ```
   pip install -r requirements.txt
   ```

This command will install all the necessary dependencies listed in the `requirements.txt` file, ensuring your project is ready to run.

## Running the Application

To run the application and start interacting with the AI chat bot interface, follow these steps:

1. Ensure your LMStudio backend is up and running. Refer to the LMStudio documentation for instructions on starting the backend server.
   Link to LM Studio's page `https://lmstudio.ai/`
3. With your backend ready, navigate to the root directory of the cloned repository (if you aren't already there).
4. Run the front end application by executing:
   ```
   python app.py
   ```
   
   The Default is...
   ```
   python Wolfs_Bot_of_Knowledge.py
   ```
   
   Replace `app.py` with the main script name of the front end application if it differs.

This will launch the front end interface of the AI chat bot, connecting it to the LMStudio backend. You can now begin interacting with the AI, upload documents, and utilize the web search functionality directly from the interface.

## Conclusion

This Front End AI Chat Bot Interface project represents a significant step forward in creating interactive and user-friendly AI applications. By leveraging the power of LMStudio for backend processing, we're able to offer a sophisticated, feature-rich user experience. Follow the setup instructions to get started and explore the capabilities of this project.

## Obtaining a Google Wrapper API Key from Serper.dev

For certain functionalities, our project requires a Google Wrapper API key, which can be obtained for free from Serper.dev. Follow these steps to sign up and get your API key:

1. Visit [Serper.dev](https://serper.dev) in your web browser.
2. Sign up for an account by providing the necessary information.
3. Once signed up, navigate to the dashboard to find your free Google Wrapper API key.

## Configuring the Serper Wrapper API Key in the Project

After obtaining your API key, you'll need to configure it within the project for the web search functionality to work. Here's how you can do that:

1. Open the project folder in your preferred file editor.
2. Locate the Python file responsible for web search functionality (usually `app.py` or a similarly named file).
3. Find the line of code where the API key needs to be set, which looks like `SERPER_API_KEY = "put_your_serper_api_wrapper_api_here"`.
4. Replace `put_your_serper_api_wrapper_api_here` with your actual Serper.dev Google Wrapper API key, ensuring to save the changes.

This will allow the application to perform web searches using your Serper.dev API key.

## Using the Program

After running the program, navigate to [http://127.0.0.1:7860/](http://127.0.0.1:7860/) in your web browser to use the program.
