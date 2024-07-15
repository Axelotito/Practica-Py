sent_message = 'Hey there! this is a secret message.'
unsend_message = 'This message has been unsent.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
  original_message = file.read()

  file.seek(0)
  file.write(unsend_message)
  file.truncate(len(unsend_message))

print("Mensaje original:", original_message)
print("Mensaje modificado:", unsend_message)
