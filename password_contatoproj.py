#Configuracao para o settings.py - SECRETE KEY
SECRET_KEY_var = ')%7e0-sn7k)hwu#a8q52_&wie!be8z%o)%l^$=367ee%%r(w2p'

# Configuracao para o Postfix - envio apenas de e-mail
EMAIL_HOST_PASSWORD_var = 'aws1ubuntu1804admpostfix33'

#configuracao para o Celery
#informando qual broker utilizar e qual o backend do broker
broker_var = 'amqp://internal:AdmrabbitmqHenryP0l1a2n3e4j5a6m7e8n9toOrganizacaoDirecaoMonitoramentoCon9t8r7o6l5e4F3a2y1o0l@54.149.121.168:5672/vhost_valoreio'
backend_var = 'redis://:AdmredisHenryP0l1a2n3e4j5a6m7e8n9toOrganizacaoDirecaoMonitoramentoCon9t8r7o6l5e4F3a2y1o0l@54.149.121.168:6379/0'
