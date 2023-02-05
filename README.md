## Introduction

Linkedin-bot is exactly what its name describes it. It is a bot that comments on posts on linkedin with the power of ChatGpt and Selenium. Now if you want to do a little trolling, you could edit the code and have it generate satire posts so that the responses aren't linkedin toxic positivity.

## Getting Started

To get a local copy up and running follow these simple example steps. And please use a [virtual environment!](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

### Prerequisites

`pip install -r requirements.txt`

Next create the credentials.json file
And fill it with the following json

```
{
    "username": "linkedin_username",
    "password": "linkedin_password",
    "api-key": "api_key"
}
```

Replace `linkedin_username` with your real linkedin username
Replace `linkedin_password` with your real linkedin password
Replace `api-key` with your the [api-key](https://github.com/acheong08/ChatGPT#setup) obtained from OpenAi]

### Execution

`python main.py`

Now sit back and make others think you really care about them even if you don't.

### Legal

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Linkedin or any of its affiliates or subsidiaries. This is an independent and unofficial API. Use at your own risk.

This project violates Linkedin's User Agreement Section 8.2, and because of this, Linkedin may (and will) temporarily or permanently ban your account. We are not responsible for your account being banned.
