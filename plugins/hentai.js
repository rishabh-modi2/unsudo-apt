let fetch = require('node-fetch')
let handler = async (m, { conn }) => {
  let res = await fetch('https://nekos.life/api/v2/img/pussy_jpg')
  if (!res.ok) throw await `${res.status} ${res.statusText}`
  let json = await res.json()
  if (!json.url) throw 'Eror!'
  conn.sendFile(m.chat, json.url, '', '© Araaa•BOT', m, 0, { thumbnail: await (await fetch(json.url)).buffer() })
}
handler.help = ['randomhentai']
handler.tags = ['newfitur','premium']
handler.command = /^randomhentai|hentai$/i
handler.premium = true

module.exports = handler
