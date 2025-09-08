alert_system = 'console'
error_severity = 'critical'
error_message = 'OMG! Something terrible happened!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@example.com', error_message)
    elif error_severity == 'medium':
        send_email('support.1@example.com', error_message)
    else:
        send_email('support.2@example.com', error_message)