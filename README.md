# Blog Generating AI

### Project Overview
The Blog Post Writing AI is a Python-based application that utilizes the Gemini-1.5-flash large language model, along with the Google Generative AI and Streamlit libraries, to generate high-quality blog content for users. This project aims to provide a convenient and efficient way for users to create engaging blog posts with minimal effort.

### Features
- **Blog Title and Keyword Input**: Users can input the desired blog title and keywords, which the AI will use to generate the blog content.
- **Word Length Customization**: Users can adjust the length of the generated blog post, ranging from 250 to 1000 words, to suit their needs.
- **Streamlit-based User Interface**: The application is built using the Streamlit framework, providing a user-friendly and interactive web-based interface.



https://github.com/user-attachments/assets/5c8452e5-c76a-4f80-928d-7fe8def246f2



### Installation and Setup

To run the Blog Post Writing AI on your local computer, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/blog-post-writing-ai.git
   ```

2. **Install the Required Dependencies**:
   ```
   cd blog-post-writing-ai
   pip install -r requirements.txt
   ```

3. **Set up the API Keys**:
   - Obtain the Google Gemini API key and the OpenAI API key.
   - Create a new file named `appapikey.py` in the project directory.
   - Add the following lines to the file, replacing the placeholders with your actual API keys:
     ```python
     google_gemini_api_key = "your-google-gemini-api-key"
     openai_api_key = "your-openai-api-key"
     ```

4. **Run the Application**:
   ```
   streamlit run app.py
   ```

   This will launch the Streamlit application, and you can access it in your web browser at `http://localhost:8501`.

### Usage

1. In the Streamlit application, you will see the "Blog Details" section in the sidebar.
2. Enter the desired blog title and keywords (separated by commas) in the respective input fields.
3. Adjust the length of the blog post using the slider.
4. Click the "Generate Blog" button to generate the blog content.
5. The generated blog post will be displayed on the main page of the application.

### API Endpoints

The Blog Post Writing AI does not provide any API endpoints. It is a standalone Streamlit application that generates blog content based on user input.

### Contributing

If you would like to contribute to the development of the Blog Post Writing AI, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

### License

This project is licensed under the [MIT License](LICENSE). 
