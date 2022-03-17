def show_emojis(msg):
    words = msg.split(' ')
    emojis = {
        ':)': '🙂',
        ':(': '🙁'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('Write a message with a happy ":)" or sad":(" face: ')
print(show_emojis(message))
