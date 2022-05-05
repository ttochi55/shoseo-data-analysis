
def main():
  pass


def save_screenshot(htmlPath='', imgPath=''):
  from selenium import webdriver
  from selenium.webdriver.support.ui import WebDriverWait

  # The old socket.ssl() support for TLS over sockets is being superseded in Python 2.6 by a new ‘ssl’ module. This package brings that module to older Python releases, 2.3.5 and up (it may also work on older versions of 2.3, but we haven’t tried it).
  import ssl

  try:
      _create_unverified_https_context = ssl._create_unverified_context
  except AttributeError:
      # Legacy Python that doesn't verify HTTPS certificates by default
      pass
  else:
      # Handle target environment that doesn't support HTTPS verification
      ssl._create_default_https_context = _create_unverified_https_context

  # WebDriver is an open source tool for automated testing of webapps across many browsers.
  import chromedriver_autoinstaller

  chromedriver_autoinstaller.install()

  driver = webdriver.Chrome()
  driver.get(htmlPath)

  WebDriverWait(driver, 10)

  driver.save_screenshot(imgPath)
  driver.quit()


if __name__ == "__main__":
    main()
