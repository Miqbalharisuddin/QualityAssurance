def test_visible_upload(self):
    # open page
    self.open("https://the-internet.herokuapp.com/upload")

    # get file path
    file_path = './data/logo.jpg'

    # upload file
    self.choose_file("#file-upload", file_path)

    # click the upload button
    self.click("#file-submit")

    # assert file uploaded text
    self.assert_text("File Uploaded!", "h3")
