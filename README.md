Sometimes you just want to email a little something to yourself, or whoever, from your command line. And you can do that, but it's kinda more than you want to deal with. 

For those occastions, there's mailme.py.


NB: For now, out of the box mailme only supports [Mailgun](http://mailgun.com/). That's easy enough to change.

---

Stick your configuration in `~/.mailme/config`:

    mailgun_api_endpoint=https://api.mailgun.net/v2/EXAMPLE.mailgun.org/messages
    mailgun_api_key=key-xxxxxxxxx
    to=yourself@exmaple.com
    from=mailme.py@example.com
    # subject = "mailme.py email" 


You can of course specify any of these from the command line: 

    » python mailme/mailme.py -h
    usage: mailme.py [-h] [-c CONFIG] [-s SUBJECT] [-f FROM] [-t TO]
                     [--mailgun_api_key MAILGUN_API_KEY]
                     [--mailgun_api_endpoint MAILGUN_API_ENDPOINT]
                     [MESSAGE]

    send quick email from yourself to yourself (or anyone), using mailgun

    positional arguments:
      MESSAGE               the message to send

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            specify a config file
      -s SUBJECT, --subject SUBJECT
                            the subject of the email
      -f FROM, --from FROM  the email the message is to be sent from
      -t TO, --to TO        the email the message is to be sent to
      --mailgun_api_key MAILGUN_API_KEY
                            mailgun secret api key
      --mailgun_api_endpoint MAILGUN_API_ENDPOINT
                            mailgun api endpoint
