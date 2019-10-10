class Decoder:

	def _stats(self, message):
	    try:
	        stats_file = open(config.STATS_FILE, 'r')
	    except IOError:
	        raise IOError("Invalid or missing stats file path.")

	    stats_entries = stats_file.read().split('\n')

	    # check if the stats entry exists if it does overwrite it with the new message
	    is_existing_entry = False
	    if stats_entries:
	        for i, entry in enumerate(stats_entries):
	            if entry:
	                if message[:5] == entry[:5]:
	                    stats_entries[i] = message
	                    is_existing_entry = True

	    # if the entry does not exist append it to the file
	    if not is_existing_entry:
	        stats_entries.append(message)

	    stats_file = open(config.STATS_FILE, 'w')
	    for entry in stats_entries:
	        if entry:
	            stats_file.write("%s\n" % entry)
	    stats_file.close()

	def _validate_email(self, email_address):
	    if not email_address or len(email_address) < 5:
	        print(1)
	        return None
	    if not re.match(r'^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$', email_address):
	        return None
	    return email_address

	def _retry_handler(self, recipient_data):
	    try:
	        csv_file = open(config.CSV_RETRY_FILENAME, 'wb+')
	    except IOError:
	        raise IOError("Invalid or missing csv file path.")
	    csv_writer = csv.writer(csv_file)
	    csv_writer.writerow([
	        recipient_data.get('name'),
	        recipient_data.get('email')
	    ])
	    csv_file.close()

	def _placeholder(self, filename):

		# Opens file
		f = open(filename,'rb')
		line = f.readlines()

		# placeholder converter
		str_decoded = line[0].decode()
		return str_decoded

	def _html_parser(self, recipient_data):
	    try:
	        html_file = open(self.html_path, 'r')
	    except IOError:
	        raise IOError("Invalid or missing html file path.")

	    html_content = html_file.read()
	    if not html_content:
	        raise Exception("The html file is empty.")

	    # replace all placeolders associated to recipient_data keys
	    if recipient_data:
	        for key, value in recipient_data.items():
	            placeholder = "<!--%s-->" % key
	            html_content = html_content.replace(placeholder, value)

	    return html_content

	def send_test(self):
	    self.send(recipient_list=config.TEST_RECIPIENTS)

	def resend_failed(self):
	    for i in range(1, 3):
	        self.send(retry_count=i)

	def count_recipients(self, csv_path=None):
	    return len(self._parse_csv(csv_path))
