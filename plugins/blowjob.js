let handler = async (m, { conn }) => {
 
  conn.sendFile(m.chat, 'https://api.xteam.xyz/randomimage/blowjob?APIKEY=4a8b9aba75823076', '', 'Here..', m)
  
}
handler.help = ['cum']
handler.tags = ['nsfw']
handler.command = /^(cum)$/i

handler.limit = true
handler.group = false
handler.premium = false

module.exports = handler
