
from linkedin_api import Linkedin
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from revChatGPT.Official import Chatbot
from time import sleep
import json


def load_credentials():
    """Loads the credentials and returns it"""

    with open("credentials.json", "r") as f:
        return json.load(f)


def setup_driver():
    """Creates the driver and returns it"""

    # Disable Chrome password saving
    chrome_opt = uc.ChromeOptions()
    prefs = {"credentials_enable_service": False,
             "profile.password_manager_enabled": False}
    chrome_opt.add_argument("--headless")
    chrome_opt.add_experimental_option("prefs", prefs)

    return uc.Chrome(options=chrome_opt)


def load_linkedin(driver):
    """Has the driver send the user to Linkedin"""
    driver.get('https://www.linkedin.com/login')
    email = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    submit = driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    email.send_keys(EMAIL_ADDRESS)
    password.send_keys(PASSWORD)
    submit.click()


def comment_linkedin(driver):
    """Get on posts in user feed, try to comment on them
    Todo: Check if bot already commented on post, skip
    """
    # Sometimes Linkedin would return nothing cause we call it too many times.
    # Thus, the while loop exists so that we can call it after a short time interval
    result = None
    posts = None
    while result is None:
        try:
            # connect
            posts = api.get_feed_posts(limit=-1, offset=0)
            result = True
        except:
            sleep(10)

    for post in posts:
        try:
            print(post)
            content = post['content']
            response = chatbot.ask(
                user_request=f"sample linkedin comment to {content}")
            print(response)
            driver.get(post['url'])
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "ql-editor")))

            comment_box = driver.find_element(By.CLASS_NAME, "ql-editor")
            comment_box.send_keys(response["choices"][0]["text"])
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(driver, 300).until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "comments-comment-box__submit-button")))
            post = driver.find_element(
                By.CLASS_NAME, "comments-comment-box__submit-button")
            post.click()
        except:
            continue


credentials = load_credentials()
EMAIL_ADDRESS = credentials["username"]
PASSWORD = credentials["password"]
API_KEY = credentials["api-key"]

api = Linkedin(EMAIL_ADDRESS, PASSWORD)
chatbot = Chatbot(
    api_key=API_KEY)

driver = setup_driver()
load_linkedin(driver)

result = None
while result is None:
    try:
        comment_linkedin(driver)
    except:
        pass
