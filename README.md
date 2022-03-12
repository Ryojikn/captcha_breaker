# captcha_breaker

This repo contains a captcha breaker for multiple purposes.


It contains four main sections:

- Extracting captcha information based on Selenium (webscraping)
- Using preprocessing to cleanup the image.
    - The best preprocessing depends upon your captcha image, you can use a bunch of techniques such as
        - Horizontal kernel filtering for removing the horizontal lines for a simpler captcha
        - Image thresholding to cleanup random lines for more complex captchas
        Or any other solution most suited for your need.
    - Dilation or  erosion can be added to increase your captcha readability.

- Using OCR
    - easyocr and pytesseract were tested
    - paddleocr to be tested (https://github.com/PaddlePaddle/PaddleOCR/issues/4838)

    - Another solution here is to use a pretrained model/train a model on Extended MNIST and use text classification instead of OCR, since most of the time letters are within a specific range from each other (splitting the image into 5 pieces for example, and classifying each letter).

- Getting the string result and placing to the input object, doing a specific action.

