function handler(m) {
  // Ini cuma contoh, jgn di uncomment -_-
  // F this.sendContact(m.chat, '62815158600891', 'Nurutomo', m)
  m.reply('Use .bot to msg owner')
  this.sendContact(m.chat, '919462541580', 'Rishabh-Modi', m)
  this.sendContact(m.chat, '', 'Rishabh-Modi', m)
}
handler.help = ['owner/creator']
handler.tags = ['info']

handler.command = /^(owner|creator)$/i

module.exports = handler
