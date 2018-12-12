from app import app


@app.template_filter('captcha_error_translation')
def captcha_error_translation(s):
    if s == 'The response parameter is missing.':
        return 'کپچامون رو پر کن '
