# Chatbot

## Overview
This is a basic text-based chatbot built using Python and the `nltk` library. The chatbot can respond to predefined patterns and provides a fallback response when an unknown input is received.

## Features
- Responds to basic greetings and questions.
- Provides a default response for unknown inputs.
- Uses Natural Language Toolkit (NLTK) for simple pattern matching.
- Runs in the terminal and allows users to chat interactively.

## Prerequisites
Make sure you have Python installed on your system. You will also need the `nltk` library.

## Installation
1. Clone this repository or copy the chatbot script.
2. Install the required package:
   ```bash
   pip install nltk
   ```

## Usage
Run the chatbot script using:
```bash
python chatbot.py
```
Then, start chatting! The chatbot will respond to greetings and basic queries.

### Example Conversation:
```
Chatbot: Hello! Type 'bye' to exit.
You: hi
Chatbot: Hello!
You: how are you?
Chatbot: I'm doing well, thank you!
You: tell me a joke
Chatbot: I'm not sure how to respond to that, but I'm always here to chat!
You: bye
Chatbot: Goodbye!
```

## Customization
You can add more pattern-response pairs in the script to make the chatbot smarter.
Example:
```python
(r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"])
```

## License
This project is open-source and available for modification.

## Future Enhancements
- Add more predefined responses.
- Use AI-based responses with NLP models.
- Implement a GUI for better user experience.

Feel free to contribute or suggest improvements!

